#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

