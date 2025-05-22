import requests
from bs4 import BeautifulSoup

def get_stock_price_by_name(stock_name):
    headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(1, 21):  # 최대 20페이지까지 확인 (보통 시총 상위는 여기 안에 있음)
        url = f"https://finance.naver.com/sise/sise_market_sum.naver?&page={page}"
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        rows = soup.select("table.type_2 tr")

        for row in rows:
            cols = row.select("td")
            if len(cols) < 2:
                continue

            name = cols[1].get_text(strip=True)
            price = cols[2].get_text(strip=True)

            if stock_name in name:
                return f"{name}의 현재 주가는 {price}원입니다."

    return "❌ 해당 종목을 찾을 수 없습니다."