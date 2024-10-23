import unreal

EditorAssetLibrary = unreal.EditorAssetLibrary()

# editor properties of Texture2D
# https://docs.unrealengine.com/5.1/en-US/PythonAPI/class/Texture2D.html

# asset_path_list = EditorAssetLibrary.list_assets("/Game/StarterContent/Textures/")
# process normalmap textures in directory
# for asset_path in asset_path_list:
#    texture = EditorAssetLibrary.load_asset(asset_path)
#    if not isinstance(texture, unreal.Texture2D):
#        continue
#    if not str(texture.get_fname()).endswith("_N"):
#        continue
#    current_compression = texture.get_editor_property("compression_settings")
#    if current_compression != unreal.TextureCompressionSettings.TC_NORMALMAP:
#        print(f"FIXING COMPRESSION SETTINGS ON: {asset_path}")
#        texture.set_editor_property(name="compression_settings", value=unreal.TextureCompressionSettings.TC_NORMALMAP)


# suffixes based on https://gist.github.com/excalith/366e15b13c1c99539aa2600ff3d5e647#textures
COMPRESSION_MAPPING = {
    "_N": unreal.TextureCompressionSettings.TC_NORMALMAP,  # normalmap
    "_D": unreal.TextureCompressionSettings.TC_DEFAULT,    # albedo/diffuse
    "_E": unreal.TextureCompressionSettings.TC_DEFAULT,    # emissive
    "_M": unreal.TextureCompressionSettings.TC_DEFAULT,    # metalness, suggested grayscale for your own materials
    "_R": unreal.TextureCompressionSettings.TC_GRAYSCALE,  # roughness
}


def validate_compression_settings(directory: str, apply_fix: bool = True):
    asset_path_list = EditorAssetLibrary.list_assets(directory)

    for asset_path in asset_path_list:
        texture = EditorAssetLibrary.load_asset(asset_path)
        if not isinstance(texture, unreal.Texture2D):
            continue

        name = str(texture.get_fname())
        name_match = False
        correct_compression = None
        for suffix in COMPRESSION_MAPPING.keys():
            if name.endswith(suffix):
                name_match = True
                correct_compression = COMPRESSION_MAPPING[suffix]
        if not name_match:
            continue

        current_compression = texture.get_editor_property("compression_settings")
        if current_compression != correct_compression:
            print(f"WRONG COMPRESSION SETTINGS ON: {asset_path}")
            if apply_fix:
                print(f"{asset_path} compression was set to {str(correct_compression)}")
                texture.set_editor_property(name="compression_settings", value=correct_compression)


if __name__ == "__main__":
    with unreal.ScopedEditorTransaction("Fix Texture Compression"):
        validate_compression_settings(directory="/Game/StarterContent/Textures/")
