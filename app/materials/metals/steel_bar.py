from .. import material, material_dict

from . import iron_bar
from ..alchemy import steelfire


class steel_bar(material):
    def __init__(self) -> None:
        super().__init__(
            name="Steel Bar",
            base_material=False,
        )

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append(material_dict(mat=steelfire(), qty=1))
        ret.append(material_dict(mat=iron_bar(), qty=5))
        return ret
