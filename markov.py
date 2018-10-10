"""Generate Markov text from text files."""

from random import choice
import string 
import sys 


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

	
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """


    # open the file with the with block 
    with open(file_path) as file:
    	
        # method .read() treat the file as one long string  
    	return file.read().strip()

# n give the oppurtunity to add the number of n-gram 
def make_chains(text_string, n):

    # create list of words 
    words = text_string.split()

    # append a None to the end of the word list to handle stopping 
    words.append(None)
    
    chains = {}

    # create the tuple of keys , range(len(words)-n >> so it does not 
    # loop to the end 
    for i in range(len(words)-n):
        word1 = words[i]
        word2 = words[i + n]
        key = (word1, word2,)
        value = words[i + n]


        # initiate the chain keys with an empty list 
        if key not in chains:
            chains[key] = []

        chains[key].append(value)


    #print keys and values in seprate lines using items 
    # for key, value in chains.items():
    #     print(key, value)

    return chains


def make_text(chains):
    """Return text from chains."""
    # picking a random key from our dic, and pull each word out of dic.key()
    
    # to check if the value ends in punctuation.
    punct = ([".","?","!"])


    # put the keys in a list to have the choice operate on it
    keys = list(chains.keys())

    # create a random key from list of keys 
    random_key = choice(keys)
    
    # check if the first item if the key is title 
    while not random_key[0].title():
        random_key = choice(keys)

    # create a list with 2 random keys 
    text = [random_key[0], random_key[1]]

    # create a random word from the list of values 
    random_word = choice(list(chains[random_key]))

    # make a loop to keep adding new word from value list to new set of keys 
    while random_word is not None:
      
        random_key = (random_key[1],random_word)
        text.append(random_word)

        if random_word[-1] in punct:
            break 
        random_word = choice(keys)


    return " ".join(text)


input_path = sys.argv[1]
input_n = int(sys.argv[2])

# Open the file and turn it into one long string
# enter the sys.argv[1] as the input path 
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,input_n)

# Produce random text
random_text = make_text(chains)

print(random_text)
