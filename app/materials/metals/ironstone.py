from ..material import material


class ironstone(material):
    def __init__(self) -> None:
        super().__init__(
            name="Ironstone",
            base_material=True,
        )

    def get_needed_material(self) -> None:
        return None
