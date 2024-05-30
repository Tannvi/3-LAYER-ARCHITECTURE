import unittest
from business.model.user import User
from business.user_service import UserService

class TestUserService(unittest.TestCase):

    def test_should_be_able_to_create_and_retrieve_user(self):
        user_service = UserService()

        user = User(
            user_name = 'test_user',
            first_name = 'Test',
            last_name = 'User'
        )
        user_id = user_service.create_user(user)
        retrieved_user = user_service.get_user(user_id)

        self.assertIsNotNone(user_id)
        self.assertEqual(user, retrieved_user)
        self.assertEqual(retrieved_user.user_id, user_id)


if __name__ == '__main__':
    unittest.main()
