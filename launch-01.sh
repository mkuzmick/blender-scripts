#! /usr/bin/env zsh

CURRENT_TIME=$(date "+%Y%m%d%H%M%S")
OUTPUT_PATH="$HOME/Desktop/output-$CURRENT_TIME.blend"
RENDER_PATH="$HOME/Desktop/_blender/renders/scripted/test-$CURRENT_TIME"

blender "$HOME/Development/blender-scripts/blender-templates/just-a-cam.blend" --background --python "$HOME/Development/blender-scripts/make-and-render.py" -- --text="just a test" --OUTPUT_PATH="$OUTPUT_PATH" --RENDER_PATH="$RENDER_PATH"
# open "$OUTPUT_PATH" -a blender
