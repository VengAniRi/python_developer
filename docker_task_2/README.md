# Сборка образа.
sudo docker build --tag=my_api_img .

# Создание и запуск контейнера (с опциями detached, пробросом порта и именем)
sudo docker run -d -p 8000:8000 --name=my_api_cont my_api_img

# Отсановка контейнера
sudo docker stop my_api_cont

# Повторный запуск контейнера
sudo docker start my_api_cont

# примеры API-запросов

# Без получения токена корректно работает только запрос на получение и фильтрацию объявлений, 
# остальные без валидного токена будут выдавать ошибку авторизации.

# получение объявлений (база объявлений изначально пуста, так что список будет пустой)
GET http://127.0.0.1:8000/api/advertisements/
Content-Type: application/json

###
# Чтобы получить токен, необходимо создать superuser через консоль, 
# зайти в админку на localhost:8000/admin/ и там уже создать токен.

# создание объявления
POST http://localhost:8000/api/advertisements/
Content-Type: application/json
Authorization: Token Токен1

{
  "title": "Тумба",
  "description": "Позже"
}

###

# создание объявления от другого пользователя
POST http://localhost:8000/api/advertisements/
Content-Type: application/json
Authorization: Token Токен2

{
  "title": "Люстра",
  "description": "Позже"
}

###

# создание неавторизованного объявления
POST http://localhost:8000/api/advertisements/
Content-Type: application/json

{
  "title": "Тумба",
  "description": "Позже"
}

###

# попытка поменять объявление
PATCH http://localhost:8000/api/advertisements/1/
Content-Type: application/json
Authorization: Token Токен2

{
  "status": "OPEN"
}

###

# фильтрация по создателю
GET http://localhost:8000/api/advertisements/?creator=2
Content-Type: application/json

###

# фильтрация по дате
GET http://localhost:8000/api/advertisements/?created_at_before=2021-07-10
Content-Type: application/json

###

# удаление
DELETE http://localhost:8000/api/advertisements/12/
Content-Type: application/json
Authorization: Token Токен3

###

# попытка поменять объявление
PATCH http://localhost:8000/api/advertisements/1/
Content-Type: application/json
Authorization: Token Токен2

{
  "status": "OPEN"
}

###

# попытка поменять объявление
PATCH http://localhost:8000/api/advertisements/30/
Content-Type: application/json
Authorization: Token Токен3

{
  "status": "OPEN"
}

###

# фильтрация по содержимому
GET http://localhost:8000/api/advertisements/?description=оЧно
Content-Type: application/json

###