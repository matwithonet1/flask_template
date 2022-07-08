from objects.user import User

def get_user(user_id, **kwargs):
    """
    Basic get function to return a JSON object of the user details passed in
    """
    return User(user_id, **kwargs).to_dict()
