#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    x = [[matrix[j][i] for j in range(len(matrix)-1,-1,-1)] for i in range(0,len(matrix[0]),1)]
    for i in range(len(x)):
        matrix[i] = x[i]
