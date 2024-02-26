Stock price chart GUI

I've builded a simple desktop GUI app that shows the price of a stock and displays it to the user as a chart. I coded it with Python.

Project requirements
The app should display a chart of the 1-min stock price of e.g., META of the last few days. The chart should be updated every minute with the latest available price (note that a 15-minute delay vs real-time is to be expected).

I used the yfinance library to retrieve the data (https://pypi.org/project/yfinance/).
