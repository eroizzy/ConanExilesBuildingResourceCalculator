from materials import material
from materials.black_ice.black_ice_wall import black_ice_wall


class test():
    def test():
        mat: black_ice_wall = black_ice_wall()

        for x in mat.get_needed_material():
            temp: material = x["mat"]
            if not temp.is_base_material():
                print(temp.get_needed_material())
            else:
                print("Base Material")

if __name__ == "__main__":
    test.test()
