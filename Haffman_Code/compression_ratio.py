import os

def get_file_size(filename):
    return os.stat(filename).st_size

# size of original data
original_size = get_file_size('original_data.txt')

# size of compressed data
compressed_size = get_file_size('compressed_data.txt')

# compression ratio
compression_ratio = original_size / compressed_size

print(f'Compression ratio: {compression_ratio:.2f}')