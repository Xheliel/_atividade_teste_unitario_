from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")

    def __init__(self, sexo_nome: str, sexo_caracter: str) -> None:
        self.sexo_nome = sexo_nome
        self.sexo_caracter = sexo_caracter