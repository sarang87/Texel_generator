# Numpy 2D array Texel generator
Texel generator takes a 2D numpy array and returns a "texelized" version of the original 2D array. The returned array is composed of "texels". Each texel is a sub matrix in the 2D array of t_rows and t_cols. the values inside each texel are the mean of the values for all the cells corresponding to the texel in the original 2D array.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

# Prerequisites
1. Python 3
2. numpy

# Installing
Load it as a separate module in the file where it needs to be used

# Example

```
if __name__ == "__main__": 
  
  #Create a 2D array of 500 * 498 with calues from 1 to 2,49000.
  input_ array = np.arange(249000).reshape(500,498)

  #Get the texelelized version of the original array in X  for a window size of 4*4. 
  texelized_array = concat_arr(texel(input_array,4,4))
```

# Author/s
Sarang Joshi

# License
This project is licensed under the MIT License - see the LICENSE.md file for details

# Acknowledgments
Hat tip to anyone whose code was used
Inspiration
etc
