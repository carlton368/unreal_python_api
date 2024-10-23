import unreal
from unreal import DataValidationResult

TRIS_COUNT_MAX = 2500


@unreal.uclass()
class TriangleCountValidator(unreal.EditorValidatorBase):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    @unreal.ufunction(override=True)
    def can_validate_asset(self, asset):
        return isinstance(asset, (unreal.StaticMesh, unreal.SkeletalMesh))

    @unreal.ufunction(override=True)
    def validate_loaded_asset(self, asset: unreal.Object) -> DataValidationResult:
        correct_path = "".join(asset.get_path_name().split(".")[:-1])
        tag_values = unreal.EditorAssetLibrary.get_tag_values(correct_path)
        if 'Triangles' not in tag_values:
            self.asset_warning(asset, unreal.Text("Could not validate asset triangle count. "
                                                  "'Triangles' tag is not available"))
            return unreal.DataValidationResult.NOT_VALIDATED

        triangle_count = int(tag_values[unreal.Name('Triangles')])
        if triangle_count > TRIS_COUNT_MAX:
            self.asset_fails(asset, unreal.Text(f'Asset has too many triangles: {triangle_count}. '
                                                f'Limit is {TRIS_COUNT_MAX}'))
            return unreal.DataValidationResult.INVALID

        return unreal.DataValidationResult.VALID


def register_triangle_count_validator():
    editor_validator_subsystem = unreal.get_editor_subsystem(unreal.EditorValidatorSubsystem)
    triangle_count_validator = TriangleCountValidator()
    editor_validator_subsystem.add_validator(triangle_count_validator)

