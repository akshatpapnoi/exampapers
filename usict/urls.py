from django.urls import path
from usict import views

app_name = 'usict'

urlpatterns = [
	path('', views.main, name = 'main'),
	path('papers/<degree>/<branch>/<semester>', views.papers, name='papers'),
]