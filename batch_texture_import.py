from pathlib import Path
from typing import Set

import unreal
# 텍스처 일괄 임포트를 위한 함수 정의
def batch_import_textures(destination_path: str, source_folder: str) -> Set[unreal.Object]:
    """
    PNG 텍스처들을 일괄적으로 임포트하는 함수
    
    Args:
        destination_path (str): 언리얼 엔진 내의 임포트될 경로
        source_folder (str): PNG 파일들이 있는 실제 경로
    
    Returns:
        Set[unreal.Object]: 임포트된 에셋들의 집합
    """
    assets_to_import = Path(source_folder).glob("*.png") # 소스 폴더에서 모든 PNG 파일들을 찾습니다
    assets_to_import = list(map(lambda path: str(path), assets_to_import)) # Path 객체들을 문자열로 변환합니다
    # 자동화된 에셋 임포트 설정을 생성합니다
    assets_import_data = unreal.AutomatedAssetImportData()
    assets_import_data.destination_path = destination_path # 임포트될 경로 설정
    assets_import_data.filenames = assets_to_import # 임포트할 파일 목록 설정
    assets_import_data.replace_existing = True # 기존 에셋 덮어쓰기 설정 여부
    # 에셋들을 임포트하고 임포트된 에셋들의 집합을 반환합니다
    imported = set(unreal.AssetToolsHelpers.get_asset_tools().import_assets_automated(assets_import_data))
    return imported

if __name__ == "__main__":
    imported = batch_import_textures("/Game/Enviro",
                                      r"Z:\tech art channel\example_textures") # 1.언리얼 엔진 내 대상 경로 2.소스 폴더 경로
    print(imported)
