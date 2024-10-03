from abc import ABC, abstractmethod
from meu_projeto.models.abstracts.pessoa import Pessoa
from meu_projeto.models.endereco import Endereco

class Juridica(Pessoa):
    def __init__(self, cnpj: str, inscricao_estadual: str, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricao_pessoal = self._verificar_inscricao_estadual(inscricao_pessoal)

    def _verificar_cnpj(self, cnpj):
        self._cnpj_vazio(cnpj)
        
    def _cnpj_vazio(cnpj):
            if not cnpj.strip():
                 raise TypeError("Preencha o seu cnpj corretamente.")
            
    def _verificar_inscricao_estadual(self, inscricao_estadual):
        self._inscricao_estadual_vazio(inscricao_estadual)
        
    def _inscricao_estadual_vazia(inscricao_estadual):
            if not inscricao_estadual.strip():
                 raise TypeError("Preencha a inscrição estadual corretamente.")