bl_info = {
    "name": "Dumdum",
    "author": "tonton",
    "version": (0, 2),
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
        layout.label(text='Dumdum1')
        layout.separator()
        layout.label(text='Dumdum2')
        layout.separator()
        layout.operator('world.new', text="Create World", icon="WORLD")

# file menu drawer
def topbar_header(self, context):
    if context.region.alignment == 'RIGHT':
        self.layout.menu('DUMDUM_MT_menu')

# Registration
def register():
    bpy.utils.register_class(DUMDUM_MT_menu)
    bpy.types.TOPBAR_HT_upper_bar.prepend(topbar_header)

def unregister():
    bpy.utils.unregister_class(DUMDUM_MT_menu)
    bpy.types.TOPBAR_HT_upper_bar.remove(topbar_header)

if __name__ == "__main__":
    register()
