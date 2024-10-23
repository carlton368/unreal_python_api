import unreal

EditorAssetLibrary = unreal.EditorAssetLibrary()

asset_path_list = EditorAssetLibrary.list_assets("/Game/StarterContent/Textures/") # 특정 경로의 모든 에셋 경로 가져오기
asset = EditorAssetLibrary.load_asset(asset_path_list[0]) # 첫 번째 텍스처 에셋 로드

with unreal.ScopedEditorTransaction("Outer"):
	# 외부 트랜잭션 시작
	# Outer will be added to transaction history
	asset.set_editor_property(name="compression_settings", value=unreal.TextureCompressionSettings.TC_GRAYSCALE) # 압축 설정을 그레이스케일로 변경
	# 내부 트랜잭션 시작
	with unreal.ScopedEditorTransaction("Inner"):
		# 압축 품질을 낮음으로 설정
		# Inner will not be added to transaction history. Those changes will be in "Outer" transaction
		asset.set_editor_property(name="compression_quality", value=unreal.TextureCompressionQuality.TCQ_LOW)

# Please remember that if the script does not modify any asset, no transaction will be saved.
# You can run it twice and notice that only a single transaction was saved.
"""
트랜잭션은 에디터에서 실행취소(Undo)/다시실행(Redo)를 위한 작업 단위입니다.
- 변경사항을 그룹화
- 실행취소/다시실행 가능
- 변경 이력 관리
"""