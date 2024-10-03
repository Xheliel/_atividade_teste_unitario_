from abc import ABC, abstractmethod
from meu_projeto.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self) -> None:
        