# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:09:15 2016

@author: lenovo
"""

from rosetta import *
init()
 
pose = pose_from_pdb("G:/ZJUT/python/Rosetta/protein/1DTD/1DTD.clean1.pdb")
to_centroid = SwitchResidueTypeSetMover("centroid")
to_centroid.apply(pose)  
scorefxn = create_score_function("score3")
energy_forword = scorefxn(pose)
print energy_forword