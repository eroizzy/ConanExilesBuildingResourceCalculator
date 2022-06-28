from abc import abstractmethod
from app.materials.material import Material


class BaseMaterial(Material):
    def __init__(self, name: str, base_material: bool = True) -> None:
        super().__init__(name, base_material)

    @abstractmethod
    def get_ingredient_list(self) -> None:
        return None
