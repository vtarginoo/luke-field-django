from rest_framework import serializers
from django.db import transaction
from field_os.models import Empresa, Posto, OrdemDeServico, ChecklistInstalacao, ItemChecklist
from field_os.util import generate_id_os
import logging



logger = logging.getLogger(__name__)

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class PostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posto
        fields = '__all__'

class OrdemDeServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeServico
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['id_os'] = generate_id_os()
        instance = super().create(validated_data)
        return instance


class ChecklistInstalacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistInstalacao
        fields = '__all__'

class ItemChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemChecklist
        fields = '__all__'



class ListaEmpresaOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeServico
        fields = '__all__'
        

class ListaPostoOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeServico
        fields = '__all__'