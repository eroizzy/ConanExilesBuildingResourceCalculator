from .. import material
from .. import material_dict

from . import black_ice
from ..woods import insulated_wood
from ..blacksmith import steel_reinforcement


class black_ice_foundation(material):
    def __init__(self) -> None:
        super().__init__(
            name="Black Ice-Reinforced Wooden Foundation",
            base_material=False,
        )

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append({"mat": black_ice, "qty": 15})
        ret.append({"mat": insulated_wood, "qty": 6})
        ret.append({"mat": steel_reinforcement, "qty": 3})
        return super().get_needed_material
