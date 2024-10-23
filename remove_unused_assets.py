from typing import List

import unreal

EditorUtilityLibrary = unreal.EditorUtilityLibrary()
EditorAssetLibrary = unreal.EditorAssetLibrary()


def get_selected_asset_paths() -> str:
    selected_assets = EditorUtilityLibrary.get_selected_assets()

    for asset in selected_assets:
        yield EditorAssetLibrary.get_path_name_for_loaded_asset(asset)


def remove_unused_assets(asset_path: str):
    references = EditorAssetLibrary.find_package_referencers_for_asset(asset_path)

    if len(references) == 0:
        delete_success = EditorAssetLibrary.delete_asset(asset_path)
        if not delete_success:
            unreal.log_warning(f"Could not delete {asset_path}")


if __name__ == "__main__":
    for path in get_selected_asset_paths():
        remove_unused_assets(path)
