from pedido import Pedido

class PedidoRelatorio():
    def exibir(self, pedido: Pedido):
        print('=== [INFOS PEDIDO] ===')
        print('-- Itens do pedido --')
        for idx, item in enumerate(pedido.itens):
            print(f'{idx+1}: {item}')
        print(f'Valor total: R$ {pedido.valor_total}')
        print(f'Cliente: {pedido.cliente}')
        print('===============')