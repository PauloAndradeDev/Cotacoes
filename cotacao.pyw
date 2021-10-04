from cotacoes_moedas.acessando_cotacoes import formatar_saida
from graph.main_window import MainWindow

cotacoes = formatar_saida()

dolar = round(float(cotacoes[0]), 2)
euro = round(float(cotacoes[1]), 2)
bitcoin = round(float(cotacoes[2]), 3)

dolar = str(dolar).replace(".", ",")
euro = str(euro).replace(".", ",")
bitcoin = str(bitcoin)

window = MainWindow(dolar, euro, bitcoin)
window.run()
