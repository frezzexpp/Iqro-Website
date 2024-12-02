from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView
from imageproxy.views import ImageProxyView




urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auftentifikatsiya:
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),


    # Proxy Img
    path('image-proxy/', ImageProxyView.as_view(), name='proxy-image'),

]

urlpatterns += i18n_patterns(
    path("i18n/", include('django.conf.urls.i18n')),
    path('api/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

)