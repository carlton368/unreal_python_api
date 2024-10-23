import unreal
from pathlib import Path

def print_all_metadata(imported_asset):
    """
    에셋의 모든 가능한 메타데이터를 출력하는 함수
    """
    asset_subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    
    print("\n=== 에셋 기본 정보 ===")
    print(f"에셋 이름: {imported_asset.get_name()}")
    print(f"에셋 경로: {imported_asset.get_path_name()}")
    print(f"에셋 타입: {imported_asset.get_class().get_name()}")
    
    # 1. FBX 기본 메타데이터
    print("\n=== FBX 기본 메타데이터 ===")
    fbx_basic_tags = [
        "FBX.Creator",
        "FBX.Version",
        "FBX.CreationTime", 
        "FBX.LastSaved",
        "FBX.Creator.Version",
        "FBX.System.Units",
        "FBX.AxisSystem",
        "FBX.OriginalUpAxis",
        "FBX.OriginalUpAxisSign",
        "FBX.OriginalFrontAxis",
        "FBX.OriginalFrontAxisSign",
        "FBX.OriginalCoordAxis",
        "FBX.OriginalCoordAxisSign",
        "FBX.FileVersion"
    ]
    
    for tag in fbx_basic_tags:
        value = asset_subsystem.get_metadata_tag(imported_asset, unreal.Name(tag))
        if value:
            print(f"{tag}: {value}")
    
    # 2. 지오메트리 메타데이터
    print("\n=== 지오메트리 메타데이터 ===")
    geometry_tags = [
        "FBX.Geometry.VertexCount",
        "FBX.Geometry.PolygonCount",
        "FBX.Geometry.EdgeCount",
        "FBX.Geometry.UVLayers",
        "FBX.Geometry.DeformerCount",
        "FBX.Geometry.MaterialCount",
        "FBX.Geometry.SkinCount",
        "FBX.Geometry.ShapeCount"
    ]
    
    for tag in geometry_tags:
        value = asset_subsystem.get_metadata_tag(imported_asset, unreal.Name(tag))
        if value:
            print(f"{tag}: {value}")
            
    # 3. 머티리얼 메타데이터
    print("\n=== 머티리얼 메타데이터 ===")
    material_tags = [
        "FBX.Material.Count",
        "FBX.Material.Names",
        "FBX.Material.DiffuseColor",
        "FBX.Material.SpecularColor",
        "FBX.Material.EmissiveColor",
        "FBX.Material.Opacity",
        "FBX.Material.Shininess"
    ]
    
    for tag in material_tags:
        value = asset_subsystem.get_metadata_tag(imported_asset, unreal.Name(tag))
        if value:
            print(f"{tag}: {value}")
            
    # 4. 애니메이션 메타데이터
    print("\n=== 애니메이션 메타데이터 ===")
    animation_tags = [
        "FBX.Animation.FrameRate",
        "FBX.Animation.Duration",
        "FBX.Animation.TakeCount",
        "FBX.Animation.TakeNames",
        "FBX.Animation.StartFrame",
        "FBX.Animation.EndFrame",
        "FBX.Animation.FrameCount"
    ]
    
    for tag in animation_tags:
        value = asset_subsystem.get_metadata_tag(imported_asset, unreal.Name(tag))
        if value:
            print(f"{tag}: {value}")
            
    # 5. 스켈레탈 메시 메타데이터
    print("\n=== 스켈레탈 메시 메타데이터 ===")
    skeletal_tags = [
        "FBX.SkeletalMesh.ImportType",
        "FBX.SkeletalMesh.BoneCount",
        "FBX.SkeletalMesh.BlendShapeCount",
        "FBX.SkeletalMesh.LODCount",
        "FBX.SkeletalMesh.bHasVertexColors",
        "FBX.SkeletalMesh.VertexColorImportOption"
    ]
    
    for tag in skeletal_tags:
        value = asset_subsystem.get_metadata_tag(imported_asset, unreal.Name(tag))
        if value:
            print(f"{tag}: {value}")
    
    # 6. 임포트 설정 메타데이터
    print("\n=== 임포트 설정 메타데이터 ===")
    import_tags = [
        "FBX.Import.FileVersion",
        "FBX.Import.MeshType",
        "FBX.mesh_type",
        "importer_rules_applied",
        "FBX.Import.AutoComputeLODScreenSize",
        "FBX.Import.VertexColorImportOption",
        "FBX.Import.bImportMeshLODs",
        "FBX.Import.bCombineMeshes",
        "FBX.Import.bGenerateLightmapUVs"
    ]
    
    for tag in import_tags:
        value = asset_subsystem.get_metadata_tag(imported_asset, unreal.Name(tag))
        if value:
            print(f"{tag}: {value}")
    
    # 7. 에셋 레지스트리 정보
    print("\n=== 에셋 레지스트리 정보 ===")
    asset_data = asset_registry.get_asset_by_object_path(imported_asset.get_path_name())
    if asset_data:
        print(f"Package Path: {asset_data.package_name}")
        print(f"Package File Path: {asset_data.package_file_path}")
        print(f"Package GUID: {asset_data.package_guid}")
        print(f"Asset Class: {asset_data.asset_class}")
        print(f"Asset Name: {asset_data.asset_name}")
        
def test_fbx_import_and_metadata(source_fbx: str, destination_path: str = "/Game/TestImport"):
    """
    FBX 파일을 임포트하고 모든 메타데이터를 출력
    """
    print(f"\n=== FBX 임포트 테스트 시작: {Path(source_fbx).name} ===\n")
    
    try:
        # 1. 임포트 설정
        static_mesh_import_data = unreal.FbxStaticMeshImportData()
        static_mesh_import_data.combine_meshes = True
        static_mesh_import_data.generate_lightmap_u_vs = True
        static_mesh_import_data.auto_generate_collision = True
        
        import_options = unreal.FbxImportUI()
        import_options.import_mesh = True
        import_options.import_textures = True
        import_options.import_materials = True
        import_options.import_animations = True
        import_options.static_mesh_import_data = static_mesh_import_data
        
        # 2. 임포트 태스크
        import_task = unreal.AssetImportTask()
        import_task.automated = True
        import_task.destination_path = destination_path
        import_task.filename = source_fbx
        import_task.replace_existing = True
        import_task.save = True
        import_task.options = import_options
        
        # 3. 임포트 실행
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([import_task])
        
        # 4. 임포트된 에셋 분석
        asset_path = f"{destination_path}/{Path(source_fbx).stem}"
        editor_asset_lib = unreal.EditorAssetLibrary()
        imported_asset = editor_asset_lib.load_asset(asset_path)
        
        if imported_asset:
            print("FBX 임포트 성공!")
            print_all_metadata(imported_asset)
            
    except Exception as e:
        print(f"에러 발생: {str(e)}")
        raise e
    
    print("\n=== 테스트 완료 ===")

# 테스트 실행
if __name__ == "__main__":
    maya_fbx = r"E:\UE5_lwj\mint_girl.fbx"  # FBX 파일 경로
    test_fbx_import_and_metadata(maya_fbx)