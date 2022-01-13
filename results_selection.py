#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:58:43 2021

@author: alain
"""



import json
import numpy as np
import os


data = 'PACS'
if data == 'RotatedMNIST':
    env_list = [0,1,2,3,4]
elif data == 'PACS':
    env_list = [0,1,2,3]

output_dir = './results/'
algo_list = os.listdir(os.path.join(output_dir,data))

score = ['']*len(env_list)
score_mat_test = np.zeros((len(algo_list),len(env_list)))
score_mat_traindomain = np.zeros((len(algo_list),len(env_list)))
name_algo = np.array(['']*len(algo_list), dtype='object')
nb_seed = np.ones(len(algo_list))*-1

for i_envs in env_list:
    for k, algo in enumerate(algo_list):
        #score[i_envs].append(algo)
        # 
        

        try:
            #print(algo)
            name_algo[k] = (algo.split('_')[0])
            #print(len(name_algo))
            nb_seed[k] = int((algo.split('seed')[1]))
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
        except:
            pass
            #name_algo.append(0)
            #seed.append(0)
    
#print(score_mat_test)
#print('\n')
#print(score_mat_traindomain)
#print(f'{algo} \t\t\t {perf_in:2.3f} \t {perf_out}')

# print(data)
# for k, algo in enumerate((algo_list)):
#     text=f"{algo:15}"
#     for j in range(len(env_list)):
#         text = text +  f" & {score_mat_traindomain[k,j]:2.3f} "
#     text += f" || {score_mat_traindomain[k,:].mean():2.3f} "
#     print(text)
    

# for k, algo in enumerate((algo_list)):
#     text=f"{algo:15}"

#     for j in range(len(env_list)):
#         text = text +  f" | {score_mat_test[k,j]:2.3f} "
#     text += f" || {score_mat_test[k,:].mean():2.3f} "
#     print(text)



algo_to_showlist = ['CORAL','ClassMMD','ClassCORAL','ClassWD']
for algo_to_show in algo_to_showlist:
    for i_seed in range(4):
        for k, algo in enumerate((algo_list)):
            #try:  
            if name_algo[k] == algo_to_show and nb_seed[k]==i_seed:
                text=f"{algo:15}"
                for j in range(len(env_list)):
                    text = text +  f" | {score_mat_traindomain[k,j]:2.3f} "
                text += f" || {score_mat_traindomain[k,:].mean():2.3f} "
                print(text)
#%% 
seed_list = [0,1,2,3]
algo_to_showlist = ['CORAL']
for algo_to_show in algo_to_showlist:
    #try:
        for seed in seed_list:
            ind_seed = np.argwhere(np.logical_and(nb_seed==seed,name_algo == algo_to_show))
            # find max performance
            best_model = np.argmax(score_mat_traindomain[ind_seed],axis=0)[0]
            text=f"{algo_to_show:15}"
            mean_val = 0
            for j in range(len(env_list)):
                best_val = score_mat_test[best_model[j],j]
                mean_val += best_val
                text = text +  f" | {best_val:2.3f} "
            text += f" || {mean_val/4:2.3f} "
            print(text)
    #except:
    #    pass
