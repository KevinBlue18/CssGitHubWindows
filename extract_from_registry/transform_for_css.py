#!/usr/bin/env python

# Transform extracted color information into a suitable Themes.ini for
# the CSS.

import configparser

origcolors = configparser.ConfigParser()
origcolors.read("colors.ini")

# file to be written out
themes = configparser.ConfigParser()

# Not handled by the extracter... hardcoding values here
fonts = {
    "font_family": "Tahoma, Arial, Liberation Sans, sans-serif",
    "font_size": "12px",
    "font_line": "1.2",
    "font_size_text": "14px",
    "font_line_text": "1.2",
    "font_size_bigger": "13px",
    "font_size_header": "14px",
}

# Mapping to items currently handled

# Q: Where do color_button_checked and color_hover come from?

items = {
    "ButtonText": "color_button_text",
    "ButtonFace": "color_button_face",
    "ButtonHilight": "color_button_highlight",
    "ButtonShadow": "color_button_shadow",
    "ButtonDkShadow": "color_button_shadow_dark",
    "WindowText": "color_window_text",
    "Window": "color_window",
    "TitleText": "color_active_caption_text",
    "ActiveTitle": "color_active_caption",
    "GradientActiveTitle": "color_active_caption_gradient",
    "InfoWindow": "color_info_background",
    "HilightText": "color_highlight_text",
    "Hilight": "color_highlight",
    "GrayText": "color_gray_text",
    "HotTrackingColor": "color_link",
}

for section in origcolors.sections():
    themes[section] = {
        "color_button_checked": "223, 223, 223",
        "color_hover": "223, 223, 255",
    }
    themes[section].update(fonts)

    for oldkey, newkey in items.items():
        themes[section][newkey] = origcolors[section][oldkey]

with open("Themes.ini", "w") as cfgfile:
    themes.write(cfgfile)
