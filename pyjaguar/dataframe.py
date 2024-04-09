from typing import Dict
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
    
    def _verificar_entrada(self, dados):
        if not isinstance(dados, dict):
            raise TypeError("`dados` precisa ser um dicionário!")
        
        for chave, valor in dados.items():
            if not isinstance(chave, str):
                raise TypeError("As chaves de `dados` precisam ser strings!")
            
            if not isinstance(valor, np.ndarray):
                raise TypeError("Os valores de `dados` precisam ser NumPy arrays!")
            
            if valor.ndim != 1:
                raise ValueError("Os valores de `dados` precisam ser um array de uma dimensão!")
            
