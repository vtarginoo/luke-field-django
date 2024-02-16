from rest_framework import viewsets, generics
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from field_os.models import Empresa, Posto, OrdemDeServico, ChecklistInstalacao, ItemChecklist
from field_os.serializer import (EmpresaSerializer, PostoSerializer, OrdemDeServicoSerializer,
                                  ChecklistInstalacaoSerializer, ItemChecklistSerializer,ListaEmpresaOSSerializer,
                                  ListaPostoOSSerializer)
from drf_yasg.utils import swagger_auto_schema

http_permitidos1 = ['get','post','put','delete']
http_permitidos2 = ['get','post','put']


class EmpresasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as empresa terceirizadas prestadoras de serviço"""
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    http_method_names = http_permitidos1

class PostosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os postos"""
    queryset = Posto.objects.all()
    serializer_class = PostoSerializer
    http_method_names = http_permitidos2

class OrdensDeServicoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as ordens de serviço"""
    queryset = OrdemDeServico.objects.all()
    serializer_class = OrdemDeServicoSerializer
    http_method_names = http_permitidos2


class ChecklistsInstalacaoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os checklists de instalação"""
    queryset = ChecklistInstalacao.objects.all()
    serializer_class = ChecklistInstalacaoSerializer
    http_method_names = http_permitidos2

class ItensChecklistViewSet(viewsets.ModelViewSet):
    """Exibindo todos os itens de checklist"""
    queryset = ItemChecklist.objects.all()
    serializer_class = ItemChecklistSerializer 
    http_method_names = http_permitidos2


class ListaOSEmpresa(generics.ListAPIView):
    """Listando Todas as Ordens de Serviço de uma Empresa"""
    serializer_class = ListaEmpresaOSSerializer

    def get_queryset(self):
        empresa_id = getattr(self.kwargs, 'pk', None)
        queryset = OrdemDeServico.objects.filter(empresa_instaladora_id = empresa_id)
        return queryset
    
    
    
class ListaOSPosto(generics.ListAPIView):
    """Listando Todas as Ordens de Serviço de um Posto"""

    serializer_class = ListaPostoOSSerializer

    def get_queryset(self):
        posto_id = getattr(self.kwargs, 'pk', None)
        queryset = OrdemDeServico.objects.filter(posto_id= posto_id)
        return queryset