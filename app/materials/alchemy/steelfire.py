from ..material import material
from ..helpers import material_dict
from . import tar
from ..stones import brimstone


class steelfire(material):
    def __init__(self) -> None:
        super().__init__(
            name="Steelfire",
            base_material=False,
        )

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append(material_dict(mat=tar, qty=2))
        ret.append(material_dict(mat=brimstone, qty=1))
        return ret
