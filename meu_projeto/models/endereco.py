from meu_projeto.models.enums.unidade_federal import UnidadeFederal

class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: UnidadeFederal) -> None:
        self.logradouro = self._verificar_logradouro
        self.numero = self._verificar_numero
        self.complemento = self._verificar_complemento
        self.cep = self._verificar_cep
        self.cidade = self._verificar_cidade
        self.uf = uf

    def _verificar_endereco(self, logradouro, numero, complemento, cep, cidade):
        self._verificar_logradouro(logradouro)
        self._verificar_numero(numero)
        self._verificar_complemento(complemento)
        self._verificar_cep(cep)
        self._verificar_cidade(cidade)

    def _verificar_logradouro(self, logradouro):
        self._logradouro_vazio(logradouro)
        self._logradouro_tipo(logradouro)

    def _logradouro_vazio(logradouro):
        if not logradouro.strip():
             raise TypeError("Preencha logradouro.")
        
    def _logradouro_tipo(logradouro):
         if not isinstance(logradouro, str):
             raise TypeError("O logradouro deve ser um texto.")
         
    def _verificar_numero(self, numero):
        self._numero_vazio(numero)
        self._numero_tipo(numero)
        self._numero_negativo(numero)

    def _numero_vazio(numero):
        if not numero.strip():
             raise TypeError("Preencha numero.")
        
    def _numero_tipo(numero):
        if not isinstance(numero, int):
             raise TypeError("O número deve ser um número.")
        
    def _numero_negativo(numero):
        if numero <= 0:
            raise ValueError("O número não pode ser negativo.")

    def _verificar_complemento(self, complemento):
        self._complemento_vazio(complemento)
        self._complemento_tipo(complemento)

    def _complemento_vazio(complemento):
        if not complemento.strip():
             raise TypeError("Preencha complemento.")
        
    def _complemento_tipo(complemento):
        if not isinstance(complemento, str):
             raise TypeError("O complemento é invalido.")
        
    def _verificar_cep(self, cep):
        self._cep_vazio(cep)

    def _cep_vazio(cep):
        if not cep.strip():
             raise TypeError("Preencha o cep.")


    def _verificar_cidade(self, cidade):
        self._cidade_vazio(cidade)
        self._cidade_tipo(cidade)

    def _cidade_vazio(cidade):
        if not cidade.strip():
             raise TypeError("Preencha cidade.")
        
    def _cidade_tipo(cidade):
        if not isinstance(cidade, str):
             raise TypeError("Cidade invalida.")
