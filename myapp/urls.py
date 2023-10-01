from django.urls import path
from .views import AppListApiView

urlpatterns = [
    path('all/', AppListApiView.as_view())
]
