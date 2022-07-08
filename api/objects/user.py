
class User(object):
    def __init__(
    self,
    user_id,
    **kwargs
    ):
        self.user_id = user_id
        self._first_name = kwargs.get('first_name')
        self._last_name = kwargs.get('last_name')
        self._city = kwargs.get('city')

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def city(self):
        return self._city

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'city': self.city
        }
