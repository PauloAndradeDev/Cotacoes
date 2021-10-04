from requests import get

url: str = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"


def __cotacoes() -> dict:
    """Acessa as cotações e retorna um objeto do tipo json."""
    return get(url=url).json()


def formatar_saida() -> list:
    """Formata o json recebido de cotacoes() em uma lista contendo a cotação do dolar, euro e bitcoin, nessa ordem."""
    entrada = __cotacoes()
    return [entrada.get("USDBRL").get("bid"), entrada.get("EURBRL").get("bid"), entrada.get("BTCBRL").get("bid")]


if __name__ == "__main__":
    print(formatar_saida())
