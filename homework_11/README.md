### Домашнее задание "GitHub Actions"
#### Цель:
- В этом ДЗ вы создадите action с выполнением тестов.
#### Результат:
- Приложение интернет-магазина с фоновыми задачами (например, отправка уведомлений при добавлении новых товаров.)
#### Описание/Пошаговая инструкция выполнения домашнего задания:
1. добавить GitHub Action с выполнением тестов (можно настроить на выполнение имеющихся тестов, например, тестов Django приложения)
2. БОНУС: применить какой-либо открытый ресурс для тестирования и проверки покрытия: Travis, codecov, coveralls и тд

#### Запуск GitHub Actions:
1. сделать push или pull_request
2. Actions (Run linter and Run tests) запустятся автоматически

#### Запуск Django проекта:
1. Установить зависимости
2. Выполнить миграции: 
```python
python manage.py makemigrations
python manage.py migrate
```
3. Добавить тестовые данные из фикстур:
```python
python manage.py loaddata store_fixture.json
```
или из кастомных команд: 
```python
python manage.py generate_test_data
```
4. Запустить сервер:
```python    
python manage.py runserver
```
5. Запустить Celery:
```python
celery -A config worker --pool=eventlet -l info
```
5. Админка доступна по:
``` http
http://127.0.0.1:8000/admin/
```
6.Запустить тесты:
```python    
pytest
```



