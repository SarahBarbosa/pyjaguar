<p align="center">
  <img src=https://imgur.com/Vp1FYue.png">
</p>

# Projeto em Construção 🚧

**Nota:** A documentação fornecida é destinada apenas ao modo de desenvolvedor.

## Acknowledgement

Os fundamentos desta biblioteca foram construídos utilizando as aulas da série "Build a Data Analysis Library from Scratch in Python" disponíveis no [YouTube](https://www.youtube.com/playlist?list=PLVyhfExBT1XDTu-oocI3ttl_OPhulAJOp), ministradas por Ted Petrou. O código-fonte original pode ser encontrado no repositório [GitHub](https://github.com/tdpetrou/pandas_cub), licenciado sob a licença BSD-3-Clause.

# Criar Variável de Ambiente

## Pré-requisitos

Certifique-se de ter o Anaconda ou Miniconda instalado em seu sistema. Se ainda não o fez, você pode baixar e instalar o Anaconda a partir do [site oficial](https://www.anaconda.com/products/distribution).

## Configurando o Ambiente

1. **Clone este repositório e instale o pyjaguar:**

```bash
git clone https://github.com/SarahBarbosa/pyjaguar
cd pyjaguar
pip install -e .
```

2. **Crie o Ambiente Conda:**

Utilize o arquivo `environment.yml` para criar o ambiente Conda:

```bash
conda env create -f environment.yml
```

3. **Ative o Ambiente:**

```bash
conda activate pyjaguar
```

## Criar um Kernel Python específico para o Ambiente de Desenvolvimento

Para usar este ambiente Conda em um notebook Jupyter ou JupyterLab, você pode criar um kernel Python específico:

```bash
python -m ipykernel install --user --name pyjaguar --display-name "Python (pyjaguar)"
```

Você pode verificar se o kernel foi instalado corretamente usando o seguinte comando:

```bash
jupyter kernelspec list
```

# Implementações futuras (TODO)

- [ ] Colapsar colunas automaticamente quando o número de colunas exceder 10.

- [ ] Adicionar datasets baixáveis. 
  
- [ ] Aprimorar a manipulação de dados temporais, incluindo suporte para fusos horários, resampling avançado e operações de séries temporais.
  
- [ ] Adicionar suporte para dados geoespaciais, permitindo operações como cálculos de distância, manipulação de geometrias e análise espacial diretamente nos DataFrames.
  
- [ ] Integrar funcionalidades avançadas para facilitar a análise de dados, incluindo técnicas de feature engineering para preparação de dados para aprendizado de máquina e análise estatística.
  
- [ ] Desenvolver tabelas interativas para uma exploração mais intuitiva e interativa dos dados, possibilitando filtragem dinâmica, ordenação e visualização personalizada.
  
- [ ] Implementar a capacidade de leitura de arquivos FITS.
  
- [ ] Aprimorar a plotagem direta e intuitiva, fornecendo recursos estatísticos integrados para uma análise mais completa e visualização eficaz dos dados.
