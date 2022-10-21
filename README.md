# MorphoSpeed

## Speed test
### OS info
Ubuntu 20.04.3 LTS
### CPU info
Intel(R) Core(TM) i5-7300HQ CPU @ 2.50GHz (4 cores, 4 threads)
### GPU info
Nvidia GeForce GTX 1050 Mobile (2 GB memory)
### Logs
```
This is a speed test for MM operators

Parameters:
Image size: (1000, 1000)
Structuring element size: (15, 15)
Iterations CPU: 10
Iterations GPU: 100
Creating tensors...
Time to create CPU tensors: 0.007 s
Time to create CPU tensors: 1.419 s

Starting computations...

Erosion
CPU
Time erosion nnMorpho CPU: 359.875 ms
Time erosion kornia CPU (unfold): 292.366 ms
Time erosion kornia CPU (convolution): 696.517 ms
Time erosion SciPy CPU: 314.151 ms
Time erosion OpenCV CPU: 1.563 ms
Time erosion scikit CPU: 24.299 ms

GPU
Time erosion nnMorpho GPU: 131.867 μs
Time erosion kornia GPU (unfold): 3954.315 μs
Time erosion kornia GPU (convolution): 65951.047 μs

Dilation
CPU
Time dilation nnMorpho CPU: 361.442 ms
Time dilation kornia CPU (unfold): 322.799 ms
Time dilation kornia CPU (convolution): 723.569 ms
Time dilation SciPy CPU: 346.577 ms
Time dilation OpenCV CPU: 1.465 ms
Time dilation scikit CPU: 23.769 ms

GPU
Time dilation nnMorpho GPU: 52.967 μs
Time dilation kornia GPU (unfold): 5366.943 μs
Time dilation kornia GPU (convolution): 63218.687 μs

Process finished with exit code 0
```
