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
 * LSTM with 32 neurons
 * LSTM with 32 neurons
 * Dense with 32 neurons
 * Dense with 5 output neurons (predicting opening, closing, highest, lowest prices and volume of the next session)

The model performed best with input features of stock prices, volume and game premiere dates. Technical and fundamental indicators did not improve it's predictions. This may be due to:
 * Technical indicators are values calculated from stock prices and volume. They do not bring any new information, only it's simplification. It is possible that the Neural Network finds patterns in raw data better.
  * Fundamental indicators change their values in a quarterly manner. It may be too long window to find it's impact on daily prices, as only 60 days were taken into account. This means that for many input vectors the fundamental features did not change at all, in others only once. There is also effect of anticipation. Investors can expect that financial reports will change in some manner, due to socio-political events, which a Neural Network do not take into account.
  
As game premiere dates reduce greatly usability of this model to only days around the date of premiere, the model was evaluated solely on stock prices and volumes of biggest Polish companies from WiG20 stock index.

For better comparision of Neural Network and Naive prediction, measure of information gain was introduced. The greater the information gain, the better did Neural Network perform. Negative value means that naive predictions performed better.

Information gain = (MAE_Naive - MAE_NN)/MAE_Naive * 100%


| Number of forcasted session  | Information gain of NN (%)  |                       |                       |                        |          |
|----------------------------|--------------------------------------------------------|-----------------------|-----------------------|------------------------|----------|
|                            | Opening price                                    | Highest price | Lowest price  | Closing price  | Volume  |
| 1                          | 43,6933                                                | 10,4783               | 11,9687               | 0,3062                 | 18,6151  |
| 2                          | 17,4060                                                | 3,8000                | 5,9033                | 0,3384                 | 26,2771  |
| 3                          | 11,5055                                                | 2,4550                | 3,3356                | -0,0948                | 27,1580  |
| 4                          | 8,1708                                                 | 0,8308                | 2,3094                | -1,4812                | 26,0574  |
| 5                          | 6,5557                                                 | 0,7612                | 1,3654                | -1,2843                | 25,0045  |
| 6                          | 4,9299                                                 | 0,3910                | 0,6491                | -1,4797                | 28,3689  |
| 7                          | 4,2896                                                 | 0,4709                | 0,5188                | -1,3329                | 29,8907  |
| 8                          | 3,6450                                                 | 0,2078                | -0,1016               | -1,4224                | 29,8691  |
| 9                          | 3,3129                                                 | 0,4167                | -0,3106               | -1,2329                | 29,8693  |
| 10                         | 3,2422                                                 | 0,5281                | -0,5203               | -0,9878                | 28,3381  |
| 11                         | 2,4894                                                 | 0,2633                | -0,7431               | -1,0199                | 31,5294  |
| 12                         | 2,7209                                                 | 0,5102                | -0,8174               | -0,9208                | 32,6343  |
| 13                         | 2,5436                                                 | 0,3663                | -0,6205               | -0,9551                | 31,2919  |
| 14                         | 2,4797                                                 | 0,3761                | -0,5417               | -0,8758                | 29,6789  |
| 15                         | 2,1597                                                 | 0,5949                | -0,4140               | -0,6866                | 28,2753  |
| 16                         | 2,4509                                                 | 0,4503                | -0,4826               | -0,4366                | 32,2856  |
| 17                         | 2,2289                                                 | 0,3300                | -0,6474               | -0,4413                | 33,1454  |
| 18                         | 1,7506                                                 | 0,1327                | -0,7096               | -0,4584                | 32,1126  |
| 19                         | 1,7671                                                 | -0,1492               | -1,0219               | -0,5408                | 31,0191  |
| 20                         | 1,3670                                                 | -0,3495               | -1,1216               | -0,6202                | 30,7026  |
| 21                         | 1,1998                                                 | -0,5749               | -1,1434               | -0,7195                | 29,3016  |
| 22                         | 1,1001                                                 | -0,5791               | -1,2375               | -0,6408                | 31,0509  |
| 23                         | 1,0172                                                 | -0,8840               | -1,5481               | -0,7689                | 30,6714  |
| 24                         | 0,8004                                                 | -0,9385               | -1,5395               | -0,8582                | 32,4483  |
| 25                         | 0,6737                                                 | -0,9179               | -1,6355               | -1,0663                | 29,5506  |
| 26                         | 0,5547                                                 | -1,1762               | -1,7358               | -1,1875                | 32,8610  |
| 27                         | 0,1157                                                 | -1,3752               | -1,6050               | -1,1611                | 31,6173  |
| 28                         | 0,3462                                                 | -1,2191               | -1,3996               | -1,0745                | 31,1501  |
| 29                         | 0,7032                                                 | -1,0172               | -1,1980               | -0,8659                | 29,8453  |
| 30                         | 0,8712                                                 | -0,8407               | -1,2300               | -0,6615                | 29,5913  |
