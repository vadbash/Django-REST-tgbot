from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from bot import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'messages', views.MessageHistoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
