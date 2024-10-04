from projeto.models.abstracts.juridica import Juridica
from projeto.models.endereco import Endereco

class PrestacaoServico(Juridica):
    # Construtor
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str, contrato_inicio: str, contrato_fim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.contrato_inicio = self._verificar_contrato_inicio(contrato_inicio)
        self.contrato_fim = self._verificar_contrato_fim(contrato_fim)

    def _verificar_contrato_inicio(self, valor):
        self.__verificar_contrato_inicio_tipo_invalido(valor)
        self.__verificar_contrato_inicio_vazio(valor)

        self.contrato_inicio = valor
        return self.contrato_inicio

    def __verificar_contrato_inicio_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O inicio de contrato deve ser alfa-númerico.")
        
    def __verificar_contrato_inicio_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O início do contrato não pode estar vazio.")
        
    def _verificar_contrato_fim(self, valor):
        self.__verificar_contrato_fim_tipo_invalido(valor)
        self.__verificar_contrato_fim_vazio(valor)

        self.contrato_fim = valor
        return self.contrato_fim

    def __verificar_contrato_fim_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O final do contrato deve ser alfa-númerico.")
        
    def __verificar_contrato_fim_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O fim do contrato não pode estar vazio.")

    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )    