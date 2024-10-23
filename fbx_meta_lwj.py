import unreal
from pathlib import Path

def test_fbx_import_and_metadata(
    source_fbx: str,
    destination_path: str = "/Game/TestImport"
):
    """
    Maya FBX 파일 임포트 및 메타데이터 테스트
    
    Args:
        source_fbx: Maya에서 내보낸 FBX 파일 경로
        destination_path: 언리얼 엔진 내 저장 경로
    """
    print(f"\n=== Maya FBX 임포트 테스트 시작: {Path(source_fbx).name} ===\n")
    
    try:
        # 1. 임포트 설정
        static_mesh_import_data = unreal.FbxStaticMeshImportData()
        static_mesh_import_data.combine_meshes = True
        static_mesh_import_data.remove_degenerates = True
        static_mesh_import_data.generate_lightmap_u_vs = True
        static_mesh_import_data.auto_generate_collision = True
        
        # FBX 임포트 옵션
        import_options = unreal.FbxImportUI()
        import_options.import_mesh = True
        import_options.import_textures = True  # Maya 텍스처도 함께 임포트
        import_options.import_materials = True
        import_options.import_animations = True  # 애니메이션 있는 경우
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
        asset_subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
        imported_asset = asset_subsystem.load_asset(asset_path)
        
        if imported_asset:
            print("FBX 임포트 성공!\n")
            
            # 5. 메타데이터 카테고리별 출력
            metadata_categories = {
                "FBX 정보": [
                    "FBX.Creator", "FBX.Version", "FBX.CreationTime",
                    "FBX.LastSaved", "FBX.Creator.Version"
                ],
                "지오메트리": [
                    "FBX.Geometry.VertexCount", "FBX.Geometry.PolygonCount",
                    "FBX.Geometry.UVLayers"
                ],
                "머티리얼/텍스처": [
                    "FBX.Material.Count", "FBX.Material.Names",
                    "FBX.Texture.Count", "FBX.Texture.Names"
                ],
                "애니메이션": [
                    "FBX.Animation.FrameRate", "FBX.Animation.Duration",
                    "FBX.Animation.TakeCount"
                ],
                "Maya 특정 정보": [
                    "FBX.Maya.", "FBX.Original"
                ]
            }
            
            for category, tags in metadata_categories.items():
                print(f"\n{category}:")
                found_data = False
                
                for tag_prefix in tags:
                    all_tags = asset_subsystem.get_metadata_tag_names(imported_asset)
                    matching_tags = [
                        tag for tag in all_tags 
                        if str(tag).startswith(tag_prefix)
                    ]
                    
                    for tag in matching_tags:
                        value = asset_subsystem.get_metadata_tag(imported_asset, tag)
                        print(f"  {tag}: {value}")
                        found_data = True
                
                if not found_data:
                    print("  데이터 없음")
            
            # 6. 추가 에셋 정보
            print("\n추가 정보:")
            print(f"  에셋 경로: {asset_path}")
            print(f"  에셋 타입: {imported_asset.get_class().get_name()}")
            
    except Exception as e:
        print(f"에러 발생: {str(e)}")
        raise e
    
    print("\n=== 테스트 완료 ===")

# 테스트 실행
def run_maya_fbx_test():
    # Maya에서 내보낸 FBX 파일 경로
    maya_fbx = r"C:\MayaExports\test_asset.fbx"  # 실제 경로로 변경하세요
    
    # 테스트 실행
    test_fbx_import_and_metadata(maya_fbx)