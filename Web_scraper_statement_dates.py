from bs4 import BeautifulSoup
import requests
import pandas as pd

# full example url http://infostrefa.com/infostrefa/pl/raporty/espi/firmy/50,2018,0,0,1
url = 'http://infostrefa.com/infostrefa/pl/raporty/espi/firmy/50,2018,0,0,1'
base_url = 'http://infostrefa.com/infostrefa/pl/raporty/espi/firmy/'

stock_list = ['ACP', 'ALE', 'CCC', 'CDR', 'CPS', 'DNP', 'JSW', 'KGHM', 'LPP', 'LTS',
              'MRC', 'OPL', 'PEO', 'PGE', 'PGN', 'PKN', 'PKO', 'PZU', 'SPL', 'TPE']
stock_idx = [50, 2068, 458, 478, 153, 1878, 342, 351, 381, 276,
             1592, 640, 77, 505, 507, 513, 77, 561, 118, 636]
stock_data_list = []

full_statements = pd.DataFrame(columns=['Spółka', 'Data', 'Tytuł', 'Kod'])


def get_info(soup, stock_name):
    statements = pd.DataFrame(columns=['Spółka', 'Data', 'Tytuł', 'Kod'])
    table_soup = soup.find('div', attrs={'class': 'table-text'}).find('tbody')
    for row_soup in table_soup.find_all('tr'):
        if row_soup.find('td', attrs={'class': 'title'}):
            date = row_soup.find('td', attrs={'class': 'title'}).text
        else:
            statement = row_soup.find('a', attrs={'target': '_blank'}).text
            code = row_soup.find_all('td')[1].text
            statements = statements.append({'Spółka': stock_name, 'Data': date, 'Tytuł': statement, 'Kod': code}, ignore_index=True)
    return statements


for stock_number in range(len(stock_list)):
    for year in range(2003, 2022):
        print('Loading data: ' + stock_list[stock_number] + ' (' + str(year) + ')')
        stock_url = base_url + str(stock_idx[stock_number]) + ',' + str(year) + ',0,0,1'

        response_wr = requests.get(stock_url)
        soup_single_site = BeautifulSoup(response_wr.text, features='html.parser')
        yearly_statements = get_info(soup_single_site, stock_list[stock_number])
        full_statements = full_statements.append(yearly_statements)

full_statements.to_csv('Testing_data/WiG20_fundamental_indicators_dates.csv')

