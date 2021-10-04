from cotacoes_moedas.acessando_cotacoes import formatar_saida
from graph.main_window import MainWindow

cotacoes = formatar_saida()
window = MainWindow(cotacoes[0], cotacoes[1], cotacoes[2])
window.run()
