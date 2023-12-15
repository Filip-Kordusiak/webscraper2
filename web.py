import bs4
import re
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

def znajdz_ean(tekst):
    start = tekst.find("EAN")
    if start != -1:
        koniec = start + 16
        return tekst[start + 3:koniec]
    else:
        return None


def znajdz_cene(tekst):
    pattern = r'zł&([^&]+) zł'
    matches = re.findall(pattern, tekst)

    # Jeśli znaleźliśmy pasujące wartości, wyświetlamy je
    if matches:
        for match in matches:
            print(match)
        return match
    else:
        return None


def znajdz_numer(tekst):
    pattern = r'Numer części([^&]+) EAN'
    matches = re.findall(pattern, tekst)

        # Jeśli znaleźliśmy pasujące wartości, wyświetlamy je
    if matches:
        for match in matches:
            print(match)
        return match
    else:
        return None


def znajdz_ilosc(tekst):
    pattern = r'Dostępna ilość: (\d+)'
    match = re.search(pattern, tekst)

        # Jeśli znaleziono pasującą wartość, wyświetlamy ją
    if match:
        dostepna_ilosc = match.group(1)
        print("", dostepna_ilosc)
        return dostepna_ilosc
    else:
        return 0


def remove_html_attributes(table):
    soup1 = BeautifulSoup(table, "html.parser")
    for tag in soup1.find_all():
        tag.attrs = {}
    return soup1.prettify()



s = Service('C:\webdriver\chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(
    'www.example.com')
m = browser.find_element("name", 'username')
m.send_keys('username')
time.sleep(0.1)
m1 = browser.find_element("name", 'password')
m1.send_keys('pass')
m1.send_keys(Keys.ENTER)
time.sleep(3)
print("klikło?")

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button primary"]'))).click()
# Znajdź przycisk "Akceptacja Cookies" na stronie


