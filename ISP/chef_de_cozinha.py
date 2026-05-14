from typing import override
from int_funcionario_cozinha import IntFuncionarioCozinha

class ChefDeCozinha(IntFuncionarioCozinha):
    @override
    def gerenciar_pedidos(self):
        print('=== [GERENCIAMENTO DE PEDIDOS] ===')
        print('Recebendo pedido...')
        print('Preparando comida...')
        print('Entregando comida...')
        print('Alternando status para concluído...')
        print('Pedido concluído!')