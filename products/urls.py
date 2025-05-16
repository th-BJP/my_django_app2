from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list, name='product_list'),
    path('<int:id>/',views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:id>/',views.category_detail, name='category_detail'),
    path('about/', views.about, name='about'),
]