stos_kategorii = []
for i in range(14, 74):
    browser.get(
        f'https://www.example.com/shop-pl/pl/c?page={i}')  # ?page={i}
    print("!!!page", i)
    browser.implicitly_wait(10)

    # o = browser.find_elements((By.XPATH, '//span[@class="kh-m2feck"]'))
    # print(len(o))
    # Znajdź element <select> za pomocą selektora CSS lub innego sposobu
    select_element = browser.find_element(By.CSS_SELECTOR, 'select.ui-select__select.ui-select__select--medium')

    # Stwórz obiekt Select
    select = Select(select_element)

    # Wybierz opcję "Produkty" za pomocą wartości
    select.select_by_value("product")
    browser.implicitly_wait(10)

    ###

    cena = browser.find_elements(By.CSS_SELECTOR, 'div.ui-item-tile-grid-view__price')
    print(len(cena))
    print(cena[0].text)
    browser.implicitly_wait(10)
    element_input = browser.find_elements(By.CSS_SELECTOR, 'input.ui-number-input.ui-number-input--align-center')

    for i in range(0, len(element_input)):
        element_input[i].clear()
        element_input[i].send_keys("100")

        # Wprowadź nową wartość (np. 100) za pomocą metody send_keys()
    element_span = browser.find_elements(By.CSS_SELECTOR, 'span.kh-memyuy')

    # Kliknij na ten element
    for i in range(0, len(element_span)):
        element_span[i].send_keys(Keys.ENTER)

    kod = browser.find_elements(By.CSS_SELECTOR, 'a.ui-link.ui-item-tile__title.ui-item-tile__link.kh-16v7r3f')
    print(kod[0])
    wszystko = ''
    try:
        wszystko = browser.find_elements(By.CSS_SELECTOR, 'div.ui-item-tile-grid-view__container')
    except:
        pass
    producent = ''
    try:
        producent = browser.find_elements(By.CSS_SELECTOR, 'a.ui-link.ui-item-tile__link.kh-16v7r3f')
    except:
        pass

    nazwa = ''
    try:
        nazwa = browser.find_elements(By.CSS_SELECTOR,
                                      'a.ui-link ui-item-tile__link ui-item-tile__description kh-16v7r3f')
    except:
        pass
    ilosc = ''
    try:
        ilosc = browser.find_elements(By.CSS_SELECTOR, 'div.ui-item-tile-grid-view__delivery-times kh-1wla3xl')
    except:
        pass
    cena = ''
    try:
        cena = browser.find_elements(By.CSS_SELECTOR, 'div.ui-item-tile-grid-view__price-grid')
    except:
        pass
    element_a = ''
    try:
        element_a = browser.find_elements(By.CSS_SELECTOR, 'a.ui-link.ui-item-tile__figure__thumbnail_container')
    except:
        pass

    more_info = browser.find_elements(By.CSS_SELECTOR,
                                      'button.ui-button.ui-button--no-shadow.ui-button--secondary.ui-button--xsmall.kh-tzh4f1')




    for i in range(0, len(kod)):
        print(kod[i].text)
        print(len(kod))
        print(wszystko[i].text)
        print(len(wszystko))
        html = element_a[i].get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        zmienna_pomocnicza = wszystko[i].text.find("cena")

        try:
            img_src = soup.find('img')['src']
            print("Link do obrazu:", img_src)

            # tutaj trzeba  zrobic znajdz dla wrażliwych danych takie jak cena ilość i w sumie tyle,

            response = requests.get(img_src)

            # Sprawdź, czy pobieranie zakończyło się sukcesem (kod odpowiedzi 200)
            if response.status_code == 200:
                # Zapisz zawartość obrazu do pliku
                if not os.path.exists('img'):
                    # Jeśli nie istnieje, stwórz go
                    os.makedirs('img')
                with open(f'img/{kod[i].text}.jpg', 'wb') as file:
                    file.write(response.content)
                print("Obraz został pomyślnie pobrany i zapisany jako 'nazwa_obrazu.jpg'")
            else:
                print("Błąd podczas pobierania obrazu:", response.status_code)
        except:
            pass

        # img_src = soup.find_all('img')
        # print("Link do obrazu:", img_src)

        # tutaj trzeba zrobic znajdz dla wrażliwych danych takie jak cena ilość i w sumie tyle,

        # print(nazwa[i].text)
        # print(ilosc[i].text)
        # print(cena[i].text)
        more_info[i].send_keys(Keys.ENTER)
        time.sleep(3)
        #################

        ################

        try:
            time.sleep(5)
            tabelka = browser.find_element(By.CSS_SELECTOR, 'table.kh-1xzm1su')  # to tabelka po kliknięciu
            print(tabelka.text)
            html = tabelka.get_attribute('outerHTML')

            zdjecia = browser.find_element(By.CSS_SELECTOR, 'div.kh-1vrm80b')
            print("", zdjecia.text)
        except:
            tabelka = 't'
        soup = bs4.BeautifulSoup(html, "html.parser")
        # print("AAAAAAAAAAAAAAAAA", soup)  # remove_html_attributes(table)#to dodać do csv
        # print("AAAAAAAAAAAAAAAAAXDXDXDXDXD", "<table>", remove_html_attributes(str(soup)), "</table>")  # to dodać do csv
        # print("DDDDDDDDDDDD", soup.text)
        print("ean", znajdz_ean(soup.text))  # to dodać do csv
        EAN1 = znajdz_ean(soup.text)
        KOD1 = znajdz_numer(soup.text)
        HTML = remove_html_attributes(str(soup))
        nazwaa = ''

        try:
            nazwaa = browser.find_element(By.CSS_SELECTOR, 'h1.kh-7wamzb').text
        except:
            try:
                nazwaa = browser.find_element(By.CSS_SELECTOR, 'h1.kh-1oteowz').text
            except:
                pass

        try:
            xd = tabelka.text
        except:
            print("")
            xd = ""
            pass

        webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
        # more_info1 = browser.find_element(By.CSS_SELECTOR,'button.ui-button.ui-button--no-shadow.ui-button--close.ui-button--medium.kh-tzh4f1')
        # more_info1.send_keys(Keys.ENTER)
        with open('dane.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')

            data_list = wszystko[i].text
            tekst_jedna_linia = data_list.replace("\n", "&")
            data_list1 = x
            tekst_jedna_linia1 = data_list1.replace("\n", "&")
            print("", tekst_jedna_linia)
            tekst_jedna_linia = [tekst_jedna_linia]
            tekst_jedna_linia1 = [tekst_jedna_linia1]
            x = list()
            x1 = list()
            paa = str(tekst_jedna_linia) + "&" + str(tekst_jedna_linia1)
            # xdd.append(tekst_jedna_linia)
            # xdd.append("&")
            # xdd.append(tekst_jedna_linia1)
            xdd.append(p)
            # csv_writer.writerows(xdd)

            print("cena", znajdz_cene(p))  # to dodać do csv
            print("cena", znajdz_ilosc(p))  # to dodać do csv

            xdd.append(p)
            HTML = HTML.replace("\n", "")
            lol = str(nazwaa) + "&" + str(KOD1) + "& " + str(znajdz_cene(p)) + "&" + str(
                znajdz_ilosc(p)) + "&" + str(EAN1) + "&" + str(HTML)

            xddd.append(lol)
            csv_writer.writerows(x1)

        # more_info[i].send_keys(Keys.ESCAPE)

    """
    
    
    
    """
