bl_info = {
    "name": "Dumdum",
    "author": "tonton",
    "version": (0, 3),
    "blender": (3, 00, 0),
    "location": "Top header",
    "description": "",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}

import bpy

# file menu
class DUMDUM_MT_menu(bpy.types.Menu):
    bl_label = "Dumdum"
    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, 'dumdum_prop', text = "Prop", icon='TIME')
        layout.separator()
        layout.operator('world.new', text="Create World", icon="WORLD")
        layout.operator('world.new', text="Create World", icon="WORLD")
        layout.separator()
        layout.operator('world.new', text="Create World", icon="WORLD")

# file menu drawer
def topbar_header(self, context):
    if context.region.alignment == 'RIGHT':
        self.layout.separator()
        if context.scene.dumdum_prop:
            self.layout.menu('DUMDUM_MT_menu', text=" Dumdum", icon='TIME')
        else:
            self.layout.menu('DUMDUM_MT_menu')

# Registration
def register():
    bpy.types.Scene.dumdum_prop = \
        bpy.props.BoolProperty(name='Property')

    bpy.utils.register_class(DUMDUM_MT_menu)
    bpy.types.TOPBAR_HT_upper_bar.prepend(topbar_header)

def unregister():
    del bpy.types.Scene.dumdum_prop
    bpy.utils.unregister_class(DUMDUM_MT_menu)
    bpy.types.TOPBAR_HT_upper_bar.remove(topbar_header)

if __name__ == "__main__":
    register()
