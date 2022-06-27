from ..material import material
from ..helpers import material_dict
from .dry_wood import dry_wood
from .resin import resin


class insulated_wood(material):
    def __init__(self) -> None:
        super().__init__(
            name="Insulated Wood",
            base_material=False,
        )

    def get_needed_material(self) -> list[material_dict]:
        ret: list[material_dict] = []
        ret.append(material_dict(mat=dry_wood(), qty=1))
        ret.append(material_dict(mat=resin(), qty=2))
        return ret
