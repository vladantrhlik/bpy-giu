import bpy
import mathutils
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

class GIHiderOperator(bpy.types.Operator):
    bl_idname = "object.gihider"
    bl_label = "GIHider"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'

    def execute(self, context):
        nodes = []

        # try loading node tree
        try: 
            tree = context.space_data.edit_tree
            nodes = tree.nodes
        except:
            return {'CANCELLED'}

        count = 0

        for n in nodes:
            if type(n) is bpy.types.NodeGroupInput:
                count += 1
                # hide all unlinked output sockets
                for o in n.outputs:
                    o.hide = not o.is_linked

        return {"FINISHED"}

class GIMergeOperator(bpy.types.Operator):
    bl_idname = "object.gimerge"
    bl_label = "GIMerge"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'

    def execute(self, context):
        nodes = context.selected_nodes
        # filter only group inputs
        nodes = list(filter(lambda x: type(x) is bpy.types.NodeGroupInput, nodes))  

        if len(nodes) < 2:
            print("not enough group inputs selected.")
            return {"CANCELLED"}
        
        # get all links in node tree
        links = []

        try: 
            tree = context.space_data.edit_tree
            links = tree.links
        except:
            return {'CANCELLED'}

        # create links only from first node group
        for l in links:
            if l.from_node in nodes[1:]:
                id_from = l.from_socket.identifier
                links.new(nodes[0].outputs[id_from], l.to_socket)
        
        # calculate new position of first node group
        l = mathutils.Vector((0, 0))
        for n in nodes:
            l += n.location

        l /= len(nodes)
        nodes[0].location = l

        # remove other node groups
        for n in nodes[1:]:
            context.space_data.edit_tree.nodes.remove(n)
        return {"FINISHED"}

class GISocketItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Test Property", default="Unknown")
    value: bpy.props.StringProperty(name="Socket Name", default="Unknown Socket")

class GIFindOperator(bpy.types.Operator):
    bl_idname = "object.gifind"
    bl_label = "GIFind"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'

    def execute(self, context):
        nodes = context.selected_nodes
        node = context.active_node

        if node not in nodes:
            print("no node selected")
            return {"CANCELLED"}
        

        bpy.ops.wm.call_menu(name='GIFindMenu')
        return {"FINISHED"}

class GIFindMenu(bpy.types.Menu):
    bl_label = "GIFind"

    def draw(self, context):
        layout = self.layout
        layout.template_search(context.scene,"gi_opt",context.scene,"gi_search_opt")

def register():
    bpy.utils.register_class(GIHiderOperator)
    bpy.utils.register_class(GIMergeOperator)

    bpy.utils.register_class(GISocketItem)

    bpy.utils.register_class(GIFindMenu)
    bpy.utils.register_class(GIFindOperator)

    bpy.types.Scene.gi_search_opt = bpy.props.CollectionProperty(type=GISocketItem)
    bpy.types.Scene.gi_opt = bpy.props.PointerProperty(type=GISocketItem)


def unregister():
    bpy.utils.unregister_class(GIHiderOperator)
    bpy.utils.unregister_class(GIMergeOperator)

    bpy.utils.unregister_class(GISocketItem)

    bpy.utils.unregister_class(GIFindMenu)
    bpy.utils.unregister_class(GIFindOperator)

    del bpy.types.Scene.gi_search_opt
    del bpy.types.Scene.gi_opt
