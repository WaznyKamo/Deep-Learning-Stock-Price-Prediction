from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# full example url http://infostrefa.com/infostrefa/pl/raporty/espi/firmy/50,2018,0,0,1
url = 'http://infostrefa.com/infostrefa/pl/raporty/espi/firmy/50,2018,0,0,1'
base_url = 'http://infostrefa.com/infostrefa/pl/raporty/espi/firmy/'

stock_list = ['ACP', 'ALE', 'CCC', 'CDR', 'CPS', 'DNP', 'JSW', 'KGHM', 'LPP', 'LTS',
              'MRC', 'OPL', 'PEO', 'PGE', 'PGN', 'PKN', 'PKO', 'PZU', 'SPL', 'TPE']
stock_idx = [50, 2068, 458, 478, 153, 1878, 342, 351, 381, 276,
             1592, 640, 77, 505, 507, 513, 77, 561, 118, 636]
stock_data_list = []

quarters = []
full_statements = pd.DataFrame(columns=['Stock', 'Date', 'Statement'])


def get_info(soup, stock_name):
    statements = pd.DataFrame(columns=['Stock', 'Date', 'Statement'])
    dates = []
    table_soup = soup.find('div', attrs={'class': 'table-text'}).find('tbody')
    for row_soup in table_soup.find_all('tr'):
        if row_soup.find('td', attrs={'class': 'title'}):
            date = row_soup.find('td', attrs={'class': 'title'}).text
        else:
            statement = row_soup.find('a', attrs={'target': '_blank'}).text
            # print(str(date) + ': ' + statement + ', ' + stock_name)
            statements = statements.append({'Stock': stock_name, 'Date': date, 'Statement': statement}, ignore_index=True)
    return statements


for stock_number in range(len(stock_list)):
    for year in range(2003, 2022):
        print('Loading data: ' + stock_list[stock_number] + ' (', + str(year) + ')')
        stock_url = base_url + str(stock_idx[stock_number]) + ',' + str(year) + ',0,0,1'

        response_wr = requests.get(stock_url)
        soup_single_site = BeautifulSoup(response_wr.text, features='html.parser')
        yearly_statements = get_info(soup_single_site, stock_list[stock_number])
        full_statements = full_statements.append(yearly_statements)

