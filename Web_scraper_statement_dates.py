from bs4 import BeautifulSoup
import requests
import pandas as pd

# full example url https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-acp,wId,103,tab,raporty

links = ['https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-acp,wId,103,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-ale,wId,33382,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-alr,wId,8679,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-ccc,wId,2947,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-cdr,wId,1815,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-cps,wId,2807,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-dnp,wId,24814,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-jsw,wId,3022,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-kgh,wId,55,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-lpp,wId,697,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-lts,wId,705,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-mrc,wId,17523,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-opl,wId,111,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-peo,wId,83,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-pge,wId,4096,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-pgn,wId,984,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-pkn,wId,87,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-pko,wId,1062,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-pzu,wId,700,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-san,wId,19431,tab,raporty',
         'https://biznes.interia.pl/gieldy/notowania-gpw/profil-akcji-tpe,wId,4918,tab,raporty']


stock_list = ['ACP', 'ALE', 'ALR', 'CCC', 'CDR', 'CPS', 'DNP', 'JSW', 'KGHM', 'LPP', 'LTS',
              'MRC', 'OPL', 'PEO', 'PGE', 'PGN', 'PKN', 'PKO', 'PZU', 'SAN', 'TPE']

full_statements = pd.DataFrame(columns=['Spółka', 'Data', 'Tytuł'])


def get_info(soup, stock_name):
    statements = pd.DataFrame(columns=['Spółka', 'Data', 'Tytuł'])
    table_soup = soup.find('ul', attrs={'class': 'business-list-article'})
    for row_soup in table_soup.find_all('li', attrs={'class': 'business-list-article-item'}):
        date = row_soup.find_all('span', attrs={'class': 'business-list-article-text'})[0].text.lstrip()
        # print(date)
        statement = row_soup.find('a', attrs={'class': 'business-list-article-link'}).text.lstrip()
        # print(statement)
        statements = statements.append({'Spółka': stock_name, 'Data': date, 'Tytuł': statement}, ignore_index=True)
    return statements


for stock_number in range(len(stock_list)):
    pack_counter = 1
    print('Loading data: ' + stock_list[stock_number])
    while True:
        stock_url = links[stock_number] + ',pack,' + str(pack_counter)
        response_wr = requests.get(stock_url)
        soup_single_site = BeautifulSoup(response_wr.text, features='html.parser')
        if soup_single_site.find('span', attrs={'class': 'business-list-article-error-not-found'}):
            break
        yearly_statements = get_info(soup_single_site, stock_list[stock_number])
        full_statements = full_statements.append(yearly_statements)
        pack_counter += 1

full_statements.to_csv('Testing_data/WiG20_fundamental_indicators_dates.csv', index=False)
