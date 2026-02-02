# Clase en vídeo: https://youtu.be/_y9qQZXE24A

### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import products, users

# Metadatos de la aplicación para OpenAPI/Swagger
description = """
## API de FastAPI - Demo

Esta es una API de ejemplo construida con FastAPI que demuestra:
- Operaciones CRUD básicas
- Documentación automática con Swagger UI
- Validación de datos con Pydantic

### Características:
- **Usuarios**: Gestión de usuarios con operaciones CRUD
- **Productos**: Listado y búsqueda de productos

### Uso:
- Documentación Swagger: `/docs`
- Documentación ReDoc: `/redoc`
- OpenAPI JSON: `/openapi.json`
"""

app = FastAPI(
    title='FastAPI Demo API',
    description=description,
    summary='API de demostración con FastAPI y documentación Swagger',
    version='1.0.0',
    terms_of_service='https://example.com/terms/',
    contact={
        'name': 'Desarrollador',
        'url': 'https://github.com/mouredev',
        'email': 'dev@example.com',
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT',
    },
    docs_url='/docs',
    redoc_url='/redoc',
    openapi_url='/openapi.json',
)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475
app.include_router(products.router)
app.include_router(users.router)

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=13618
app.mount('/static', StaticFiles(directory='static'), name='static')


# Url local: http://127.0.0.1:8000


@app.get('/')
async def root():
    return 'Hola FastAPI!'


# Url local: http://127.0.0.1:8000/url


@app.get('/url')
async def url():
    return {'url': 'https://mouredev.com/python'}


# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
