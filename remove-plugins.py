#!/usr/bin/env python3

import os
import re
import shutil

from unitypackage_extractor.extractor import extractPackage as extract


def remove_relative_files(src, dst):
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(".meta"):
                continue
            file_des_path = os.path.join(root, file)
            # remove src prefix
            file_des_path = dst + file_des_path[len(src) :]
            print("check removing file: ", file_des_path)
            if os.path.exists(file_des_path):
                os.remove(file_des_path)
                print("removed")
            else:
                print("file not exist")

            file_des_path_meta = file_des_path + ".meta"
            print("check removing file: ", file_des_path_meta)
            if os.path.exists(file_des_path_meta):
                os.remove(file_des_path_meta)
                print("removed")
            else:
                print("file not exist")


def remove_empty_folders(folder_path):
    if not os.path.isdir(folder_path):
        return

    # remove empty subfolders
    files = os.listdir(folder_path)
    if len(files):
        for f in files:
            fullpath = os.path.join(folder_path, f)
            if os.path.isdir(fullpath):
                remove_empty_folders(fullpath)

    # if folder empty, delete it
    files = os.listdir(folder_path)
    if len(files) == 0:
        print("Removing empty folder:", folder_path)
        os.rmdir(folder_path)
        if os.path.exists(folder_path + ".meta"):
            os.remove(folder_path + ".meta")


def main():
    print("will remove plugins from unity")

    file_dir = os.path.dirname(os.path.realpath(__file__))
    plugin_dir = os.path.join(file_dir, "plugins")
    unity_dir = os.path.join(file_dir, "unity")

    for plugin_name in os.listdir(plugin_dir):
        if not plugin_name.endswith(".unitypackage"):
            continue

        print("removing plugin: ", plugin_name)
        plugin_path = os.path.join(plugin_dir, plugin_name)
        plugin_tmp_folder = os.path.splitext(plugin_path)[0]
        if os.path.exists(plugin_tmp_folder):
            shutil.rmtree(plugin_tmp_folder)
        extract(plugin_path, plugin_tmp_folder)

        remove_relative_files(plugin_tmp_folder, unity_dir)

    remove_empty_folders(unity_dir)


if __name__ == "__main__":
    main()
