from selenium import webdriver
from time import sleep

# 1. 국세청홈텍스 메인화면으로 이동
driver = webdriver.Chrome('chromedriver')
Url = "https://www.hometax.go.kr"
driver.get(url=Url)
sleep(3)
# 2. 검색 돋보기 클릭 후, 검색어 입력 및 검색실행
driver.find_element_by_id('group88615689').click()
sleep(1) # 안기다려주니 안되는경우 있네(ajax도 아닌데)
driver.find_element_by_id('query').send_keys('전자세금계산서')
driver.find_element_by_id('btnAutoSearch').click()
sleep(5)
# 3. iframe안에 결과절이 있으니, 모드변경
iframe = driver.find_element_by_css_selector('#txppIframe')
driver.switch_to_frame(iframe)
# 아래는 주예진학생이 해결한 방법
# locate = '//*[@id="not_te_menu"]/div[7]/div[2]/div/div/div/table/tbody//td[3]'
locate = '//*[@id="not_te_menu"]/div[7]/div[2]/div/div/div/table/tbody/tr[*]/td[3]'
elements = driver.find_elements_by_xpath(locate) # 반드시 s를 붙혀주세요.
for element in elements:
    print(element.text)