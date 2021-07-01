from plotly.graph_objs import Figure, Scatter

from crypto_viz.services.repositories.indicator import IndicatorRepository


def build_candle_lists(quotes: list[dict[str, float]]):
	timestamp = []
	open_ = []
	high = []
	low = []
	close = []
	for data in quotes:
		timestamp.append(data["timestamp"])
		open_.append(data["open"])
		high.append(data["high"])
		low.append(data["low"])
		close.append(data["close"])

	return timestamp, open_, high, low, close


def add_moving_avg_figure(indicators_list: list[str], fig: Figure, ind_repo: IndicatorRepository, symbol_name: str, timestamps: list[str]):
	for ind in indicators_list:
		indicators = ind_repo.get_indicators(symbol_name=symbol_name, indicator_name=ind)
		mm_values = []
		for timest in timestamps:
			if indicators.get(timest):
				mm_values.append(indicators.get(timest))
			else:
				mm_values.append(None)

		fig.add_trace(
			Scatter(
				x=timestamps,
				y=mm_values
			))

	return fig


def add_key_levels_figure(symbol, fig: Figure, repo: IndicatorRepository):
	key_levels = repo.get_key_levels(symbol_name=symbol)
	for level in key_levels:
		fig.add_hline(y=level)

	return fig