```bash
git clone https://github.com/Mahi-markus/api-dockerize-document.git
cd  api-dockerize-document
```
**run the following command**
```bash
docker compose build
```

```bash
docker compose up
```

**open anotther terminal and run the following command** 

```bash
docker exec -it api-dockerize-document-web-1 python manage.py makemigrations
```

```bash
docker exec -it api-dockerize-document-web-1 python manage.py migrate

```

**you can test this below api using postman**

```bash

http://localhost:8000/api/hello/

```