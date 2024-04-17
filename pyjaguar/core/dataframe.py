from typing import Dict, List, Tuple
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
        self._verificar_entrada(dados)
        self._verificar_comprimento(dados)
        self._dados = self._converter_unicode_para_object(dados)
        
    def _verificar_entrada(self, dados: Dict[str, np.ndarray]) -> None:
        if not isinstance(dados, dict):
            raise TypeError("O parâmetro 'dados' deve ser um dicionário!")

        for chave, valor in dados.items():
            if not isinstance(chave, str):
                raise TypeError("As chaves do dicionário 'dados' devem ser strings!")

        if not isinstance(valor, np.ndarray):
                raise TypeError("Eita! Os valores do dicionário precisam ser NumPy arrays!")

        if valor.ndim != 1:
            raise ValueError("Os valores do dicionário 'dados' devem ser arrays unidimensionais!")
        
    def _verificar_comprimento(self, dados: Dict[str, np.ndarray]) -> None:
        comprimentos = set(len(valor) for valor in dados.values())
        if len(comprimentos) != 1:
            raise ValueError("Todos os arrays no dicionário 'dados' devem ter o mesmo comprimento!")

    def _converter_unicode_para_object(self, dados: Dict[str, np.ndarray]) -> None:
        for chave, valor in dados.items():
            if valor.dtype.kind == "U":
                dados[chave] = valor.astype("object")
        return dados
    
    # ----------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Retorna o número de linhas no DataFrame.
        """
        return len(next(iter(self._dados.values())))

    @property
    def colunas(self) -> List[str]:
        """
        Retorna uma lista dos nomes das colunas.
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
            raise TypeError("Os nomes das novas colunas devem estar em uma lista!")

        if len(colunas) != len(self._dados):
            raise ValueError(f"A lista com os nomes das novas colunas deve ter o mesmo comprimento do DataFrame!")
        else:
            for col in colunas:
                if not isinstance(col, str):
                    raise TypeError("Oops! Todos os nomes das colunas devem ser strings!")

        if len(colunas) != len(set(colunas)):
            raise ValueError("Os nomes das suas colunas têm duplicatas. Isso não é permitido!")

        self._dados = dict(zip(colunas, self._dados.values()))
    
    @property
    def dimensao(self) -> Tuple[int, int]:
        """
        Retorna uma tupla contendo o número de linhas e o número de colunas respectivamente.

        Exemplo
        -------
        >>> dados = {"A": np.array([1, 2, 3]), "B": np.array(["x", "y", "z"])}
        >>> df = pj.DataFrame(dados)
        >>> df.dimensao
        (3, 2)
        """
        return len(self), len(self._dados)
        
    def _formatar_linha_html(self, indice: int) -> str:
        """
        Formata uma linha do DataFrame em HTML.
        """
        linha_html = f"<tr><td><strong>{indice}</strong></td>"
        for _, valores in self._dados.items():
            tipo = valores.dtype.kind
            if tipo == "f":
                linha_html += f"<td>{valores[indice]:.2f}</td>"
            else:
                linha_html += f"<td>{valores[indice]}</td>"
        linha_html += "</tr>"
        return linha_html

    def _repr_html_(self) -> str | None:
        """
        Usado para criar uma string HTML para exibir adequadamente o DataFrame
        em um Notebook Jupyter.
        """
        html = "<table><thead><tr><th></th>"
        html += "".join(f"<th>{col:10}</th>" for col in self.colunas)
        html += "</tr></thead><tbody>"
        
        num_linhas = min(len(self), 5)
        for i in range(num_linhas):
            html += self._formatar_linha_html(i)

        if len(self) > 5:
            html += f"<tr><td colspan='{len(self.colunas) + 1}'>...</td></tr>"
            for i in range(len(self) - 5, len(self)):
                html += self._formatar_linha_html(i)

        html += "</tbody></table>"
        return html
    
    @property
    def para_numpy(self) -> np.ndarray:
        """
        Converte o DataFrame para um NumPy array.

        Retorna
        -------
        numpy.ndarray

        Exemplo
        -------
        >>> dados = {"A": np.array([1, 2, 3]), "B": np.array(["x", "y", "z"])}
        >>> df = pj.DataFrame(dados)
        >>> df.para_numpy
        array([[1, 'x'],
               [2, 'y'],
               [3, 'z']], dtype=object)
        """
        return np.column_stack(list(self._dados.values()))

        

