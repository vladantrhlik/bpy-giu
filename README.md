# GIU
Blender addon with useful operators to speed up workflow with large Group Inputs in Blender Geometry Nodes.

## Supported Operators
- GIHide - hide all unused socket of Group Inputs in current node tree
- GIMerge - merge 2 or more selected Group Inputs to one
- GIFind - unhide one socket in group input via search bar
- GIUsage - find usage of given parameter in tree
- GISeparate - split group input into two group inputs by selecting links to separate (currently doesn't work for links with reroutes :/)

## Usage
- Inside Geometry Nodes workspace use `alt+g` to bring up pie menu with all supported operators