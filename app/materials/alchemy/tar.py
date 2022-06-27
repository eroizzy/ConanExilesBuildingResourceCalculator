from .. import material


class tar(material):
    def __init__(self) -> None:
        super().__init__(
            name="Tar",
            base_material=True,
        )

    def get_needed_material(self) -> None:
        return None