from app.materials.base_material import BaseMaterial


class Test:
    def print_resource_tree(self) -> None:
        pass

    def test(self):
        print(BaseMaterial("Ironstone"))


if __name__ == "__main__":
    Test().test()
