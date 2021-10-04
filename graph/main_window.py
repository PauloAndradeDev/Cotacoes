from tkinter import (
    Tk,
    Label
)
from tkinter.ttk import Separator


class MainWindow:
    def __init__(self, dolar: str, euro: str, bitcoin: str) -> None:
        """Construtor da classe MainWindow."""
        self.__lista_cotacoes: list = list([dolar, euro, bitcoin])
        self.__main_window: Tk = Tk()
        self.__main_window.title("Cotações")
        self.__main_window.configure(background="#FFFFFF")
        self.__main_window.resizable(0, 0)
        self.__main_window.geometry(
            newGeometry="%dx%d+%d+%d" % (
                400,
                200,
                self.__main_window.winfo_screenwidth() / 2 - 400 / 2,
                self.__main_window.winfo_screenheight() / 2 - 200 - 2
            )
        )
        # Make Widgets:
        self.__make_labels(self.__lista_cotacoes[0], self.__lista_cotacoes[1], self.__lista_cotacoes[2])
        self.__make_separators()

    def __make_labels(self, dolar: str, euro: str, bitcoin: str) -> None:
        """Método responsável por criar todas as labels da janela principal."""
        Label(
            master=self.__main_window, text="Cotações do Dia", background="#FFFFFF", font=("Candara Light Italic", 20)
        ).place(x=100, y=5)
        # Label(master=self.__main_window, text="", background="").place(x=, y=)
        # Label(master=self.__main_window, text="", background="").place(x=, y=)
        # Label(master=self.__main_window, text="", background="").place(x=, y=)

    def __make_separators(self) -> None:
        """Método responsável por criar todos os separadores da janela principal."""
        pass

    def run(self) -> None:
        self.__main_window.mainloop()


if __name__ == "__main__":
    MainWindow().run()
