import uuid
from django.db import models


class Empresa(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    uf = models.CharField(max_length=2)  
  

class Posto(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_estabelecimento = models.CharField(max_length=5, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)  

    

class OrdemDeServico(models.Model):
    class Meta:
        verbose_name_plural = "Ordens de Serviço"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_os = models.CharField(max_length=20, default= 'OS-YYMM-XXXX',unique=True, editable=False)  #unique=True,
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE)
    empresa_instaladora = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    aberta_em = models.DateTimeField(auto_now_add=True)
    fechada_em = models.DateTimeField(null=True, blank=True) 
    
   

class ChecklistInstalacao(models.Model):
    class Meta:
        verbose_name_plural = "Checklists de Instalações"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ordem_de_servico = models.ForeignKey(OrdemDeServico, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, default=f"CheckList-{str(id)[-4:]}")
    concluido = models.BooleanField(default=False)

class ItemChecklist(models.Model):
    class Meta:
        verbose_name_plural = "Itens Checklist"
    
    TIPO = (
       ('text', 'Text'),
       ('image', 'Image'), 
       ('boolean', 'Boolean')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checklist_instalacao = models.ForeignKey(ChecklistInstalacao, on_delete=models.CASCADE, null='false')
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPO, blank=False, null=False,default='texto')
    valor = models.CharField(max_length=255, blank=True, null=True)  # Pode armazenar string ou URL de imagem
    concluido = models.BooleanField(default=False)
    
    




