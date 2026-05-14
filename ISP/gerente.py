from typing import override
from int_entregador import IntEntregador
from int_admin import IntAdmin
from int_funcionario_cozinha import IntFuncionarioCozinha

class Gerente(IntEntregador, IntAdmin, IntFuncionarioCozinha):
    @override
    def gerenciar_entregas(self):
        print('=== [GERENCIAMENTO DE ENTREGAS] ===')
        print('Designando entregador...')
        print('Acompanhando status da entrega...')
        print('Entrega concluída!')

    @override
    def gerenciar_pedidos(self):
        print('=== [GERENCIAMENTO DE PEDIDOS] ===')
        print('Confirmando pedido...')
        print('Enviando para cozinha...')
        print('Recebendo pedido...')
        print('Acompanhando o garçom entregar o pedido...')
        print('Pedido concluído!')

    @override
    def enviar_notificacao(self):
        print('=== [ENVIO DE NOTIFICAÇÕES] ===')
        print('Notificando motoboy de alteração de endereço...')
        print('Notificando cozinha de cancelamento de pedido...')
        print('Notificações enviadas com sucesso!')

    @override
    def gerar_relatorio(self):
        print('=== [GERAÇÃO DE RELATÓRIO] ===')
        print('Gerando relatório de desempenho geral...')
        print('Relatório emitido!')