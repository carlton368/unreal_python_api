import unreal

EditorAssetLibrary = unreal.EditorAssetLibrary()

asset_path_list = EditorAssetLibrary.list_assets("/Game/StarterContent/Textures/")
asset = EditorAssetLibrary.load_asset(asset_path_list[0])

with unreal.ScopedEditorTransaction("Outer"):
	# Outer will be added to transaction history
	asset.set_editor_property(name="compression_settings", value=unreal.TextureCompressionSettings.TC_GRAYSCALE)
	with unreal.ScopedEditorTransaction("Inner"):
		# Inner will not be added to transaction history. Those changes will be in "Outer" transaction
		asset.set_editor_property(name="compression_quality", value=unreal.TextureCompressionQuality.TCQ_LOW)

# Please remember that if the script does not modify any asset, no transaction will be saved.
# You can run it twice and notice that only a single transaction was saved.