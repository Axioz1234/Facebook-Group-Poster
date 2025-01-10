import time
from telnetlib import EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
import win32clipboard
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    # Set up Facebook login account name and password
    account = "newarchcity.2021@gmail.com"
    password = "N.A.C_%%"

    # Set up Facebook groups to post, you must be a member of the group
    groups_alShrouk = [
        "https://www.facebook.com/groups/762815287148079/",  # 1
        "https://www.facebook.com/groups/652587505607964/",  # 2
        "https://www.facebook.com/groups/1008175969226970/",  # 3
        "https://www.facebook.com/groups/2288258627945258/",  # 4
        "https://www.facebook.com/groups/287286348731941/",  # 5
        "https://www.facebook.com/groups/3ayezsha22/",  # 6
        "https://www.facebook.com/groups/2426858454077659/",  # 7
        "https://www.facebook.com/groups/1775995265945290/",  # 8
        "https://www.facebook.com/groups/buysellrealestates/",  # 9
        "https://www.facebook.com/groups/ueworks/",  # 10
        "https://www.facebook.com/groups/1603465469897474/",  # 11
        "https://www.facebook.com/groups/1602843280021990/",  # 12
        "https://www.facebook.com/groups/1602235606655080/",  # 13
        "https://www.facebook.com/groups/1277302602326609/",  # 14
        "https://www.facebook.com/groups/1051490108369992/",   # 15
        "https://www.facebook.com/groups/874191472675591/",  # 16
        "https://www.facebook.com/groups/houserealestate/",  # 17
        "https://www.facebook.com/groups/WhatsUp.EGYPT.Real.Estate/",  # 18
        "https://www.facebook.com/groups/722283927913028/",  # 19
        "https://www.facebook.com/groups/sokan.elshorok/",  # 20
        "https://www.facebook.com/groups/630080997013053/",  # 21
        "https://www.facebook.com/groups/Cvhatrealestate/",  # 22
        "https://www.facebook.com/groups/578634225978689/",  # 23
        "https://www.facebook.com/groups/mrsre/",  # 24
        "https://www.facebook.com/groups/538237826350825/",  # 25
        "https://www.facebook.com/groups/brokers.egypt/",  # 26
        "https://www.facebook.com/groups/430879577096890/",  # 27
        "https://www.facebook.com/groups/430428323828129/",  # 28
        "https://www.facebook.com/groups/356463258348706/",  # 29
        "https://www.facebook.com/groups/305303532986499/",  # 30
        "https://www.facebook.com/groups/290010758316778/",  # 31
        "https://www.facebook.com/groups/newcairoo/",  # 32
        "",  # 33
        "",  # 34
        ""  # 35
    ]

    groups_alTagmo3 = [
        "https://www.facebook.com/groups/1008175969226970/",  # 1
        "https://www.facebook.com/groups/320769232008646/",  # 2
        "https://www.facebook.com/groups/newcairo/",  # 3
        "https://www.facebook.com/groups/2923476221211807/",  # 4
        "https://www.facebook.com/groups/1987637021514797/",  # 5
        "https://www.facebook.com/groups/1751529888455373/?multi_permalinks=3085643488377333",  # 6
        "https://www.facebook.com/groups/1723316004560385/",  # 7
        "https://www.facebook.com/groups/buysellrealestates/",  # 8
        "https://www.facebook.com/groups/emtlkaqar01013047445/",  # 9
        "https://www.facebook.com/groups/1625082647712052/",  # 10
        "https://www.facebook.com/groups/ueworks/",  # 11
        "https://www.facebook.com/groups/1603465469897474/",  # 12
        "https://www.facebook.com/groups/1602843280021990/",  # 13
        "https://www.facebook.com/groups/1602235606655080/",  # 14
        "https://www.facebook.com/groups/1556335304417794/",  # 15
        "https://www.facebook.com/groups/874191472675591/",  # 16
        "https://www.facebook.com/groups/houserealestate/",  # 17
        "https://www.facebook.com/groups/WhatsUp.EGYPT.Real.Estate/",  # 18
        "https://www.facebook.com/groups/771147612934105/",  # 19
        "https://www.facebook.com/groups/722283927913028/",  # 20
        "https://www.facebook.com/groups/Cvhatrealestate/",  # 21
        "https://www.facebook.com/groups/mrsre/",  # 22
        "https://www.facebook.com/groups/brokers.egypt/",  # 23
        "https://www.facebook.com/groups/185229848351744/",  # 24
        "https://www.facebook.com/groups/newcairoo/",  # 25
        "",  # 26
        "",  # 27
        "",  # 28
        ""
    ]

    # Set up paths of images to post
    images_list = [
        "G:/Building No. 61 & 62/Building No. 62/20211101_115416.jpg",
        "",
        ""
    ]

    # User input if shorouk or tagmo3
    groupType = input("Please Enter if you want Al Shrouk (1) or Al Tagmo3(2): ")
    while (groupType != '1') and (groupType != '2'):
        groupType = input("please enter 1 for Al shrouk Groups or 2 for Al Tagmo3 Groups ")

    # Set up text content to post
    print("Please Enter The Text: ")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    message = '\n'.join(lines)

    # Login Facebook
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.facebook.com')

    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(account)
    passelement = driver.find_element(By.XPATH, '//*[@id="pass"]')
    passelement.send_keys(password)
    passelement.send_keys(Keys.RETURN)
    time.sleep(2)

    # Counter to know how many posts posted
    counter = 0

    # If shourouk or tagamo3
    if groupType == 1 :
        GroupsLoop(groups_alShrouk, driver, message, images_list, counter)
    else :
        GroupsLoop(groups_alTagmo3, driver, message, images_list, counter)

    # Close driver
    driver.close()


