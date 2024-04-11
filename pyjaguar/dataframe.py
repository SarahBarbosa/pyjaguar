from typing import Dict, List
import numpy as np

class DataFrame:

    def __init__(self, dados: Dict[str, np.ndarray]) -> None:
        """
        Inicializa um DataFrame contendo dados heterogêneos bidimensionais.

        Para criar um DataFrame, passe um dicionário de NumPy arrays para o 
        parâmetro "dados", onde as chaves representam os nomes das colunas.

        Parâmetros
        ----------
        dados : Dict[str, np.ndarray]
            Um dicionário onde as chaves são os nomes das colunas e os valores 
            são arrays NumPy contendo os dados.

        Exemplo
        -------
        >>> import pyjaguar as pj
        >>> dados = {"A": np.array([1, 2, 3]), "B": np.array(["x", "y", "z"])}
        >>> df = pj.DataFrame(dados)
        """
        # Verifica os tipos de entradas corretos
        self._verificar_entrada(dados)

        # Verifica se os comprimentos dos arrays são iguais
        self._verificar_comprimento(dados)

        # Converte arrays unicode em object
        self._dados = self._converter_unicode_para_object(dados)

    def _verificar_entrada(self, dados: Dict[str, np.ndarray]) -> None:
        if not isinstance(dados, dict):
            raise TypeError("Você está tentando me confundir? `dados` precisa ser um dicionário!")
        
        for chave, valor in dados.items():
            if not isinstance(chave, str):
                raise TypeError("Sério? As chaves de `dados` precisam ser strings!")
            
            if not isinstance(valor, np.ndarray):
                raise TypeError("Eita! Os valores de `dados` precisam ser NumPy arrays!")
            
            if valor.ndim != 1:
                raise ValueError("Oops! Os valores de `dados` precisam ser um array de uma dimensão!")
    
    def _verificar_comprimento(self, dados: Dict[str, np.ndarray]) -> None:
        comprimentos = set(len(valor) for valor in dados.values())
        if len(comprimentos) != 1:
            raise ValueError("Algo deu errado... Todos os arrays precisam ter o mesmo comprimento!")
    
    def _converter_unicode_para_object(self, dados: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        novos_dados = {}
        for chave, valor in dados.items():
            novos_dados[chave] = valor.astype("object") if valor.dtype.kind == "U" else valor
        return novos_dados
    
    # Implementando o método especial no pyjaguar    
    def __len__(self) -> int:
        """
        Retorna
        -------
        int
            O número de linhas no DataFrame.
        """
        return len(next(iter(self._dados.values())))
    
    @property
    def colunas(self) -> List[str]:
        """
        Retorna
        -------
        list
            A lista dos nomes das colunas
        """      
        return list(self._dados)

    @colunas.setter
    def colunas(self, colunas: List[str]) -> None:
        """
        Define os nomes das colunas do DataFrame.

        Parâmetros
        ----------
        colunas : List[str]
            Uma lista de strings contendo os nomes das colunas. A lista deve ter o mesmo 
            comprimento que o número de colunas atual do DataFrame.
        
        Retorna
        -------
        None
        """
        if not isinstance(colunas, list):
            raise TypeError("Oh não! As novas colunas deve estar em uma lista!")
        
        if len(colunas) != len(self._dados):
            raise ValueError(f"Ooops! A lista com novas colunas deve ter comprimento igual a {len(self._dados)}!")
        else:
            for col in colunas:
                if not isinstance(col, str):
                    raise TypeError("Oops! Todos os nomes das colunas devem ser strings!")
        
        if len(colunas) != len(set(colunas)):
            raise ValueError("Parece que suas colunas têm duplicatas. Isso não é permitido!")
        
        self._dados = dict(zip(colunas, self._dados.values()))
        
        


