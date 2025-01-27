```bash
cd  api-dockerize-document
```
```bash
docker compose build
```

```bash
docker compose up
```


```bash
docker exec -it api-dockerize-document-web-1 python manage.py makemigrations
```

```bash
docker exec -it api-dockerize-document-web-1 python manage.py migrate

```