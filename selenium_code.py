from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse

def get_stock_price(stock_name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 종목명을 URL 인코딩 (한글 가능)
        encoded_name = urllib.parse.quote(stock_name)

        # 네이버 모바일 주식 검색 결과 URL
        search_url = f"https://m.stock.naver.com/search/result?query={encoded_name}"
        driver.get(search_url)
        time.sleep(2)

        # 첫 번째 검색 결과 클릭
        first_result = driver.find_element(By.CSS_SELECTOR, "ul.lst_stock_search > li a")
        first_result.click()
        time.sleep(2)

        # 주가 및 이름 추출
        price = driver.find_element(By.CLASS_NAME, "stock_now").text
        name = driver.find_element(By.CLASS_NAME, "stock_name").text

        return f"{name}의 현재 주가는 {price}입니다."

    except Exception as e:
        return f"❌ 오류 발생: {str(e)}"

    finally:
        driver.quit()
