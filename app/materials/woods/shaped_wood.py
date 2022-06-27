from .. import material
from ..import material_dict
from . import wood


class shaped_wood(material):
    def __init__(self) -> None:
        super().__init__(
            name="Shaped Wood",
            base_material=False,
        )

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append(material_dict(mat=wood, qty=10))
        return ret
