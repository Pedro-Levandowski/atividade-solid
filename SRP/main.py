from pedido import Pedido
from pedido_relatorio import PedidoRelatorio
from pedido_repository import PedidoRepository

itens_pedido = ['Mouse Gamer', 'Mousepad', 'Fone de Ouvido Bluetooth']
valor_total_pedido = 445
cliente_pedido = 'Pedro Levandowski'

pedido_1 = Pedido(itens_pedido, valor_total_pedido, cliente_pedido)

repository = PedidoRepository()
relatorio = PedidoRelatorio()

repository.salvar(pedido_1)
relatorio.exibir(pedido_1)