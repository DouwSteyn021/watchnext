import spacy
import numpy as np

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm1 * norm2)
    return similarity

def suggest_movie(description):
    # Load the spaCy language model
    nlp = spacy.load("en_core_web_md")

    # Read movie descriptions from the file
    with open('/Users/douwsteyn/Watch_next/movies.txt', 'r') as file:
        movie_descriptions = file.read().splitlines()

    # Create word vector for the input description
    input_vector = nlp(description).vector

    # Calculate similarity scores between the input description and other movie descriptions
    similarity_scores = []
    for movie_description in movie_descriptions:
        movie_vector = nlp(movie_description).vector
        similarity_score = cosine_similarity(input_vector, movie_vector)
        similarity_scores.append(similarity_score)

    # Get the index of the movie with the highest similarity score
    most_similar_index = similarity_scores.index(max(similarity_scores))

    # Read movie titles from the file
    with open('/Users/douwsteyn/Watch_next/movies.txt', 'r') as file:
        movie_titles = file.read().splitlines()

    # Return the title of the most similar movie
    most_similar_title = movie_titles[most_similar_index]

    return most_similar_title

# Example usage
watched_description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately,
Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''
most_similar_movie = suggest_movie(watched_description)
print("You may enjoy watching:", most_similar_movie)
