from app.materials import material
from typing import TypedDict


class material_dict(TypedDict):
    mat: material
    qty: int
