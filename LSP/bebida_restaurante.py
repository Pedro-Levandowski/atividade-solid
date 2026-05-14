from typing import override
from produto_restaurante import ProdutoRestaurante

class BebidaRestaurante(ProdutoRestaurante):
    @override
    def preparar(self):
        print('=== [BEBIDA] ===')
        print('Pegando copo...')
        print('Adicionando bebida ao copo...')
        print('Fechando copo...')
        print('Bebida servida com sucesso!')