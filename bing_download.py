import requests
import os
from datetime import datetime

# 存储目录
save_dir = "bing_pics"
os.makedirs(save_dir, exist_ok=True)

# 国内必应API，zh-CN中文壁纸
api = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
res = requests.get(api, timeout=10)
data = res.json()

# 拼接4K原图链接
img_url = "https://cn.bing.com" + data["images"][0]["url"]
today = datetime.now().strftime("%Y%m%d")
save_path = os.path.join(save_dir, f"bing_{today}.jpg")

# 下载图片
img_data = requests.get(img_url).content
with open(save_path, "wb") as f:
    f.write(img_data)

print(f"已保存今日壁纸：{save_path}")
