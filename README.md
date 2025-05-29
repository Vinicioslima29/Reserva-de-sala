<font size="7">**API de Reserva de Salas**</font>


Este repositório contém uma API de Reserva de Salas, desenvolvida com Flask e SQLAlchemy.

_____________________________________________________________________________________________________________________________________________
### PRINCIPAIS FUNCIONALIDADES

Esta API é um microsservoço que faz parte de uma outra API de um sistema escolar, sendo responsável somente pelo gerenciamento das reservas das salas por turma. 

Portanto, esta API **depende** da API do [Sistema Escolar](https://github.com/EduardoRm61/Grupo8_Api_Impacta.git).

A comunicação entre os serviços ocorre via requisições HTTP REST, para validar:

Se a Turma existe (GET /turmas/<id<id>>)

____________________________________________________________________________________________________________________________________________
### TECNOLOGIAS UTILIZADAS

- Python 3.10 ou superior
- Flasck
- SQLAlchemy
- SQLite
- Requests

### COMO EXECUTAR A API

**1. Clone o repositório**

```bash
git clone https://github.com/Vinicioslima29/Reserva-de-sala.git
```

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Execute a API**
```bash
python app.py
```
Após a inicialização, a API estará disponível em http://localhost:5001.

### ENDPOINTS PRINCIPAIS
- GET /reserva – Lista todas as reservas
- GET /reserva/<id<id>> – Detalha uma reserva
- POST /reserva – Cria uma nova reserva




###  RODANDO COM O DOCKER LOCALMENTE
<div align="center">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Logo" width="">
</div>

### 1. Build da imagem

```bash
docker build -t flask-api .
```

### 2. Rodar o container

```bash
docker run -p 5001:5001 flask-api
```


____________________________________________________________________________________________________________________________________________
### EXPLICAÇÃO DA ARQUITETURA

A API segue uma arquitetura RESTful, com separação clara entre os recursos e suas respectivas operações CRUD. Os principais componentes são:



<div align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Logo" width="">
</div>
Utilizado como framework web para gerenciar requisições HTTP e lógica de negócios.

<br>
<br>
<div align="center">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="Logo" width="">
</div>
Gerencia o acesso ao banco de dados relacional, permitindo mapeamento objeto-relacional (ORM).



____________________________________________________________________________________________________________________________________________


### AUTORES
Alessandra F Rigonatti <br>
Eduardo Nunes <br>
Rafaela Wohlers Rodrigues<br> 
Thainá Foltran de Lima<br> 
Vinicios de Lima Basteiro<br>
