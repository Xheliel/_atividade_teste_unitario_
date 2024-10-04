from projeto.models.abstracts.juridica import Juridica
from projeto.models.endereco import Endereco

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.produto = self._verificar_produto(produto)
    
    def _verificar_produto(self, valor):
        self.__verificar_produto_tipo_invalido(valor)
        self.__verificar_produto_vazio(valor)

        self.produto = valor
        return self.produto

    def __verificar_produto_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O produto deve ser um texto")

    def __verificar_produto_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O produto não pode estar vazio")
  
    def apresentar(self):
        return (
            f"Nome: {self.nome}"
        )