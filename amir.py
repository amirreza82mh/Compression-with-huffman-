def huffman(string):

    alphabet_frequancy = {}    
    alphabets = []

    alphabet_frequancy = CountWord(string, alphabet_frequancy)
    alphabets = listAlphabet(string) 

    #bulid heap
    for i in range(len(alphabets)//2-1, -1, -1):
        min_heap(alphabets, alphabet_frequancy, len(alphabets), i)
    
    while(len(alphabets)-1 > 0):
        left = pop_element(alphabets, alphabet_frequancy)
        right = pop_element(alphabets, alphabet_frequancy)
        node = Node(None, left, right)
        alphabet_frequancy[node] = alphabet_frequancy[left] + alphabet_frequancy[right]
        del(alphabet_frequancy[left], alphabet_frequancy[right])
        alphabets.append(node)
        up_heaify(alphabets, alphabet_frequancy, len(alphabets) - 1 )

    #assigned code 
    codes = {}

    def assign_code(node, code):
        if type(node) is str:
            codes[node] = code
        else:
            assign_code(node.left, code + '0')
            assign_code(node.right, code + '1')

    root = alphabets.pop()
    assign_code(root, "")

    #encode string
    encode = ''.join(codes[c] for c in string)




def up_heaify(alphabet, dictionary, i):
    index_parent = (i - 1) // 2
    child = alphabet[i]
    parent = alphabet[index_parent]


    # Check if the element is at the root or in its correct position
    if i == 0 or dictionary[child] <= dictionary[parent]:
        return

    # Swap the element with its parent
    alphabet[i], alphabet[index_parent] = alphabet[index_parent], alphabet[i]

    # Perform heapify_up recursively on the parent
    up_heaify(alphabet, dictionary, index_parent)

def min_heap(alphabet, dictionary, lenght, i):        #Min heapSort  O(nlogn)
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
        min_heap(heap, dictionary, len(heap), 0)

    return popped_element


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

class Node:
    def __init__(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

string = 'در این راستا'
huffman(string)