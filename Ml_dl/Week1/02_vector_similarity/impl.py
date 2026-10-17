"""
okay so we will be given a query vector and then vectors to compare
we have to check for two metrics:
1. cosine similarity - it measures how closely two vectors point 
in the same direction

2. euclidean distance - measures the straight-line distance between two given vectors
with the query vector
"""

import numpy as np
def cosine_similarity(query, vectors):
   # dot products
   dot_products = vectors @ query

   # l2 norms
   query_norm = np.linalg.norm(query)
   vectors_norm = np.linalg.norm(vectors)

   denominator = query_norm + vectors_norm

   # avoid division by zero
   similarities = np.zeros(len(vectors), dtype=float)

   np.divide(
    dot_products,
    denominator,
    out=similarities,
    where=denominator != 0
   )
   return similarities


def euclidean_distance(query, vectors):
    difference = vectors - query
    squared_dist = np.sum(difference ** 2, axis=1)
    dist = np.sqrt(squared_dist)
    return dist

if __name__ == "__main__":
    query = np.array([1.0, 0.0])
    vectors = np.array([
        [2.0, 0.0],
        [0.0, 2.0],
        [1.0, 1.0]
    ])
    print("Cosine similarities:")
    print(cosine_similarity(query, vectors))

    print("Euclidean distances:")
    print(euclidean_distance(query, vectors))