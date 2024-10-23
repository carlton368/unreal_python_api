from pathlib import Path
from typing import Set

import unreal

def batch_import_textures(destination_path: str, source_folder: str) -> Set[unreal.Object]:
    assets_to_import = Path(source_folder).glob("*.png")
    assets_to_import = list(map(lambda path: str(path), assets_to_import))

    assets_import_data = unreal.AutomatedAssetImportData()
    assets_import_data.destination_path = destination_path
    assets_import_data.filenames = assets_to_import
    assets_import_data.replace_existing = True

    imported = set(unreal.AssetToolsHelpers.get_asset_tools().import_assets_automated(assets_import_data))
    return imported

if __name__ == "__main__":
    imported = batch_import_textures("/Game/Enviro", r"Z:\tech art channel\example_textures")
    print(imported)
