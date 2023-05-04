from django.contrib import admin
from CadastroCliente.models import Cliente, Profissao, Telefone, Interesse

# Register your models here.
# Classe para exibir Telefones no cadastro Telefone
class Telefones(admin.StackedInline):
    model = Telefone

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cidade']
    list_display_links = ['id', 'nome']
    list_filter = ['bairro', 'cidade', 'ativo']
    search_fields = ['nome']
    inlines = [Telefones]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Profissao)
admin.site.register(Telefone)
admin.site.register(Interesse)