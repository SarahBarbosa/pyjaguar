import numpy as np
import pyjaguar as pj
import pytest

# Arrays para teste
a = np.array(["a", "b", "c"])
b = np.array(["c", "d", None])
c = np.random.rand(3)
d = np.array([True, False, True])
e = np.array([1, 2, 3])

# DataFrame para teste
df = pj.DataFrame({"a": a, "b": b, "c": c, "d": d, "e": e})


class TestSelecao:

    def test_uma_coluna(self):
        # Testa a seleção de uma única coluna
        assert np.array_equal(df["a"].para_array[:, 0], a)  
        assert np.array_equal(df["c"].para_array[:, 0], c) 
    
    def test_multiplas_colunas(self):
        # Testa a seleção de múltiplas colunas
        colunas = ["a", "b"]
        df_esperado = df[colunas]                       
        df_resposta = pj.DataFrame({"a": a, "b": b})   

        # Verifica se as colunas selecionadas são iguais ao DataFrame esperado
        assert np.array_equal(df_esperado._dados["a"], df_resposta._dados["a"])
        assert np.array_equal(df_esperado._dados["b"], df_resposta._dados["b"])
    
    def test_booleano_simples(self):
        # Testa a seleção usando um array booleano
        bool_arr = np.array([True, False, False])
        df_bool = pj.DataFrame({"col": bool_arr})       

        df_esperado = df[df_bool]                      
        df_resposta = pj.DataFrame({"a": a[bool_arr], "b": b[bool_arr], 
                                    "c": c[bool_arr], "d": d[bool_arr], 
                                    "e": e[bool_arr]}) 
        
        assert np.array_equal(df_esperado._dados, df_resposta._dados)

        # Testa se uma exceção é levantada quando o DataFrame booleano possui mais de uma coluna
        with pytest.raises(ValueError):
            df_bool = pj.DataFrame({"col": bool_arr, "col2": bool_arr})
            df[df_bool]

        # Testa se uma exceção é levantada quando o DataFrame booleano possui tipos de dados inválidos
        with pytest.raises(TypeError):
            df_bool = pj.DataFrame({"col": np.array[1, 2, 3]})
    
    def test_tupla_simultanea(self):
        # Testa se exceções são levantadas ao usar uma tupla vazia ou múltiplos elementos como índice
        with pytest.raises(TypeError):
            df[set()]
        with pytest.raises(ValueError):
            df[(1, 2, 3)]
    
    def test_elemento_unico(self):     
        # Testa se a seleção de um único elemento retorna o resultado esperado      
        df_esperado = df[1, "e"]
        df_resposta = pj.DataFrame({"e": np.array([2])})

        assert np.array_equal(df_esperado._dados, df_resposta._dados)
    
    def test_todas_selecoes_linha(self):
        df1 = pj.DataFrame({"a": np.array([True, False, True]), "b": np.array([1, 3, 5])})
        
        with pytest.raises(ValueError):
            df[df1, "e"]
        with pytest.raises(TypeError):
            df[df1["b"], "c"]

        df_esperado = df[df1["a"], "c"]
        df_resposta = pj.DataFrame({"c": c[[True, False, True]]})
        assert np.array_equal(df_esperado._dados["c"], df_resposta._dados["c"])

        df_esperado = df[[1, 2], 0]
        df_resposta = pj.DataFrame({"a": a[[1, 2]]})
        assert np.array_equal(df_esperado._dados["a"], df_resposta._dados["a"])

        df_esperado = df[1:, 0]
        assert np.array_equal(df_esperado._dados["a"], df_resposta._dados["a"])

    def test_lista_colunas(self):
        df_resposta = pj.DataFrame({"c": c, "e": e})
        
        df_esperado = df[:, [2, 4]]
        assert np.array_equal(df_esperado._dados["c"], df_resposta._dados["c"])
        assert np.array_equal(df_esperado._dados["e"], df_resposta._dados["e"])
        
        df_esperado = df[:, [2, "e"]]
        assert np.array_equal(df_esperado._dados["c"], df_resposta._dados["c"])
        assert np.array_equal(df_esperado._dados["e"], df_resposta._dados["e"])
        
        df_esperado = df[:, ["c", "e"]]
        assert np.array_equal(df_esperado._dados["c"], df_resposta._dados["c"])
        assert np.array_equal(df_esperado._dados["e"], df_resposta._dados["e"])

        df_esperado = df[2, ["a", "e"]]
        df_resposta = pj.DataFrame({"a": a[[2]], "e": e[[2]]})
        assert np.array_equal(df_esperado._dados["a"], df_resposta._dados["a"])
        assert np.array_equal(df_esperado._dados["e"], df_resposta._dados["e"])

        df_resposta = pj.DataFrame({"c": c[[1, 2]], "e": e[[1, 2]]})
        df_esperado = df[[1, 2], ["c", "e"]]
        assert np.array_equal(df_esperado._dados["c"], df_resposta._dados["c"])
        assert np.array_equal(df_esperado._dados["e"], df_resposta._dados["e"])

        df1 = pj.DataFrame({"a": np.array([True, False, True]), "b": np.array([1, 3, 5])})
        df_resposta = pj.DataFrame({"c": c[[0, 2]], "e": e[[0, 2]]})
        df_esperado = df[df1["a"], ["c", "e"]]
        assert np.array_equal(df_esperado._dados["c"], df_resposta._dados["c"])
        assert np.array_equal(df_esperado._dados["e"], df_resposta._dados["e"])
