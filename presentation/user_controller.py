from business.model.user import User


class UserController:

    def __init__(self, user_service):
        self.user_service = user_service

    def create_user(self, incoming_data):
        user = User(
            incoming_data.get('user_name', None),
            incoming_data.get('first_name', None),
            incoming_data.get('lastname', None),
        )
        user_id = self.user_service.create_user(user)
        user.user_id = user_id
        return user.__dict__

        user.user_name = incoming_data.get('user_name', None)
        user.first_name = incoming_data.get('first_name', None)
        user.last_name = incoming_data.get('last_name', None)
        self.user_service.create_user(user)

    def get_user(self, user_id):
        user = self.user_service.get_user(int(user_id))
        return user.__dict__
    
