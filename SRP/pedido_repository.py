from pedido import Pedido

class PedidoRepository():
    def salvar(self, pedido: Pedido):
        print(f'[SALVAR] Pedido do cliente "{pedido.cliente}" com valor total de "R$ {pedido.valor_total:.2f}" salvo com sucesso!')
