# Tariff API

FastAPI приложение для получения тарифов с внешнего API.

## Технологии

- Python 3.11
- FastAPI 0.104.1
- Docker
- aiohttp 3.8.6
- pydantic 2.4.2
- uvicorn 0.24.0

## Зависимости

```pip-requirements
fastapi==0.104.1
uvicorn[standard]==0.24.0
aiohttp==3.8.6
pydantic==2.4.2
pydantic-settings==2.0.3
python-dotenv==1.0.0
```

## Конфигурация

Создайте файл `.env` в корне проекта со следующими переменными:

```env
API_BASE_URL=https://dev.whatcrm.net/v3
TOKEN=your_token_here
CURRENCY=RUB
CRM=lk
```

## Запуск приложения

### С использованием Docker

1. Сборка и запуск контейнера:
```bash
docker-compose up --build
```

Dockerfile:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. API будет доступно по адресу: `http://localhost:8000`

### Локальный запуск

1. Создание виртуального окружения:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Установка зависимостей:
```bash
pip install -r requirements.txt
```

3. Запуск приложения:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### GET /tariffs

Получение списка тарифов.

Пример ответа:
```json
[
		{
				"id": 194,
				"name": "1 месяц 1390.00/30 дней",
				"price": 1390.0,
				"currency": "RUB",
				"description": "1 месяц 1390.00/30 дней - Всего: 1 390.00₽"
		},
		{
				"id": 195,
				"name": "3 месяца 1390.00/месяц",
				"price": 4170.0,
				"currency": "RUB",
				"description": "3 месяца 1390.00/месяц - Всего: 4 170.00₽"
		}
]
```

## Структура проекта

```
app/
├── api/                # API endpoints
│   └── tariff_router.py
├── config/            # Конфигурации
│   └── settings.py
├── core/             # Базовые компоненты
│   └── http_client.py
├── models/           # Pydantic модели
│   └── tariff.py
├── repositories/     # Работа с данными
│   └── tariff_repository.py
├── services/         # Бизнес-логика
│   └── tariff_service.py
├── exceptions.py     # Обработка ошибок
├── logger.py        # Настройка логирования
└── main.py          # Точка входа
```

## Обработка ошибок

API включает обработку следующих ошибок:
- 500 Internal Server Error - при ошибках взаимодействия с внешним API
- 404 Not Found - если тарифы не найдены
- 400 Bad Request - при некорректных параметрах запроса

## Документация API

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Логирование

Приложение включает систему логирования с записью:
- Информации о запросах к внешнему API
- Ошибок при обработке данных
- Информации о количестве обработанных тарифов

## Лицензия

MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


