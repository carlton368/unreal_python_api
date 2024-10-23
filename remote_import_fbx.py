from pathlib import Path

import unreal


@unreal.uclass()
class RemoteImporter(unreal.Object):
    """
    @unreal.uclass(): 언리얼 엔진의 클래스 시스템에 이 파이썬 클래스를 등록
    unreal.Object: 모든 언리얼 오브젝트의 기본 클래스를 상속
    """
    @unreal.ufunction(ret=bool, params=[str, str], meta=dict(Category="TechArtCorner")) # 1.반환 타입 지정 2.매개변수 타입 지정 3.에디터에서의 분류 카테고리
    def import_fbx(self, source_path, ue_destination):
        """
        @unreal.ufunction(): 언리얼 엔진에서 호출 가능한 함수로 등록
        ret: 반환 타입 (bool - 성공/실패 여부)
        params: 매개변수 타입 목록
        meta: 함수의 메타데이터 (에디터 UI 등에서 사용)
        """
        # 스태틱 메시 임포트 설정
        static_mesh_import_data = unreal.FbxStaticMeshImportData()
        static_mesh_import_data.combine_meshes = True # 여러 메시를 하나로 결합 여부
        static_mesh_import_data.remove_degenerates = True # 문제가 있는 폴리곤 제거 여부

        # 추가 가능한 설정들:
        # (테스트 전) static_mesh_import_data.generate_lightmap_u_vs = True     # 라이트맵 UV 생성 여부
        # (테스트 전) static_mesh_import_data.auto_generate_collision = True    # 충돌체 자동 생성 여부
        # (테스트 전) static_mesh_import_data.transform_vertex_to_absolute = True  # 버텍스 위치를 절대값으로 변환 여부

        options = unreal.FbxImportUI()
        options.import_mesh = True # 메시 데이터 임포트 여부
        options.import_textures = False # 텍스처 임포트 비활성화 여부
        options.import_materials = True # 머티리얼 임포트 여부
        options.automated_import_should_detect_type = True # 자동으로 에셋 타입 감지 여부
        options.static_mesh_import_data = static_mesh_import_data

        # 추가 가능한 옵션들:
        # options.import_animations = False            # 애니메이션 임포트 비활성화 여부
        # options.create_physics_asset = False         # 물리 에셋 생성 비활성화 여부
        # options.force_front_x_axis = False          # X축 방향 강제 설정 여부
        # options.convert_scene = True                # 씬 단위 변환 여부

        task = unreal.AssetImportTask()
        task.automated = True # 자동화된 임포트 작업 여부
        task.destination_name = Path(source_path).stem # 파일 이름 추출
        task.destination_path = ue_destination # 저장될 경로
        task.filename = source_path # 소스 파일 경로
        task.replace_existing = True # 기존 파일 덮어쓰기 여부
        task.save = False  # I disabled autosave for testing purposes, # 저장 여부(테스트를 위해 비활성화)
        task.options = options
        # 추가 가능한 태스크 설정:
        # task.factory_class = None                # 특정 팩토리 클래스 지정
        # task.group_name = "MyImportGroup"        # 임포트 그룹 이름
        # task.factory = None                      # 커스텀 팩토리 지정
        
        # 4. 임포트 실행
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

        return True

