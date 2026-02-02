# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=5382

### Users API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

# Inicia el server: uvicorn users:app --reload

router = APIRouter(
    prefix='/users',
    tags=['Usuarios'],
    responses={
        404: {'description': 'Usuario no encontrado'},
        400: {'description': 'Datos inválidos'},
    },
)


class User(BaseModel):
    """
    Modelo de usuario para la API.

    Attributes:
        id: Identificador único del usuario
        name: Nombre del usuario
        surname: Apellido del usuario
        url: URL del perfil o sitio web
        age: Edad del usuario
    """

    id: int = Field(..., description='Identificador único del usuario', example=1)
    name: str = Field(..., description='Nombre del usuario', example='Brais')
    surname: str = Field(..., description='Apellido del usuario', example='Moure')
    url: str = Field(
        ..., description='URL del perfil o sitio web', example='https://moure.dev'
    )
    age: int = Field(..., description='Edad del usuario', ge=0, le=150, example=35)


users_list = [
    User(id=1, name='Brais', surname='Moure', url='https://moure.dev', age=35),
    User(id=2, name='Moure', surname='Dev', url='https://mouredev.com', age=35),
    User(id=3, name='Brais', surname='Dahlberg', url='https://haakon.com', age=33),
]


@router.get(
    '/usersjson',
    summary='Obtener usuarios en JSON',
    description='Retorna una lista de usuarios en formato JSON. Este endpoint es útil para pruebas.',
    response_description='Lista de usuarios en formato JSON',
)
async def usersjson():  # Creamos un JSON a mano
    return [
        {'name': 'Brais', 'surname': 'Moure', 'url': 'https://moure.dev', 'age': 35},
        {'name': 'Moure', 'surname': 'Dev', 'url': 'https://mouredev.com', 'age': 35},
        {
            'name': 'Haakon',
            'surname': 'Dahlberg',
            'url': 'https://haakon.com',
            'age': 33,
        },
    ]


@router.get(
    '/',
    summary='Listar todos los usuarios',
    description='Retorna una lista completa de todos los usuarios registrados en el sistema.',
    response_description='Lista de usuarios',
)
async def users():
    return users_list


@router.get(
    '/{id}',
    summary='Obtener usuario por ID',
    description='Busca y retorna un usuario específico por su identificador único.',
    responses={
        200: {'description': 'Usuario encontrado', 'model': User},
        404: {'description': 'Usuario no encontrado'},
    },
)
async def user(id: int):  # Path
    return search_user(id)


# @router.get("/user/")  # Query
# async def user(id: int):
#     return search_user(id)


# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=8529


@router.post(
    '/',
    summary='Crear nuevo usuario',
    description='Crea un nuevo usuario en el sistema. El ID debe ser único.',
    response_model=User,
    status_code=201,
    responses={
        201: {'description': 'Usuario creado exitosamente', 'model': User},
        400: {'description': 'El usuario ya existe'},
    },
)
async def createUser(user: User):
    if isinstance(search_user(user.id), User):
        raise HTTPException(status_code=400, detail='El usuario ya existe')

    users_list.append(user)
    return user


@router.put(
    '/',
    summary='Actualizar usuario',
    description='Actualiza los datos de un usuario existente. Busca por ID.',
    response_model=User,
    responses={
        200: {'description': 'Usuario actualizado', 'model': User},
        404: {'description': 'Usuario no encontrado'},
    },
)
async def updateUser(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {'error': 'No se ha actualizado el usuario'}

    return user


@router.delete(
    '/{id}',
    summary='Eliminar usuario',
    description='Elimina un usuario del sistema por su identificador único.',
    responses={
        200: {'description': 'Usuario eliminado exitosamente'},
        404: {'description': 'Usuario no encontrado'},
    },
)
async def deleteUser(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')

    return {'message': 'Usuario eliminado correctamente', 'id': id}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {'error': 'No se ha encontrado el usuario'}
