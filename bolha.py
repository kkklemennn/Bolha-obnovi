from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.bolha.com/moja-bolha/uporabnik/moji-oglasi/neaktivni-oglasi')

uporabnik = driver.find_element_by_xpath('//*[@id="login-username"]')
uporabnik.send_keys('uporabnik')

geslo = driver.find_element_by_xpath('//*[@id="login-password"]')
geslo.send_keys('geslo')

prijava = driver.find_element_by_xpath('//*[@id="login-submitButton"]')
prijava.click()

driver.get('https://www.bolha.com/moja-bolha/uporabnik/moji-oglasi/potekli-oglasi')
#driver.get('https://www.bolha.com/moja-bolha/uporabnik/moji-oglasi/neaktivni-oglasi')

potekli = driver.find_element_by_class_name('UserEntityList-itemCount').text
stPoteklih = int(''.join(filter(str.isdigit, potekli)))

while(stPoteklih > 0):
    driver.get('https://www.bolha.com/moja-bolha/uporabnik/moji-oglasi/potekli-oglasi')
    potekli = driver.find_element_by_class_name('UserEntityList-itemCount').text
    stPoteklih = int(''.join(filter(str.isdigit, potekli)))
    time.sleep(1.2)
    obnovi = driver.find_elements_by_xpath(".//*[text()='Obnovi']")
    if (len(obnovi) > 0):
        obnovi[0].click()
        time.sleep(1.2)
        obnoviOglas = driver.find_element_by_xpath('//*[@id="ad-submitButton"]')
        obnoviOglas.click()
        time.sleep(1.2)
