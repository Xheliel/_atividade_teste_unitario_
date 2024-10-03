from abc import ABC, abstractmethod
from meu_projeto.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco

        @abstractmethod
        def apresentar(self):
            pass

        def _verificar_pessoa(self, id, nome, telefone, email):
            self._verificar_id(id)
            self._verificar_nome(nome)
            self._verificar_telefone(telefone)
            self._verificar_email(email)

        def _verificar_id(self, id):
            self._id_vazio(id)
            self._id_tipo(id)
            self._id_negativo(id)

            self.id = id
            return self.id

        def _id_vazio(id):
            if not id.strip():
                 raise TypeError("Preencha id.")
            
        def _id_tipo(id):
         if not isinstance(id, int):
             raise TypeError("Preencha corretamente o id.")
         
        def _id_negativo(id):
         if id <= 0:
            raise ValueError("O id não pode ser negativo.")
         

        def _verificar_nome(self, nome):
            self._nome_vazio(nome)
            self._nome_tipo(nome)

        def _nome_vazio(nome):
            if not nome.strip():
                 raise TypeError("Preencha o seu nome corretamente.")
            
        def _nome_tipo(nome):
         if not isinstance(nome, str):
             raise TypeError("Preencha corretamente o seu nome utilizando letras.")
         
         def _verificar_telefone(self, telefone):
            self._telefone_vazio(telefone)

        def _telefone_vazio(telefone):
            if not telefone.strip():
                 raise TypeError("Preencha o seu telefone corretamente.")
            
        def _verificar_email(self, email):
            self._email_vazio(email)
            
        def _email_vazio(email):
            if not email.strip():
                 raise TypeError("Preencha o seu email corretamente.")
            
        