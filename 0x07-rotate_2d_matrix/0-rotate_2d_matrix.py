#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

