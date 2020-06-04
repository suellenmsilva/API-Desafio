#Rest API em Flask & SQL Alchemy

#Como criar o db

Entre no shell python

$ python

from app import db 

db.create_all() - para criar o db

exit() - para sair do shell 

#Rodar a aplicação
No terminal 

python app.py  (http://localhost:5000)

#Endpoints
GET /contact - Rota para retornar todos os contatos

GET /contact/:id - Rota para retornar apenas o contanto desajado pelo ID

POST /contact - Rota para adicionar um novo contato

PUT /contact/:id - Rota para atualizar um contato desejado pelo ID

DELETE /contact/:id - Rota para deletar um contato desejado pelo ID


