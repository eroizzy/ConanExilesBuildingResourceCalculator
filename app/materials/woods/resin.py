from .. import material


class resin(material):
    def __init__(self) -> None:
        super().__init__(
            name="Resin",
            base_material=True,
        )

    def get_needed_material(self) -> None:
        return None
