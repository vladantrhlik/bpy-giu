import bpy
import mathutils

class GIHideOperator(bpy.types.Operator):
    bl_idname = "object.gihide"
    bl_label = "GIHider"

    @classmethod
    def description(cls, context, properties):
        return "Hide all unused sockets of group inputs in current node tree"

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
            self.report({'ERROR'}, "Unable to find node tree.")
            return {'CANCELLED'}

        count = 0

        for n in nodes:
            if type(n) is bpy.types.NodeGroupInput:
                count += 1
                # hide all unlinked output sockets
                for o in n.outputs:
                    o.hide = not o.is_linked

        self.report({'INFO'}, f"{count} Group Inputs hidden.")

        return {"FINISHED"}

class GIMergeOperator(bpy.types.Operator):
    bl_idname = "object.gimerge"
    bl_label = "GIMerge"

    @classmethod
    def description(cls, context, properties):
        return "Merge 2 or more selected group inputs into one"

    @classmethod
    def get_selected_gis(cls, context):
        nodes = context.selected_nodes
        # filter only group inputs
        return list(filter(lambda x: type(x) is bpy.types.NodeGroupInput, nodes))  

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR' and len(GIMergeOperator.get_selected_gis(context)) > 1

    def execute(self, context):
        nodes = GIMergeOperator.get_selected_gis(context)

        if len(nodes) < 2:
            self.report({'ERROR'}, "Select 2 or more Group Inputs.")
            return {"CANCELLED"}
        
        # get all links in node tree
        links = []

        try: 
            tree = context.space_data.edit_tree
            links = tree.links
        except:
            self.report({'ERROR'}, "Unable to find node tree.")
            return {'CANCELLED'}

        # create links only from first node group
        count = 0
        for l in links:
            if l.from_node in nodes[1:]:
                id_from = l.from_socket.identifier
                links.new(nodes[0].outputs[id_from], l.to_socket)
                count += 1
        
        # calculate new position of first node group
        l = mathutils.Vector((0, 0))
        for n in nodes:
            l += n.location

        l /= len(nodes)
        nodes[0].location = l

        # remove other node groups
        for n in nodes[1:]:
            context.space_data.edit_tree.nodes.remove(n)

        self.report({'INFO'}, f"{len(nodes)} Group Inputs merged, {count} connections reconnected.")
        return {"FINISHED"}


def generate_group_input_sockets(scene, context):
    opts = []
    tree = context.space_data.edit_tree
    for a in tree.interface.items_tree:
        # skip panels
        if type(a) is bpy.types.NodeTreeInterfacePanel or a.in_out == "OUTPUT": continue
        name = a.name
        if len(a.parent.name) > 0:
            name = f"{a.parent.name} > {name}"

        value = a.identifier
        name = name
        opts.append((value, name, ""))
    return opts

class GIFindOperator(bpy.types.Operator):
    bl_idname = "object.gifind"
    bl_label = "GIFind"
    bl_property = "my_enum"

    my_enum: bpy.props.EnumProperty(name="Sockets", description="", items=generate_group_input_sockets)

    @classmethod
    def description(cls, context, properties):
        return "Unhide input socket in selected group input using search menu"

    @classmethod
    def get_selected_gi(cls, context):
        # get active node group input
        nodes = context.selected_nodes
        node = context.active_node

        if node not in nodes or not type(node) is bpy.types.NodeGroupInput:
            return None
        
        return node

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR' and GIFindOperator.get_selected_gi(context) != None

    def execute(self, context):
        node = GIFindOperator.get_selected_gi(context)

        if node == None:
            self.report({'ERROR'}, "No group input selected")
            return {"CANCELLED"}
        
        node.outputs[self.my_enum].hide = False

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {'FINISHED'}


class GIUsageOperator(bpy.types.Operator):
    bl_idname = "object.giusage"
    bl_label = "GIUsage"
    bl_property = "my_enum2"

    my_enum2: bpy.props.EnumProperty(name="Usages", description="", items=generate_group_input_sockets)

    @classmethod
    def description(cls, context, properties):
        return "Find usage of group input socket"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'

    def execute(self, context):
        links = []

        # try loading node tree
        try: 
            tree = context.space_data.edit_tree
            links = tree.links
        except:
            self.report({'ERROR'}, "Unable to find node tree.")
            return {'CANCELLED'}
        
        group_inputs = []
        link_count = 0

        for l in links:
            if type(l.from_node) is bpy.types.NodeGroupInput and l.from_socket.identifier == self.my_enum2:
                link_count += 1
                if not l.from_node in group_inputs:
                    group_inputs.append(l.from_node)
        
        #print(f"Socket used in {link_count} links going from {len(group_inputs)} group inputs.")
        self.report({'INFO'}, f"Socket used in {link_count} links going from {len(group_inputs)} group inputs.")

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {'FINISHED'}