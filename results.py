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
data = 'PACS'
if data == 'RotatedMNIST':
    env_list = [0,1,2,3,4]
elif data == 'PACS':
    env_list = [0,1,2,3]

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

print(data)
for k, algo in enumerate((algo_list)):
    text=f"{algo:15}"
    for j in range(len(env_list)):
        text = text +  f" & {score_mat_traindomain[k,j]:2.3f} "
    text += f" || {score_mat_traindomain[k,:].mean():2.3f} "
    print(text)
for k, algo in enumerate((algo_list)):
    text=f"{algo:15}"

    for j in range(len(env_list)):
        text = text +  f" | {score_mat_test[k,j]:2.3f} "
    text += f" || {score_mat_test[k,:].mean():2.3f} "
    print(text)
