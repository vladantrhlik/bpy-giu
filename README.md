# 🌿 Group Input Utils
*A simple Blender add-on with utilities to speed up working with large Group Inputs in Geometry Nodes.*

## ✨ Why?
When dealing with large and complicated node trees, it's very important to keep workspace nice and clean. With many parameters group inputs can get VERY large and make it harder to navigate and expand existing node tree. 

This addon adds few useful functions which should speedup working with large group inputs and make our lifes easier.

## ⚡ Installation
1. **Download the .zip**
   - Either download this repository as a `.zip`  
   - **OR** go to the **Actions** tab → pick the latest run → download the artifact `GIU.zip` (contains only the needed files).
2. In Blender:  
   `Edit → Preferences → Add-ons → Install from Disk...` → select the `.zip`

## 🎮 Usage
Once installed, press **`Alt + G`** in the **Geometry Node Editor** to open the **pie menu**.  
From here, you can access all available functions:

### 🔹 GIHide
Hide all unused sockets of Group Inputs in the current node tree.  

<p align="center">
  <table>
    <tr>
      <td align="center"><img src="img/hide_1.png" width="100%"><br></td>
      <td align="center" valign="middle">➡️</td>
      <td align="center"><img src="img/hide_2.png" width="100%"><br></td>
    </tr>
  </table>
</p>

### 🔹 GIMerge
Merge two or more selected Group Inputs into a single node.  

<p align="center">
  <table>
    <tr>
      <td align="center"><img src="img/merge_1.png" width="100%"><br></td>
      <td align="center" valign="middle">➡️</td>
      <td align="center"><img src="img/merge_2.png" width="100%"><br></td>
    </tr>
  </table>
</p>

### 🔹 GIFind
Unhide a specific socket in the selected Group Input via search menu.

<p align="center">
  <table>
    <tr>
      <td align="center"><img src="img/find_1.png" width="100%"><br></td>
      <td align="center" valign="middle">➡️</td>
      <td align="center"><img src="img/find_2.png" width="100%"><br></td>
      <td align="center" valign="middle">➡️</td>
      <td align="center"><img src="img/find_3.png" width="100%"><br></td>
    </tr>
  </table>
</p>

### 🔹 GISeparate
Split a Group Input into two by selecting links to separate.  

<p align="center">
  <table>
    <tr>
      <td align="center"><img src="img/separate_1.png" width="100%"><br></td>
      <td align="center" valign="middle">➡️</td>
      <td align="center"><img src="img/separate_2.png" width="100%"><br></td>
      <td align="center" valign="middle">➡️</td>
      <td align="center"><img src="img/separate_3.png" width="100%"><br></td>
    </tr>
  </table>
</p>

### 🔹 GIUsage
Show how many times a given parameter is used in the node tree (displayed in the bottom panel (it's not very useful yet xd)).

