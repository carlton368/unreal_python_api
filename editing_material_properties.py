import unreal

EditorAssetLibrary = unreal.EditorAssetLibrary()
MaterialEditingLibrary = unreal.MaterialEditingLibrary()

# Convenient wrapper example

def set_material_vector(material_instance: unreal.MaterialInstanceConstant, parameter_name: unreal.Name, value) -> bool:
    # Optional assert.
    # assert isinstance(material_instance, unreal.MaterialInstanceConstant)

    assert parameter_name in MaterialEditingLibrary.get_vector_parameter_names(material_instance)
    return MaterialEditingLibrary.set_material_instance_vector_parameter_value(instance=material_instance,
                                                                               parameter_name=parameter_name,
                                                                               value=value)


instance: unreal.MaterialInstanceConstant = EditorAssetLibrary.load_asset(
    "/Game/StarterContent/Materials/example_instance")
MaterialEditingLibrary.clear_all_material_instance_parameters(instance)

set_material_vector(material_instance=instance, parameter_name="Emissive color 01", value=[0.1, 0.2, 0.3, 0.4])
print(MaterialEditingLibrary.get_material_instance_vector_parameter_value(instance=instance,
                                                                          parameter_name="Emissive color 01"))

set_material_vector(material_instance=instance, parameter_name="Emissive color 02", value=[0.1, 0.2, 0.3, 0.4])
print(MaterialEditingLibrary.get_material_instance_vector_parameter_value(instance=instance,
                                                                          parameter_name="Emissive color 02"))


MaterialEditingLibrary.update_material_instance(instance)
