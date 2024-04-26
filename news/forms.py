# from django.contrib.auth.models import User
from django import forms


from .models import News, Category, Comment, User,AbstractUser





class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = ['first_name', 'last_name', 'username', 'email', 'rasm']


class NewsForm(forms.ModelForm):
    class Meta:        
        model = News 
        fields = ['title', 'text','rasm', 'tur']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['izoh']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=20)

class PasswordForm(forms.Form):
    password_1= forms.CharField(max_length=10)
    password_2 = forms.CharField(max_length=10)

