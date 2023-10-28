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

<span>E ele irá retornar Esse Json, com username, email e a senha criptografada</span>

```
{
    "username": "Nomedousuario",
    "password": "pbkdf2_sha256$320000$e7lEsYLNqtulPpFKKnm7kh$VPkRwlELas4o6MOq/pFfRN1TC4b2EO6rlEl58QxjH+8="
  }

```


<span>No endpoint https://apenas.pythonanywhere.com/api/login/ Com o metodo POST</span>

``` 
{
    "username":"Nomedousuario",
    "password":"SenhaDoUsuario"
  }
```

<span>E ele irá retornar essa mensagem se tiver com username e password corretos</span>
```
{
    "userAuth": "true"
  }
```
<span>Se o usuario não existir, ou estiver errado, irá retornar</span>
```
{
    "userAuth": [
        "false"
    ]
}
```
<span>Se o usuario estiver correto, e a senha incorreta, irá retornar</span>

```
{
    "password": [
        "Senha invalida"
    ]
}
```



Api Login - Doc

Nesta api, foi utilizado Django e RestApi para o seu desenvolvimento, e um banco de dados SQL: o Sqlite3, padrão de aplicações Django, realizando o tratamento de dados internamente para responder os requests em formato ".json". Permitindo somente requisições Post, exclusivamente por questões de segurança.

Temos as principais classes localizadas nos arquivos serializers.py, views.py e apps.py. 

Sendo as serializers responsáveis por converter dados complexos, como models, consultas, e instâncias em um formato legível por outras aplicações(JSON/XML). Para entrada ou saída de dados. Ex:

        - classe "CreateUserSerializer": Criando e utilizando o modelo da classe do usuário, com os atributos username, e-mail e senha sendo campos obrigatórios, 	verificando e validando as informações em seguida. (Att)

    	- classe "LoginUserSerializer": Validando a entrada de dados para executar o login. Retornando erros de entrada ou saída dos campos obrigatórios (login e senha).	


Já as classes dentro do views.py, em geral estão criando a relação e controle dentro da comunicação entre api's, retornando erros e status de portas, http e response.






A classe em apps, apenas estabelece modelos básicos para a nossa aplicação.

O arquivo url, básico do Django, controla as dependências e domínios da nossa api.


