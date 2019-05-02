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
Standard errors for regression are measures of how spread out your y variables are around the mean, μ.The standard error of the regression slope, s (also called the standard error of estimate) represents the average distance that your observed values deviate from the regression line. The smaller the “s” value, the closer your values are to the regression line.


<p align="center">
  <img src="https://github.com/Preston5789/Stock_Regression_Algorithm/blob/master/Pics/StandardError.png" width="250" title="hover text">
</p>

In the script, two slopes are determined. One for the last 35 data points and the other for the next 95 data points after that. The slope and assoiciated error for each time period are plotted against the server time. A sample graph is seen below: 

<p align="center">
  <img src="https://github.com/Preston5789/Stock_Regression_Algorithm/blob/master/Pics/Sample2.PNG" width="600" title="hover text">
</p>

The calculation for the last 35 data points is shown below:
```
if(len(tracker_list[position]) >= 35):
      temptimearray = numpy.asarray(temptime_list[position]).astype(numpy.float)
      temparray = numpy.asarray(temp_list[position]).astype(numpy.float)
      temparray /= numpy.float(tracker_list[position][0])
 
      print(tracker_list[position][0])
      model = linregress(temptimearray,temparray)
      slope = model.slope
      slope_list[position].append(slope)
      slopetime_list[position].append(timer)
 
      intercept = model.intercept
      line = slope*temptimearray + intercept
 
      avgx = sum(temptimearray)/len(temptimearray)
      devx = (temptimearray - avgx)**2
      devx = sum(devx)
      devx = (devx)**0.5
 
      error = (temparray - line)**2
      error = sum(error)/33
      error = (error)**(.5)
      error = 4.957*error/devx
```      



## Built With

* [Python-Binance](https://github.com/sammchardy/python-binance) - API for stock price websocket, buying, and selling
* [Numpy](https://www.numpy.org/) - scientific computing with Python
* [Scipy](https://www.scipy.org/) - used for linear regression calculations


## Authors

* **Preston Phillips** - [Preston5789](https://github.com/Preston5789)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


