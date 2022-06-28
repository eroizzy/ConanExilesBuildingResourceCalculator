from app.materials.material import Material
from app.materials.ingredients import Ingredient


class CraftedMaterial(Material):
    def __init__(
        self, name: str, ingredient_list: list[Ingredient], base_material: bool = False
    ) -> None:
        super().__init__(name, base_material)
        self.ingredient_list = ingredient_list

    def get_ingredient_list(self) -> list[Ingredient]:
        return self.ingredient_list
