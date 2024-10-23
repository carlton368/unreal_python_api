import unreal


@unreal.uclass()
class MyScriptObject(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        print("SCRIPT EXECUTED")


def main():
    menus = unreal.ToolMenus.get()

    # CUSTOM SCRIPT CONTEXT MENU ENTRY
    asset_context_menu = menus.find_menu("ContentBrowser.AssetContextMenu.StaticMesh")

    script_object = MyScriptObject()
    script_object.init_entry(
        owner_name=asset_context_menu.menu_name,
        menu=asset_context_menu.menu_name,
        section="GetAssetActions",
        name="Unreal Engine 5 Python Automation Course",
        label="Unreal Engine 5 Python Automation Course",
        tool_tip="Custom Script Entry"
    )
    script_object.register_menu_entry()


    tool_menu_entry_script_data = script_object.data
    script_icon = unreal.ScriptSlateIcon(style_set_name="UMGStyle",
                                         style_name="Palette.Icon",
                                         small_style_name="Palette.Icon.Small")
    tool_menu_entry_script_data.icon = script_icon


    # REFRESH UI
    menus.refresh_all_widgets()


if __name__ == "__main__":
    main()
