from materials.material import material
from typing import TypedDict


class material_dict(TypedDict):
    mat: material
    qty: int
