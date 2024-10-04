from abc import abstractmethod
from projeto.models.abstracts.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

class Fisica(Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.data_nascimento = self._verificar_data_nascimento(data_nascimento)

    @abstractmethod
    def apresentar(self):
        pass

    def _verificar_data_nascimento(self, valor):
        self.__verificar_data_nascimento_tipo_invalido(valor)
        self.__verificar_data_nascimento_vazio(valor)

        self.data_nascimento = valor
        return valor
    
    def __verificar_data_nascimento_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A data de nascimento deve ser númerica.")

    def __verificar_data_nascimento_vazio(self, valor):
        if not valor.strip():
            raise ValueError("A data de nascimento não pode estar vazia.")