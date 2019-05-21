#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: screenShot.py
# First Edit: 2019-05-21
# Last Change:  21-May-2019.
import time

import pyautogui


def main():
    time.sleep(100)
    pages = 190

    for i in range(pages):
        name = "IngaSuiron" + str(i)
        pyautogui.screenshot(name, region=(47, 332, 1339, 2237))
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(2)

        break


if __name__ == "__main__":
    # execute only if run as a script
    main()
