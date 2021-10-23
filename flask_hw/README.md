# Команда для запуска стандартного контейнера с postgres, нужного для работы приложения
sudo docker run --name flask-pg -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=flask_api -p 5432:5432 -d postgres

# В файле client.py есть тестовые запросы для API