import bpy
import json
import math
import os
import sys
import argparse

def get_arguments():
    argv = sys.argv
    usage_text = (
            "Run blender in background mode with this script:"
            "  blender --background --python " + __file__ + " -- [options]"
        )
    if "--" not in argv:
        argv = []  # as if no args are passed
    else:
        argv = argv[argv.index("--") + 1:]  # get all args after "--"
    parser = argparse.ArgumentParser(description=usage_text)
    parser.add_argument(
        "-t", "--text", dest="text", type=str, required=True,
        help="This text will be used to render an image",
    )
    parser.add_argument(
        "-o", "--OUTPUT_PATH", dest="OUTPUT_PATH", type=str, required=True,
        help="This text will be used to define the output path",
    )
    parser.add_argument(
        "-r", "--RENDER_PATH", dest="RENDER_PATH", type=str, required=True,
        help="This text will be used to define the render path",
    )
    args = parser.parse_args(argv)
    return args

def main():
    print(f'starting makeAndRender')
    the_args = get_arguments()
    print(the_args.text)
    print(the_args.OUTPUT_PATH)
    homeDirectory = os.getenv("HOME")
    bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name=(f'text test')
    bpy.context.active_object.data.body=f'text: {the_args.text}'
    bpy.context.active_object.data.size=1
    bpy.context.active_object.data.align_x='CENTER'
    bpy.context.active_object.data.extrude=.2
    bpy.context.active_object.data.bevel_depth=.04
    bpy.context.active_object.location[0] = 0
    bpy.context.active_object.location[1] = 0
    bpy.context.active_object.rotation_euler[0] = 1.5708

    # bpy.ops.object.convert(target='MESH')


    bpy.ops.mesh.primitive_plane_add(size=10, location=(0,0,-.3))
    bpy.ops.object.light_add(type='SPOT', radius=1, location=(0, -4, 15))
    bpy.context.active_object.data.energy=5000

    # bpy.ops.material.new()
    # bpy.data.node_groups["Shader Nodetree"].nodes["Principled BSDF"].inputs[7].default_value = 0.179487
    # bpy.context.object.active_material.name = "Material-001"




    bpy.ops.wm.save_as_mainfile(filepath=f'{the_args.OUTPUT_PATH}')

    print("rendering")
    sceneKey = bpy.data.scenes.keys()[0]
    print(f'sceneKey = {sceneKey}')
    for obj in bpy.data.objects:
        if ( obj.type == 'CAMERA' ):
            print(f'Rendering scene: {sceneKey}. Camera name: {obj.name}')
            bpy.data.scenes[sceneKey].camera = obj
            bpy.data.scenes[sceneKey].render.engine = 'BLENDER_EEVEE'
            bpy.data.scenes[sceneKey].render.resolution_x = 1920
            bpy.data.scenes[sceneKey].render.resolution_y = 1080
            bpy.data.scenes[sceneKey].render.filepath = the_args.RENDER_PATH
            bpy.ops.render.render(write_still=True, scene=sceneKey)


if __name__ == "__main__":
    main()
