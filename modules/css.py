HIDE_IMG_FS = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

HIDE_STREAMLIT_STYLE = """
<style>
#MainMenu {visibility: hidden;}
.stDeployButton {display:none;}
footer {visibility: hidden;}
</style>

"""

CUSTOM_COLUMN_4 = '''<style>

[data-testid="column"] {
    width: calc({25% - 1rem) !important;
    flex: 1 1 calc(25% - 1rem) !important;
    min-width: calc(25% - 1rem) !important;
}
</style>'''

CUSTOM_COLUMN_5 = '''<style>

[data-testid="column"] {
    width: calc(20% - 1rem) !important;
    flex: 1 1 calc(20% - 1rem) !important;
    min-width: calc(20% - 1rem) !important;
}
</style>'''