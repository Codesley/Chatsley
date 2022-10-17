from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUp(UserCreationForm): #Tells Django we will use user creation form 
    class Meta:
        model = User
        fields = ['username','password1','password2']

        # Using Django's user model from https://docs.djangoproject.com/en/4.1/topics/auth/default/
        