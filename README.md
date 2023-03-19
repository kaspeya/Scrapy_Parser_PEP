# Проект парсинга PEP
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://scrapy.org/)

## Асинхронный парсинг документов PEP на базе фреймворка Scrapy.

> Парсер собирает данные со страницы с общей информацией о PEP (https://peps.python.org/), переходит по ссылкам, собирает данные о PEP с каждой ссылки и выводит собранную информацию в два файла .csv:
> *Файл с общим списком PEP (номер, название и статус);
> *Файл со сводкой по статусам, в нем подсчитывает количество каждого статуса и сумму всех статусов документов PEP на основе первого файла (статус, количество, общий тотал).

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:kaspeya/scrapy_parser_pep.git
```

Создать и активировать виртуальное окружение:
```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Запуск парсера
```
scrapy crawl pep
```
Автор: [Елизавета Шалаева](https://github.com/kaspeya)
