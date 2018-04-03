def lazy_property(fn):
    """Decorator that makes a property lazy-evaluated."""
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property


def async_lazy_property(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    async def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, await fn(self))
        return getattr(self, attr_name)

    return _lazy_property
