from typing import override
from int_entregador import IntEntregador

class Motoboy(IntEntregador):
    @override
    def gerenciar_entregas(self):
        print('=== [GERENCIAMENTO DE ENTREGAS] ===')
        print('Iniciando entrega...')
        print('Deslocando-se ao destino...')
        print('Entregando pedido...')
        print('Status da entrega alternado para concluído!')