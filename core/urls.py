from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # مسار صفحة تسجيل الدخول
    path('home/', views.home, name='home'),    # مسار الصفحة الرئيسية
    path('signup/', views.signup, name='signup'),  # مسار صفحة إنشاء الحساب
]
