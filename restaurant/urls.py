from django.urls import path
from .views import index, menuItemView, singleMenuItemView

urlpatterns = [
    path('index/', index, name='index'),

    # API
    path('menu/', menuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', singleMenuItemView.as_view(), name='singleMenu'),
]