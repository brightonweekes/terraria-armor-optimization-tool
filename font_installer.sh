#!/bin/bash

sudo mkdir /usr/share/fonts

sudo cp ./guiAssets/andy_bold.ttf /usr/share/fonts

fc-cache -f -v
