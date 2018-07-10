#!/usr/bin/env python
# SPDX-License-Identifier: MIT

import configparser

with open("base.css", "r") as f:
    base_css = f.read()

config = configparser.ConfigParser()
config.read("Themes.ini")

for theme in config.sections():
    css = base_css

    for key in config[theme]:
        if key.startswith("color"):
            css = css.replace(f"__{key}__", f"rgb({config[theme][key]})")
        else:
            css = css.replace(f"__{key}__", f"{config[theme][key]}")

    with open(f"Generated_Themes/{theme}.user.css", "w") as out:
        out.write(css)
