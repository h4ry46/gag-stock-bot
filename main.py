import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

last_html = ""

def fetch_stock_html():
    url = "https://arcaiuz.com/grow-a-garden-stock"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        print(f"📶 Status code: {res.status_code}")
        if res.status_code != 200:
            return ""
        return res.text
    except Exception as e:
        print("❌ Lỗi khi kết nối:", e)
        return ""

def sleep_until_next_5min():
    now = datetime.now()
    sleep_seconds = 300 - (now.minute % 5) * 60 - now.second
    print(f"⏰ {now.strftime('%H:%M:%S')} | Ngủ {sleep_seconds} giây đến mốc kế tiếp...\n")
    time.sleep(sleep_seconds)

while True:
    print("🔄 Đang kiểm tra stock...")

    html = fetch_stock_html()

    if html == "":
        print("⚠️ Không có dữ liệu, bỏ qua.")
    elif html != last_html:
        print("✅ Stock đã thay đổi!")
        print("----- HTML BẮT ĐẦU -----")
        print(html[:500], "...")
        print("----- HTML KẾT THÚC -----")
        last_html = html
    else:
        print("⚪ Không có thay đổi.")

    sleep_until_next_5min()
