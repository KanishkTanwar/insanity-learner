from django.urls import path
from register.views import signin, signout, signup

app_name = "register"

urlpatterns = [
    path('signout', signout, name="signout"),
    path('signin', signin, name="signin"),
    path('signup', signup, name="signup"),
]