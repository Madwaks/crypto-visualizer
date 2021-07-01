import hashlib
import json
import inspect
from base64 import b64encode
from hashlib import md5
from typing import Callable, Optional, Any

from flask_caching import Cache, function_namespace


class ResourceCache(Cache):
    def _memoize_make_cache_key(
        self,
        make_name: None = None,
        timeout: Optional[Callable] = None,
        forced_update: bool = False,
        hash_method: Callable = hashlib.md5,
        source_check: Optional[bool] = False,
        args_to_ignore: Optional[Any] = None,
    ) -> Callable:
        def make_cache_key(f, *args, **kwargs):
            fname, _ = function_namespace(f)
            if callable(make_name):
                altfname = make_name(fname)
            else:
                altfname = fname
            updated = altfname + json.dumps(dict(
                args=self._extract_self_arg(f, args),
                kwargs=kwargs), sort_keys=True)
            return b64encode(
                md5(updated.encode('utf-8')).digest()
            )[:16].decode('utf-8')

        return make_cache_key

    @staticmethod
    def _extract_self_arg(f, args):
        argspec_args = inspect.getfullargspec(f).args

        if argspec_args and argspec_args[0] in ('self', 'cls'):
            if hasattr(args[0], '__name__'):
                return (args[0].__name__,) + args[1:]
            return (args[0].__class__.__name__,) + args[1:]
        return args
