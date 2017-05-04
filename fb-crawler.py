import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
# driver.set_window_size(1120, 550)
# driver.get("https://duckduckgo.com/")
# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
# print driver.page_source.encode('utf-8')

driver.get("XXX")
assert "Facebook" in driver.title


usr = "XXX"
pwd = "XXX"

# elem = driver.find_element_by_id("email")
elem = driver.find_element_by_name("email")
elem.send_keys(usr)
# elem = driver.find_element_by_id("pass")
elem = driver.find_element_by_name("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

count=1
while True:
    print count
    print driver.current_url
    with open('humansofhkust/source' + str(count) + '.html', 'w') as file:
        file.write(driver.page_source.encode("UTF8"))
    with open("humansofhkust/url.txt", "a") as myfile:
        myfile.write('['+ str(count)+'] '+driver.current_url + '\n')
    try:
        driver.find_element_by_link_text("Show more").click()
        driver.get(driver.current_url)
        # driver.save_screenshot('screenie'+ str(count) + '.png')
    except:
        driver.save_screenshot('screenie'+ str(count) + '.png')
        break

    count = count + 1
    time.sleep(1)

# count = 0
# while (count < 3):
#     driver.save_screenshot('screenie'+ str(count) + '.png')
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     count = count + 1
#     time.sleep(5)


# with open('source.txt', 'w') as file:
#     file.write(driver.page_source.encode("UTF8"))
# driver.page_source.encode("UTF8")
# driver.get("https://www.facebook.com/humansofhkust/")

driver.quit()
