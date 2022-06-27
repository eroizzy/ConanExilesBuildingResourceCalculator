from ..material import material
from ..helpers import material_dict
from .ironstone import ironstone


class iron_bar(material):
    def __init__(self) -> None:
        super().__init__(
            name="Iron Bar",
            base_material=False,
        )

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append(material_dict(mat=ironstone, qty=2))
        return ret
