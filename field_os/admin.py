from django.contrib import admin
from field_os.models import Empresa, Posto, OrdemDeServico, ChecklistInstalacao, ItemChecklist

# Registros de Models para a exibição no Admin


class EmpresaAdmin(admin.ModelAdmin):
    
    list_display = ('id','nome', 'cnpj', 'uf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20



class PostoAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_estabelecimento','nome', 'cnpj', 'uf')
    list_display_links = ('codigo_estabelecimento', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


class OrdemDeServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'posto', 'empresa_instaladora', 'aberta_em', 'fechada_em')
    list_display_links = ('id', 'empresa_instaladora')
    search_fields = ('id','posto__nome', 'empresa_instaladora__nome')  
    list_per_page = 20
    list_filter = ('empresa_instaladora',)

class ChecklistInstalacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordem_de_servico', 'nome', 'concluido')
    list_display_links = ('id',)
    search_fields = ('ordem_de_servico__posto__nome', 'ordem_de_servico__empresa_instaladora__nome', 'nome')  # Adicione os campos que deseja pesquisar
    list_per_page = 20

class ItemChecklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'checklist_instalacao', 'nome', 'get_tipo_display', 'valor', 'concluido')
    list_display_links = ('id',)
    search_fields = ('checklist_instalacao__ordem_de_servico__posto__nome', 'checklist_instalacao__ordem_de_servico__empresa_instaladora__nome', 'nome')  # Adicione os campos que deseja pesquisar
    list_per_page = 20


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Posto, PostoAdmin)
admin.site.register(OrdemDeServico, OrdemDeServicoAdmin)
admin.site.register(ChecklistInstalacao, ChecklistInstalacaoAdmin)
admin.site.register(ItemChecklist, ItemChecklistAdmin)