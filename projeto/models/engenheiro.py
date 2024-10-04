from projeto.models.abstracts.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crea: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_nascimento, cpf, rg, matricula, setor, salario)
        self.crea = self._verificar_crea(crea)

    def _verificar_crea(self, valor):

        self.__verificar_crea_invalido(valor)
        self.__verificar_crea_vazio(valor)
        self.__verificar_crea_tam(valor)

        self.crea = valor
        return valor
    
    def __verificar_crea_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CREA deve ser alfa-numérico.")
        
    def __verificar_crea_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O CREA não pode estar vazio.")
        
    def __verificar_crea_tam(self, valor):
        if len(valor) < 9 or len(valor) > 13:
            raise ValueError("O tamanho do CREA não pode ser menor de 9 caractéres, ou maior que 13 carácteres.")
           
    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )