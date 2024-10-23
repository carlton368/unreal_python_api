import unreal

# Recommendation:
# Go to Editor Preferences -> Miscellaneous -> Display UI Extension Points

# Check out list_tool_menus.py and available_menu_names.txt to find out list of extandable menus


@unreal.uclass()
class MyScriptObject(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        print("SCRIPT EXECUTED")


def main():
    menus = unreal.ToolMenus.get()

    # CUSTOM SUBMENU
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    if not main_menu:
        print("Failed to find the Main menu. Script terminated prematurely.")
        return
    custom_menu = main_menu.add_sub_menu("Custom Menu", "Python Automation", "Menu Name", "Menu Label")

    edit_menu = menus.find_menu("LevelEditor.MainMenu.Edit")
    if not edit_menu:
        print("Failed to find the Edit menu. Script terminated prematurely.")
        return

    # CUSTOM SCRIPT MENU ENTRY
    script_object = MyScriptObject()
    script_object.init_entry(
        owner_name=edit_menu.menu_name,
        menu=edit_menu.menu_name,
        section="EditMain",
        name="Unreal Engine 5 Python Automation Course",
        label="Unreal Engine 5 Python Automation Course",
        tool_tip="Custom Script Entry"
    )
    script_object.register_menu_entry()

    # CUSTOM SCRIPT CONTEXT MENU ENTRY
    asset_context_menu = menus.find_menu("ContentBrowser.AssetContextMenu.StaticMesh")
    script_object2 = MyScriptObject()
    script_object2.init_entry(
        owner_name=asset_context_menu.menu_name,
        menu=asset_context_menu.menu_name,
        section="GetAssetActions",
        name="Unreal Engine 5 Python Automation Course",
        label="Unreal Engine 5 Python Automation Course",
        tool_tip="Custom Script Entry"
    )
    script_object2.register_menu_entry()

    # REFRESH UI
    menus.refresh_all_widgets()


if __name__ == '__main__':
    main()
