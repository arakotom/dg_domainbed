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


for a in ClassCORAL #CORAL ERM
do
for t in 0 1 2  3    # a stands for the algorithm
do
	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 1
	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 0.5
	python train.py --dataset PACS --test_envs $t --algorithm $a --mmd_gamma 2

done
done