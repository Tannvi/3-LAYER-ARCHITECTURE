from persistence.storage import UserStorage



class InMemoryStorage(UserStorage):
    def __init__(self):
        self._data = []

    def get(self, user_id):
        return self._data[user_id]

    def save(self, user):
        user_id = len(self._data)
        user.user_id = user_id
        self._data.append(user)
        return user_id