from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"restaurante", views.RestauranteViewSet)


urlpatterns = [
    # path('contacto/<str:nombre>', views.contacto, name= 'contacto'),
    # path('categorias/', views.categorias, name = 'categorias'),
    # path('productos/', views.productFormView, name = 'productos'),
    path('categorias/cantidad', views.categoria_contador),
    path('categorias/cantidad-usuarios', views.usuario_contador),
    path('', include(router.urls)),

]

schema_view = get_schema_view(
   openapi.Info(
      title="Django Module",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="luisricardorivasgiwencer@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
