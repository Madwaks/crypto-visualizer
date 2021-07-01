import pickle
from pathlib import Path

import requests

from crypto_viz.app import cache


class QuoteRepository:
	@cache.memoize()
	def get_quotes(self, symbol_name: str="ETHBTC", time_unit: str = "4h"):
		quote_path = self.get_quote_path(symbol_name, time_unit)
		if not quote_path.exists():
			quotes = requests.get(f"http://localhost:8000/core/api/quotes/{symbol_name}/{time_unit}").json()
			with quote_path.open("wb") as f:
				pickle.dump(quotes, f)
		else:
			with quote_path.open("rb") as f:
				quotes = pickle.load(f)
		return quotes

	@staticmethod
	def get_quote_path(symbol_name: str="ETHBTC", time_unit: str = "4h") -> Path:
		return Path(f"data/quotes/{symbol_name}-{time_unit}.pkl")

