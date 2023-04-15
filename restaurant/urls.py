from django.urls import path
from .views import index, menuItemView, singleMenuItemView, BookingViewSet

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # PAGE
    path('index/', index, name='index'),

    # API
    path('menu/', menuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', singleMenuItemView.as_view(), name='singleMenu'),

    # AUTHENTICATION
    path('api-token-auth/', obtain_auth_token, name='auth')
]