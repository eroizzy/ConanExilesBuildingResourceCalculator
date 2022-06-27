from ..material import material


class wood(material):
    def __init__(self) -> None:
        super().__init__(
            name="Wood",
            base_material=True,
        )

    def get_needed_material(self) -> None:
        return None
