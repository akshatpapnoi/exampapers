from django.urls import path
from usict import views

app_name = 'usict'

urlpatterns = [
	path('', views.main, name = 'main'),
]