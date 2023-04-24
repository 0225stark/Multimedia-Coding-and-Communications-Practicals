import heapq
import heapq
import collections
import json
import csv
import math
from collections import defaultdict
# from huffman_coding import *


class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_freq_dict(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    return freq_dict

def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(char, freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(freq=left.freq+right.freq, left=left, right=right)
        heapq.heappush(heap, parent)
    
    return heap[0]



def build_codebook(root):
    codebook = {}
    def traverse(node, code):
        if node.char is not None:
            codebook[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')
    traverse(root, '')
    return codebook

def encode_text(text, codebook):
    return ''.join(codebook[char] for char in text)

def decode_text(encoded_text, root):
    decoded_text = []
    node = root
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = root
    return ''.join(decoded_text)

def huffman_encode(text):
    freq_dict = build_freq_dict(text)
    root = build_huffman_tree(freq_dict)
    codebook = build_codebook(root)
    encoded_text = encode_text(text, codebook)
    return encoded_text, root

def huffman_decode(encoded_text, root):
    decoded_text = decode_text(encoded_text, root)
    return decoded_text

f=open("original_data.txt","r")
text=f.read()
f.close()
# text = "This is My example input text"
encoded_text, root = huffman_encode(text)

print(f'Original text: {text}')
print(f'Encoded text: {encoded_text}')
decoded_text = huffman_decode(encoded_text, root)
print(f'Decoded text: {decoded_text}')

file = open("compressed_data.txt", "w")

# Write a string to the file
file.write(encoded_text)

# Close the file
file.close()

import json

def save_huffman_tree(root, filename):
    """Save the Huffman tree to a JSON file"""
    def encode_node(node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return [node.char, node.freq]
        return [encode_node(node.left), encode_node(node.right)]

    with open(filename, 'w') as f:
        json.dump(encode_node(root), f)

# Call the function to save the Huffman tree to a JSON file
save_huffman_tree(root, 'huffman_tree.json')

import csv

def create_symbol_code_table(root):
    """Create a symbol code table from the Huffman tree"""
    def encode_node(node, code):
        if node is None:
            return
        if node.left is None and node.right is None:
            symbol_code[node.char] = code
            return
        encode_node(node.left, code+'0')
        encode_node(node.right, code+'1')

    symbol_code = {}
    encode_node(root, '')

    return symbol_code

# Call the function to create the symbol code table
symbol_code = create_symbol_code_table(root)

# Output the symbol code table to a CSV file
with open('symbol_code_table.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Symbol', 'Code'])
    for symbol, code in symbol_code.items():
        writer.writerow([symbol, code])



# Define a dictionary to store the frequency of each symbol
symbol_freq = collections.defaultdict(int)
for symbol in text:
    symbol_freq[symbol] += 1

# Implement the Huffman coding algorithm
heap = [[freq, [symbol, '']] for symbol, freq in symbol_freq.items()]
heapq.heapify(heap)
while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

# Store the symbol codes in a dictionary
symbol_code = dict(sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[-1]), x)))

# Write the coding tree to a JSON file
with open('coding_tree.json', 'w') as f:
    json.dump(symbol_code, f)

# Write the symbol code table to a CSV file
with open('symbol_code_table.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Symbol', 'Code'])
    for symbol, code in symbol_code.items():
        writer.writerow([symbol, code])

# Calculate the average code length
total_bits = 0
total_freq = 0
for symbol, code in symbol_code.items():
    total_bits += len(code) * symbol_freq[symbol]
    total_freq += symbol_freq[symbol]
avg_code_length = total_bits / total_freq

# Calculate the entropy
entropy = 0
for symbol, freq in symbol_freq.items():
    prob = freq / total_freq
    entropy -= prob * math.log2(prob)

# Calculate the efficiency
efficiency = entropy / avg_code_length

# Write the results to a text file
with open('compression_stats.txt', 'w') as f:
    f.write('Average Code Length: {:.3f} bits/symbol\n'.format(avg_code_length))
    f.write('Entropy: {:.3f} bits/symbol\n'.format(entropy))
    f.write('Efficiency: {:.3f}\n'.format(efficiency))
print()
print('Average Code Length: {:.3f} bits/symbol'.format(avg_code_length))
print('Entropy: {:.3f} bits/symbol'.format(entropy))
print('Efficiency: {:.3f}'.format(efficiency))








