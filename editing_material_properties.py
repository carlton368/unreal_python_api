import unreal
# 자주 사용할 에디터 라이브러리들을 변수에 할당합니다
EditorAssetLibrary = unreal.EditorAssetLibrary()
MaterialEditingLibrary = unreal.MaterialEditingLibrary()

# Convenient wrapper example
def set_material_vector(material_instance: unreal.MaterialInstanceConstant, parameter_name: unreal.Name, value) -> bool:
    """
    머티리얼 인스턴스의 벡터 파라미터 값을 설정하는 함수
    
    Args:
        material_instance: 수정할 머티리얼 인스턴스
        parameter_name: 수정할 파라미터의 이름
        value: 설정할 벡터 값 [R,G,B,A]
    
    Returns:
        bool: 설정 성공 여부
    """
    # Optional assert. # 선택적으로 타입 체크를 할 수 있습니다
    # assert isinstance(material_instance, unreal.MaterialInstanceConstant) 
    # 파라미터 이름이 실제로 존재하는지 확인합니다
    assert parameter_name in MaterialEditingLibrary.get_vector_parameter_names(material_instance)
    # 벡터 파라미터 값을 설정하고 결과를 반환합니다
    return MaterialEditingLibrary.set_material_instance_vector_parameter_value(instance=material_instance,
                                                                               parameter_name=parameter_name,
                                                                               value=value)

# 원하는 머티리얼 인스턴스를 로드합니다
instance: unreal.MaterialInstanceConstant = EditorAssetLibrary.load_asset(
    "/Game/StarterContent/Materials/example_instance") # 머티리얼 인스턴스 경로 입력
MaterialEditingLibrary.clear_all_material_instance_parameters(instance) # 기존 파라미터들을 모두 초기화합니다
# 이미시브 컬러(여기선 Emissive color 01) 파라미터를 값을 설정
set_material_vector(material_instance=instance,
                     parameter_name="Emissive color 01", 
                     value=[0.1, 0.2, 0.3, 0.4])
print(MaterialEditingLibrary.get_material_instance_vector_parameter_value(instance=instance,
                                                                          parameter_name="Emissive color 01"))
# 이미시브 컬러(여기선 Emissive color 02) 파라미터의 값을 설정
set_material_vector(material_instance=instance, parameter_name="Emissive color 02", value=[0.1, 0.2, 0.3, 0.4])
print(MaterialEditingLibrary.get_material_instance_vector_parameter_value(instance=instance,
                                                                          parameter_name="Emissive color 02"))

# 변경사항을 머티리얼 인스턴스에 적용합니다
MaterialEditingLibrary.update_material_instance(instance)
