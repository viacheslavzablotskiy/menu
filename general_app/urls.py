from importlib.util import find_spec
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [

                  path(r'^swagger(?P\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  path('admin/', admin.site.urls),
                  path('api/', include("menu_app.urls")),


                  path('', include('menu_admin.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

for menu_app in settings.MENUEXAMPLE_APPS:
    mod = menu_app + '.urls'
    if find_spec(mod):
        urlpatterns.append(path(menu_app + '/', include(mod)))
