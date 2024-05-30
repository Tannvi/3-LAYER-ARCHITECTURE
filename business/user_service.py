from business.model.user import User
from persistence.inmemory_storage import InMemoryStorage


class UserService:
    
    def __init__(self):
        self._user_storage = InMemoryStorage()

    def create_user(self, user: User) -> int:
        return self._user_storage.save(user)

    def get_user(self, user_id: int) -> User:
        return self._user_storage.get(user_id)