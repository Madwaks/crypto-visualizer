import requests

from crypto_viz.utils.enums import AvailableIndicators

INDICATORS_CHECKLIST = [
            {'label': label, 'value': value} for label, value in zip(AvailableIndicators.labels, AvailableIndicators.names)]

STYLE_MM_CHECKLIST = {'display': 'inline-block', "margin-right": "20px", "margin-bottom": "50px"}

symbols = requests.get("http://localhost:8000/core/api/symbols").json()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
