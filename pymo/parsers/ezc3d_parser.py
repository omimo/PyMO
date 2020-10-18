'''
C3D Parser Class


By Omid Alemi
Created: July, 2020
'''

import numpy as np
import pandas as pd

from pymo.data import Joint, MocapData

#TODO: Do we really need a class here?
class C3DParser():
    '''
    Parses a C3D file using the ezc3d library and creates a 
    PyMo.MocapData object.
    '''

    def __init__(self):
        import ezc3d 
        


    def parse(self, filename):
        import ezc3d
        ezc = ezc3d.c3d(filename)

        param_points = ezc['header']['points']

        #TODO: Handle the cases the file does not have these info
        marker_labels = ezc['parameters']['POINT']['LABELS']['value']
        marker_descriptions = ezc['parameters']['POINT']['DESCRIPTIONS']['value']


        mocap_data = MocapData()        
        mocap_data.skeleton = None
        mocap_data.root_name = None

        
        mocap_data.channel_names = marker_labels
        mocap_data.framerate = param_points['frame_rate']
        mocap_data.metadata = {}
        mocap_data.metadata['marker_descriptions'] = marker_descriptions

        
        points = ezc['data']['points']

        values = []
        column_names = []

        for m in range(len(marker_labels)): #TODO: Make the ordering more clear to the user
            column_names.append('%s_Xposition'%marker_labels[m])
            column_names.append('%s_Zposition'%marker_labels[m])
            column_names.append('%s_Yposition'%marker_labels[m])

        for f in range(points.shape[2]):
            frame_values = []

            for m in range(points.shape[1]):
                frame_values.append(points[0,m,f])
                frame_values.append(points[1,m,f])
                frame_values.append(points[2,m,f])

            values.append(frame_values)
        
        values = np.asarray(values)

        

        time_index = pd.to_timedelta([f[0] for f in values], unit='s')

        
        

        mocap_data.values = pd.DataFrame(data=values[:,0:len(column_names)], index=time_index, columns=column_names) #just a hack for now - need to double check

        return mocap_data
        