# Tariff API

FastAPI приложение для получения тарифов с внешнего API.

## Технологии

- Python 3.11
- FastAPI
- Docker
- aiohttp
- pydantic

## Запуск приложения

### С использованием Docker

1. Сборка и запуск контейнера:
```bash
docker-compose up --build
```

2. API будет доступно по адресу: http://localhost:8000

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
		"id": 1,
		"name": "Basic",
		"price": 100.0,
		"currency": "RUB",
		"description": "Basic tariff"
	}
]
```

## Структура проекта

```
app/
├── api/            # API endpoints
├── config/         # Конфигурации
├── core/           # Базовые компоненты
├── models/         # Pydantic модели
├── repositories/   # Работа с данными
├── services/       # Бизнес-логика
└── main.py         # Точка входа
```

## Документация API

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc