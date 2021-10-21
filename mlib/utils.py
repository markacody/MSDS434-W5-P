"""
Utilities makes custom functions in the appliable module: 
    * registered
    * discovered
    * documented
"""

import importlib

from sensible.loginit import logger

log = logger(__name__)


def appliable_functions():
    """
    Register and discover function. Returns a list of functions in the appliable module available to group by operations. 
    """
    from . import appliable
    module_items = dir(appliable)
    # Filter out special items __
    func_list = list(filter(lambda x: not x.startswith("__"), module_items))
    return func_list


def plugins_map():
    """
    Create a dictionary of callable functions
    """
    plugins = {}
    funcs = appliable_functions()
    for func in funcs:
        plugin_load_msg = "Loading appliable functions/plugins: {func}".format(
            func=func)
        log.info(plugin_load_msg)
        plugins[func] = getattr(
            importlib.import_module("nlib.appliable"), func)
    return plugins
