from django.shortcuts import render

from CadastroCliente.models import Cliente, Profissao
from CadastroCliente.models import Telefone

# Create your views here.
def index(request):
    meu_nome = 'Beltrano da Costa'
    lista_frutas = ['Laranja', 'Maça', 'Banana']
    context = {
        'nome': meu_nome,
        'frutas': lista_frutas
    }
    return render(request, 'index.html', context)

def lista_clientes(request):
    #busca todos os clientes cadastrados na tabela admin
    lista_clientes = Cliente.objects.all()
    lista_profissoes = Profissao.objects.all()
    #dicionario (variavel) context é que vai mandar pros templates)
    context = {
        "clientes": lista_clientes,
        "profissoes": lista_profissoes, 
    }
    return render(request, 'lista_clientes.html', context)

def detalhar_cliente(request, id):
    #buscando no banco de dados o cliente pelo ID
    cliente = Cliente.objects.get(id = id)
    telefones = Telefone.objects.filter(cliente_id = id)
    context = {
        "cliente" : cliente,
        "telefones" : telefones
    }

    return render(request, 'cliente_detalhes.html', context)