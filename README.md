# TODO (Backend)

API REST para gerenciamento de tarefas (TODO), desenvolvida com Django e Django REST Framework.

## Repositório do Frontend

🔗 [Todo (Frontend)](https://github.com/Matheus-Faneco/todo-angular)

### Como rodar
Os repositórios tanto do backend quanto do frontend possuem um Dockerfile já configurado para um ambiente de desenvolvimento.

Porém é possível rodar o projeto usando as imagens no Docker Hub, basta criar um arquivo docker-compose.yml. As imagens do frontend e do backend serão baixadas no Docker Hub e os containers estarão prontos pra execução.
```
services:
  backend:
    image: faneco/desenvolvimento-backend:latest
    ports:
      - "8000:8000"
    command: python manage.py runserver 0.0.0.0:8000

  frontend:
    image: faneco/desenvolvimento-frontend:latest
    ports:
      - "4200:4200"
    command: npm start
```
