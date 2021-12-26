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
    algo_list = ['ClassCORAL','ClassMMD']
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
    
step_list = [1100]
seed_list = [0,1,2,3]

for step in step_list:
    for seed in seed_list:
        for algo in algo_list:
            if algo in ['ERM', 'Transfer'] :
                mmd_gamma_list = [0]
            else:
                mmd_gamma_list = [0.1, 0.5,1,2]
            if setting == 1:

                for mmd_gamma in mmd_gamma_list:
                    for envs in env_list:
                        command = f"python train.py --algorithm {algo} --dataset {data:} --lr {lr:2.5f}"
                        command += f" --test_envs {envs:d} --mmd_gamma  {mmd_gamma:2.1f} --step {step:d}"
                        command += f" --seed {seed:d}"
                        print(command)
                        os.system(command)
            elif setting ==2 : ###
                ###  Transfer algorithm setiing
                for envs in env_list:
                    command = f"python train.py --algorithm {algo} --dataset {data:} --lr {lr:2.5f}"
                    command += f" --test_envs {envs:d} --step {steps_tran:d} " 
                    command += f"--train_delta {train_delta:2.2f} --d_steps_per_g {d_steps:d} --lr_d {lr_d:2.3f}"
                    command += f" --seed {seed:d}"
    
                    print(command)
                    os.system(command)





