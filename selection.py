import unreal

# ALL ASSETS IN DIRECTORY # EditorAssetLibrary는 에셋 관리를 위한 주요 class
EditorAssetLibrary = unreal.EditorAssetLibrary()

assets = EditorAssetLibrary.list_assets("/Game/StarterContent/Architecture/") # list_assets()로 지정된 경로의 모든 에셋 목록을 가져옵니다
example_asset_path = assets[0] #assets[0]으로 첫 번째 에셋의 경로를 가져옵니다

example_asset = EditorAssetLibrary.load_asset(example_asset_path) #load_asset()으로 실제 에셋을 메모리에 로드합니다

# 잘못된 방법 (warning 발생) EditorAssetLibrary.load_asset("/Game/StarterContent/Architecture/Floor_400x400.Floor_400x400") # warning
EditorAssetLibrary.load_asset("/Game/StarterContent/Architecture/Floor_400x400") # 올바른 에셋로드 방법
example_asset.get_full_name()  # class info and path #get_full_name(): 클래스 타입을 포함한 전체 경로 가져오기 (예: StaticMesh'/Game/StarterContent/Architecture/Floor_400x400.Floor_400x400')
example_asset.get_path_name()  # path #get_path_name(): 에셋의 전체 경로 가져오기 (예: /Game/StarterContent/Architecture/Floor_400x400.Floor_400x400)
example_asset.get_fname()  # file name #get_fname(): 오직 파일 이름만 반환 (예: Floor_400x400.Floor_400x400)

EditorAssetLibrary.find_asset_data(example_asset_path) # 에셋의 상세 메타데이터 반환
example_asset.get_class() # could be compared with another class # 에셋의 클래스 타입 반환
isinstance(example_asset, unreal.StaticMesh) # StaticMesh 타입인지 확인 (True/False 반환) !!!!!!!!!!!!!중요!!!!!!!!!!!!!!!!!!!타입 체크를 통해 특정 에셋 타입인지 확인할 수 있습니다

# SELECTED ASSETS
EditorUtilityLibrary = unreal.EditorUtilityLibrary()
selected_assets = EditorUtilityLibrary.get_selected_assets() #EditorUtilityLibrary를 통해 현재 에디터에서 선택된 에셋들에 접근합니다
EditorUtilityLibrary.get_selected_asset_data() #선택된 에셋들의 목록과 메타데이터를 가져올 수 있습니다

# ALL ACTORS
# EditorActorSubsystem = unreal.EditorActorSubsystem()  # Unreal older than 5.3 # Unreal 5.3 이전 버전
EditorActorSubsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)  # Unreal 5.3 and newer # Unreal 5.3+ 버전
# EditorActorSubsystem.get_all_level_actors()  # TypeError: needs an argument (and () to fix)
actors = EditorActorSubsystem.get_all_level_actors() # returns actual objects, not paths #get_all_level_actors()로 현재 레벨의 모든 액터를 가져옴(경로가 아닌 object 반환)
# 특정 타입의 액터 찾기
for actor in actors:
    if isinstance(actor, unreal.SkyAtmosphere): # isinstance()로 특정 타입의 액터를 필터링 가능
        print(actor)

# Selected actors 
selected_actors = EditorActorSubsystem.get_selected_level_actors()# 선택된 액터들 가져오기


"""
주요 활용 팁:

에셋 경로는 항상 /Game/으로 시작해야 합니다
에셋 로드 시 중복된 이름을 피해야 합니다
타입 체크를 통해 안전하게 에셋과 액터를 처리할 수 있습니다
에디터의 선택 상태를 스크립트로 쉽게 활용할 수 있습니다
"""