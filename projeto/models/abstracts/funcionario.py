from abc import abstractmethod
from projeto.models.abstracts.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Funcionario(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = self.verificar_matricula(matricula)
        self.setor = setor
        self.salario = self.verificar_salario(salario)

    @abstractmethod
    def apresentar(self):
        pass

    def verificar_matricula(self, valor):
        """Método para verificação da matrícula"""
        self.__verificar_matricula_tipo_invalido(valor)
        self.__verificar_matricula_vazio(valor)
        self.__verificar_matricula_tam(valor)

        self.matricula = valor
        return valor
    
    def __verificar_matricula_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A matrícula deve ser alfa-numérica.")
        
    def __verificar_matricula_vazio(self, valor):
        if not valor.strip():
            raise ValueError("A matrícula não pode estar vazia.")

    def __verificar_matricula_tam(self, valor):
        if len(valor) < 10:
            raise ValueError("A matrícula deve ter 10 carácteres.")

    def verificar_salario(self, valor):
        self.__verificar_salario_tipo_invalido(valor)
        self.__verificar_salario_min(valor)

        self.salario = valor
        return valor
    
    def __verificar_salario_tipo_invalido(self, valor):
        if not isinstance(valor, float):
            raise TypeError("O salário deve ser decimal.")
        
    def __verificar_salario_min(self, valor):
        if valor < 1412.00:
            raise ValueError("O salário não pode ser abaixo do mínimo.")