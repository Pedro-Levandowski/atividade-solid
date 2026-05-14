from gerente import Gerente
from chef_de_cozinha import ChefDeCozinha
from motoboy import Motoboy

gerente = Gerente()
print('----- GERENTE ------')
gerente.gerenciar_pedidos()
gerente.gerenciar_entregas()
gerente.enviar_notificacao()
gerente.gerar_relatorio()
print('-----------')

chef_de_cozinha = ChefDeCozinha()
print('----- CHEF DE COZINHA ------')
chef_de_cozinha.gerenciar_pedidos()
print('-----------')

motoboy = Motoboy()
print('----- MOTOBOY ------')
motoboy.gerenciar_entregas()
print('-----------')

