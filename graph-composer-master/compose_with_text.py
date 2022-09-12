"""
Empty Compose Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import os
import re
import string
import random

from graph_text import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def make_graph(words):
    g = Graph()
    previous_word = None
    
    for word in words:
        word_vertex = g.get_vertex(word)
    
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex
    
    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    
    return composition

def main():
    """Create new text using Markov Chain Graph """
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition)


if __name__ == '__main__':
    print(main())