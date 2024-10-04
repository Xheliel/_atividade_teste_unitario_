from projeto.models.enums.unidade_federal import UnidadeFederativa

class Endereco:
    # Construtor
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self._logradouro = self._verificar_logradouro(logradouro)
        self._numero = self._verificar_numero(numero)
        self._complemento = complemento
        self._cep = cep
        self._cidade = cidade
        self._uf = uf

    def _verificar_logradouro(self, valor):
        self.__verificar_logradouro_tipo_invalido(valor)
        self.__verificar_logradouro_vazio(valor)

        self.logradouro = valor
        return self.logradouro
    
    def __verificar_logradouro_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve ser um texto.")
        
    def __verificar_logradouro_vazio(self, valor):
        """Método auxiliar para verificar logradouros vazios"""
        if not valor.strip():
            raise TypeError("O logradouro não pode estar vazio.")

    def _verificar_numero(self, valor):
        self.__verificar_numero_tipo_invalido(valor)
        self.__verificar_numero_vazio(valor)

        self.numero = valor
        return self.numero
    
    def __verificar_numero_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("Deve constar numeração")
        
    def __verificar_numero_vazio(self, valor):
        if valor < 0:
            raise ValueError("O número não pode ser negativo")
    
    def __str__(self) -> str:
        return (
            f"Logradouro: {self._logradouro}"
            f"\nNúmero: {self._numero}"
            f"\nComplemento: {self._complemento}"
            f"\nCEP: {self._cep}"
            f"\nCidade: {self._cidade}"
            f"\nEstado: {self._uf.nome}"
            f"\nSigla: {self._uf.sigla}"
        )