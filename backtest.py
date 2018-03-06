from abc import ABCMeta, abstractmethod

class Strategy(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def generate_signals(self):
		raise NotImplementedError("Should implement generate_signals()!")

class Portfolio(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def backtest_portfolio(self):
		raise NotImplementedError("Should implement (backtest_portfolio)!")