import unreal


@unreal.uclass()
class MyCustomScriptObject(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        print("SCRIPT EXECUTED")

@unreal.uclass()
class AnotherCustomScriptObject(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        print("ANOTHER SCRIPT EXECUTED")


def main():
    menus = unreal.ToolMenus.get()
    asset_context_menu = menus.find_menu(unreal.Name("ContentBrowser.AssetContextMenu.StaticMesh"))

    custom_menu = asset_context_menu.add_sub_menu("Custom.Menu","Custom Menu","Label",
                                                  "We added this menu our selves!")

    ### SEPARATOR
    separator_entry = unreal.ToolMenuEntry(name=unreal.Name("Separator Entry"), type=unreal.MultiBlockType.SEPARATOR)
    custom_menu.add_menu_entry("", separator_entry)

    ### SCRIPT MENU ENTRY
    script_object = MyCustomScriptObject()
    script_object.init_entry(
        owner_name=custom_menu.menu_name,
        menu=custom_menu.menu_name,
        section="",
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

    ### SCRIPT MENU ENTRY THAT DOES NOT DISPLAY LABEL
    another_menu_entry = unreal.ToolMenuEntry(
        name=unreal.Name("Another Menu entry"),
        type=unreal.MultiBlockType.MENU_ENTRY,
        script_object=AnotherCustomScriptObject(),
    )
    another_menu_entry.set_label("Test Label")

    custom_menu.add_menu_entry("", another_menu_entry)

    # REFRESH UI
    menus.refresh_all_widgets()


if __name__ == "__main__":
    main()
