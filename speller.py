# Speller: Loading dictionary
class Node:
    def __init__(self, word=None):
        self.val = word
        self.next = None
        
def hash_word(word):
    """Takes in a word and returns its hash table index."""
    return ord(word[0])-97
       
def insert_word(idx, word):
    """Takes in a word and inserts it into the hash table using input index."""
    node = table[idx]
    new_node = Node(word)
    while node.next:
        node = node.next
    node.next = new_node

def load(file):
    """Loads the file into the hash table."""
    file = open(file,"r")
    for wrd in file:               # Each line has single word
        word = wrd.strip('\n')
        idx = hash_word(word)
        insert_word(idx, word)
    print('File loaded successfully.')
    
def size(table):
    """Retunrs size of the dictionary"""
    count = 0
    for i in range(26):
        node = table[i]
        while node.next:
            node = node.next
            count += 1
    return count-26

def check(file):
    """Checks given text for misspelling and return them & their count."""
    misspelled = []
    for word in file:
        idx = hash_word(word)
        node = table[idx]
        node = node.next
        flag = 1
        while node.next:
            if node.val == word:
                flag = 0
                break
            node = node.next
        if flag == 1:
            misspelled.append(word)
    return misspelled        
        
# Initialising the hash table
table = []
for i in range(26):
    table.append(Node(chr(i+97)))
# print(table)

load("large")
# print(table[0].val)

print(f"The dictionary has {size(table)} words.")

text = open("aca.txt","r")
print(f"The text has {check(text)} misspelled words.")

# check function: if a fn is in dict or not; case insensitive; 
# unload: free up the memory