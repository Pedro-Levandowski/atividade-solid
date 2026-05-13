from pagamento_cartao import PagamentoCartao
from pagamento_dinheiro import PagamentoDinheiro
from pagamento_pix import PagamentoPIX

cartao = PagamentoCartao()
dinheiro = PagamentoDinheiro()
pix = PagamentoPIX()

valor_total_compra = 728.90

pagamento_via_cartao = cartao.processar_pagamento(valor_total_compra)
pagamento_via_dinheiro = dinheiro.processar_pagamento(valor_total_compra)
pagamento_via_pix = pix.processar_pagamento(valor_total_compra)