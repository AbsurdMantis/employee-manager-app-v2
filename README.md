# Employee Manager Application (Frontend + Backend)

Esse repositório baseia-se em https://github.com/rodrigoclira/employee-manager-app-v1 . Na versão v2 do repositório foi adicionado uma aplicação de frontend para acessar a API disponibilizada com DRF. Sendo assim duas aplicações são inicializadas por _containers_ docker, a _frontend_ e a _backend_.

Ambas aplicações podem ser inicializadas usando o comando abaixo
```
sudo docker-compose up --build
```


![image](https://user-images.githubusercontent.com/276077/174942615-b4e7e945-2d89-4c23-836e-9ab8931b5ed3.png)


A aplicação de _frontend_ fica disponível na porta 8000

![image](https://user-images.githubusercontent.com/276077/174942679-b3aa5eaa-ab51-4c51-aa21-36f55fb13a49.png)



Ela se comunica com a aplicação de backend que está disponível na porta 8001

![image](https://user-images.githubusercontent.com/276077/174942952-37e7e1f6-75b8-4db0-ba93-87933617a63e.png)


Na aplicação de _frontend_ apenas o endpoint GET /employee e o GET /employee/ID da API estão sendo utilizados. 
Todas as views que utilizam esses endpoints estão implementadas no arquivo _views.py_ do app _web_, como exibido na imagem abaixo.

![image](https://user-images.githubusercontent.com/276077/174943242-8d6cd8ff-691f-45bb-846e-0e029004bc00.png)

Navegue na aplicação disponível na porta 8000 (_frontend_) e avalie o código dela. 

![image](https://user-images.githubusercontent.com/276077/175022904-fbe4d379-0fc8-4ce0-8e5e-9d55171e1921.png)


Para finalizar as aplicações inicializadas com o _docker-compose_, utilize o comando abaixo:

```
sudo docker-compose down
```

ou ```CTRL+C```

# Atividade

1. Como exibido na imagem do arquivo _views.py_, não há nenhuma estratégia de cache no app frontend. 
Use o memcached (como exibido no exemplo de aula) para adicionar uma estratégia de cache de baixo nível nas funções 'views.usuarios' e 'views.detalhes'. 
Utilize o 'json' obtido da API para ser a informação salva no cache. 

2. A aplicação de backend possui uma bateria de testes no arquivo backend/luizalabs/api/tests.py . Utilize o workflow do github (github action) para executar esse teste toda vez que o repositório seja modificado. Essa abordagem vai facilitar a detecção de códigos com bugs (para ver como executar os testes, acesso o [README](https://github.com/rodrigoclira/employee-manager-app-v1) do repositório original). 
> Para mais informações de como proceder, leia [Configurando o github actions](https://cassiobotaro.dev/do_zero_a_implantacao/integracao/#configurando-o-github-actions)


Use como exemplo de arquivo abaixo. Nele ainda é necessário adicionar os comandos para executar os testes da aplicação. 

```
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions
#https://hacksoft.io/github-actions-in-action-setting-up-django-and-postgres/
name: Run Backend Tests

on:
  push:
    branches:
      - master
      - main

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        cd backend/
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```

Se tudo estiver configurado corretamente, você vai ver uma imagem como abaixo ao lado do nome do projeto. 
![image](https://user-images.githubusercontent.com/276077/174945420-25ece68f-3c74-4b62-86a9-fd996300e9ec.png)

Aproveire e coloque um badge no README.md como na imagem abaixo

![image](https://user-images.githubusercontent.com/276077/174945545-81e84dfc-c56a-42c8-a368-a8f72ef2f053.png)

Para copiar o badge, você precisa ir na aba "Action" e seguir o caminho descrito na imagem abaixo. 
![image](https://user-images.githubusercontent.com/276077/174945825-dbd8f6b4-5ddc-45b9-9761-16e3c1cdd64e.png)

Por fim, salve o código do badge no README. Pronto!

> Pontuação Extra (+1 ponto)
> 
> Adicione todas as funcionalidades da API na aplicação de frontend (DELETE, PUT, POST)

## Referência

https://medium.com/@nutanbhogendrasharma/consume-rest-api-in-django-web-application-130c0daa6f70

https://docs.djangoproject.com/en/4.0/topics/cache/

https://github.com/rodrigoclira/devweb2/tree/main/caching#exemplo-de-cache-de-baixo-n%C3%ADvel
