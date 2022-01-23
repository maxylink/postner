import os
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException




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
password.send_keys("chiemelie")
sleep(1)
login=driver.find_element_by_name("login")
login.click()
sleep(4)




i = 1

while i<=50000:


 groups_links_list = [
   "https://www.facebook.com/groups/CryptoPMIndia", "https://www.facebook.com/groups/bitcoincryptosingapore", "https://www.facebook.com/groups/1151827914899298", "https://www.facebook.com/groups/2782001165164383", "https://www.facebook.com/groups/2782001hhh", "https://www.facebook.com/groups/2020733191524486", "https://www.facebook.com/groups/5440056676034888", "https://www.facebook.com/groups/internationalcryptominers", "https://www.facebook.com/groups/1977782575833348", "https://www.facebook.com/groups/753677805258668", "https://www.facebook.com/groups/423287535042518", "https://www.facebook.com/groups/1953339638311954", "https://www.facebook.com/groups/818536955169151", "https://www.facebook.com/groups/755878041998722", "https://www.facebook.com/groups/753677805258668", "https://www.facebook.com/groups/751840511663201", "https://www.facebook.com/groups/316292243440591", "https://www.facebook.com/groups/1088619671559643", "https://www.facebook.com/groups/387055385984329", "https://www.facebook.com/groups/341683990228113", "https://www.facebook.com/groups/716910665175389", "https://www.facebook.com/groups/cryptocurrencybitcoininvestment", "https://www.facebook.com/groups/newsbitcoinworld", "https://www.facebook.com/groups/usabusinessgroupz", "https://www.facebook.com/groups/2782001165164383", "https://www.facebook.com/groups/2438045376224715", "https://www.facebook.com/groups/2020733191524486", "https://www.facebook.com/groups/1893338250702751", "https://www.facebook.com/groups/internationalcryptominers", "https://www.facebook.com/groups/1829098377306709", "https://www.facebook.com/groups/UcoincashIndonesiaRaya", "https://www.facebook.com/groups/1709996879303044", "https://www.facebook.com/groups/1572466832810159", "https://www.facebook.com/groups/bitcoinworldtm", "https://www.facebook.com/groups/1142220402650653", "https://www.facebook.com/groups/binancecom", "https://www.facebook.com/groups/insidecrypto.news", "https://www.facebook.com/groups/germanbtc", "https://www.facebook.com/groups/595862454626204", "https://www.facebook.com/groups/530659007137021", "https://www.facebook.com/groups/1130482460326432", "https://www.facebook.com/groups/1894175397292966", "https://www.facebook.com/groups/hyip.raj.2"
    ]

 
 for group in groups_links_list:
    driver.get(group)
    sleep(7)
    
    try:
      driver.find_element_by_css_selector("div[class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 ph5uu5jm b3onmgus e5nlhep0 ecm0bbzt ri2l8tne gloz99to r516eku6 k83vx86k'] div div div[class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq s1i5eluu tv7at329']").click()

    except NoSuchElementException: 
      sleep(2)

    sleep(2)
       
    try:
      sleep(4) 
      driver.execute_script("window.scrollTo(0, 200)")
      postbox = driver.find_element_by_xpath("//span[normalize-space()='Write something...']")
      postbox.click()
      sleep(4)

    

      element = driver.switch_to.active_element
    
    
      sleep(4)
      element.send_keys("https://www.facebook.com/photo/?fbid=427505469079207&set=a.427049755791445")
      sleep(6)
      element.send_keys("Sel")
      element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
      sleep(2)
      messages = ['I can not guarantee that you are rich,\nbut I can give you income every day\nDo not miss the opportunity, what are you waiting for? \nBelieve me this is the best platform to invest with now.\nRegister and start earning with the link below\nhttp://www.google.com/search?q=site%3Azendforex.com']
      for message in messages:
        element.send_keys(message)
   
    
    
    
      sleep(5)
      driver.find_element_by_xpath("//div[@aria-label='Remove Post Attachment']//i[@class='hu5pjgll m6k467ps']").click()

    


      postbutton = driver.find_element_by_xpath("//div[@aria-label='Post']")
      sleep(1)
      postbutton.click()
      sleep(7)
    
     
      sleep(400)
    except NoSuchElementException: 
      sleep(2)

    
   
  
   
    
i=i+1  
