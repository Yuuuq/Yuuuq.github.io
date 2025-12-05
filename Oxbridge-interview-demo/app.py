# app.py

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI
from interview_prompt import OXBRIDGE_INTERVIEW_SYSTEM_PROMPT

# 读取 .env 中的环境变量
load_dotenv()

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

app = Flask(__name__)

@app.route("/")
def home():
    return "Oxbridge Interview Backend is running."

@app.route("/api/interview", methods=["POST"])
def interview():
    """
    接收前端传来的 history + userMessage，
    调用 OpenAI 模型，返回“面试官”的下一句话。
    """
    data = request.get_json(force=True)
    history = data.get("history", [])
    user_message = data.get("userMessage")

    if not user_message:
        return jsonify({"error": "userMessage is required"}), 400

    # 组装 messages：先是 system，再是历史，再是当前用户消息
    messages = [
        {
            "role": "system",
            "content": OXBRIDGE_INTERVIEW_SYSTEM_PROMPT
        }
    ]

    # history 需要是列表，里面每项有 role 和 content
    # 我们简单信任前端传的是正确格式
    messages.extend(history)

    # 加上本次用户的最新回答
    messages.append({
        "role": "user",
        "content": user_message
    })

    try:
        # 调用 Responses API
        response = client.responses.create(
            model="Qwen/Qwen2.5-72B-Instruct",  # 或 gpt-5.1-mini / 你账号有权限的其他模型
            input=messages,
        )

        # 从结果中拿到文本输出（官方 SDK 提供了 output_text 字段）
        interviewer_reply = response.output_text

        return jsonify({
            "reply": interviewer_reply
        })
    except Exception as e:
        print("Error when calling OpenAI:", e)
        return jsonify({
            "error": "OpenAI request failed",
            "detail": str(e)
        }), 500


if __name__ == "__main__":
    # debug=True 会在本地开发时自动重载代码，很方便
    app.run(host="0.0.0.0", port=5000, debug=True)