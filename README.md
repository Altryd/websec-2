# Безопасность веб-приложений. ЛР №2 Борисычев Михаил 6411-100503D

### Был выбран вариант 1 - расписание.
Проект написан на:
- backend: python flask для веб-сервера, bs4 для парсинга с настоящего сайта;
- frontend: react.js, небольшое использование bootstrap для CSS.


# Установка зависимостей и запуск бекенда
Серверная часть запускалась на версии python 3.11
0) Перейдите в каталог **backend**, предварительно создав виртуальное окружение python
1) `pip install -r requirements.txt`
2) `python start_site.py`

Бекенд-приложение запустится на порту 5000

# Установка зависимостей и запуск фронтенда
0) Перейдите в каталог **frontend/websec2**
1) `npm install`
2) `npm run start`

Приложение запустится на порту 3000.

## Для тестирования приложения перейдите на адрес http://localhost:3000/

Возможности приложения:
- Выбор группы/преподавателя
- Автоматическое определение текущей недели
- Использование cookie для запоминания пользователя
- Переключение между неделями

Пример страницы приложения:
![Примерный вид приложения](https://i.imgur.com/djw8Dfk.png)