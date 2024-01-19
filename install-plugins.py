#!/usr/bin/env python3

import os
import sys

from unitypackage_extractor.extractor import extractPackage as extract


def deal_with_unity_path(unity_path, save_folder_path):
    if os.path.exists(unity_path):
        return unity_path

    platform = sys.platform

    save_path = os.path.join(save_folder_path, "unity_path.save")
    unity_path = ""

    if os.path.exists(save_path):
        with open(save_path, "r", encoding="UTF-8") as f:
            unity_path = f.read().strip()

        if os.path.exists(unity_path):
            return unity_path

    if platform == "darwin":
        if unity_path == "":
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            if file_path == "":
                return
            if file_path.endswith("Unity.app"):
                file_path = os.path.join(file_path, "Contents", "MacOS", "Unity")
            with open(save_path, "w", encoding="UTF-8") as f:
                f.write(file_path)
            unity_path = file_path

    elif platform == "win32" or platform == "cygwin" or platform == "msys":
        if unity_path == "" or not os.path.exists(save_path):
            file_path = filedialog.askopenfilename()
            if file_path != "":
                with open(save_path, "w", encoding="UTF-8") as f:
                    f.write(file_path)
                unity_path = file_path

    return unity_path


def main():
    print("will install plugins to unity")

    file_dir = os.path.dirname(os.path.realpath(__file__))

    # deal with unity path & platforms
    unity_path = ""
    unity_path = deal_with_unity_path(unity_path, file_dir)

    if not os.path.exists(unity_path):
        print("unity path not found")
        exit(-1)

    print("using unity path: " + unity_path)
    unity_dir = os.path.join(file_dir, "unity")

    # -quit -batchmode -nographics -force-opengl
    cmd = (
        '"'
        + unity_path
        + '"'
        + " -projectPath "
        + unity_dir
        + " -executeMethod Wtf.Editor.BatchImportAssetPackages.ImportSelectPlugins -logFile "
        + os.path.join(unity_dir, "output.txt")
    )

    os.system(cmd)


if __name__ == "__main__":
    main()
