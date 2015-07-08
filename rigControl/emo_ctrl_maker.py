import bpy 
bpy.ops.pose.constraint_add(type='ACTION')
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].target = bpy.data.objects["control"]
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].subtarget = "EMO-demo"
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].transform_channel = 'LOCATION_Y'
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].action = bpy.data.actions["EMO-demo"]
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].target_space = 'LOCAL'
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].max = 1
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].frame_start = 1
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].frame_end = 101
bpy.context.object.pose.bones["lip_D_L"].constraints["Action"].influence = 1



# Active object
ob = bpy.context.object
print ('object: ', ob)
if ob.type == 'ARMATURE':
    armature = ob.data
    print ('armature: ', armature)
    for bone in armature.bones:
        print(bone.name)
