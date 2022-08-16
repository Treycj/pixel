"""pouch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from pixel.views import AdminViewSet, CartViewSet, Content_ownerViewSet, CustomerViewSet, OrdersViewSet, Payment_DetailsViewSet, PaymentViewSet, ProductViewSet, UserViewSet



router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'content_owner', Content_ownerViewSet)
router.register(r'admin', AdminViewSet)
router.register(r'product', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'payment_details', Payment_DetailsViewSet)




urlpatterns = [
    path('adminS/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
