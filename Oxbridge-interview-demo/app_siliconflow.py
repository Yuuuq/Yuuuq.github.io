# app_siliconflow.py

from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os
from openai import OpenAI
from interview_prompt import OXBRIDGE_INTERVIEW_SYSTEM_PROMPT
from question_cards import ALL_QUESTION_CARDS
from question_cards import QUESTION_CARDS_BY_ID, QUESTION_CARDS_BY_SUBJECT_LEVEL

load_dotenv()

from question_cards import physics_loop_the_loop_cart

def build_messages(history, latest_user_message, question_card):
    # 把题卡塞进一个 system/assistant 提示，让模型“悄悄参考”
    question_card_text = f"""
You are running an Oxbridge-style mock interview.

QUESTION CARD (for interviewer only, do not reveal directly):
- Subject: {question_card['subject']}
- Student-facing question: "{question_card['student_prompt']}"
- Solution outline (do not read aloud): {question_card['solution_outline_steps']}
- Common misconceptions: {question_card['common_misconceptions']}
- Hints (light): {question_card['light_hints']}
- Hints (strong): {question_card['strong_hints']}
- Extension questions: {question_card['extension_questions']}

TASK:
1. Silently decide:
   - Is the student: {{on the right track, partially correct, misconception, stuck}}?
   - Which move to take:
     {{CHECK_UNDERSTANDING, PROBE_ASSUMPTIONS, REQUEST_NEXT_STEP,
       GIVE_HINT_LIGHT, GIVE_HINT_STRONG, CORRECT_GENTLY,
       EXTEND_IF_STRONG, CONSOLIDATE}}.
2. Reply with ONLY what the interviewer would say next to the student, in natural spoken English.
3. Do NOT:
   - Show your internal labels or the solution outline.
   - Jump straight to the full solution unless the student is clearly at the end.
"""

    messages = []

    # 系统角色：设定“你是谁”“行为规范”
    messages.append({"role": "system", "content": OXBRIDGE_INTERVIEW_SYSTEM_PROMPT})

    # 再给一条 system/assistant 信息，提供题卡
    messages.append({"role": "system", "content": question_card_text})

    # 加历史对话（这里 history 里 role 已经是 user/assistant）
    messages.extend(history)

    # 加上这次学生的最新发言
    messages.append({"role": "user", "content": latest_user_message})

    return messages

# 初始化 SiliconFlow 客户端
client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1"),
)

# 你可以在 SiliconFlow 平台上换成自己想要的模型
DEFAULT_MODEL = os.getenv("SILICONFLOW_MODEL", "Pro/deepseek-ai/DeepSeek-V3.2")

app = Flask(__name__)

@app.route("/chat")
def chat_page():
    # 从当前目录发送 chat.html
    return send_from_directory(".", "chat.html")

@app.route("/")
def home():
    return "Oxbridge Interview Backend (SiliconFlow) is running."

@app.route("/api/questions", methods=["GET"])
def list_questions():
    summaries = []
    for card in ALL_QUESTION_CARDS:
        # Short label for UI: first line of prompt, truncated
        first_line = card["student_prompt"].splitlines()[0]
        summaries.append({
            "id": card["id"],
            "subject": card["subject"],
            "level": card.get("level"),
            "title": first_line[:120],
        })
    return jsonify(summaries)

@app.route("/api/interview", methods=["POST"])
def interview():
    data = request.get_json(force=True) or {}
    history = data.get("history", [])
    user_message = data.get("userMessage")
    question_id = data.get("questionId")      # NEW
    subject = data.get("subject")
    level = data.get("level")

    if not user_message:
        return jsonify({"error": "userMessage is required"}), 400

    # 1) If a specific question id is provided, use that
    if question_id and question_id in QUESTION_CARDS_BY_ID:
        question_card = QUESTION_CARDS_BY_ID[question_id]

    # 2) Else, if subject+level provided, pick one at random
    elif subject and level:
        import random
        key = (subject, level)
        candidates = QUESTION_CARDS_BY_SUBJECT_LEVEL.get(key)
        if not candidates:
            return jsonify({"error": f"No questions for {key}"}), 400
        question_card = random.choice(candidates)

    # 3) Fallback default (for old clients)
    else:
        # e.g. default to one known-good card
        question_card = QUESTION_CARDS_BY_ID["physics_car_power_drag"]

    messages = build_messages(
        history=history,
        latest_user_message=user_message,
        question_card=question_card,
    )

    try:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=512,
            # 可选：防止它乱写 Student:，多加一道保险
            stop=["Student:"],
        )

        interviewer_reply = completion.choices[0].message.content

        return jsonify({"reply": interviewer_reply})
    except Exception as e:
        print("Error when calling SiliconFlow:", e)
        return jsonify({
            "error": "SiliconFlow request failed",
            "detail": str(e)
        }), 500

@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json(force=True) or {}
    history = data.get("history", [])

    # 把对话砌成文字
    convo_lines = []
    for msg in history:
      speaker = "Interviewer" if msg["role"] == "assistant" else "Student"
      convo_lines.append(f"{speaker}: {msg['content']}")
    convo_text = "\n".join(convo_lines)

    eval_prompt = f"""
You have just finished an Oxbridge-style mock interview with a student.

CONVERSATION TRANSCRIPT:
{convo_text}

Now, step out of the role-play and produce an internal evaluation.
Based on the conversation above, rate the student on:
- Conceptual understanding (0–10)
- Mathematical/technical execution (0–10)
- Communication clarity (0–10)
- Teachability (0–10)

Then produce a short written feedback summary addressed to the student.
"""

    completion = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": "You are an experienced Oxbridge admissions tutor."},
            {"role": "user", "content": eval_prompt},
        ],
    )
    text = completion.choices[0].message.content
    return jsonify({"evaluation": text})

if __name__ == "__main__":
    # 本地开发时直接运行这个文件
    app.run(host="0.0.0.0", port=5001, debug=True)