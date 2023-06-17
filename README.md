<div align="center">
	<img src="misc/openai-api.png" width="800" >
	</a>
</div>

<p align='center'>
    🚀 OpenAI api 花式用法 🚀
</p>


# 👻 前言

最近半年，基于 ChatGPT 的小工具、第三方网站如雨后春笋般层出不穷，我整理了自己项目中关于 OpenAI 的常用接口及高阶封装，供大家一起学习和参考。



# 🏴󠁶󠁵󠁭󠁡󠁰󠁿功能特性

| Features                         |  Status        |    Version   |
| -------------------------------- | :------------: | :----------: |
| 最简单的API调用                   | ✅ Supported  | V0.1           |
| 支持代理的API调用                 | 🔧 Developing | V0.2           |
| 支持多key自动切换的API调用        | 🔧 Developing | V1.5           |
| 支持多key多进程的API调用          | 🔧 Developing | V2.0           |


# ⚡️环境配置

打开 `config` 文件夹， 将 `apikey.txt.template` 复制为 `apikey.txt`，将你的apikey (格式如`sk-xxx`)放到该文件中。 为了保护用户隐私，该文件已经被git版本管理器忽略，不用担心会泄露到github上。

## 😊 依赖库

核心的依赖库:

- python 3.8+
- openai 0.27.0+

使用 Conda 创建 python 虚拟环境：
```shell
conda create -n api python=3.8 -y
conda activate api
```

安装依赖包:
```shell
pip install -r requirements.txt
```

# 🔥 运行代码
Tips: 记得先配置 `apikey.txt` !!!

运行 `v0.1` 版代码（假设你的网络可以正常访问 OpenAI 接口）。
```bash
python v0.1.py
```

输出结果：
```text
prompt: 小明的爸爸有三个孩子，老大叫王一宝，老二叫王二宝，老三叫什么？

response: 小明。
```

如果报错如下，说明你当前的网络不支持访问 OpenAI 的接口，需要 V0.2 加版本的网络代理才行：
```text
openai.error.APIConnectionError: Error communicating with OpenAI: HTTPSConnectionPool(host='api.openai.com', port=443)
```


# 👍 交流合作

欢迎小伙伴们多多贡献代码和建议。如果你觉得这个项目有帮助，麻烦star支持一下，非常感谢，ღ( ´･ᴗ･` )比心。