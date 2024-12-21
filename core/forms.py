from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# نموذج تسجيل الدخول
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label="اسم المستخدم")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="كلمة المرور")

# نموذج إنشاء حساب جديد
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="البريد الإلكتروني")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # 'password1' و 'password2' هما الحقول التي تم استخدامها في النموذج
