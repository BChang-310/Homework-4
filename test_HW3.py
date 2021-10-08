# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:39:30 2021

@author: bchan
"""
import numpy as np


prob1_1 = np.array([[0., 0.], 
                    [2.5, -4.33012702], 
                    [6.83012702, -1.83012702], 
                    [4.33012702, 2.5]])

prob2_1a = 40

prob2_1b = np.array([30, 40, 50, 60])

prob2_2a = 64.
        
prob2_2b = np.array([60., 58., 56., 54., 52.])

prob2_2c = np.array([88., 78., 68., 58., 48.])

prob2_2d = np.array([[86., 84.], 
                     [76., 74.], 
                     [66., 64.]])

prob2_2e = np.array([[90., 88., 86., 84., 82.], 
                     [70., 68., 66., 64., 62.], 
                     [50., 48., 46., 44., 42.]])

prob2_3a = 26.

prob2_3b = np.array([[3, 6, 9], 
                     [12, 15, 18], 
                     [21, 24, 27]])

prob2_3c = np.array([[1, 2, 3], 
                     [10, 11, 12], 
                     [19, 20, 21]])

prob2_3d = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
        
prob2_3e = np.array([6, 15, 24])

prob2_3f = np.array([[[13, 14], [16, 17]], 
                     [[22, 23], [25, 26]]])

sol = {'1_1': prob1_1,
       '2_1a': prob2_1a,
       '2_1b': prob2_1b,
       '2_2a': prob2_2a,
       '2_2b': prob2_2b,
       '2_2c': prob2_2c,
       '2_2d': prob2_2d,
       '2_2e': prob2_2e,
       '2_3a': prob2_3a,
       '2_3b': prob2_3b,
       '2_3c': prob2_3c,
       '2_3d': prob2_3d,
       '2_3e': prob2_3e,
       '2_3f': prob2_3f}

def test_solution(student,  problem_num, solution=sol):
    # print('-'*50)
    print(f'Problem {problem_num.replace("_",".")}: ')
    print(f'\t Your solution = \n \t\t{student}')
    if np.allclose(student, solution[problem_num]):
        print('\t Correct!')
    else:
        print('\t Incorrect')
    print('-'*50)
        
        
        
    
    
