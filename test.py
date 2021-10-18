from accounts.models import User

user_data = {
    "email": "roshan@gmail.com",
    "password": "Rosham",
    "username": "roshan"
}

User.objects.create_user(**user_data)