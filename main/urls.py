from django.urls import path
from .views import ( CategoriesApiView, AdminCategoriesApiView,
                    ProductsApiView, AdminProductsApiView )

app_name = 'main'


urlpatterns = [
    path('categories/', CategoriesApiView.as_view()),
    path('products/', ProductsApiView.as_view()),
    path('products/of-<uuid:cguid>/', ProductsApiView.as_view()),

    path('admin/categories/', AdminCategoriesApiView.as_view()),
    path('admin/categories/<uuid:guid>/', AdminCategoriesApiView.as_view()),
    path('admin/products/', AdminProductsApiView.as_view()),
    path('admin/products/of-<uuid:guid>/', AdminProductsApiView.as_view()),
]
