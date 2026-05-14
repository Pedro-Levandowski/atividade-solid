from typing import override
from produto_restaurante import ProdutoRestaurante

class HamburguerRestaurante(ProdutoRestaurante):
    @override
    def preparar(self):
        print('=== [HAMBURGUER] ===')
        print('Colocando carne na chapa...')
        print('Cortando pão...')
        print('Adiconando maionese ao pão...')
        print('Virando a carne...')
        print('Adicionando queijo à carne...')
        print('Colocando carne no pão...')
        print('Colocando salada no pão...')
        print('Fechando hamburguer...')
        print('Hamburguer servido com sucesso!')