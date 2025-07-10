# Rick & Morty Characters API

A Django REST API for managing and retrieving Rick & Morty character data, with periodic synchronization from the official Rick & Morty API.

## Requirements

- Python 3.10+
- Redis (for Celery broker and backend)
- pip (Python package manager)

All Python dependencies are listed in [requirements.txt](requirements.txt).

## Technologies Used

- **Django**: Web framework for the backend.
- **Django REST Framework**: For building RESTful APIs.
- **drf-spectacular**: For OpenAPI schema and Swagger documentation.
- **Celery**: For background tasks (syncing characters).
- **django-celery-beat**: For periodic task scheduling.
- **SQLite**: Default database (can be changed in settings).
- **Redis**: Message broker and result backend for Celery.

## How to Run

### 1. Install Dependencies

```sh
pip install -r requirements.txt
```

### 2. Set Up Redis

Ensure Redis is running locally on port 6379 (default).

**On macOS (with Homebrew):**
```sh
brew install redis
brew services start redis
```

**On Ubuntu:**
```sh
sudo apt-get install redis-server
sudo service redis-server start
```

### 3. Apply Migrations

```sh
python manage.py migrate
```

### 4. Run the Development Server

```sh
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

### 5. Start Celery Worker

In a separate terminal, run:

```sh
celery -A rick_and_morty_api worker --beat --scheduler django --loglevel=info
```

This will start the Celery worker and enable periodic synchronization with the Rick & Morty API.

### 6. Access API Documentation

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## Endpoints

### Character Endpoints

- `GET /api/characters/`: List all characters.
- `GET /api/characters/{id}/`: Retrieve a specific character by ID.

### Location Endpoints

- `GET /api/locations/`: List all locations.
- `GET /api/locations/{id}/`: Retrieve a specific location by ID.

### Episode Endpoints

- `GET /api/episodes/`: List all episodes.
- `GET /api/episodes/{id}/`: Retrieve a specific episode by ID.

## Celery Tasks

- `sync_characters`: Periodically sync characters from the Rick & Morty API.


## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add your feature'`.
5. Push to the branch: `git push origin feature/YourFeature`.
6. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.