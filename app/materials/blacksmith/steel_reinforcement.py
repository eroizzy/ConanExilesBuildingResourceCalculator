from ..material import material
from ..helpers import material_dict
from ..metals.steel_bar import steel_bar


class steel_reinforcement(material):
    def __init__(self) -> None:
        super().__init__(
            name="Steel Reinforcement",
            base_material=False,
        )

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append(material_dict(mat=steel_bar(), qty=2))
        return ret
