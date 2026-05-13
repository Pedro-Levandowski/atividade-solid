from abc import ABC, abstractmethod

class FormaPagamento(ABC):
    def __init__(self):
        self.desconto = False
        self.acrescimo = False
    
    @abstractmethod
    def processar_pagamento(self, valor_total: float) -> bool:
        pass