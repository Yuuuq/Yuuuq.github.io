# test_siliconflow_chat.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# 读取 .env
load_dotenv()

# 初始化 SiliconFlow 客户端
client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1"),
)

def main():
    messages = [
        {
            "role": "user",
            "content": "Please ask me one Oxbridge-style maths or CS interview question in English."
        }
    ]

    # 这里的 model 名字，你可以在 SiliconFlow 的模型列表里查看。
    # 下面这个是官网文档示例里用的一个模型：Qwen/Qwen2.5-72B-Instruct 
    resp = client.chat.completions.create(
        model="Pro/deepseek-ai/DeepSeek-V3.2",
        messages=messages,
    )

    # OpenAI 兼容接口的标准取值方式：choices[0].message.content 
    print("Model reply:\n", resp.choices[0].message.content)

if __name__ == "__main__":
    main()