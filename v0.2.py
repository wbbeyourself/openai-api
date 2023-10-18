# coding=utf-8
# @author: beyourself
# @date: 2023/06/17

import os
# jumper_url = "https://api.chatanywhere.com.cn/v1"
# os.environ['OPENAI_API_BASE'] = jumper_url

import openai
from tools import get_lines

APIKEY_FILE = 'config/apikey.txt'
assert os.path.exists(APIKEY_FILE), f"Please config your {APIKEY_FILE}!"
# 读取 apikey
keys = get_lines(APIKEY_FILE)
assert len(keys) > 0 and 'sk' in keys[0], f"Invalid apikey in {APIKEY_FILE}!"
# 取一个key出来
apikey = keys[0]

# 引入代理魔法，其中 7890 是代理的端口
proxy = "http://127.0.0.1:7890"
os.environ["HTTP_PROXY"] = proxy
os.environ["HTTPS_PROXY"] = proxy

# 调用 ChatGPT
openai.api_key = apikey
ENGINE_TURBO = 'gpt-3.5-turbo'
# ENGIN_GPT4 = 'gpt-4'
def call_gpt3_5_turbo(prompt):
    response = openai.ChatCompletion.create(
        model=ENGINE_TURBO,
        messages=[{"role": "user", "content": prompt}]
    )
    text = response['choices'][0]['message']['content'].strip()
    return text

prompt = '小明的爸爸有三个孩子，老大叫王一宝，老二叫王二宝，老三叫什么？'
prompt = '我爸妈结婚为什么不邀请我？'

# 这是最简单的版本，我假设你的网络可以直接调用 openai 的接口，不需要魔法
response = call_gpt3_5_turbo(prompt)

print(f"\n\nprompt: {prompt}")
print(f"\n\nresponse: {response}")