from enum import Enum

class UnidadeFederal(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, uf_nome: str, uf_caracter: str) -> None:
        self.uf_nome = uf_nome
        self.uf_caracter = uf_caracter