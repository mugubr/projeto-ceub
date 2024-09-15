<a id="readme-top"></a>
# Projeto  de TI - CEUB

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="../doceria-frontend/src/assets/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Katherine Corrales - Doceria (backend)</h3>

  <p align="center">
    Projeto feito para as disciplinas de Projeto de TI 1 e 2 do Centro Universitário de Brasília - UniCUEB
</div>


## Sobre o projeto

![image](https://github.com/user-attachments/assets/ba4503d3-4055-4ffd-a080-1f5115339158)


A Katherine Corrales - Doceria é uma empresa especializada na produção e comercialização de doces artesanais. Atualmente, a empresa enfrenta desafios significativos na integração e otimização de seus processos logísticos, financeiros e de relacionamento com clientes. Esses desafios impactam diretamente a eficiência operacional da empresa e sua capacidade de expansão.

<p align="right">(<a href="#readme-top">topo</a>)</p>



### Tecnologias utilizadas

* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="50" height="50" alt="Python"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" width="50" height="50" alt="Pytest"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original-wordmark.svg" width="60" height="60" alt="FastAPI"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/poetry/poetry-original.svg" width="50" height="50" alt="Poetry"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original-wordmark.svg" width="50" height="50" alt="PostgreSQL"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" width="50" height="50" alt="SQLAlchemy"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" width="50" height="50" alt="Docker"/>
          
          
          
          
          

<p align="right">(<a href="#readme-top">topo</a>)</p>



## Executando o projeto

Como executar o projeto localmente

### Pré-requisitos

* [Poetry](https://python-poetry.org/)

### Executando

1. Clone o repositório
   ```sh
   git clone https://github.com/mugubr/projeto-ceub.git
   ```
2. No diretório ```/doceria-backend```, crie um arquivo ```.env``` com as seguintes variáveis de ambiente
   ```sh
    DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
    ADMIN="katherine.corrales"
    SECRET_KEY = 'chave'
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
   ```

3. Execute o arquivo ```docker-compose.yaml```, localizado na raiz do projeto
   ```sh
   docker-compose up --build doceria_backend
   ```
4. Após os containers estarem rodando, acesse a documentação da API  em ```https://localhost:8000/docs``` e adicione um ```Cliente``` de usuário ```katherine.corrales``` (o restante dos dados fica a seu critério), que será o administrador do sistema
   
![image](https://github.com/user-attachments/assets/cddd2e70-592d-4009-9994-d99888a47e48)

5. Para acessar o sistema como administrador, utilize o ```Cliente```criado na etapa anterior, com a senha cadastrada. Para acessar o sistema como cliente, basta criar um novo ```Cliente```