def GroupsLoop(group_links_list, driver, message, images_list, counter):
    # Post on each group
    for group in group_links_list:
        whichTab(driver)
        counter = counter + 1
        try:
            postingProcess(group, driver, message, images_list, counter)
        except():
            time.sleep(40)
            postingProcess(group, driver, message, images_list, counter)
    while True:
        if hasXpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div[2]/div[1]", driver):
            time.sleep(5)
        else:
            break


def send_to_clipboard(clip_type, data):
    try:
        win32clipboard.OpenClipboard()
    except:
        time.sleep(1)
        win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def hasXpath(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


def goingToPostLayout(driver):
    # Public Post xPath
    createPublicPost = "//span[contains(text(),'Create a public post…')]"
    discussUnderSell = "//span[contains(text(),'Start Discussion')]"
    discussionButton = "//a[@aria-hidden='false']//span[@dir='auto'][normalize-space()='Discussion']"
    moreOption = "//body/div/div/div/div/div/div/div/div/div/div[@aria-label='Preview of a Group']/div/div/div[@role='main']/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
    discussionOption = "//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[@role='menu']/div/div/div[@aria-hidden='false']/div/div/div/a[6]/div[1]"
    whatsOnYourMind = "(//div[@class='oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl orhb3f3m czkt41v7 fmqxjp7s emzo65vh l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'])[1]"
    element = driver.find_element(By.XPATH, "(//span[contains(text(),'Joined')])[1]")
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(0.5)
    # if default page
    if hasXpath(createPublicPost, driver):
        driver.find_element(By.XPATH, createPublicPost).click()
    # if not a default Group, Sell & Buy Under it discuss it
    elif hasXpath(discussUnderSell, driver):
        driver.find_element(By.XPATH, discussUnderSell).click()
    # if discuss is on the list
    elif hasXpath(discussionButton, driver):
        # driver.find_element(By.XPATH, discussionButton).click()
        driver.find_element(By.XPATH, discussionButton).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, whatsOnYourMind)))
        driver.find_element(By.XPATH, whatsOnYourMind).click()
    # One with 'more' option
    elif hasXpath(moreOption, driver):
        driver.find_element(By.XPATH, moreOption).click()
        driver.find_element(By.XPATH, discussionOption).click()
    else:
        if hasXpath(createPublicPost, driver):
            driver.find_element(By.XPATH, createPublicPost).click()
        # if not a default Group, Sell & Buy Under it discuss it
        elif hasXpath(discussUnderSell, driver):
            driver.find_element(By.XPATH, discussUnderSell).click()
        # if discuss is on the list
        elif hasXpath(discussionButton, driver):
            # driver.find_element(By.XPATH, discussionButton).click()
            driver.find_element(By.XPATH, discussionButton).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, whatsOnYourMind)))
            driver.find_element(By.XPATH, whatsOnYourMind).click()
        # One with 'more' option
        elif hasXpath(moreOption, driver):
            driver.find_element(By.XPATH, moreOption).click()
            driver.find_element(By.XPATH, discussionOption).click()
        else:
            print("sorry there is no such group type in my program")

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, writeYourPost)))
    # driver.find_element(By.XPATH, writeYourPost)


def postingProcess(group, driver, message, images_list, counter):
    if group == "" or group == " ":
        return

    driver.get(group)
    # Freeze if the internet is slow
    time.sleep(1.5)

    # Printing the name of the page
    try:
        print(str(counter) + " Now Trying in Page : " + driver.find_element(By.CSS_SELECTOR, ".oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.hnhda86s").text)
    except:
        time.sleep(3)
        print(str(counter) + " Now Trying in Page : " + driver.find_element(By.CSS_SELECTOR, ".oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8.hnhda86s").text)

    # Calling Function
    goingToPostLayout(driver)

    time.sleep(0.5)

    # Typing Post Content
    while True:
        if hasXpath("//div[@data-block='true']//div", driver):
            break
    postBox = driver.find_element_by_xpath("//div[@data-block='true']//div").send_keys(message)

    for photo in images_list:
        # Coping photo to clipboard
        if photo == "" or photo == " ":
            break
        image = Image.open(photo)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)

        # Pasting photo in facebook
        time.sleep(1)
        driver.find_element_by_xpath("//span[@data-text='true']").send_keys(Keys.CONTROL + "v")
        time.sleep(1)

    # Pressing Exit for Testing
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/i").click()

    # Clicking post button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div/div[1]/div/span/span").click()
    print("Posting")

    time.sleep(1)


def whichTab(driver):
    handles = driver.window_handles
    size = len(handles)
    while True:
        for x in range(size):
            if handles[x] != driver.current_window_handle:
                driver.switch_to.window(handles[x])
            # Check if posting process is still going
            if hasXpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div[2]/div[1]", driver):
                continue
            return
        if size < 5:
            driver.execute_script('''window.open("https://www.facebook.com")''')
            driver.switch_to.window(driver.window_handles[size])
            time.sleep(1)
            return
        print("Searching For a Free Tab")
        time.sleep(7)


if __name__ == '__main__':
    main()
