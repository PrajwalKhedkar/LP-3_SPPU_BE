import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    # Step 1: Calculate frequency of each character
    freq = Counter(data)

    # Step 2: Create a priority queue (min-heap) of nodes
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    # Step 3: Build Huffman tree by combining nodes with lowest frequency
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Return the root of the Huffman tree
    return heap[0]

def build_huffman_codes(node, code, huffman_codes):
    if node:
        if node.char is not None:
            huffman_codes[node.char] = code
        build_huffman_codes(node.left, code + '0', huffman_codes)
        build_huffman_codes(node.right, code + '1', huffman_codes)

def huffman_encoding(data):
    if len(data) == 0:
        return "", None
    
    # Step 1: Build Huffman tree
    root = build_huffman_tree(data)
    
    # Step 2: Build Huffman codes from Huffman tree
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)
    
    # Step 3: Encode the input data using Huffman codes
    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if len(encoded_data) == 0:
        return ""
    
    decoded_data = []
    current = root
    
    # Step 1: Traverse the Huffman tree to decode the encoded data
    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        
        if current.char is not None:
            decoded_data.append(current.char)
            current = root  # Reset to root for next character
    
    return ''.join(decoded_data)

# Example usage:
if __name__ == "__main__":
    data =input('Enter your string:\n')
    
    # Encoding
    encoded_data, tree = huffman_encoding(data)
    print("Encoded data:", encoded_data)
    
    # Decoding
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded data:", decoded_data)
