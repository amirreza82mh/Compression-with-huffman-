def huffman(string):
    alphabet_frequancy = {}     #make an empty dictionary for word and teir frequancy
    alphabets = []
    alphabet_frequancy = CountWord(string, alphabet_frequancy)
    alphabets = listAlphabet(string) 
    lenght_of_alphabets = len(alphabets)
    # lenght_of_frequancy = len(alphabet_frequancy)
    for i in range(lenght_of_alphabets//2-1, -1, -1):
        min_heap(alphabets, alphabet_frequancy, lenght_of_alphabets, i)
    
    while(len(alphabets)-1):
        left = alphabets.pop(0)
        right = alphabets.pop(0)
        frequancy = alphabet_frequancy[left] + alphabet_frequancy[right]
        del(alphabet_frequancy[left], alphabet_frequancy[right])
        node = Node(None, left, right)
        alphabet_frequancy[node] = frequancy
        alphabets.append(node)
        for i in range(len(alphabets)//2-1, -1, -1):
            min_heap(alphabets, alphabet_frequancy, len(alphabets),i)

    codes = {}
    root = alphabets.pop()
    assigned_code(root, '')

    def assigned_code(node, code):
        if node.char is not None:
            codes[node.char] = code
        else:
            assigned_code(node.left, code + '0')
            assigned_code(node.right, code + '1')

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
    def init(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

string = 'در این راستا'
huffman(string)



