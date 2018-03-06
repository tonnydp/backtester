import numpy as np
import pandas as pd
import quandl

from backtest import Strategy, Portfolio

class RandomForecastingStrategy(Strategy):

	def __init__(self, symbol, bars):
		self.symbol = symbol
		self.bars = bars

	def generate_signals(self):
		signals = pd.DataFrame(index=self.bars.index)
		signals['signal'] = np.sign(np.random.randn(len(signals)))

		signals['signal'][0:5] = 0.0

		return signals

class MarketOnOpenPortfolioi(Portfolio):
	def __init__(self, symbol, bars, signals, initial_capital=100000.0):
		self.symbol = symbol
		self.bars = bars
		self.initial_capital = float(initial_capital)
		self.positions = self.generate_positions()

	def generate_positions(self):
		positions = pd.DataFrame(index=signals.index).fillna(0.0)
		positions[self.symbol] = 100 * signals['signal']
		return positions

	def backtest_portfolio(self):
		portfolio = self.positions * self.bars['Open']
		pos_diff = self.positions.diff()
		portfolio['holdings'] = (self.positions * self.bars['Open']).sum(axis=1)
		portfolio['cash'] = self.initial_capital - (pos_diff * self.bars['Open']).sum(axis=1).cumsum()

		portfolio['total'] = portfolio['cash'] = portfolio['holdings']
		portfolio['return'] = portfolio['total'].pct_change()
		return portfolio

if __name__== "__main__":
	quandl.ApiConfig.api_key = "nHNNE742KnpMGRKFttFC"
	symbol = 'IBM'
	bars = quandl.get('NYSE/IBM', collapse='daily')
	# bars = quandl.get("GOOG/NYSE_%s" % symbol, collapse="daily")
	rfs = RandomForecastingStrategy(symbol, bars)
	signals = rfs.generate_signals()
	portfolio = MarketOnOpenPortfolioi(symbol, bars, signals, initial_capital=100000.0)
	returns = portfolio.backtest_portfolio()

	print(returns.tail(10))