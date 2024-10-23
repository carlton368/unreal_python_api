import unreal

import_subsystem = None # 임포트 서브시스템을 저장할 변수
registered_once = False # 콜백 중복 등록 방지용 플래그
# 메시 타입별 저장 디렉토리 매핑 정의
mesh_type_to_directory_mapping = {
    "environment": "Enviro",
    "weapons": "Weapons",
    "deco": "Deco"
}


def my_post_import_callback(factory: unreal.Factory, created_object: unreal.Object):
    """
    에셋 임포트 후 실행되는 콜백 함수
    
    Args:
        factory: 임포트에 사용된 팩토리 객체
        created_object: 임포트된 에셋 객체
    """
    unreal.log(f"POST IMPORT: Factory {factory}")
    unreal.log(f"POST IMPORT: Imported {created_object}")
    # 스태틱 메시가 아니면 처리하지 않음
    if not isinstance(created_object, unreal.StaticMesh):
        return
    # 에디터 에셋 서브시스템 가져오기
    EditorAssetSubsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
    if not EditorAssetSubsystem:
        return
    # 재임포트 여부 확인
    is_reimport = "True" == EditorAssetSubsystem.get_metadata_tag(created_object, unreal.Name("importer_rules_applied"))
    print(f"{'REIMPORTING' if is_reimport else 'FIRST TIME IMPORT'}")
    # 메타데이터 설정
    EditorAssetSubsystem.set_metadata_tag(created_object, # 대상 에셋
                                          unreal.Name("importer_rules_applied"), # 태그 이름
                                          "True")# 태그 값

    value = EditorAssetSubsystem.get_metadata_tag(created_object, unreal.Name("FBX.mesh_type")) # 메시 타입 메타데이터 가져오기(중요!)
    # 에셋 이동 처리를 위한 에디터 에셋 라이브러리 객체 생성
    EditorAssetLibrary = unreal.EditorAssetLibrary()
    destination_path = f"/Game/{mesh_type_to_directory_mapping.get(value)}/{created_object.get_fname()}" # 메시 타입에 따른 새로운 경로 생성
    EditorAssetLibrary.rename_asset(created_object.get_path_name(), destination_path) # 에셋을 새 경로로 이동


def register_import_callbacks():
    global import_subsystem, registered_once
    # 이미 등록되었다면 중복 등록 방지
    if registered_once:
        return
    registered_once = True
    # 임포트 서브시스템 가져오고 콜백 등록
    import_subsystem = unreal.get_editor_subsystem(unreal.ImportSubsystem)# 임포트 서브시스템 가져오기 # 이 서브시스템은 에셋 임포트와 관련된 모든 이벤트를 처리
    import_subsystem.on_asset_post_import.add_callable(my_post_import_callback)
    # on_asset_post_import: 에셋 임포트 완료 후 발생하는 이벤트
    # add_callable: 이벤트 발생 시 실행될 함수 등록
