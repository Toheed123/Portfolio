from branch import views
from django.urls import path
urlpatterns = [
    path('', views.hello),
]