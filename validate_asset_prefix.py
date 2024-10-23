import unreal
from unreal import Object, DataValidationResult


@unreal.uclass()
class AssetPrefixValidator(unreal.EditorValidatorBase):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

    @unreal.ufunction(override=True)
    def can_validate_asset(self, asset):
        # possible use of issubclass() instead of isinstance()
        return isinstance(asset, (unreal.Texture, unreal.Blueprint, unreal.Material, unreal.MaterialInstance))

    @unreal.ufunction(override=True)
    def validate_loaded_asset(self, asset: Object) -> DataValidationResult:
        # Texture T_
        # Material M_
        # MaterialInstance MI_
        # Blueprint BP_
        name = str(asset.get_fname())
        message = "Name should start with "
        match asset.__class__:
            case unreal.Texture:
                if name.startswith("T_"):
                    return unreal.DataValidationResult.VALID
                message += "T_"
            case unreal.Blueprint:
                if name.startswith("BP_"):
                    return unreal.DataValidationResult.VALID
                message += "BP_"
            case unreal.Material:
                if name.startswith("M_"):
                    return unreal.DataValidationResult.VALID
                message += "M_"
            case unreal.MaterialInstance:
                if name.startswith("MI_"):
                    return unreal.DataValidationResult.VALID
                message += "MI_"

        self.asset_warning(asset, unreal.Text(message))
        return unreal.DataValidationResult.INVALID


def register_asset_prefix_validator():
    editor_validator_subsystem = unreal.get_editor_subsystem(unreal.EditorValidatorSubsystem)
    validator = AssetPrefixValidator()
    editor_validator_subsystem.add_validator(validator)
