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
            master=self.__main_window,
            text="Cotações do Dia",
            background="#FFFFFF",
            foreground="#808080",
            font=("Candara Light Italic", 20)
        ).place(x=110, y=5)
        Label(master=self.__main_window, text="DOLAR", background="#FFFFFF", foreground="#436253", font=("Arial", 13)).place(x=38, y=60)
        Label(master=self.__main_window, text="EURO", background="#FFFFFF", foreground="#3e4758", font=("Arial", 13)).place(x=167, y=60)
        Label(master=self.__main_window, text="BITCOIN", background="#FFFFFF", foreground="#8ea97c", font=("Arial", 13)).place(x=280, y=60)
        Label(master=self.__main_window,
              text=f"R$ {dolar}",
              background="#FFFFFF",
              foreground="#436253",
              font=("Arial Black", 14)
              ).place(x=25, y=85)
        Label(master=self.__main_window,
              text=f"R$ {euro}",
              background="#FFFFFF",
              foreground="#3e4758",
              font=("Arial Black", 14)
              ).place(x=148, y=85)
        Label(master=self.__main_window,
              text=f"R$ {bitcoin}",
              background="#FFFFFF",
              foreground="#8ea97c",
              font=("Arial Black", 14)
              ).place(x=260, y=85)

    def __make_buttons(self):
        pass

    def __make_separators(self) -> None:
        """Método responsável por criar todos os separadores da janela principal."""
        Separator(master=self.__main_window, orient="horizontal").place(x=25, y=40, width=350)

    def run(self) -> None:
        self.__main_window.mainloop()
