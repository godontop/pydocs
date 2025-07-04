# 以查询pip的所有可用版本为例
import requests
import json


response = requests.get('https://pypi.python.org/pypi/pip/json')
data = response.json()
# 打印所有可用版本
print("所有可用的pip版本如下：")
print(data['releases'].keys())
print()

# 打印最新版本的信息
print("pip 的最新版本是：")
newestversion = data['info']['version']
print(newestversion)
print()

# 打印pip最新版本的详细信息
print("pip最新版的详细信息如下")
print(json.dumps(data['releases'][newestversion], indent=4))

