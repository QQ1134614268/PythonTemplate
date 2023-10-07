# -*- coding:utf-8 -*-
"""
@Time: 2023/3/24
@Description: todo ChatGpt
"""
import os

import openai

# 填写注册OpenAI接口账号时获取的 OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 提问
issue = '你是谁？'

# 访问OpenAI接口
response = openai.Completion.create(
    model='text-davinci-003',
    prompt=issue,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6
)

# 返回信息
resText = response.choices[0].text

print(resText)
