from pickle import dumps, loads

from redis import Redis as _Redis

from swiper import settings


class Redis(_Redis):
    def get(self, name):
        """
        Return the value at key ``name``, or None if the key doesn't exist
        """
        pickled = super().get(name)
        try:
            return loads(pickled)
        except TypeError:
            return pickled

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.
        """
        pickled = dumps(value, -1)
        return super().set(name, pickled, ex, px, nx, xx)


rds = Redis(**settings.REDIS)
