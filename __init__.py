import bpy
from .operators import *
from .menu import *

ops = [GIHideOperator, GIMergeOperator, GIFindOperator, GIMenu, GIOpenMenu]

def register():
    for c in ops:
        bpy.utils.register_class(c)

def unregister():
    for c in ops:
        bpy.utils.unregister_class(c)