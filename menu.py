import bpy

class GIOpenMenu(bpy.types.Operator):
    bl_idname = "object.giopenmenu"
    bl_label = "GIOpenMenu"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="GIMenu")
        return {"FINISHED"}

class GIMenu(bpy.types.Menu):
    bl_label = "GIU Menu"

    def draw(self, context):
        pie = self.layout.menu_pie()

        pie.operator("object.gifind", text="Find", icon="ZOOM_ALL")
        pie.operator("object.gimerge", text="Merge", icon="LINKED")
        pie.operator("object.gihide", text="Hide", icon="HIDE_ON")
        pie.operator("object.giusage", text="Usage", icon="HIDE_ON")