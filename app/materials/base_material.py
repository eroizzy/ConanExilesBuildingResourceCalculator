from . import Material

class BaseMaterial(Material):
    def __init__(self, name: str, base_material: bool = True) -> None:
        super().__init__(name, base_material)

    def get_needed_material(self) -> None:
        return None