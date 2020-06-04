# Rest API em Flask & SQL Alchemy

### Para criar um novo o db

Entre no shell python dentro da pasta do seu projeto

```sh
$ python
$ from app import db 
$ db.create_all() 
$ exit() 
```

### Rodar a aplicação
No terminal execute para inicializar o projeto  
```sh
$ python app.py 
```
Use o Postman com a url (http://localhost:5000), com os endpoints para fazer a chamada na API


### Endpoints
<p> - GET /contact - Rota para retornar todos os contatos</p>

<p> - GET /contact/:id - Rota para retornar apenas o contanto desajado pelo ID</p>

<p> - POST /contact - Rota para adicionar um novo contato</p>

<p> - PUT /contact/:id - Rota para atualizar um contato desejado pelo ID</p>

<p> - DELETE /contact/:id - Rota para deletar um contato desejado pelo ID</p>

## Construído com 
- Linguagem utilizada: **Python 3.8**
- Biblioteca utilizada: **Flask** & **SQLAlchemy**
- Ferramenta utilizada para chamada na API: [Postman](https://www.postman.com/)

## Autores 
<p> Suellen Medeiros</p>


