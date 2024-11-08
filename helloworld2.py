from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from constant import addressArray
from sys import platform
import os
import shutil
from progress.bar import Bar
from zipfile import ZipFile

cwd = os.getcwd()
downloadPath = str(cwd) + os.path.sep + "Downloads"
newpath = downloadPath + '/ComedFiles'

# Create ChromeOptions object that specifies where we files should
# we downloaded (this is to the current path) -- if we just downloaded
# to our own `Downloads` directories everyone would have to rewrite the
# program for their own machines (not good)
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--no-proxy-server')
prefs = {"download.default_directory" : downloadPath}
chromeOptions.add_experimental_option("prefs",prefs)

print(len(addressArray))

def downloadPLCs():
    import os

    try: shutil.rmtree("Downloads")
    except: pass
    os.mkdir("Downloads")

    if platform == "darwin":
        driver = webdriver.Chrome(
            executable_path="./chromedriver", chrome_options=chromeOptions)
    elif platform == "win32" or platform == "win64":
        driver = webdriver.Chrome(
            executable_path="./chromedriver.exe", chrome_options=chromeOptions)
    else:
        driver = webdriver.Chrome(
            executable_path="./chromedriver", chrome_options=chromeOptions)
    driver.get('https://secure.comed.com/MyAccount/MyService/Pages/UsageDataTool.aspx')

    # for explicit waits
    def wait_for_clickable(by, s, timeout=10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, s)))

    # Recursive solution to ensure that each and every account number is fetched
    # This function is called to ensure that an account number which is interrupted
    # account number search is completed
    def completeAcct(acct):
        try:
            acctBox = wait_for_clickable(By.ID, 'AccountNumber')
            addBtn = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Addbtn')
            acctBox.send_keys(acct)
            addBtn.click()
        except:
            noThanksBox = wait_for_clickable(By.XPATH, '//*[@title="No, thanks"]')
            noThanksBox.click()
            completeAcct(acct)

    def getDownloadButton():
        try:
            noThanksBox = wait_for_clickable(By.XPATH, '//*[@title="No, thanks"]')
            noThanksBox.click()
        except:
            pass

        button = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Downloadbtn')
        return button

    chkBox = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_RequestOption_0')
    chkBox.click()

    iter = 0
    acctBox = wait_for_clickable(By.ID, 'AccountNumber')
    addBtn = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Addbtn')

    keysToPop = set()

    for acct in Bar('Downloading Accounts').iter(addressArray.keys()):
        if iter < 10:
            # if len(acct) != 10:
                # keysToPop.add(acct)
                # continue

            try:
                acctBox = wait_for_clickable(By.ID, 'AccountNumber')
                addBtn = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Addbtn')
                acctBox.send_keys(acct)
                addBtn.click()
                iter = iter + 1
            except:
                # Click out of feedback window
                noThanksBox = wait_for_clickable(By.XPATH, '//*[@id="acsFocusFirst"]')
                noThanksBox.click()
                completeAcct(acct)
                iter = iter + 1
                continue

            errorMessage = None
            try:
                errorMessage = wait_for_clickable(By.ID, "ctl00_ctl89_g_86daaf10_fb31_4f6d_adf3_d7c384f128a3_ctl00_lblValMsg")
            except:
                try:
                    errorMessage = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_pnlError')
                except:
                    pass

            if errorMessage is not None:
                #print("error")
                #print(acct)
                keysToPop.add(acct)

        else:
            downloadBtn = getDownloadButton()
            downloadBtn.click()
            sleep(1)
            driver.get('https://secure.comed.com/MyAccount/MyService/Pages/UsageDataTool.aspx')

            chkBox = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_RequestOption_0')
            chkBox.click()

            iter = 0
            try:
                acctBox = wait_for_clickable(By.ID, 'AccountNumber')
            except:
                noThanksBox = wait_for_clickable(By.XPATH, '//*[@title="No, thanks"]')
                noThanksBox.click()
                acctBox = wait_for_clickable(By.ID, 'AccountNumber')

            addBtn = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Addbtn')
            acctBox.send_keys(acct)
            iter = iter + 1
            addBtn.click()
            acctBox = wait_for_clickable(By.ID, 'AccountNumber')
            addBtn = wait_for_clickable(By.ID, 'ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Addbtn')

    if iter > 0:
        downloadBtn = getDownloadButton()
        downloadBtn.click()
        sleep(1)

    #print("Removed keys/accounts:")
    #print(keysToPop)

    for key in keysToPop:
        addressArray.pop(key, None)

    import os
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    # Ensure file is finished downloading
    from math import ceil
    while len(list(filter(lambda x: x.endswith('zip'), os.listdir(downloadPath)))) != ceil(len(addressArray) / 10):
        sleep(1)
    driver.quit()

def unzipSummaries():
    import zipfile
    counter = 0
    for file in os.listdir(downloadPath):
        if os.path.isfile(os.path.join(downloadPath + '/', file)) and 'SummaryUsageData' in file:
            os.rename(os.path.join(downloadPath + '/', file), os.path.join(downloadPath + '/', 'file' + str(counter)) + '.zip')
            counter += 1
    for file in os.listdir(downloadPath):
        if os.path.isfile(os.path.join(downloadPath + '/', file)):
            acctBundle = zipfile.ZipFile(downloadPath + '/' + file, 'r')
            acctBundle.extractall(newpath)
            acctBundle.close()
            os.remove(downloadPath  + '/' + file)
#downloadPLCs()
unzipSummaries()

import useDownloaded 
#useDownloaded.create_workbook()

