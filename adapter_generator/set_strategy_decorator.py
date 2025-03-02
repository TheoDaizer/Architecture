def set_strategy(strategy):
    def decorator(_):
        def _set_strategy_wrapper(adapter, **kwargs):
            return strategy(adapter, **kwargs)
        return _set_strategy_wrapper
    return decorator
