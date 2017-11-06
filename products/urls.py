from django.conf.urls import url, include
from .views import ProductViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    )),
]
