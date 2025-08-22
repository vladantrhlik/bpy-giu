# Group Input Utils
Simple Blender addon with useful functions to speed up workflow with large Group Inputs in Blender Geometry Nodes.

## Why
When dealing with large and complicated node trees, it's very important to keep workspace nice and clean. With many parameters group inputs can get VERY large and make it harder to navigate and expand existing node tree. This addon adds few usefull functions which should speedup working with large group inputs and make out life easier.

## Usage
### Installation
1. Download .zip from actions panel (TODO)
2. In Blender goto Edit → Preferences → Add-ons → Install from Disk... (top right drop down arrow menu) → select .zip

### Functions
Currently the addon uses shortcut `alt+g` to bring up **pie menu** in Geometry Node tree workspace. In this menu you can select from all available functions:
 - **GIHide** - hide all unused sockets of group inputs in current node tree
<p align="center">
  <table border="0">
    <tr>
      <td align="center">
        <img alt="Light" src="img/hide_1.png" width="100%"><br>
      </td>
      <td align="center" valign="middle">→</td>
      <td align="center">
        <img alt="Dark" src="img/hide_2.png" width="100%"><br>
      </td>
    </tr>
  </table>
</p>

 - **GIMerge** - merge 2 or more selected group inputs to one
<p align="center">
  <table border="0">
    <tr>
      <td align="center">
        <img alt="Light" src="img/merge_1.png" width="100%"><br>
      </td>
      <td align="center" valign="middle">→</td>
      <td align="center">
        <img alt="Dark" src="img/merge_2.png" width="100%"><br>
      </td>
    </tr>
  </table>
</p>

 - **GIFind** - unhide one socket in selected group input via search bar
<p align="center">
  <table border="0">
    <tr>
      <td align="center">
        <img alt="Light" src="img/find_1.png" width="100%"><br>
      </td>
      <td align="center" valign="middle">→</td>
      <td align="center">
        <img alt="Dark" src="img/find_2.png" width="100%"><br>
      </td>
      <td align="center" valign="middle">→</td>
      <td align="center">
        <img alt="Dark" src="img/find_3.png" width="100%"><br>
      </td>
    </tr>
  </table>
</p>

 - **GISeparate** - split group input into two group inputs by selecting links to separate
<p align="center">
  <table border="0">
    <tr>
      <td align="center">
        <img alt="Light" src="img/separate_1.png" width="100%"><br>
      </td>
      <td align="center" valign="middle">→</td>
      <td align="center">
        <img alt="Dark" src="img/separate_2.png" width="100%"><br>
      </td>
      <td align="center" valign="middle">→</td>
      <td align="center">
        <img alt="Dark" src="img/separate_3.png" width="100%"><br>
      </td>
    </tr>
  </table>
</p>

 - **GIUsage** - find number of usages of given parameter in tree (showed in bottom panel)
