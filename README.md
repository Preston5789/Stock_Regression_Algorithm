# Linear Regression Stock Trader

This is an script that determines when to buy or sell stocks based off of linear regression statistics. This script detects changes in the rate of change of the price. 

The script is currently built to handle 15 stocks, but can easily modified for 100+.

## Setup

### Installing

Download the zip and open Stock_Regress.py in your prefered IDE. Make sure to have python-binance API package. 

The program is divided into 4 scripts:
stock_connect: connects to RestAPI web socket and stores stock data

stock_plots: generates the ggplot graphs and UI interface to change stocks

stock_trade: contains the buying and selling scripts

stock_reg: performs the regression and error calculation

The code is run from the stock_plots file, but the API credentials and selected stocks need to be set in the stock_connect file. 
P

Place person Binance info below:
```
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
api_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

Choose which stocks you want to monitor for trade activity. Place this into the stock_connect file.
```
tickerlist = ['bnbeth@ticker', 'neoeth@ticker','bateth@ticker', 'xlmeth@ticker','zrpeth@ticker',
              'zrxeth@ticker', 'adaeth@ticker','kmdeth@ticker', 'naveth@ticker','enjeth@ticker',
              'knceth@ticker', 'rlceth@ticker','rcneth@ticker', 'evxeth@ticker','icxeth@ticker']
```

Once stock_connect has all the parameters, run the stock_plots function.
### Going From Simulation to Actual Selling

The Jesus int controlls whether the script sends the sell command to the API. Set to zero for simulation. Set to 1 for active trading.

### Navigating The App

Click the "Next Stock Button" to navigate between stocks

Click the "Generate Graph" button to graph all historical data for selected stock

Click the "Wrap it Up" button to sell all traded stocks bath to ETH

<p align="center">
  <img src="https://github.com/Preston5789/Stock_Regression_Algorithm/blob/master/Pics/Sample1.PNG" width="900" title="hover text">
</p>



## The Math
Standard errors for regression are measures of how spread out your y variables are around the mean, μ.The standard error of the regression slope, s (also called the standard error of estimate) represents the average distance that your observed values deviate from the regression line. The smaller the “s” value, the closer your values are to the regression line.


<p align="center">
  <img src="https://github.com/Preston5789/Stock_Regression_Algorithm/blob/master/Pics/StandardError.png" width="250" title="hover text">
</p>
(https://www.statisticshowto.datasciencecentral.com/find-standard-error-regression-slope/)

In the script, two slopes are determined. One for the last 35 data points and the other for the next 95 data points after that. The slope and assoiciated error for each time period are plotted against the server time. A sample graph is seen below: 

<p align="center">
  <img src="https://github.com/Preston5789/Stock_Regression_Algorithm/blob/master/Pics/Sample2.PNG" width="600" title="hover text">
</p>

The calculation for the last 35 data points is shown below. The lists are converted to numpy arrays so that they can be passed through the linregress function. The slope and intercept are calculated. 
```
if(len(tracker_list[position]) >= 35):
      temptimearray = numpy.asarray(temptime_list[position]).astype(numpy.float)
      temparray = numpy.asarray(temp_list[position]).astype(numpy.float)
      model = linregress(temptimearray,temparray)
      slope = model.slope
      slope_list[position].append(slope)
      slopetime_list[position].append(timer)
      intercept = model.intercept
      line = slope*temptimearray + intercept
````

Next, the 99.9% confidence interval is determined 
````
      avgx = sum(temptimearray)/len(temptimearray)
      devx = sum((temptimearray - avgx)**2)**0.5
      error = (sum((temparray - line)**2)/33)**0.5
      error = 4.957*error/devx
````      



## Built With

* [Python-Binance](https://github.com/sammchardy/python-binance) - API for stock price websocket, buying, and selling
* [Numpy](https://www.numpy.org/) - scientific computing with Python
* [Scipy](https://www.scipy.org/) - used for linear regression calculations


## Authors

* **Preston Phillips** - [Preston5789](https://github.com/Preston5789)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


