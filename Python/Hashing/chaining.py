'''
Hashing
- A data structure which allows insert, remove and lookup in O(1)

Basic applications:
- Indexing in database
- Cryptography
- Symbol Tables in Compiler/Interpreter
- Dictionaries, caches, etc.

Hash function: map key in key-value pair to a range of m smaller values
, where m is the size of the hash table. The new keys are in range 0 and m - 1.

Efficiency quantified by load factor:
    lf = n/m
    n = Total # keys to be inserted into hash table
    m = Size of hash table

    O(1 + lf) for insert, delete and search

Avoid collisions using:

1. Chaining: stored values with the same hashed key in a linked list.

'''

def display_hash(Hashtable):
    for i in range(len(Hashtable)):
        print(i, end=" ")

        for j in Hashtable[i]:
            print('-->', end=" ")
            print(j, end=" ")
            
        print()

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

def Hashing(keyvalue):
    # Hash function
    return keyvalue % len(Hashtable)

if __name__ == '__main__':

    # Create a hash table as a nested list
    Hashtable = [[] for _ in range(10)]
    insert(Hashtable, 10, 'Jack')
    insert(Hashtable, 20, 'Amy')
    insert(Hashtable, 32, 'Ivan')
    display_hash(Hashtable)