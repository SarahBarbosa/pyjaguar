<p align="center">
  <img src=https://imgur.com/Vp1FYue.png">
</p>

# Projeto em Construção 🚧

**Nota:** Este projeto está em construção e a documentação fornecida é destinada apenas ao modo de desenvolvedor.

# Criar Variável de Ambiente

## Pré-requisitos

Certifique-se de ter o Anaconda ou Miniconda instalado em seu sistema. Se ainda não o fez, você pode baixar e instalar o Anaconda a partir do [site oficial](https://www.anaconda.com/products/distribution).

## Configurando o Ambiente

1. **Clone este repositório:**

```bash
git clone https://github.com/SarahBarbosa/pyjaguar
cd pyjaguar
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

# Criar um Kernel Python específico para o Ambiente de Desenvolvimento

Para usar este ambiente Conda em um notebook Jupyter ou JupyterLab, você pode criar um kernel Python específico:

```bash
python -m ipykernel install --user --name pyjaguar --display-name "Python (pyjaguar)"
```

Você pode verificar se o kernel foi instalado corretamente usando o seguinte comando:

```bash
jupyter kernelspec list
```