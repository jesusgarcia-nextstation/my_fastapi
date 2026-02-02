# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475

### Products API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix='/products',
    tags=['Productos'],
    responses={
        404: {'description': 'Producto no encontrado'},
        400: {'description': 'Índice inválido'},
    },
)


class Product(BaseModel):
    """
    Modelo de producto para la API.

    Attributes:
        id: Identificador único del producto
        name: Nombre del producto
        price: Precio del producto
    """

    id: int = Field(..., description='Identificador único del producto', example=1)
    name: str = Field(..., description='Nombre del producto', example='Producto 1')
    price: float = Field(..., description='Precio del producto', ge=0, example=29.99)


products_list = [
    Product(id=1, name='Producto 1', price=29.99),
    Product(id=2, name='Producto 2', price=49.99),
    Product(id=3, name='Producto 3', price=19.99),
    Product(id=4, name='Producto 4', price=99.99),
    Product(id=5, name='Producto 5', price=9.99),
]


@router.get(
    '/',
    summary='Listar todos los productos',
    description='Retorna una lista completa de todos los productos disponibles.',
    response_description='Lista de productos',
    response_model=list[Product],
)
async def products():
    return products_list


@router.get(
    '/{id}',
    summary='Obtener producto por ID',
    description='Busca y retorna un producto específico por su identificador único.',
    responses={
        200: {'description': 'Producto encontrado', 'model': Product},
        404: {'description': 'Producto no encontrado'},
    },
    response_model=Product,
)
async def productId(id: int):
    try:
        return products_list[id]
    except IndexError:
        raise HTTPException(status_code=404, detail='Producto no encontrado')
