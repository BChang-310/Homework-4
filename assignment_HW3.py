'''
PGE310 Fall 2021 Homework 3

This homework is divided into 2 parts: 

  - In Problem 1 you will practice plotting while using a fun linear algebra
        application, the rotation matrix.
  - Problem 2 will help you practice indexing and slicing NumPy arrays in
        1D, 2D, and 3D.

Please submit this assignment as a Python file (.py) on Github classroom.
For more comprehensive instructions on how to test and submit your code,
refer to the posted instructions document on Canvas.

Indexing and slicing can be tricky, even for seasoned Python pros, but it's one
of the most useful skills to learn! And as always, we're here to help!

Feel free to contact Dr. P, Alex, Bernie, or Ziming with problems, questions, or comments.

'''

# Import NumPy and Matplotlib
import numpy as np
import matplotlib.pyplot as plt
from test_HW3 import test_solution

#%%
'''
Problem 1:
    Please complete the following:
        - In rotate_image(), create a 2D rotation matrix, R, and multiply 
            batman_data by R
        - Rotate the data points by 60 degrees using rotate_image().
        - In two separate figures, plot the original data and the rotated data
          with the following attributes:
            * Plot the coordinates, batman_coord
            * Set the axis to 'square' formatting
            * Set both the x and y limits to [-8, 8]
            * Label both the x and y axes
            * Add a title
'''

def rotate_image(image, theta):
    # data = a 2D array with a column of x data and a column of y data
    # theta = the rotation angle in degrees
    
    theta = np.radians(theta)  # Convert degrees to radians
    
    # Create rotation matrix
    R = 
    
    # Apply rotation matrix to the data
    rotated_image = 
    
    return rotated_image


def batman_plot(batman_coord):
    plt.figure(dpi=300)  # Initialize new figure
    plt.plot([0, 0], [-8, 8], 'k-', linewidth=1)  # Plot vertical line for y axis 
    plt.plot([-8, 8], [0, 0], 'k-', linewidth=1)  # Plot horizontal line for x axis
    # Add your plotting code here
    
    return
    

# Load data for the Batman logo, columns of x and y points
batman_data = np.genfromtxt('batman.csv', delimiter=',')

# Set the rotation angle
rotation_angle = 

# Call the rotation function and save the rotated data 
batman_data_rotated = 

# Call the plotting functions
batman_plot(batman_data)
batman_plot(batman_data_rotated)

# Test the rotation matrix operation function
square = np.array([[0, 0], [5, 0], [5, 5], [0, 5]])
test_solution(rotate_image(square, 60), '1_1')

#%%
'''
Problem 2:
    This problem will guide you through indexing 1D, 2D, and 3D arrays along with the 
    different types of elements, rows, columns, planes, and subsets. 
     
     **In our questions, we will use base-1 indexing: we will only refer to elements and 
     not indices. Please refer to the attached instructions for further clarification.
     
     **Please do not change the variable names.
        The automatic grader will be checking the names we provided.
'''

#%% Problem 2.1
array_1d = np.arange(0,100,10)
print('array_1d = \n', array_1d, '\n')

#%% Problem 2.1a
array_1d_index = 
test_solution(array_1d_index, '2_1a')

#%% Problem 2.1b
array_1d_slice = 
test_solution(array_1d_slice, '2_1b')

#%% Problem 2.2
array_2d = np.linspace(90, 42, 25).reshape((5,5))
print('array_2d = \n', array_2d, '\n')

#%% Problem 2.2a
array_2d_index = 
test_solution(array_2d_index, '2_2a')

#%% Problem 2.2b
array_2d_row_slice = 
test_solution(array_2d_row_slice, '2_2b')

#%% Problem 2.2c
array_2d_col_slice = 
test_solution(array_2d_col_slice, '2_2c')

#%% Problem 2.2d
array_2d_subset = 
test_solution(array_2d_subset, '2_2d')

#%% Problem 2.2e
array_2d_skip_rows = 
test_solution(array_2d_skip_rows, '2_2e')

#%% Problem 2.3
array_3d = np.arange(1, 28).reshape((3,3,3))
print('array_3d = \n', array_3d, '\n')

#%% Problem 2.3a
array_3d_index = 
test_solution(array_3d_index, '2_3a')

#%% Problem 2.3b
array_3d_x_slice = 
test_solution(array_3d_x_slice, '2_3b')

#%% Problem 2.3c
array_3d_y_slice = 
test_solution(array_3d_y_slice, '2_3c')

#%% Problem 2.3d
array_3d_z_slice = 
test_solution(array_3d_z_slice, '2_3d')

#%% Problem 2.3e
array_3d_z_col = 
test_solution(array_3d_z_col, '2_3e')

#%% Problem 2.3f
array_3d_subset = 
test_solution(array_3d_subset, '2_3f')








