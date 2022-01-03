#!/usr/bin/python3
# Clear the DISPLAY.
# unsetenv DISPLAY
# Call MATLAB with the appropriate input and output,
# make it immune to hangups and quits using ''nohup'',
# and run it in the background.



import os
import getopt,sys


opts, args = getopt.getopt(sys.argv[1:], "s:")
for opt, arg in opts:
    if opt == '-s':
        setting = int(arg)

if setting == 1:
    algo_list = ['CORAL']
elif setting == 2:
    algo_list = ['Transfer']


data = 'PACS'
if data == 'PACS':
    env_list = [0,1,2,3]
    lr = 5e-5
    train_delta = 0.3
    lr_d = 0.001
    d_steps = 30
    steps_tran = 80000
    
step_list = [1000]
seed_list = [1,2]

for step in step_list:
    for seed in seed_list:
        for algo in algo_list:
            if algo in ['ERM', 'Transfer'] :
                mmd_gamma_list = [0]
            elif algo in ['ClassCORAL']:
                mmd_gamma_list = [0.01, 0.05,0.1,0.2]
                mmd_gamma_list = [0.2,0.3]
                reg_wda_list = [0.01,0.1]

            elif algo in ['ClassMMD']:
                mmd_gamma_list = [0.001,0.005]
                reg_wda_list = [0.1]
            elif algo in  ['ClassWD']:
                mmd_gamma_list = [0.0005]
                reg_wda_list = [0.005]
            elif algo in ['CORAL','MMD']:
                mmd_gamma_list = [0.01,0.05]
                reg_wda_list = [1]
            if setting == 1:
                
                for reg_wda in reg_wda_list:
                    for reg_align in mmd_gamma_list:
                        for envs in env_list:
                            command = f"python train.py --algorithm {algo} --dataset {data:} --lr {lr:2.5f}"
                            command += f" --test_envs {envs:d} --reg_align  {reg_align:2.4f} --step {step:d}"
                            command += f" --reg_wda {reg_wda:2.3f}"
                            command += f" --seed {seed:d} --trial_seed 0"
                            print(command)
                            os.system(command)
            elif setting ==2 : ###
                ###  Transfer algorithm setiing
                for envs in env_list:
                    command = f"python train.py --algorithm {algo} --dataset {data:} --lr {lr:2.5f}"
                    command += f" --test_envs {envs:d} --step {steps_tran:d} " 
                    command += f"--train_delta {train_delta:2.2f} --d_steps_per_g {d_steps:d} --lr_d {lr_d:2.3f}"
                    command += f" --seed {seed:d} --trial_seed 0"
    
                    print(command)
                    os.system(command)





