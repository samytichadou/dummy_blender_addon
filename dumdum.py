bl_info = {
    "name": "Dumdum",
    "author": "tonton",
    "version": (0, 1),
    "blender": (3, 00, 0),
    "location": "Top header",
    "description": "",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}


import bpy


# file menu drawer
def topbar_header(self, context):
    if context.region.alignment == 'RIGHT':
        layout = self.layout
        self.layout.label(text='Dumdum')


# Registration
def register():
    bpy.types.TOPBAR_HT_upper_bar.prepend(topbar_header)


def unregister():
    bpy.types.TOPBAR_HT_upper_bar.remove(topbar_header)


if __name__ == "__main__":
    register()
