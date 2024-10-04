from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__()
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def apresentar(self):
        pass

    def _verificar_id(self, valor):
        self.__verificar_id_tipo_invalido(valor)
        self.__verificar_id_vazio(valor)

        self.id = valor
        return self.id
    
    def __verificar_id_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("O ID deve ser um número.")
        
    def __verificar_id_vazio(self, valor):
        if valor < 0:
            raise ValueError("O ID não pode ser negativo.")
        
    def _verificar_nome(self, valor):
        self.__verificar_nome_tipo_invalido(valor)
        self.__verificar_nome_vazio(valor)

        self.nome = valor
        return self.nome
    
    def __verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
        
    def __verificar_nome_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O nome não pode estar vazio.")
        