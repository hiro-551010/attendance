import os 
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
setup()


from accounts.models import User, Profile

def select_user():
    users = User.objects.all()
    for user in users:
        print(user.id, user.email, user.profile.phone_number)

select_user()

