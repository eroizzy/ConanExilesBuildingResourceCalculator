from abc import abstractmethod


class material(object):
    def __init__(self, name: str, base_material: bool = False) -> None:
        self._name = name
        self.base_material = base_material

    @property
    def name(self) -> str:
        return f"{ self._name }"

    @name.setter
    def name(self, name):
        self._name = name

    def is_base_material(self) -> bool:
        return self.base_material

    @abstractmethod
    def get_needed_material(self) -> list[object]:
        pass

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
