from tkinter import (
    Tk,
    Label
)
from tkinter.ttk import Separator


class MainWindow:
    def __init__(self) -> None:
        """Construtor da classe MainWindow."""
        self.__main_window: Tk = Tk()
        self.__main_window.title("Principais Cotações")
        self.__main_window.configure(background="#FFFFFF")
        self.__main_window.geometry(
            newGeometry="%dx%d+%d+%d" % (
                400,
                200,
                self.__main_window.winfo_screenwidth() / 2 - 400 / 2,
                self.__main_window.winfo_screenheight() / 2 - 200 - 2
            )
        )
        # Make Widgets:
        self.__make_labels()
        self.__make_separators()

    def __make_labels(self, dolar: str, euro: str, bitcoin: str) -> None:
        """Método responsável por criar todas as labels da janela principal."""
        pass

    def __make_separators(self) -> None:
        """Método responsável por criar todos os separadores da janela principal."""
        pass

    def run(self) -> None:
        self.__main_window.mainloop()


if __name__ == "__main__":
    MainWindow().run()
