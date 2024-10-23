from pathlib import Path
from typing import List

import unreal
# 임포트할 파일들의 대상 경로와 소스 경로를 설정합니다
destination_path = "/Game/Enviro"   # 언리얼 엔진 내에 임포트될 경로
source_path = r"Z:\tech art channel\example_meshes" # 이 경로에 있는 FBX 파일을 임포트합니다.
assets_to_import = list(Path(source_path).glob("*.fbx")) # 소스 경로에서 모든 .fbx 파일들을 찾아서 리스트로 저장
# FBX 스태틱 메시 임포트 설정을 생성합니다
static_mesh_import_data = unreal.FbxStaticMeshImportData() 
static_mesh_import_data.combine_meshes = True # 여러 메시들을 하나로 결합하여 임포트 할 지 여부
static_mesh_import_data.remove_degenerates = True # 디제너레이트 폴리곤 제거 여부
# FBX 임포트 옵션을 설정합니다
options = unreal.FbxImportUI()
options.import_mesh = True # 메시 임포트 여부
options.import_textures = False # 텍스처 임포트 여부
options.import_materials = True # 머티리얼 임포트 여부
options.automated_import_should_detect_type = True # 자동으로 에셋 타입 감지할 지 여부
options.static_mesh_import_data = static_mesh_import_data
# 임포트 작업들을 저장할 리스트 생성
tasks: List[unreal.AssetImportTask] = []
# 각 FBX 파일마다 임포트 태스크를 생성합니다
for input_file_path in assets_to_import:
    task = unreal.AssetImportTask()
    task.automated = True # 자동 임포트 모드 활성화
    task.destination_path = destination_path # 임포트될 경로 설정
    task.destination_name = input_file_path.stem   # 파일 이름에서 확장자를 제외한 이름 사용
    task.filename = str(input_file_path)  # 임포트할 파일의 전체 경로
    task.replace_existing = True  # 기존 에셋 덮어쓰기 여부
    task.save = True  # 임포트 후 자동 저장 여부
    task.options = options   # 위에서 설정한 임포트 옵션 적용

    tasks.append(task)
# 모든 임포트 태스크를 실행합니다
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(unreal.Array.cast(unreal.AssetImportTask, tasks))
# 임포트된 각 에셋의 경로를 출력합니다
for task in tasks:
    for path in task.imported_object_paths:
        print(f"Imported {path}")

"""
기능:
여러 FBX 파일들을 한 번에 임포트할 수 있습니다
메시 결합, 디제너레이트 폴리곤 제거 등의 최적화 옵션을 포함합니다
텍스처는 제외하고 메시와 머티리얼만 임포트합니다
기존 에셋은 자동으로 덮어씁니다
"""