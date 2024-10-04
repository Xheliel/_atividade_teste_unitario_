from enum import Enum

class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"

    def __init__(self, texto) -> None:
        self.texto = texto