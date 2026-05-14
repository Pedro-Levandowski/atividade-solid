from typing import override
from produto_restaurante import ProdutoRestaurante

class PizzaRestaurante(ProdutoRestaurante):
    @override
    def preparar(self):
        print('=== [PIZZA] ===')
        print('Abrindo a massa da pizza...')
        print('Adicionando molho de tomate à pizza...')
        print('Adiconando queijo à pizza...')
        print('Adicionando tomate à pizza...')
        print('Levando a pizza ao forno...')
        print('Tirando a pizza do forno...')
        print('Pizza servida com sucesso!')
        