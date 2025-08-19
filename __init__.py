import bpy
from .operators import *
from .menu import *

ops = [GIHideOperator, GIMergeOperator, GIFindOperator, GIUsageOperator, GIMenu, GIOpenMenu, SocketOption, GISeparate]
addon_keymaps = []


def register():
    for c in ops:
        bpy.utils.register_class(c)
    
    # assign Ctrl+G shortcut
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
        kmi = km.keymap_items.new(GIOpenMenu.bl_idname, type='G', value='PRESS', alt=True)
        addon_keymaps.append((km, kmi))


def unregister():
    for c in ops:
        bpy.utils.unregister_class(c)
    
    addon_keymaps.clear()