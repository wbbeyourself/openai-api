import os
jumper_url = "https://api.chatanywhere.com.cn/v1"
os.environ['OPENAI_API_BASE'] = jumper_url

proxy = "http://127.0.0.1:7890"
os.environ["HTTP_PROXY"] = proxy
os.environ["HTTPS_PROXY"] = proxy

import openai
# openai.api_key = 'YOUR_API_KEY'

# ENGINE_TURBO = 'gpt-3.5-turbo-16k'
ENGIN_GPT4 = 'gpt-4'

# ENGIN_GPT4 = 'gpt-4-32k'
def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model=ENGIN_GPT4,
        messages=[{"role": "user", "content": prompt}]
    )
    text = response['choices'][0]['message']['content'].strip()
    return text

prompt = '小明的爸爸有三个孩子，老大叫王一宝，老二叫王二宝，老三叫什么？'
prompt = '我爸妈结婚为什么不邀请我？'

response = call_openai(prompt)

print(f"\n\nprompt: {prompt}")
print(f"\n\nresponse: {response}")