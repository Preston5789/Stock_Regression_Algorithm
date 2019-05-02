# Linear Regression Stock Trader

This is an script that determines when to buy or sell stocks based off of linear regression statistics. 

The script is currently built to handle 15 stocks, but can easily modified for 100+.

## Setup

### Installing

Download the zip and open Stock_Regress.py in Pycharm or equivalent. Make sure to have python-binance API package. 

Place person Binance info below:
```
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
api_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

Choose which stocks you want to monitor for trade activity
```
tickerlist = ['bnbeth@ticker', 'neoeth@ticker','bateth@ticker', 'xlmeth@ticker','zrpeth@ticker',
              'zrxeth@ticker', 'adaeth@ticker','kmdeth@ticker', 'naveth@ticker','enjeth@ticker',
              'knceth@ticker', 'rlceth@ticker','rcneth@ticker', 'evxeth@ticker','icxeth@ticker']
```
### Navigating The App

Click the "Next Stock Button" to navigate between stocks

Click the "Generate Graph" button to graph all historical data for selected stock

Click the "Wrap it Up" button to sell all traded stocks bath to ETH

<p align="center">
  <img src="https://github.com/Preston5789/Stock_Regression_Algorithm/blob/master/Pics/Sample1.PNG" width="600" title="hover text">
</p>

## The Math

<p align="center">
  <img src="https://github.com/Preston5789/Stock_Regression_Algorithm/blob/master/Pics/StandardError.png" width="350" title="hover text">
</p>

## Built With

* [Python-Binance](https://github.com/sammchardy/python-binance) - API for stock price websocket, buying, and selling
* [Numpy](https://www.numpy.org/) - scientific computing with Python
* [Scipy](https://www.scipy.org/) - used for linear regression calculations


## Authors

* **Preston Phillips** - [Preston5789](https://github.com/Preston5789)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


