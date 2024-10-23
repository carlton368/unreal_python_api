import unreal
from unreal import DataValidationResult


@unreal.uclass()
class SquareTextureValidator(unreal.EditorValidatorBase):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    @unreal.ufunction(override=True)
    def can_validate_asset(self, asset):
        return isinstance(asset, unreal.Texture2D)

    @unreal.ufunction(override=True)
    def validate_loaded_asset(self, asset: unreal.Texture2D) -> DataValidationResult:
        if not asset.blueprint_get_size_x() == asset.blueprint_get_size_y():
            self.asset_fails(asset, unreal.Text("Texture is not square"))
            return unreal.DataValidationResult.INVALID

        return unreal.DataValidationResult.VALID


@unreal.uclass()
class PowerOfTwoTextureValidator(unreal.EditorValidatorBase):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    @unreal.ufunction(override=True)
    def can_validate_asset(self, asset):
        return isinstance(asset, unreal.Texture2D)

    @unreal.ufunction(override=True)
    def validate_loaded_asset(self, asset: unreal.Texture2D) -> DataValidationResult:
        valid_sizes = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192)
        if asset.blueprint_get_size_x() not in valid_sizes or asset.blueprint_get_size_y() not in valid_sizes:
            self.asset_fails(asset, unreal.Text(f"Texture dimensions (X, Y) are not one of {valid_sizes}"))
            return unreal.DataValidationResult.INVALID

        return unreal.DataValidationResult.VALID


def register_texture_validators():
    editor_validator_subsystem = unreal.get_editor_subsystem(unreal.EditorValidatorSubsystem)
    square_validator = SquareTextureValidator()
    power_of_two_validator = PowerOfTwoTextureValidator()
    editor_validator_subsystem.add_validator(square_validator)
    editor_validator_subsystem.add_validator(power_of_two_validator)

