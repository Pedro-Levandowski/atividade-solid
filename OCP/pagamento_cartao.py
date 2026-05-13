from forma_pagamento import FormaPagamento

class PagamentoCartao(FormaPagamento):
    def __init__(self):
        self.desconto = False
        self.acrescimo = 0.02

    def processar_pagamento(self, valor_total) -> bool:
        fator_multiplicacao = 1
        try:
            fator_multiplicacao = (1 - self.desconto) if self.desconto else (1 + self.acrescimo)
        except Exception:
            pass
        valor_final = float(f'{(valor_total*fator_multiplicacao):.2f}')
        print(f'Pagamento de "R$ {valor_final:.2f}" realizado com sucesso no Cartão!')
        return True