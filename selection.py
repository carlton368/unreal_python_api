import unreal

# ALL ASSETS IN DIRECTORY
EditorAssetLibrary = unreal.EditorAssetLibrary()

assets = EditorAssetLibrary.list_assets("/Game/StarterContent/Architecture/")
example_asset_path = assets[0]

example_asset = EditorAssetLibrary.load_asset(example_asset_path)

EditorAssetLibrary.load_asset("/Game/StarterContent/Architecture/Floor_400x400.Floor_400x400") # warning
EditorAssetLibrary.load_asset("/Game/StarterContent/Architecture/Floor_400x400")
example_asset.get_full_name()  # class info and path
example_asset.get_path_name()  # path
example_asset.get_fname()  # file name

EditorAssetLibrary.find_asset_data(example_asset_path)
example_asset.get_class() # could be compared with another class
isinstance(example_asset, unreal.StaticMesh)

# SELECTED ASSETS
EditorUtilityLibrary = unreal.EditorUtilityLibrary()
selected_assets = EditorUtilityLibrary.get_selected_assets()
EditorUtilityLibrary.get_selected_asset_data()

# ALL ACTORS
# EditorActorSubsystem = unreal.EditorActorSubsystem()  # Unreal older than 5.3
EditorActorSubsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)  # Unreal 5.3 and newer
# EditorActorSubsystem.get_all_level_actors()  # TypeError: needs an argument (and () to fix)
actors = EditorActorSubsystem.get_all_level_actors() # returns actual objects, not paths
for actor in actors:
    if isinstance(actor, unreal.SkyAtmosphere):
        print(actor)

# Selected actors
selected_actors = EditorActorSubsystem.get_selected_level_actors()
