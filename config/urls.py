from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from course.views import SubjectViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="classroom API",
      default_version='v1',
      description="test classroom api",
      terms_of_service="https://youtu.be/xm3YgoEiEDc?si=THLqoDDzw8gu3dnV",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('subject', SubjectViewSet)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    path('api/v1/account/', include('account.urls')),
    path('api/v1/course/', include('course.urls')),
    path('api/v1/group/', include('group.urls')),
    path('api/v1/', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
