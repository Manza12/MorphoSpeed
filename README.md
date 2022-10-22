# MorphoSpeed

## Specifications
### OS info
Ubuntu 20.04.3 LTS
### CPU info
Intel(R) Core(TM) i5-7300HQ CPU @ 2.50GHz (4 cores, 4 threads)
### GPU info
Nvidia GeForce GTX 1050 Mobile (2 GB memory)

## Tests
### Logs speed test
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

## Logs memory test
```
This is a memory test for MM operators

Parameters:
Image size: (1000, 1000)
Structuring element size: (15, 15)
Iterations CPU: 10
Iterations GPU: 100
Creating tensors...
Time to create CPU tensors: 0.007 s
Time to create CPU tensors: 1.421 s

Starting computations...

Erosion
CPU
-------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
                     Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg       CPU Mem  Self CPU Mem    # of Calls  
-------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
              aten::empty         3.34%      50.000us         3.34%      50.000us      25.000us       7.74 Mb       7.74 Mb             2  
                aten::pad         0.93%      14.000us        71.51%       1.072ms       1.072ms       3.92 Mb           0 b             1  
    aten::constant_pad_nd         3.14%      47.000us        70.58%       1.058ms       1.058ms       3.92 Mb           0 b             1  
              aten::fill_        68.58%       1.028ms        68.58%       1.028ms     514.000us           0 b           0 b             2  
             aten::narrow         0.27%       4.000us         0.93%      14.000us       3.500us           0 b           0 b             4  
-------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
Self CPU time total: 1.499ms

-----------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
                         Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg       CPU Mem  Self CPU Mem    # of Calls  
-----------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
                    aten::sub        47.32%     127.666ms        47.32%     127.666ms     127.666ms     858.31 Mb     858.31 Mb             1  
                    aten::min        52.31%     141.137ms        52.33%     141.166ms      70.583ms     183.11 Mb     183.11 Mb             2  
                  aten::empty         0.01%      16.000us         0.01%      16.000us      16.000us       3.92 Mb       3.92 Mb             1  
          aten::empty_strided         0.00%       9.000us         0.00%       9.000us       4.500us         904 b         904 b             2  
                     aten::eq         0.01%      36.000us         0.02%      55.000us      55.000us         225 b         221 b             1  
-----------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
Self CPU time total: 269.786ms

-----------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
                         Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg       CPU Mem  Self CPU Mem    # of Calls  
-----------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
                  aten::empty         0.01%      38.000us         0.01%      38.000us       9.500us     862.23 Mb     862.23 Mb             4  
                    aten::min        13.72%      94.708ms        13.72%      94.720ms      94.720ms      11.44 Mb      11.44 Mb             1  
                aten::resize_         0.00%       2.000us         0.00%       2.000us       2.000us     197.75 Kb     197.75 Kb             1  
          aten::empty_strided         0.00%       6.000us         0.00%       6.000us       3.000us         904 b         904 b             2  
                    aten::neg         0.00%      17.000us         0.00%      17.000us      17.000us         900 b         900 b             1  
-----------------------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  ------------  
Self CPU time total: 690.440ms


Process finished with exit code 0
```
