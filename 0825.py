from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('D:/222233334455/chromedriver.exe')
Url = "https://www.hometax.go.kr"
driver.get(url=Url)
sleep(3)# 3초동안 기다려라(인터넷이 느리니까)

driver.find_element_by_id('group88615689').click()
sleep(1)
driver.find_element_by_id('query').send_keys('전자세금계산서')
driver.find_element_by_id('btnAutoSearch').click()
sleep(3)

iframe = driver.find_element_by_id('txppIframe')
# iframe = driver.find_element_by_css_selector('#txppIframe')
sleep(2)
driver.switch_to_frame(iframe)
sleep(1)

driver.execute_script("doCollection('preans','2,1');")
sleep(3)

# 각 페이지 눌러보기 
#for page in range(1,10):
    # driver.execute_script("doPaging('%s');"%page*10)
   # driver.find_element_by_xpath('//*[@id="search_body]/div[i]/div/div[2]/div/div[2]/div/div[1]/ul/li[%2]/a'&page).click()
sleep(3)

for i in range(1,11):
    element = driver.find_element_by_xpath('//*[@id="not_te_menu"]/div[3]/div/div/div/table/tbody/tr['+str(i)+']/td[3]/a')
    print(element.text)

for i in range(1,11):
    element = driver.find_elements_by_css_selector('#not_te_menu > div.w2group.tbl_box.mt10 > div > div > div > table > tbody > tr:nth-child('+str(i)+') > td.title > a')
    print(element.text)

