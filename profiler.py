import time
import torch
from nnMorpho.operations import erosion as erosion_morpho
from kornia.morphology import erosion as erosion_kornia
import torch.autograd.profiler as profiler

print("This is a memory test for MM operators")
print()

# Parameters
image_size = (1000, 1000)
str_el_size = (15, 15)
iterations_cpu = 10
iterations_gpu = 100

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
input_image_cpu_kornia = torch.unsqueeze(torch.unsqueeze(input_image_cpu, 0), 0)
str_el_cpu = torch.rand(str_el_size, device='cpu')

input_image_np = input_image_cpu.numpy()
str_el_np = str_el_cpu.numpy()
print('Time to create CPU tensors: %.3f s' % (time.time() - start))

# GPU
start = time.time()
input_image_gpu = torch.rand(image_size, device='cuda:0')
input_image_gpu_kornia = torch.unsqueeze(torch.unsqueeze(input_image_gpu, 0), 0)
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
with profiler.profile(with_stack=True, profile_memory=True) as prof:
    erosion_morpho(input_image_cpu, str_el_cpu)
print(prof.key_averages(group_by_input_shape=True).table(sort_by='self_cpu_memory_usage', row_limit=5))


# kornia
with profiler.profile(with_stack=True, profile_memory=True) as prof:
    erosion_kornia(input_image_cpu_kornia, str_el_cpu, engine='unfold')
print(prof.key_averages(group_by_input_shape=True).table(sort_by='self_cpu_memory_usage', row_limit=5))


# kornia
with profiler.profile(with_stack=True, profile_memory=True) as prof:
    erosion_kornia(input_image_cpu_kornia, str_el_cpu, engine='convolution')
print(prof.key_averages(group_by_input_shape=True).table(sort_by='self_cpu_memory_usage', row_limit=5))
