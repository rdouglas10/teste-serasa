# Serasa - Developer Test

Consturção de uma API para gestão de produtor rual, com algumas validações, tais como: 
 - [X]  O sistema deverá validar CPF e CNPJ digitados incorretamente.
 - [X]  A soma de área agrícultável e vegetação, não deverá ser maior que a área total da fazenda.
 - [X]  Cada produtor pode plantar mais de uma cultura em sua Fazenda.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de validação do código e execução.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

1 - Faça o clone do projeto:
```
git clone <link-projeto>
```
2 - Entre no diretório "teste-serasa":
```
cd teste-serasa
```
3 - Crie um ambiente virtual para instalar as libs que serão utilizadas:
```
python -m venv .venv
```
4 - Ative o ambiente virtual:
```
source .venv/bin/activate
```
5 - Instale as dependências:
```
pip install -r requirements.txt
```
6 - Configuração de banco de dados:
```
Já existe uma configuração apontando para um banco chamado: teste_serasa 
(config.py), se for manter, basta somente criar a base no SGBD e a tabela 
será criada, caso contrário, deve-se alterar o nome da base no arquivo e 
criar a base no SGBD com o mesmo nome.

```
6 - Após esses passos, basta executar o comando abaixo, a aplicação será levantada e a(s) tabela(s) será(ão) criada(s) na base de dados:
```
python app.py
```


## ⚙️ Executando os testes

Para executar os testes unitários, rode o seguinte comando:

```
pytest
```


## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Flask](https://flask.palletsprojects.com/en/3.0.x/) - O framework web usado
* [venv](https://docs.python.org/3/library/venv.html) - Gerente de Dependência
* [Postgres](https://www.psycopg.org/) - Banco de dados
* [Postman](https://www.postman.com/) - Plataforma de API


## ✒️ Autor

* **Desenvolvedor** -Randerson Douglas



## 🎁 Outras informações

* Segue o arquivo com as respostas das perguntas, dentro da pasta: **avaliacao**
* Segue a collection que contém as chamadas para os endpoints, dentro da pasta **collection**;
* Segue o arquivo que contém a estrutura do banco de dados (tabela), dentro da pasta **database_script**;


---