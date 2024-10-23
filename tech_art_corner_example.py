import unreal

from ImporterRules import importer_rules_manager, Rule
from ImporterRules.Actions import ImportActionBase
from ImporterRules.Queries import QueryBase

mesh_type_to_directory_mapping = {
    "environment": "Enviro",
    "weapons": "Weapons",
    "deco": "Deco"
}


class ContainsMeshTypeProperty(QueryBase):

    def test(self, factory: unreal.Factory, created_object: unreal.Object) -> bool:
        EditorAssetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
        if not EditorAssetSubsystem:
            return False

        value = EditorAssetSubsystem.get_metadata_tag(created_object, unreal.Name("FBX.mesh_type"))
        if value not in mesh_type_to_directory_mapping:
            print(f"ERROR '{value}' is not a supported FBX.mesh_type")
            return False

        return True


class MoveMeshBasedOnType(ImportActionBase):
    def apply(self, factory: unreal.Factory, created_object: unreal.Object) -> bool:
        print("MoveMeshBasedOnType")
        if created_object is None:
            return False

        EditorAssetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
        EditorAssetLibrary = unreal.EditorAssetLibrary()
        value = EditorAssetSubsystem.get_metadata_tag(created_object, unreal.Name("FBX.mesh_type"))

        destination_path = f"/Game/{mesh_type_to_directory_mapping.get(value)}/{created_object.get_fname()}"
        EditorAssetLibrary.rename_asset(created_object.get_path_name(), destination_path)
        return True


importer_rules_manager.register_rules(
    class_type=unreal.StaticMesh,
    rules=[
        Rule(
            queries=[
                ContainsMeshTypeProperty(),
            ],
            actions=[
                MoveMeshBasedOnType(),
            ]
        )
    ]
)
