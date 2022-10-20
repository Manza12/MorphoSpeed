import time
import torch
from nnMorpho.operations import erosion as erosion_morpho
from nnMorpho.operations import dilation as dilation_morpho
from kornia.morphology import erosion as erosion_kornia
from kornia.morphology import dilation as dilation_kornia
from scipy.ndimage import grey_erosion as erosion_scipy
from scipy.ndimage import grey_dilation as dilation_scipy
from cv2 import erode as erosion_cv
from cv2 import dilate as dilation_cv

print("This is a performance test for MM operators")
print()

# Parameters
image_size = (1000, 1000)
str_el_size = (15, 15)
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
start = time.time()
for _ in range(iterations_cpu):
    erosion_morpho(input_image_cpu, str_el_cpu)
print('Time erosion nnMorpho CPU: %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

# kornia
start = time.time()
for _ in range(iterations_cpu):
    erosion_kornia(torch.unsqueeze(torch.unsqueeze(input_image_cpu, 0), 0), str_el_cpu, engine='unfold')
print('Time erosion kornia CPU (unfold): %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

start = time.time()
for _ in range(iterations_cpu):
    erosion_kornia(torch.unsqueeze(torch.unsqueeze(input_image_cpu, 0), 0), str_el_cpu, engine='convolution')
print('Time erosion kornia CPU (convolution): %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

# SciPy
start = time.time()
for _ in range(iterations_cpu):
    erosion_scipy(input_image_np, structure=str_el_np)
print('Time erosion SciPy CPU: %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

# OpenCV
start = time.time()
for _ in range(iterations_cpu):
    erosion_cv(input_image_np, str_el_np)
print('Time erosion OpenCV CPU: %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

print()

# GPU
print('GPU')

# nnMorpho
start = time.time()
for _ in range(iterations_gpu):
    erosion_morpho(input_image_gpu, str_el_gpu)
print('Time erosion nnMorpho GPU: %.3f μs' % (1e6*(time.time() - start)/iterations_gpu))

# kornia
start = time.time()
for _ in range(iterations_gpu):
    erosion_kornia(torch.unsqueeze(torch.unsqueeze(input_image_gpu, 0), 0), str_el_gpu, engine='unfold')
print('Time erosion kornia GPU (unfold): %.3f μs' % (1e6*(time.time() - start)/iterations_gpu))

start = time.time()
for _ in range(iterations_gpu):
    erosion_kornia(torch.unsqueeze(torch.unsqueeze(input_image_gpu, 0), 0), str_el_gpu, engine='convolution')
print('Time erosion kornia GPU (convolution): %.3f μs' % (1e6*(time.time() - start)/iterations_gpu))

print()

# Dilation
print('Dilation')

# CPU
print('CPU')

# nnMorpho
start = time.time()
for _ in range(iterations_cpu):
    dilation_morpho(input_image_cpu, str_el_cpu)
print('Time dilation nnMorpho CPU: %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

# kornia
start = time.time()
for _ in range(iterations_cpu):
    dilation_kornia(torch.unsqueeze(torch.unsqueeze(input_image_cpu, 0), 0), str_el_cpu, engine='unfold')
print('Time dilation kornia CPU (unfold): %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

start = time.time()
for _ in range(iterations_cpu):
    dilation_kornia(torch.unsqueeze(torch.unsqueeze(input_image_cpu, 0), 0), str_el_cpu, engine='convolution')
print('Time dilation kornia CPU (convolution): %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

# SciPy
start = time.time()
for _ in range(iterations_cpu):
    dilation_scipy(input_image_np, structure=str_el_np)
print('Time dilation SciPy CPU: %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

# OpenCV
start = time.time()
for _ in range(iterations_cpu):
    dilation_cv(input_image_np, str_el_np)
print('Time dilation OpenCV CPU: %.3f ms' % (1e3*(time.time() - start)/iterations_cpu))

print()

# GPU
print('GPU')

# nnMorpho
start = time.time()
for _ in range(iterations_gpu):
    dilation_morpho(input_image_gpu, str_el_gpu)
print('Time dilation nnMorpho GPU: %.3f μs' % (1e6*(time.time() - start)/iterations_gpu))

# kornia
start = time.time()
for _ in range(iterations_gpu):
    dilation_kornia(torch.unsqueeze(torch.unsqueeze(input_image_gpu, 0), 0), str_el_gpu, engine='unfold')
print('Time dilation kornia GPU (unfold): %.3f μs' % (1e6*(time.time() - start)/iterations_gpu))

start = time.time()
for _ in range(iterations_gpu):
    dilation_kornia(torch.unsqueeze(torch.unsqueeze(input_image_gpu, 0), 0), str_el_gpu, engine='convolution')
print('Time dilation kornia GPU (convolution): %.3f μs' % (1e6*(time.time() - start)/iterations_gpu))
