#!/usr/bin/env python3

import os
import re
import shutil


def main():
    print("will download plugins in list")

    file_dir = os.path.dirname(os.path.realpath(__file__))
    plugin_list_path = os.path.join(file_dir, "plugin-list.txt")
    if not os.path.exists(plugin_list_path):
        print("no plugin-list.txt")
        return

    plugins_path = os.path.join(file_dir, "plugins")
    if not os.path.exists(plugins_path):
        os.mkdir(plugins_path)

    with open(plugin_list_path, "r") as f:
        plugin_list = f.readlines()

    url_list = []
    for plugin_url in plugin_list:
        plugin_url = plugin_url.strip()
        if not plugin_url:
            continue

        if plugin_url.startswith("#"):
            continue

        if not plugin_url.startswith("http"):
            continue

        url_list.append(plugin_url)

    if not url_list or len(url_list) == 0:
        print("no plugin to download")
        return

    os.chdir(plugins_path)
    for plugin_url in url_list:
        file_name = plugin_url.split("/")[-1]

        file_path = os.path.join(plugins_path, file_name)
        if os.path.exists(file_path):
            print("plugin already downloaded: ", file_name)
            continue

        print("downloading plugin: ", file_name)
        os.system('curl -O -v "%s"' % plugin_url)


if __name__ == "__main__":
    main()
