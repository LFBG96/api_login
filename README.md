#Documentação provisória

<h1>Consumir a API</h1>

<span>No endpoint https://apenas.pythonanywhere.com/api/create/</span>
<span>Você manda como POST esse json, todos os campos são obrigatorios</span>

```
{
    "username":"Nomedousuario",
    "password":"SenhaDoUsuario"
  }
```

<span>E ele irá retornar Esse Json, com username e senha criptografada</span>

```
{
  "username": "Nomedousuario",
  "password": "pbkdf2_sha256$600000$rmmteQIhR1sisxm7Bas4X5$oiQa4kKlNgXpaEsXSVP9J2pCQl6Sc9j7IRGMJZGmkDI=",
  "timestamp": "2023-10-30T12:49:19.304685Z"
}

```

<span>Se o usuario já estiver no banco de dados, irá retornar o Json</span>

```
{
  "username": [
    "Um usuário com este nome de usuário já existe."
  ]
}
```

<span>No endpoint https://apenas.pythonanywhere.com/api/login/ Com o metodo POST</span>

``` 
{
    "username":"Nomedousuario",
    "password":"SenhaDoUsuario"
  }
```

<span>E ele irá retornar essa mensagem se tiver com username e password corretos, o token tem duração de 5 minutos</span>
```
{
  "userAuth": "true",
 "token_type": "Bearer",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NjcwNTgxLCJpYXQiOjE2OTg2NzAyODEsImp0aSI6IjYyMjlhZDU4NGRhMzQ1YTM5YjM2MmEwODQyMjJhYmYzIiwidXNlcl9pZCI6NX0.l22m9uOdo4EPV6J2XYF5GDdSJOD2wfCaQOEQXtslekg",
  "timestamp": "2023-10-30T12:51:21.882856Z"
}
```
<span>Se o usuario não existir, ou estiver errado, irá retornar</span>
```
{
  "userAuth": [
    "false"
  ],
  "timesamp": [
    "2023-10-30 12:54:40.463912+00:00"
  ]
}
```
<span>Se o usuario estiver correto, e a senha incorreta, irá retornar</span>

```
{
  "password": [
    "Senha invalida"
  ],
  "timesamp": [
    "2023-10-30 12:55:01.657066+00:00"
  ]
}
```



<span>Exemplo do token que vai junto com a requisição </span>
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NjcxNTIxLCJpYXQiOjE2OTg2NzEyMjEsImp0aSI6IjA3OTAwYjY2MDY0ZTQyNTBiZTQwZDQ0NGE5ZWQ4NjdiIiwidXNlcl9pZCI6MX0.43T02FADjsXAvIXUvQzoJ_lX3OCi1k82G3AJGVh4PgY
```
<span>Com o token de login válido, pode dar um GET no endpoint: http://apenas.pythonanywhere.com/api/a/ que irá retornar </span>
```
{
  "mensagem": "Token válido",
  "fato": "LOL>Dota",
  "timestamp": "2023-10-30T13:06:22.180813Z"
}
```


Api Login - Doc

Nesta api, foi utilizado Django e RestApi para o seu desenvolvimento, e um banco de dados SQL: o Sqlite3, padrão de aplicações Django, realizando o tratamento de dados internamente para responder os requests em formato ".json".

Temos as principais classes localizadas nos arquivos serializers.py, views.py e apps.py. 

Sendo as serializers responsáveis por converter dados complexos, como models, consultas, e instâncias em um formato legível por outras aplicações(JSON/XML). Para entrada ou saída de dados. Ex:

        - classe "CreateUserSerializer": Criando e utilizando o modelo da classe do usuário, com os atributos username, e-mail e senha sendo campos obrigatórios, 	verificando e validando as informações em seguida. (Att)

    	- classe "LoginUserSerializer": Validando a entrada de dados para executar o login. Retornando erros de entrada ou saída dos campos obrigatórios (login e senha).	


Já as classes dentro do views.py, em geral estão criando a relação e controle dentro da comunicação entre api's, retornando erros e status de portas, http e response.






A classe em apps, apenas estabelece modelos básicos para a nossa aplicação.

O arquivo url, básico do Django, controla as dependências e domínios da nossa api.

<h1>Códigos de retorno</h1>

200 OK
Tudo funcionou como esperado e a validação dos dados foi realizada com sucesso.

400 Requisição inválida
O parâmetro de entrada informado não é válido.

401 Não Autorizado
Problemas durante a autenticação.

405 Metodo não permitido

500 Erro no Servidor
Ocorreu algum erro interno no Servidor.


