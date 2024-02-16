from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from field_os.views import (EmpresasViewSet,PostosViewSet,OrdensDeServicoViewSet,
                            ChecklistsInstalacaoViewSet,ItensChecklistViewSet,ListaOSEmpresa,ListaOSPosto)



schema_view = get_schema_view(
   openapi.Info(
      title="LukeField (MVP)",
      default_version='v1',
      description="API voltada para gestão de técnicos instaladores e ordens de serviço para a Luke Field",
      terms_of_service="#",
      contact=openapi.Contact(email="vtarginoo@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register('empresas', EmpresasViewSet, basename='empresa')
router.register('postos', PostosViewSet, basename='posto')
router.register('ordens-de-servico', OrdensDeServicoViewSet, basename='ordem-de-servico')
router.register('checklist', ChecklistsInstalacaoViewSet, basename='checklistinstalacao')
router.register('itenschecklist', ItensChecklistViewSet, basename='itemchecklist')



urlpatterns = [ 
    path('', include(router.urls)),
    path('empresas/<uuid:pk>/ordens-de-servico', ListaOSEmpresa.as_view()),
    path('postos/<uuid:pk>/ordens-de-servico', ListaOSPosto.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

    ]



