from ..material import material


class black_ice(material):
    def __init__(self) -> None:
        super().__init__(name="Black Ice", base_material=True)

    def get_needed_material(self) -> None:
        return None
