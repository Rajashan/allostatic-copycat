import spacy
import networkx as nx

# Load English model in Spacy
nlp = spacy.load("en_core_web_sm")

# Sample sentence
sentence = "The cat chased the mouse"

# Parse sentence using Spacy
doc = nlp(sentence)

# Create a graph and add nodes for each word
graph = nx.Graph()
for token in doc:
    graph.add_node(token.text, pos=token.pos_)

# Add edges based on gestalt principles
for i, token1 in enumerate(doc):
    for j, token2 in enumerate(doc):
        # Use proximity to connect nearby words
        if abs(i - j) <= 1:
            graph.add_edge(token1.text, token2.text)
        # Use similarity to connect words with similar parts-of-speech
        elif token1.pos_ == token2.pos_:
            graph.add_edge(token1.text, token2.text)
        # Use closure to group words that form coherent phrases
        elif (i+1 == j) and (token1.pos_ == "DET") and (token2.pos_ in ["NOUN", "PROPN", "PRON"]):
            graph.add_edge(token1.text, token2.text)

# Print graph
print(graph.nodes())
print(graph.edges())
