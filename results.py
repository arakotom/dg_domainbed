#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:58:43 2021

@author: alain
"""



import json
import numpy as np
import os


algo_list = ['ERM', 'CORAL','ClassCORAL']
env_list = [0,1,2,3,4]
data = 'RotatedMNIST'
output_dir = './results/'
for algo in algo_list:
    for i_envs in env_list:
        with open(os.path.join(output_dir,data, algo,'results-[i_envs]'), 'r') as myfile:
            lines=myfile.readlines()
    
    
        
        obj = json.loads(lines[-1])
        test_envs = obj['args']['test_envs'][0]
        perf_in  = obj[f"env{test_envs}_in_acc"]
        perf_out  = obj[f"env{test_envs}_out_acc"]
    
        print(f'{algo} \t\t\t {perf_in:2.3f} \t {perf_out}')
            