#         # Market value indicators
#         WK = get_indicator(soup_wr, 'WK')                      # book value
#         C_WK = get_indicator(soup_wr, 'CWK')                   # price/book value
#         Z = get_indicator(soup_wr, 'Z')                        # profit
#         C_Z = get_indicator(soup_wr, 'CZ')                     # price/profit
#         P = get_indicator(soup_wr, 'P')                        # income
#         C_P = get_indicator(soup_wr, 'CP')                     # price/income
#         ZO = get_indicator(soup_wr, 'ZO')                      # operational profit
#         C_ZO = get_indicator(soup_wr, 'CZO')                   # price/operational profit
#         WK_Graham = get_indicator(soup_wr, 'WKGraham')
#         C_WK_Graham = get_indicator(soup_wr, 'CWKGraham')
#         EV = get_indicator(soup_wr, 'EV')
#         EV_P = get_indicator(soup_wr, 'EVP')
#         EV_EBIT = get_indicator(soup_wr, 'EVEBIT')
#         EV_EBITDA = get_indicator(soup_wr, 'EVEBITDA')
#         stock_data = pd.DataFrame(list(zip(stock_quarters, WK, C_WK, Z, C_Z, P, C_P, ZO, C_ZO, WK_Graham, C_WK_Graham, EV, EV_P, EV_EBITDA, EV_EBIT)),
#                                   columns=['Kwartały', 'Wartość księgowa', 'Cena/WK', 'Zysk','Cena/Zysk', 'Przychód', 'Cena/Przychód', 'Zysk operacyjny', 'Cena/Zysk operacyjny', 'Wartość księgowa Grahama',
#                                            'Cena/Wartość księgowa Grahama', 'Wartość przedsiębiorstwa', 'Wartość przedsiębiorstwa/Przychody', 'Wartość przedsiębiorstwa/EBIT', 'Wartość przedsiębiorstwa/EBITDA'])
#         stock_data.insert(0, 'Spółka', stock_list[stock_index])
#         # Profitability indicators
#         stock_url_rentownosc = url_rentownosc + stock_list[stock_index]
#         response_rentownosc = requests.get(stock_url_rentownosc)
#         soup_rentownosc = BeautifulSoup(response_rentownosc.text, features='html.parser')
#         stock_data['ROE'] = get_indicator(soup_rentownosc, 'ROE')
#         stock_data['ROA'] = get_indicator(soup_rentownosc, 'ROA')
#         stock_data['Marża zysku operacyjnego'] = get_indicator(soup_rentownosc, 'OPM')
#         stock_data['Marża zysku netto'] = get_indicator(soup_rentownosc, 'ROS')
#         stock_data['Marża zysku ze sprzedaży'] = get_indicator(soup_rentownosc, 'RS')
#         stock_data['Marża zysku brutto'] = get_indicator(soup_rentownosc, 'GPM')
#         stock_data['Marża zysku brutto ze sprzedaży'] = get_indicator(soup_rentownosc, 'RBS')
#         stock_data['Rentowność operacyjna aktywów'] = get_indicator(soup_rentownosc, 'ROPA')
#         # Cash flow indicators
#         stock_url_pp = url_przeplywy_pieniezne + stock_list[stock_index]
#         response_pp = requests.get(stock_url_pp)
#         soup_pp = BeautifulSoup(response_pp.text, features='html.parser')
#         stock_data['Udział zysku netto w przepływach operacyjnych'] = get_indicator(soup_pp, 'ZNPO')
#         stock_data['Wskaźnik źródeł finansowania inwestycji'] = get_indicator(soup_pp, 'ZFI')
#         # Liabilities indicators
#         stock_url_zadluzenie = url_zadluzenie + stock_list[stock_index]
#         response_zadluzenie = requests.get(stock_url_zadluzenie)
#         soup_zadluzenie = BeautifulSoup(response_zadluzenie.text, features='html.parser')
#         stock_data['Zadłużenie ogólne'] = get_indicator(soup_zadluzenie, 'DTAR')
#         stock_data['Zadłużenie kapitału własnego'] = get_indicator(soup_zadluzenie, 'CG')
#         stock_data['Zadłużenie długoterminowe'] = get_indicator(soup_zadluzenie, 'LDER')
#         stock_data['Zadłużenie środków trwałych'] = get_indicator(soup_zadluzenie, 'PZAT')
#         stock_data['Pokrycie aktywów trwałych kapitałami stałymi'] = get_indicator(soup_zadluzenie, 'PELDR')
#         stock_data['Trwałość struktury finansowania'] = get_indicator(soup_zadluzenie, 'TSF')
#         stock_data['Zastosowanie kapitału obcego'] = get_indicator(soup_zadluzenie, 'ZKO')
#         stock_data['Wskaźnik ogólnej sytuacji finansowej'] = get_indicator(soup_zadluzenie, 'OSF')
#         stock_data['Zadłużenie netto'] = get_indicator(soup_zadluzenie, 'NetDebt')
#         stock_data['Zadłużenie netto / EBITDA'] = get_indicator(soup_zadluzenie, 'NetDebtEBITDA')
#         stock_data['Zadłużenie finansowe netto'] = get_indicator(soup_zadluzenie, 'DebtFin')
#         stock_data['Zadłużenie finansowe netto / EBITDA'] = get_indicator(soup_zadluzenie, 'DebtFinEBITDA')
#         # Liquidity indicators
#         stock_url_plynnosc = url_plynnosc + stock_list[stock_index]
#         response_plynnosc = requests.get(stock_url_plynnosc)
#         soup_plynnosc = BeautifulSoup(response_plynnosc.text, features='html.parser')
#         stock_data['I stopień pokrycia'] = get_indicator(soup_plynnosc, 'SP1')
#         stock_data['II stopień pokrycia'] = get_indicator(soup_plynnosc, 'SP2')
#         stock_data['Płynność gotówkowa'] = get_indicator(soup_plynnosc, 'CAR')
#         stock_data['Płynność szybka'] = get_indicator(soup_plynnosc, 'QR')
#         stock_data['Płynność bieżąca'] = get_indicator(soup_plynnosc, 'CR')
#         stock_data['Płynność podwyższona'] = get_indicator(soup_plynnosc, 'PP')
#         stock_data['Pokrycie zobowiązań należnościami'] = get_indicator(soup_plynnosc, 'RCLR')
#         stock_data['Udział kapitału pracującego w aktywach'] = get_indicator(soup_plynnosc, 'KP')
#         # Activity indicators
#         stock_url_aktywnosc = url_aktywnosc + stock_list[stock_index]
#         response_aktywnosc = requests.get(stock_url_aktywnosc)
#         soup_aktywnosc = BeautifulSoup(response_aktywnosc.text, features='html.parser')
#         stock_data['Pokrycie kosztów kapitałem obrotowym'] = get_indicator(soup_aktywnosc, 'PKKO')
#         stock_data['Rotacja należności'] = get_indicator(soup_aktywnosc, 'RN')
#         stock_data['Cykl należności'] = get_indicator(soup_aktywnosc, 'CRN')
#         stock_data['Cykl zobowiązań'] = get_indicator(soup_aktywnosc, 'CPZ')
#         stock_data['Rotacja zapasów'] = get_indicator(soup_aktywnosc, 'RZ')
#         stock_data['Cykl zapasów'] = get_indicator(soup_aktywnosc, 'CRZ')
#         stock_data['Rotacja majątku obrotowego'] = get_indicator(soup_aktywnosc, 'RMO')
#         stock_data['Rotacja majątku trwałego'] = get_indicator(soup_aktywnosc, 'RMT')
#         stock_data['Rotacja majątku ogółem'] = get_indicator(soup_aktywnosc, 'RM')
#         stock_data['Cykl operacyjny'] = get_indicator(soup_aktywnosc, 'COP')
#         stock_data['Cykl konwersji gotówki'] = get_indicator(soup_aktywnosc, 'CSP')
#
#     stock_data_list.append((stock_data))
#
# final_dataframe = pd.concat(stock_data_list)
#
full_statements.to_csv('Testing_data/WiG20_fundamental_indicators_dates.csv')
# print('File created')
