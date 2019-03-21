
import csv
import numpy as np
import bpy
from source.post_processors.blender.helpers import centered, mirrored
from source.post_processors.blender.objects import (cylinder_geometry,
                                                    composite_geometry,
                                                    triangular_prism)



class blender_scene(object):

    def __init__(self,prefix=''):
        self.prefix = prefix
        scale = 1/20
        self.scale = scale

        self.hps_top = np.array([[0], [0], [0]],dtype=np.float64)*scale
        self.s_outer_raduis = 1*scale
        self.hps_bottom = np.array([[0], [0], [0]],dtype=np.float64)

        self._inputs = ['hps_top', 's_outer_raduis', 'hps_bottom']
        self.geometries = {'gms_block': 'rbs_block'}

    
    def get_data(self,csv_file):
        self.cfg_file = csv_file
        with open(csv_file, newline='') as csvfile:
            content = csv.reader(csvfile)
            next(content)
            for row in content:
                attr = row[0]
                if attr in self._inputs:
                    value = getattr(self,attr)
                    setattr(self,attr,value)
                    if isinstance(value, np.ndarray):
                        value = np.array(row[1:],dtype=np.float64)
                        value = np.resize(value,(3,1))*self.scale
                        setattr(self,attr,value)
                    else:
                        value = float(row[1])*self.scale
                        setattr(self,attr,value)

    def load_anim_data(self,csv_file):
        with open(csv_file, newline='') as csvfile:
            content = csv.reader(csvfile)
            keys = {k:i for i,k in enumerate(next(content)[1:])}
            arr = np.array(list(content))[:,1:]
            arr = np.array(arr,dtype=np.float64)

        scale = self.scale
        for i,row in enumerate(arr,1):
            for g,b in self.geometries.items():
                k = keys['%s%s.x'%(self.prefix,b)]
                obj = getattr(self,g).obj
                obj.location = [float(n)*scale for n in row[k:k+3]]
                obj.rotation_quaternion = [float(n) for n in row[k+3:k+7]]
                obj.keyframe_insert('location', frame=i)
                obj.keyframe_insert('rotation_quaternion', frame=i)

        bpy.context.scene.render.frame_map_old = i+1
        bpy.context.scene.render.frame_map_new = 24*2
        bpy.context.scene.frame_end = bpy.context.scene.render.frame_map_new

    def create_scene(self):
        self.gms_block = cylinder_geometry(self.hps_top,self.hps_bottom,self.s_outer_raduis)

        self.setup_VIEW_3D()

    @staticmethod
    def setup_VIEW_3D():
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                        bpy.ops.view3d.view_all(override)

