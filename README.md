#Documentação provisória

<h1>Consumir a API</h1>

<span>No endpoint https://apenas.pythonanywhere.com/api/create/</span>
<span>Você manda como POST esse json, todos os campos são obrigatorios</span>

```
{
    "username":"Nomedousuario",
    "email":"Email@live.com",
    "password":"SenhaDoUsuario"
  }
```

<span>E ele irá retornar Esse Json, com username, email e a senha criptografada</span>

```
{
    "username": "Nomedousuario",
    "email": "Email@live.com",
    "password": "pbkdf2_sha256$320000$e7lEsYLNqtulPpFKKnm7kh$VPkRwlELas4o6MOq/pFfRN1TC4b2EO6rlEl58QxjH+8="
  }

```


<span>No endpoint https://apenas.pythonanywhere.com/api/login/</span>
<span>Ele necessita apenas do username e password para funcionar</span>

``` 
{
    "username":"Nomedousuario",
    "password":"SenhaDoUsuario"
  }
```

<span>E ele irá retornar essa mensagem se tiver com username e password corretos</span>
```
{
    "mensagem": "logado com sucesso"
  }
```


Api Login - Doc

Nesta api, foi utilizado Django e RestApi para o seu desenvolvimento, e um banco de dados SQL: o Sqlite3, padrão de aplicações Django, realizando o tratamento de dados internamente para responder os requests em formato ".json". Permitindo somente requisições Post, exclusivamente por questões de segurança.

Temos as principais classes localizadas nos arquivos serializers.py, views.py e apps.py. 

Sendo as serializers responsáveis por converter dados complexos, como models, consultas, e instâncias em um formato legível por outras aplicações(JSON/XML). Para entrada ou saída de dados. Ex:

