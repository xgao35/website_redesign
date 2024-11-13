# %% ######################################################################
# imports
import os
import json

# %% ######################################################################
# load page index .json file
home = os.getcwd() + "/content"
index = home + "/index.json"

with open(index, 'r') as f:
    file = json.load(f)

# %% ######################################################################
# function to generate navbar


def generate_navbar_html(files):
    """Function to generate the navbar from the structure specified
       in the index.json file"""

    html = '\t<div id="mySidebar" class="sidebar">' + \
           '\n\t\t<p style="color:#e5a734">' + \
           '\n\t\t\tHuman Neocortical Neurosolver' + \
           '\n\t\t</p>\n\t\t<br>'

    tab = '\t\t'

    def create_menu_item(file, label, tab):
        return f'\n{tab}<a href="{file}">{label}</a>'

    def create_menu_section(section_label):
        section = f'\n{tab}<div class="sidebar-list">' + \
                  f'\n{tab}\t<a id="sidebar-header" onclick="toggleSubmenu' + \
                  '(event)">' + \
                  f'\n{tab}{tab}{section_label}' + \
                  f'\n{tab}\t</a>' + \
                  f'\n{tab}\t<div class="submenu">'
        return section

    def build_navbar(files):
        items_html = ''
        for key, value in files.items():
            if isinstance(value, str):
                # Basic menu item
                items_html += create_menu_item(key, value, tab)
            elif isinstance(value, list):
                # Toggle section
                section_label = value[0]
                submenu = value[1]
                items_html += create_menu_section(section_label)
                # Now, add the child items directly under the parent item
                for child_file, child_label in submenu.items():
                    items_html += create_menu_item(child_file,
                                                   child_label,
                                                   tab+tab)
                items_html += f'\n{tab}\t</div>'
                items_html += f'\n{tab}</div>'
        return items_html

    html += build_navbar(files)
    html += '\n\t</div>'
    return html


# print(generate_navbar_html(file))
