docker-compose up -d --build

# make sure the postgres container is ready, then run migrations
sleep 5
docker exec backend-api-1 python /src/manage.py makemigrations 
docker exec backend-api-1 python /src/manage.py migrate


# docker exec backend-db-1 python manage.py migrate

#docker rmi -f $(docker images -aq)