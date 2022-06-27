from ..material import material
from ..helpers import material_dict
from .black_ice import black_ice
from ..woods.insulated_wood import insulated_wood
from ..blacksmith.steel_reinforcement import steel_reinforcement


class black_ice_wall(material):
    def __init__(self) -> None:
        super().__init__(name="Black Ice-Reinforced Wooden Wall", base_material=False)

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append(material_dict(mat=black_ice(), qty=8))
        ret.append(material_dict(mat=insulated_wood(), qty=3))
        ret.append(material_dict(mat=steel_reinforcement(), qty=2))

        return ret
