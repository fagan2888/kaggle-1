from numpy import *
from random import shuffle

def random_vector(vector_length):
    """
    Returns a vector with 1's and -1's randomly distributed throughout the vector.
    Input must be a multiple of 100.
    """
    if vector_length % 100 != 0:
        raise Exception('vector_length must be a multiple of 100')
    nonzero_count = vector_length * 0.02
    zero_count = vector_length - nonzero_count
    z = zeros(zero_count)
    positives = ones(nonzero_count/2)
    negs = ones(nonzero_count/2)
    merged = array(list(z) + list(positives) + list(negs))
    shuffle(merged)
    return merged

def empty_vectors(words, vector_length):
    """
    Takes a list of words and an integer as input.
    Returns a dict with each word as a key and the
    value a numpy array of zeros, equal to the length of the vector_length parameter.
    """
    words = set(words) # unique them
    dict = {}
    for w in words:
        dict[w] = zeros(vector_length)
    return dict

def word_vectors(corpus, vector_length):
    """
    Takes a list of words and an integer as input.
    """
    count = 0
    empty = empty_vectors(corpus, vector_length)
    for word in corpus:
        if count % 10 == 0:
            context_vector = random_vector(vector_length)
        empty[word] += context_vector
        count += 1
    return empty

def cosine(v1,v2):
    return float(dot(v1,v2) / (linalg.norm(v1) * linalg.norm(v2)))

if __name__ == "__main__":
    words = ['hey', 'hi', 'bye']
    print word_vectors(words, 100)
