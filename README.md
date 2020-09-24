# Script para salvar planilhas do CVM informando uma data

## Requisitos

Ter o docker instalado em sua máquina e preferência linux
O docker pode ser instalado com o comando abaixo:

```bash
curl -fsSL https://get.docker.com/ | sh

sudo usermod -aG docker seuusuario
```

## Utilização

### 1 - Clonar repositório
```bash
https://github.com/hevertongomes/skuad-script.git
```

### Com o terminal aberto dentro da pasta clonada seguir os passos abaixo:

### 2 - Digitar o comando para criar uma imagem

```bash
docker build -t skuadtest .
```

### 3 - Digitar comando para criar container e rodar script

```bash
docker run --name getcsv -ti skuadtest
```

### Ira aparecer a seguinte mensagem: Insira um data no formato - YYYYMM: exemplo de preenchimento = 201801

### Deve-se aguardar o download

### 4 - Digitar comando para passar arquivo do container para uma pasta de preferência

```bash
docker cp getcsv:/code/dados.csv ~/Documentos/test/Skuad/files/
```

### Pode-se alterar para desejado após o ~/