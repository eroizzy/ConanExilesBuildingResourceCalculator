from app.materials.material import Material


class Ingredient:
    def __init__(self, material: Material, qty: int) -> None:
        self._material = material
        self._qty = qty

    @property
    def material(self) -> Material:
        return self._material

    @property
    def qty(self) -> int:
        return self._qty

    def __str__(self) -> str:
        return f"{self.qty} x {self.material.name}"

    def __repr__(self) -> str:
        return self.__str__()
