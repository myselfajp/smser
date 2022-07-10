from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# class signup_form(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields= ['first_name','username','phone_number']