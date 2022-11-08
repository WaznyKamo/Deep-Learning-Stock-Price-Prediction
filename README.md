# Stock Price Prediction Using LSTM Deep Learning Network

A multivariate prediction of stock prices using neural network.

## Enviroment:

The project was made in Anaconda enviroment, expanded with keras-gpu library. Machine learning and analysis was performed in Jupyter Notebooks and web scraping in Python files in Pycharm IDE. Calculations were done on RTX 3080 graphics card, so some changes in code might be needed in order to perform learning in diffrent enviroment.

## Data acquisition:

The project uses data from many sources in order to give many diffrent approaches for prediction and see what performs best. 

Data type and its source:
  * Stock prices (opening, closing, highest, lowest) and volume - daily prices and volumes from a single session. Data downloaded from https://stooq.pl
  * Technical indicators - values calculated from stock prices and volume. The formulas written in code can be seen in Technical_indicators_tuning.ipynb file
  * Fundamental indicators - indicators and their values collected https://www.biznesradar.pl/ using web scraping (exact adresses can be seen in the Web_scraper_for_fundamental_indicators.py file)
  * Dates of financial reports - Fundamental indicators were provided only with year and quarter as a date. In order to know precisely when the data impacted the daily stock prices we needed to know the dates of financial reports. They were collected from https://biznes.interia.pl/ using web scraping (exact addresses can be seen in Web_scraper_statement_dates.py file)
  * Game premieres - data collected by hand from Google and Steam

## Predicting the future:

Algorithm uses daily data from past 60 sessions and makes predictions 1-day ahead. We can predict furhter in the future using results from preceding days, although, that leads to errors building up, resulting in less accuracy.

Tested parameters were:
  * Type of data (prices, indicators, outside events) listed above in Data acquisition chapter
  * Amount and category of stock data - training on single company (CD Projekt), 20 biggest companies from WiG20 and companies from gaming sector in order to see the impact of more specific or general data and amount of data used for training
  * Architecture of a Neural Network

## Results and predictions evaluation

Most prediction algorithms found on the internet do not have any way of evaluating the usability of the model. In order to see if the predictions have any added value for a investor, they were compared with Naive predictions - assuming that the prices will not change in a following sessions. Error lower than that will at least induce, that the direction of price change is correct. Lastly the predictions were compared with another simple method - linear regression.

Neural Network architecture that performed the best:
 * Input layer
 * LSTM with 64 neurons
 * Dense with 100 neurons
 * Dense with 5 output neurons (predicting opening, closing, highest, lowest prices and volume of the next session)


