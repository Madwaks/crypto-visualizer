from dash import Dash

from crypto_viz.cache import ResourceCache
from crypto_viz.layouts import layout
from crypto_viz.settings import external_stylesheets


class CryptoViz(Dash):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = layout


app = CryptoViz(__name__, external_stylesheets=external_stylesheets)

cache = ResourceCache(app.server,with_jinja2_ext=False, config={
    'CACHE_TYPE': 'memcached',
    'CACHE_DIR': 'cache-directory'
})
