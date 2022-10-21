import time
import timeit
import torch
from nnMorpho.operations import erosion as erosion_morpho
from nnMorpho.operations import dilation as dilation_morpho
from kornia.morphology import erosion as erosion_kornia
from kornia.morphology import dilation as dilation_kornia
from scipy.ndimage import grey_erosion as erosion_scipy
from scipy.ndimage import grey_dilation as dilation_scipy
from cv2 import erode as erosion_cv
from cv2 import dilate as dilation_cv

print('Speed test')

# Parameters
image_size = (1000, 1000)
str_el_size = (21, 21)
iterations_cpu = 10
iterations_gpu = 10

print('Parameters:')
print('Image size:', image_size)
print('Structuring element size:', str_el_size)
print('Iterations CPU:', iterations_cpu)
print('Iterations GPU:', iterations_gpu)

# Create tensors
print('Creating tensors...')

# CPU
start = time.time()
input_image_cpu = torch.rand(image_size, device='cpu')
str_el_cpu = torch.rand(str_el_size, device='cpu')

input_image_np = input_image_cpu.numpy()
str_el_np = str_el_cpu.numpy()
print('Time to create CPU tensors: %.3f s' % (time.time() - start))

# GPU
start = time.time()
input_image_gpu = torch.rand(image_size, device='cuda:0')
str_el_gpu = torch.rand(str_el_size, device='cuda:0')
print('Time to create CPU tensors: %.3f s' % (time.time() - start))

print()

# Computations
print('Starting computations...')
print()

# Erosion
print('Erosion')

# CPU
print('CPU')

# nnMorpho
print('nnMorpho - CPU')
timeit.timeit('nnMorpho.operations.erosion(input_image_cpu, str_el_cpu)', number=1)
print(t)
