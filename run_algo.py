#!/usr/bin/python
# Clear the DISPLAY.
# unsetenv DISPLAY
# Call MATLAB with the appropriate input and output,
# make it immune to hangups and quits using ''nohup'',
# and run it in the background.



import os

data = 'PACS'
env_list = [0,1,2,3]
algo_list = ['ERM'] #['CORAL','ClassCORAL','ClassMMD']
mmd_gamma_list = [0.1, 0.5,1,2]
step_list = [1000]
seed_list = [0]
for step in step_list:
    for seed in seed_list:
        for algo in algo_list:
            for envs in env_list:
                for mmd_gamma in mmd_gamma_list:
                    command = f"python train.py --algorithm {algo} --dataset {data:}"
                    command += f" --test_envs {envs:d} --mmd_gamma  {mmd_gamma:2.1f} --step {step:d}"
                    command += f" --seed {seed:d}"
                    print(command)
                    os.system(command)

#for a in ClassCORAL CORAL ERM
#do
#for t in 0 1 2  3 4    # a stands for the algorithm
#do
#	python train.py --dataset RotatedMNIST --test_envs $t --algorithm $a
#done
#done

# for s in 1000 2000
# do
# for a in ClassCORAL CORAL ERM # a stands for the algorithm
# do
# for t in 0 1 2  3     # a stands for the algorithm
# do

# 	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 1 --steps $s
# 	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 0.5 --steps $s
# 	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 2 --steps $s
    
# done
# done
# done