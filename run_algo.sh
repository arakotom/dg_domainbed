#!/bin/bash
# Clear the DISPLAY.
# unsetenv DISPLAY
# Call MATLAB with the appropriate input and output,
# make it immune to hangups and quits using ''nohup'',
# and run it in the background.



#for a in ClassCORAL CORAL ERM
#do
#for t in 0 1 2  3 4    # a stands for the algorithm
#do
#	python train.py --dataset RotatedMNIST --test_envs $t --algorithm $a
#done
#done

for s in 1000 2000
do
for a in ClassCORAL CORAL ERM # a stands for the algorithm
do
for t in 0 1 2  3     # a stands for the algorithm
do

	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 1 --steps $s
	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 0.5 --steps $s
	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 2 --steps $s
    
done
done
done