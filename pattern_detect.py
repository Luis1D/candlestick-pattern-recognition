import talib
import yfinance as yf

data = yf.download("SPY", start="2017-01-01", end="2017-04-30")

morning_stars = talib.CDLMORNINGSTAR(data['Open'],data['High'],data['Low'],data['Close'])

engulfing = talib.CDLENGULFING(data['Open'],data['High'],data['Low'],data['Close'])

data['morning_star'] = morning_stars
data['engulfing'] = engulfing

engulfing_days = data[data['engulfing'] != 0]

print(engulfing_days)