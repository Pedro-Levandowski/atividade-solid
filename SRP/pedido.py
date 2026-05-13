class Pedido():
    def __init__(self, itens: list, valor_total: float, cliente: str):
        self._itens = itens
        self._valor_total = valor_total
        self._cliente = cliente

    @property
    def itens(self):
        return self._itens
    
    @property
    def valor_total(self):
        return self._valor_total

    @property
    def cliente(self):
        return self._cliente