from materials.black_ice.black_ice_wall import black_ice_wall, material_dict, material


class test():
    def print_resource_tree(self, mat: material_dict, spacer: int=0) -> None:
        this_material = mat["mat"]
        qty = mat["qty"]
        indent= "".join(["\t" for x in range(spacer)])
        decorator: str = f'- { qty } '
        print(f'{ indent }{ decorator }{ this_material.name }')
        if not this_material.is_base_material():
            for m in this_material.get_needed_material():
                self.print_resource_tree(m, spacer=spacer+1)
    
    def test(self):
        mat: black_ice_wall = black_ice_wall()

        self.print_resource_tree(material_dict(mat=mat,qty=1))

        # for x in mat.get_needed_material():
        #     temp: material = x["mat"]
        #     if not temp.is_base_material():
        #         print(temp.get_needed_material())
        #     else:
        #         print("Base Material")


if __name__ == "__main__":
    test().test()
