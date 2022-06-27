from ..material import material


class brimstone(material):
    def __init__(self) -> None:
        super().__init__(
            name="Brimstone",
            base_material=True,
        )

    def get_needed_material(self) -> None:
        return None
