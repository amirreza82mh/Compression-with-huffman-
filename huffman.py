def huffman(string):

    alphabet_frequancy = {}         
    alphabets = []

    alphabet_frequancy = CountWord(string, alphabet_frequancy)
    alphabets = listAlphabet(string) 

    #bulid heap array  O(nlogn)
    for i in range(len(alphabets)//2-1, -1, -1):
        min_heap(alphabets, alphabet_frequancy, len(alphabets), i)
    
    while(len(alphabets)-1 > 0):
        left = pop_element(alphabets, alphabet_frequancy)
        right = pop_element(alphabets, alphabet_frequancy)
        result = alphabet_frequancy[left] + alphabet_frequancy[right]  # find frequancy of root 
        if type(left) is str:
            left = Node(left, None, None)    # make a node for char
        if type(right) is str:
            right = Node(right, None, None) 
        node = Node(None, left, right)   # make a node for char
        alphabet_frequancy[node] = result
        alphabets.append(node)   # add node to array 
        down_to_up_heaify(alphabets, alphabet_frequancy, len(alphabets) - 1 )   # heapify array after append

    #assigned code 
    codes = {}

    def assign_code(node, code):
        if node.char is not None:  
            codes[node.char] = code  # assigned code for each char   
        else:
            assign_code(node.left, code + '0')
            assign_code(node.right, code + '1')

    root = alphabets.pop()
    assign_code(root, "")

    #encode string
    encode = ''.join(codes[c] for c in string)

    return encode, codes, alphabet_frequancy, root 

def CountWord(string, alphabet_frequancy):      # make a dictionary of alphabet with teir frequancy    O(n)
    for i in string:
        alphabet_frequancy[i] = alphabet_frequancy.get(i, 0) + 1    
    return alphabet_frequancy

def listAlphabet(string):    #make an string of alphabet O(n)
    List = []
    for i in string:
        if i in List:
            continue
        else:
            List.append(i)
    return List

def min_heap(alphabet, dictionary, lenght, i):        #build min heap  O(logn)
    minium = alphabet[i]
    l = 2 * i + 1
    r = 2 * i + 2
    if l < lenght:
        leftchild = alphabet[l]
    if r < lenght:
        rigthchild = alphabet[r]

    if l < lenght and dictionary[minium] > dictionary[leftchild]:
        minium = leftchild

    if r < lenght and dictionary[minium] > dictionary[rigthchild]:
        minium = rigthchild

    if minium != alphabet[i]:
        indexOfMin = alphabet.index(minium)
        alphabet[i], alphabet[indexOfMin] = alphabet[indexOfMin], alphabet[i]  # swap
        min_heap(alphabet,dictionary, lenght, alphabet.index(minium))

def pop_element(heap, dictionary):
    if len(heap) == 0:
        return None

    # Remove the root element
    popped_element = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    if len(heap) != 0:
        # Reconstruct the heap
        up_to_down_heapify(heap, dictionary, 0)

    return popped_element

def up_to_down_heapify(heap, dictionary, i):   # heapify array from up to down
    maxium = heap[i]
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(heap):
        leftchild = heap[l]
    if r < len(heap):
        rigthchild = heap[r]
    
    if l < len(heap) and dictionary[maxium] > dictionary[leftchild]:
        maxium = leftchild

    if r < len(heap) and dictionary[maxium] > dictionary[rigthchild]:
        maxium = rigthchild
    
    if maxium != heap[i]:
        indexOfMax = heap.index(maxium)
        heap[i], heap[indexOfMax] = heap[indexOfMax], heap[i]   # swawp 
        up_to_down_heapify(heap, dictionary, indexOfMax)


def down_to_up_heaify(alphabet, dictionary, i):  # heapify array from down to up
    index_parent = (i - 1) // 2
    child = alphabet[i]
    parent = alphabet[index_parent]


    # Check if the element is at the root or in its correct position
    if i == 0 or dictionary[child] >= dictionary[parent]:
        return

    # Swap the element with its parent
    alphabet[i], alphabet[index_parent] = alphabet[index_parent], alphabet[i]

    # Perform heapify_up recursively on the parent
    down_to_up_heaify(alphabet, dictionary, index_parent)

def huffman_decoding(encoded, root):

    decoded = ""
    node = root
    for bit in encoded:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decoded += node.char
            node = root
    return decoded

class Node:
    def __init__(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right