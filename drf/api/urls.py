from django.urls import path , include
from .views import *
from rest_framework_nested import routers

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'', CategoryViewSet, basename='category')

products_router = routers.NestedSimpleRouter(router, r'',lookup = 'category', trailing_slash=True)
products_router.register(r'p', ProductViewSet, basename='products')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
]