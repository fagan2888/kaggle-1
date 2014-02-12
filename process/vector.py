import numpy
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
    z = numpy.zeros(zero_count)
    positives = numpy.ones(nonzero_count/2)
    negs = numpy.ones(nonzero_count/2) * -1
    merged = numpy.array(list(z) + list(positives) + list(negs))
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
        dict[w] = numpy.zeros(vector_length)
    return dict

def word_vectors(corpus, vector_length):
    """
    Takes a list of words and an integer as input.
    """
    words = {}
    for word in corpus:
        words[word] = random_vector(vector_length)
    return words

def cosine(v1,v2):
    return float(numpy.dot(v1,v2) / (numpy.linalg.norm(v1) * numpy.linalg.norm(v2)))

class VectorSpace:

    def __init__(self, unique_words, vector_length=100):
        self.vectors = word_vectors(unique_words, vector_length)
        self.vector_length = vector_length 

    def vector(self, document):
        """
        Takes a list of words as input.
        Returns the vector sum of each of those words.
        """
        document_vector = numpy.zeros(self.vector_length)
        for word in document:
            if word in self.vectors:
                document_vector += self.vectors[word]
            else:
                print Warning("'{0}' not in self.vectors".format(word))
        return document_vector

if __name__ == "__main__":
    words = ['hey', 'hi', 'bye']
    vs = VectorSpace(words)
    print vs.vector(['hey', 'hey', 'bye', 'x'])
