def fetch_user_data(user_id):
    """
    Fetch user data from database using the user ID.
    """
    return {"id": user_id, "name": "John Doe"}

class User:
    """
    Represents a user in the system.
    """

    def __init__(self, user_id, name):
        """
        Initialize a User instance.
        """
        self.user_id = user_id
        self.name = name

    def display(self):
        """
        Display user details.
        """
        return f"User ID: {self.user_id}, Name: {self.name}"
