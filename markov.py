"""Generate Markov text from text files."""

from random import choice
import string 


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

	w
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as file:
    	
    	return file.read().strip()


def make_chains(text_string):


    words = text_string.split()
    words.append(None)
    
    chains = {}

    for i in range(len(words)-2):
        word1 = words[i]
        word2 = words[i + 1]
        key = (word1, word2,)
        value = words[i + 2]



        if key not in chains:
            chains[key] = []

        chains[key].append(value)
    #print(chains)
    # print keys and values in seprate lines 
    # for key, value in chains.items():
    #     print(key, value)
    return chains


def make_text(chains):
    """Return text from chains."""
    # picking a random key from our dic, and pull each word out of dic.key()
    random_key = choice(list(chains.keys()))
    #print(random_key)

    # create a list with 2 random keys 
    text = [random_key[0], random_key[1]]

    # create a random word from the list of values 
    random_word = choice(chains[random_key])


   

    # make a loop to keep adding new word from value list to new set of keys 
    while random_word is not None: 
        random_key = (random_key[1],random_word)
        text.append(random_word)

        random_word = choice(chains[random_key])



    return " ".join(text)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
