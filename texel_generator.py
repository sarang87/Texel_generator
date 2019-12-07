#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:24:00 2019

@author: wickedshaman
"""
from sklearn.cluster import KMeans
import numpy as np

""" 
    Create a texel (an aggregation) of cells with the mean of the values from a 2D numpy array. 
  
    Parameters: 
        in_arr (numpy 2D_array): The input 2D numpy array form which texels have to be created 
        row_slices (int): The number of rows for the texel window
        col_slices (int): The number of rows columns the texel window 
        
    Returns: 
        out_arr (list): A list of lists where each internal list is composed of the mean of the slice window 
"""
def texel(in_arr, row_slice=4, col_slice=4):
    out_arr = []
    rows = in_arr.shape[0]
    cols = in_arr.shape[1]
    print (rows)
    for i in range(0,rows,row_slice):
        l1 = []
        for j in range(0,cols,col_slice):
            c=in_arr[i:i+row_slice,j:j+col_slice]
            l1.append(np.full(c.shape,np.mean(in_arr[i:i+row_slice,j:j+col_slice])))
        out_arr.append(l1)
    return out_arr

def concat_arr(in_arr):
    out_arr = []
    for i in in_arr:
        m = i[0]
        for j in range(len(i)-1):
            m = np.concatenate((m,i[j+1]),1)
        print(m.shape)
        print("\n")
        out_arr.append(m)
    print(len(out_arr))
    arr_0 = out_arr[0]
    for i in range(len(out_arr)-1):        
        arr_0 = np.append(arr_0, out_arr[i+1],axis=0)
    return arr_0

if __name__ == "__main__": 
    print("executed directly")
    #input("Enter number of array elements")
    a=np.arange(249000).reshape(500,498)
    print(a.shape)
    #for i in concat_arr(texel(a,10,10)):
    #    print(i)
    
    X = concat_arr(texel(a,4,4))
    kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
    print("\n\nSklearn")
    print (kmeans.labels_)
    print (kmeans.cluster_centers_)

