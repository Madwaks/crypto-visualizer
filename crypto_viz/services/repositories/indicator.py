import pickle
from json import dumps, loads
from pathlib import Path

import requests

from crypto_viz.app import cache


class IndicatorRepository:
	@cache.memoize(timeout=120)
	def get_indicators(self,symbol_name:str="ETHBTC",indicator_name:str="MM7",time_unit:str="4h"):
		indicators_path = self.get_indicator_path(symbol_name, indicator_name=indicator_name, time_unit=time_unit)
		if not indicators_path.exists():
			indicators = requests.get(f"http://localhost:8000/indicators/api/{indicator_name}/{symbol_name}/{time_unit}").json()
			indicators = {ind.get("timestamp"): ind.get("value") for ind in indicators}
			with indicators_path.open("wb") as f:
				pickle.dump(indicators, f)
		else:
			with indicators_path.open("rb") as f:
				indicators = pickle.load(f)

		return indicators

	def get_key_levels(self, symbol_name: str = "ETHBTC", time_unit: str = "4h") -> list[float]:
		key_level_path = self.get_key_level_path(symbol_name, time_unit=time_unit)
		if key_level_path.exists():
			indicators = requests.get(f"http://localhost:8000/indicators/api/{symbol_name}/{time_unit}").json()
			indicators = [ind.get("value") for ind in indicators]
			with key_level_path.open("wb") as f:
				pickle.dump(indicators, f)
		else:
			with key_level_path.open("rb") as f:
				indicators = pickle.load(f)

		return indicators


	def get_key_level_path(self, symbol_name: str = "ETHBTC", time_unit: str = "4h"):
		return Path(f"data/indicators/key-levels-{symbol_name}-{time_unit}.pkl")

	@staticmethod
	def get_indicator_path(symbol_name: str = "ETHBTC", indicator_name: str = "MM7", time_unit: str = "4h") -> Path:
		return Path(f"data/indicators/{symbol_name}-{indicator_name}-{time_unit}.pkl")
