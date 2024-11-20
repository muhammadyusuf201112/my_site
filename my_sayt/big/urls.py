from django.urls import path
from .views import List_View

urlpatterns = [
    path('', List_View.as_view(), name='home')
]