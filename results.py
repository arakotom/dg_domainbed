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
env_list = [0,1,2,3]
data = 'PACS'
output_dir = './results/'
score = ['']*len(env_list)
score_mat_test = np.zeros((len(algo_list),len(env_list)))
score_mat_traindomain = np.zeros((len(algo_list),len(env_list)))


for i_envs in env_list:
    for k, algo in enumerate(algo_list):
        #score[i_envs].append(algo)

        with open(os.path.join(output_dir,data, algo,f'results-[{i_envs:}]'), 'r') as myfile:
            lines=myfile.readlines()
    
    
        
        obj = json.loads(lines[-1])
        test_envs = obj['args']['test_envs'][0]
        perf_target_out  = obj[f"env{test_envs}_out_acc"]
    
        perf_source_out = 0
        for j in env_list:
            if j !=i_envs : # j is not target domain
                perf_source_out+= obj[f"env{j}_out_acc"]
        perf_source_out/= (len(env_list)-1)
        score_mat_test[k,i_envs] = perf_target_out
        score_mat_traindomain[k,i_envs] = perf_source_out

    
print(score_mat_test)
print(score_mat_traindomain)
#print(f'{algo} \t\t\t {perf_in:2.3f} \t {perf_out}')

for k, algo in enumerate((algo_list)):
    text=f"{algo:10}"
    for j in range(len(env_list)-1):
     text += f"& {score_mat_traindomain[j]:2.3f}"
    print(text)

