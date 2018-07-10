import configparser
from winreg import *

color_mapping = {
    "Color #0": "Scrollbar",
    "Color #1": "Background",
    "Color #2": "ActiveTitle",
    "Color #3": "InactiveTitle",
    "Color #4": "Menu",
    "Color #5": "Window",
    "Color #6": "WindowFrame",
    "Color #7": "MenuText",
    "Color #8": "WindowText",
    "Color #9": "TitleText",
    "Color #10": "ActiveBorder",
    "Color #11": "InactiveBorder",
    "Color #12": "AppWorkSpace",
    "Color #13": "Hilight",
    "Color #14": "HilightText",
    "Color #15": "ButtonFace",
    "Color #16": "ButtonShadow",
    "Color #17": "GrayText",
    "Color #18": "ButtonText",
    "Color #19": "InactiveTitleText",
    "Color #20": "ButtonHilight",
    "Color #21": "ButtonDkShadow",
    "Color #22": "ButtonLight",
    "Color #23": "InfoText",
    "Color #24": "InfoWindow",
    "Color #25": "ButtonAlternateFace",
    "Color #26": "HotTrackingColor",
    "Color #27": "GradientActiveTitle",
    "Color #28": "GradientInactiveTitle",
    "Color #29": "MenuHilight",
    "Color #30": "MenuBar",
}
font_mapping = {
    "Font #0": "CaptionFont",
    "Font #1": "SmCaptionFont",
    "Font #2": "MenuFont",
    "Font #3": "StatusFont",
    "Font #4": "MessageFont",
    "Font #5": "IconFont",
}

cfg = configparser.RawConfigParser()
cfg.optionxform = lambda option: option

cu_hive = ConnectRegistry(None, HKEY_CURRENT_USER)
schemes = OpenKey(cu_hive, r"Control Panel\Appearance\New Schemes")

for key in range(QueryInfoKey(schemes)[0]):
    cur_theme = OpenKey(schemes, str(key))
    theme_name = QueryValueEx(cur_theme, "LegacyName")[0]

    cfg[theme_name] = {}

    style = OpenKey(cur_theme, r"Sizes\0")

    # Load the colors
    for col in range(31):
        color = QueryValueEx(style, "Color #{}".format(col))[0]
        red = color & 0xff
        green = (color & 0xff00) >> 8
        blue = (color & 0xff0000) >> 16

        cfg[theme_name][
            color_mapping["Color #{}".format(col)]
        ] = "{}, {}, {}".format(red, green, blue)

    # Load the fonts
    # SKIPPED. Must figure out how to properly extract the data.

    # for fon in range(6):
    #     font = QueryValueEx(style, "Font #{}".format(fon))

with open("colors.ini", "w") as cfgfile:
    cfg.write(cfgfile)
