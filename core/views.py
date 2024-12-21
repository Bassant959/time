from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from .models import User

# صفحة إنشاء الحساب
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # الحصول على البيانات المدخلة
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # إنشاء المستخدم في قاعدة البيانات مع تشفير كلمة المرور
            user = User.objects.create(username=username, email=email)
            user.set_password(password)  # تشفير كلمة المرور
            user.save()  # حفظ المستخدم في قاعدة البيانات

            # إضافة رسالة نجاح
            messages.success(request, "تم إنشاء الحساب بنجاح!")
            
            # تسجيل الدخول مباشرة بعد الإنشاء
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # تسجيل الدخول
                return redirect('home')  # التوجيه إلى الصفحة الرئيسية

            # في حالة فشل التوثيق
            return redirect('login')  # التوجيه إلى صفحة تسجيل الدخول بعد التسجيل

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

# صفحة تسجيل الدخول
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # التحقق من صحة البيانات باستخدام authenticate
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')  # إعادة التوجيه إلى الصفحة الرئيسية
            else:
                form.add_error(None, "بيانات تسجيل الدخول غير صحيحة")
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})

# الصفحة الرئيسية
def home(request):
    return render(request, 'core/home.html')
