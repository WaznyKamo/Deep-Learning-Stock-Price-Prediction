from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


base_url = 'https://www.biznesradar.pl/wskazniki-wartosci-rynkowej/'
stock_list = ['ACP', 'ALE', 'CCC', 'CDR', 'CPS', 'DNP', 'JSW', 'KGHM', 'LPP', 'LTS',
              'MRC', 'OPL', 'PEO', 'PGE', 'PGN', 'PKN', 'PKO', 'PZU', 'SPL', 'TPE']
stock_list = ['ACP']

quarters = []


def get_quarters(soup):
    dates = []
    for date_soup in soup.find_all('th', attrs={"class": "thq h"}):
        dates.append(date_soup.text.split()[0])
    dates.append(soup.find('th', attrs={"class": "thq h newest"}).text.split()[0])
    return(dates)


def get_indicator(soup, indicator_tag):
    indicator_raw = soup.find('tr', attrs={"data-field": indicator_tag})
    indicators = []
    for indicator_soup in indicator_raw.find_all("td", attrs={"class": "h"}):
        if indicator_soup.find("span", attrs={"class": "pv"}):
            indicators.append(indicator_soup.find("span", attrs={"class": "pv"}).text)
        else:
            indicators.append(None)
    return indicators


for stock_index in range(len(stock_list)):
    stock_url = base_url + stock_list[stock_index]
    print(stock_url)
    response = requests.get(stock_url)
    soup = BeautifulSoup(response.text, features='html.parser')
    stock_quarters = get_quarters(soup)
    WK = get_indicator(soup, 'WK')                      # book value
    C_WK = get_indicator(soup, 'CWK')                   # price/book value
    Z = get_indicator(soup, 'Z')                        # profit
    C_Z = get_indicator(soup, 'CZ')                     # price/profit
    P = get_indicator(soup, 'P')                        # income
    C_P = get_indicator(soup, 'CP')                     # price/income
    ZO = get_indicator(soup, 'ZO')                      # operational profit
    C_ZO = get_indicator(soup, 'CZO')                   # price/operational profit
    WK_Graham = get_indicator(soup, 'WKGraham')
    WK_Graham = get_indicator(soup, 'WKGraham')
    WK_Graham = get_indicator(soup, 'WKGraham')
    print(C_Z)
    stock_data = pd.DataFrame(list(zip(stock_quarters, C_WK, C_Z)), columns=['Kwartały', 'Cena/WK', 'Cena/Zysk'])
    print(stock_data)


    # links_with_text = ['http:' + a['href'] for a in soup.find('span') if a.text]  # pobranie wszystkich adresów i edycja ich do czytalnej formy
#
# products_list = []
# products_file = open('products.csv', 'w', newline='', encoding='utf-8')
# products_writer = csv.writer(products_file, delimiter=';')
#
# products_writer.writerow(['ID', 'Nazwa', 'Marka', 'Model', 'Kategoria', 'Opis', 'Cena', 'URL_zdjecia'])
# sizes_writer.writerow(['Product ID', 'Attribute (Name:Position)', 'Value', 'Quantity'])
#
#
# product_id = import_data(polbuty_meskie_urls, 'Męskie@Półbuty', product_id)
# product_id = import_data(sportowe_meskie_urls, 'Męskie@Sportowe', product_id)
# product_id = import_data(lacze_meskie_urls, 'Męskie@Klapki', product_id)
# product_id = import_data(polbuty_damskie_urls, 'Damskie@Półbuty', product_id)
# product_id = import_data(sportowe_damskie_urls, 'Damskie@Sportowe', product_id)
# product_id = import_data(lacze_damskie_urls, 'Damskie@Klapki', product_id)
#
#
# products_file.close()
# sizes_file.close()