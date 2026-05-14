from bebida_restaurante import BebidaRestaurante
from hamburguer_restaurante import HamburguerRestaurante
from pizza_restaurante import PizzaRestaurante
from produto_restaurante import ProdutoRestaurante

produto = ProdutoRestaurante()
bebida = BebidaRestaurante()
hamburguer = HamburguerRestaurante()
pizza = PizzaRestaurante()

produto.preparar()
bebida.preparar()
hamburguer.preparar()
pizza.preparar()