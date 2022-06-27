from .. import material


class dry_wood(material):
    def __init__(self) -> None:
        super().__init__(
            name="Dry Wood",
            base_material=True,
        )

    def get_needed_material(self) -> None:
        return None
