from . import views
from django.urls import path


urlpatterns = [
    path("", views.getCategory),
    path("<str:category>/", views.getOneCategory, name="home category"),
    path('product/<str:id>', views.getOneProduct, name='single Product'),
    path('add_product/<str:id>',views.addToCart,name="add to cart"),
    path('getAllCart',views.getAllCart,name="getAllCart"),
]
