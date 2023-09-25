from django.contrib import admin
from django.urls import path
from auth import settings
from app.views import *
from app.form import MyPasswordResetFrom, MySetPasswordForm
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('login/', u_login,name="login"),
    path('signup/',signup,name="signup"),
    path('profile/',profile,name="profile"),
    path('upld_doc/',upld_doc,name="upld_doc"),
    path('change_password/',change_password,name="change_password"),
    path('logout/',logoutUser,name="logout"),
    path('reset-password/',PasswordResetView.as_view(template_name='forget_pass_form.html', form_class=MyPasswordResetFrom),name="reset-password"),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-done/',PasswordResetDoneView.as_view(template_name='forget_pass_done.html'),name='password_reset_done'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='forget_pass_complite.html'),name="password_reset_complete")
]+static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
