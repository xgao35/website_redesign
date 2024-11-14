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

    def create_page_link(file, label, tab):
        return f'\n{tab}<a href="{file}">{label}</a>'

    def create_toggle_section(toggle_label):
        section = f'\n{tab}<div class="sidebar-list">' + \
                  f'\n{tab}\t<a id="sidebar-header" onclick="toggleSubmenu' + \
                  '(event)">' + \
                  f'\n{tab}{tab}{toggle_label}' + \
                  f'\n{tab}\t</a>' + \
                  f'\n{tab}\t<div class="submenu">'
        return section

    def build_navbar(files):
        navbar_html = ''
        for section, contents in files.items():
            # For pages that are not nested in a toggle
            if isinstance(contents, str):
                navbar_html += create_page_link(section, contents, tab)
            # For pages that are nested in a toggle
            elif isinstance(contents, list):
                toggle_label = contents[0]
                toggle_contents = contents[1]
                # Add toggle <div> sections and link
                navbar_html += create_toggle_section(toggle_label)
                # Add pages under toggle
                for sub_page, sub_name in toggle_contents.items():
                    navbar_html += create_page_link(sub_page,
                                                    sub_name,
                                                    tab+tab)
                # Close toggle <div> sections
                navbar_html += f'\n{tab}\t</div>'
                navbar_html += f'\n{tab}</div>'
        return navbar_html

    html += build_navbar(files)
    html += '\n\t</div>'
    return html


# print(generate_navbar_html(file))
