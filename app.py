import os
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select




from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), options = options)
driver.maximize_window()

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver.get("https://www.facebook.com/")
sleep(3)



email=driver.find_element_by_id("email")
email.send_keys("100054592715360")
password=driver.find_element_by_id("pass")
password.send_keys("chidozie5")
sleep(1)
login=driver.find_element_by_name("login")
login.click()
sleep(4)




i = 1

while i<=50000:


 groups_links_list = [
   "https://www.facebook.com/groups/3686706161407106", "https://www.facebook.com/groups/2782001165164383", "https://www.facebook.com/groups/2020733191524486", "https://www.facebook.com/groups/5440056676034888", "https://www.facebook.com/groups/internationalcryptominers", "https://www.facebook.com/groups/1977782575833348", "https://www.facebook.com/groups/753677805258668", "https://www.facebook.com/groups/423287535042518", "https://www.facebook.com/groups/1953339638311954", "https://www.facebook.com/groups/818536955169151", "https://www.facebook.com/groups/755878041998722", "https://www.facebook.com/groups/753677805258668", "https://www.facebook.com/groups/751840511663201", "https://www.facebook.com/groups/316292243440591", "https://www.facebook.com/groups/1088619671559643", "https://www.facebook.com/groups/387055385984329", "https://www.facebook.com/groups/341683990228113", "https://www.facebook.com/groups/716910665175389", "https://www.facebook.com/groups/cryptocurrencybitcoininvestment", "https://www.facebook.com/groups/newsbitcoinworld", "https://www.facebook.com/groups/usabusinessgroupz", "https://www.facebook.com/groups/2782001165164383", "https://www.facebook.com/groups/2438045376224715", "https://www.facebook.com/groups/2020733191524486", "https://www.facebook.com/groups/1893338250702751", "https://www.facebook.com/groups/internationalcryptominers", "https://www.facebook.com/groups/1829098377306709", "https://www.facebook.com/groups/UcoincashIndonesiaRaya", "https://www.facebook.com/groups/1709996879303044", "https://www.facebook.com/groups/1572466832810159", "https://www.facebook.com/groups/bitcoinworldtm", "https://www.facebook.com/groups/1142220402650653", "https://www.facebook.com/groups/binancecom", "https://www.facebook.com/groups/insidecrypto.news", "https://www.facebook.com/groups/germanbtc", "https://www.facebook.com/groups/595862454626204", "https://www.facebook.com/groups/530659007137021", "https://www.facebook.com/groups/1130482460326432", "https://www.facebook.com/groups/1894175397292966", "https://www.facebook.com/groups/hyip.raj.2"
    ]

 
 for group in groups_links_list:
    driver.get(group)
    sleep(7)
       
    
    driver.execute_script("window.scrollTo(0, 200)")
    postbox = driver.find_element_by_xpath("//div[@class='oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl orhb3f3m czkt41v7 fmqxjp7s emzo65vh l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y']")
    postbox.click()
    sleep(4)

    

    element = driver.switch_to.active_element
    
    
    sleep(4)
    element.send_keys("https://www.facebook.com/photo/?fbid=2151059395034056&set=a.2130956000377729")
    sleep(6)
    element.send_keys("Sel")
    element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    sleep(2)
    messages = ['Many investors have lost all their investment profits because they don not believe in reality ,\nwhile some lost their major withdrawals to fake companies and many are still loosing till now.\nI am here to introduce you all to the greatest paying and legitimate investment company of our time..I have been receiving my withdrawals automatic and I am so glad to witness the uprising of my daily investment with Zend Cryptos Investments platform.\nBelieve me this is the best platform to invest with now.\nRegister and strat earning like me now.Follow the link now.\nhttp://www.google.com/search?q=site%3Azendforex.com','great investment platform today ']
    for message in messages:
      element.send_keys(message)
   
    
    
    
    sleep(5)
    driver.find_element_by_xpath("//div[@aria-label='Remove Post Attachment']//i[@class='hu5pjgll m6k467ps']").click()

    


    postbutton = driver.find_element_by_xpath("//div[@aria-label='Post']")
    sleep(1)
    postbutton.click()
    sleep(2)
    
    
    driver.get("https://facebook.com/")
    sleep(5) 
    driver.find_element_by_xpath("//div[@aria-label='Account']//*[name()='svg']").click()
    sleep(4)
    driver.find_element_by_xpath("//span[normalize-space()='Log Out']").click()

    sleep(2)

    
    
    driver.get("https://facebook.com/")
    sleep(1)

    email=driver.find_element_by_id("email")
    email.send_keys("100054592715360")
    password=driver.find_element_by_id("pass")
    password.send_keys("chidozie5")
    sleep(1)
    login=driver.find_element_by_name("login")
    login.click()
    sleep(4)


    
    sleep(1)

    
i=i+1  
