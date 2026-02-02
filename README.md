# Mi Primera API con FastAPI

Proyecto minimalista para aprender FastAPI con las mejores prácticas.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

1. Crear el entorno virtual:
   ```bash
   python -m venv .venv
   ```

2. Activar el entorno virtual:
   - **Linux/Mac:** `source .venv/bin/activate`
   - **Windows:** `.venv\Scripts\activate`

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Instalar dependencias de desarrollo (opcional):
   ```bash
   pip install -r requirements.txt -r ".[dev]"
   ```

## Uso

### Desarrollo

```bash
fastapi dev main.py
```

O usando uvicorn directamente:
```bash
uvicorn main:app --reload
```

La API estará disponible en:
- **API:** http://127.0.0.1:8000
- **Documentación:** http://127.0.0.1:8000/docs

### Producción

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Linting y Formateo

Verificar código:
```bash
ruff check .
```

Formatear código:
```bash
ruff format .
```

## Endpoints

### Principal

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Mensaje de bienvenida |
| GET | `/saludo/{nombre}` | Saludo personalizado |
| GET | `/ping` | Verificar estado |

### Users

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/users/` | Obtener todos los usuarios |
| GET | `/users/{user_id}` | Obtener usuario por ID |
| POST | `/users/` | Crear usuario |
| PUT | `/users/{user_id}` | Actualizar usuario |
| DELETE | `/users/{user_id}` | Eliminar usuario |

### Products

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/products/` | Obtener todos los productos |
| GET | `/products/{product_id}` | Obtener producto por ID |
| POST | `/products/` | Crear producto |
| PUT | `/products/{product_id}` | Actualizar producto |
| DELETE | `/products/{product_id}` | Eliminar producto |

## Archivos Estáticos

La API sirve archivos estáticos desde el directorio `static/`:

- **Imágenes:** `/static/images/{nombre_archivo}`
- **JSON:** `/static/json/{nombre_archivo}`

## Estructura del Proyecto

```
my_fastapi/
├── main.py              # Aplicación FastAPI
├── pyproject.toml       # Configuración del proyecto y Ruff
├── requirements.txt     # Dependencias
├── .gitignore          # Archivos ignorados
├── README.md           # Este archivo
├── routers/
│   ├── __init__.py
│   ├── users.py        # Routers de usuarios
│   └── products.py     # Routers de productos
└── static/
    ├── images/
    └── json/
        └── prueba.json
```

## Aprende Más

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Ruff](https://docs.astral.sh/ruff/)
