from django.urls import path
from register.views import signin, signout

app_name = "register"

urlpatterns = [
    path('signout', signout, name="signout"),
    path('signin', signin, name="signin"),
]