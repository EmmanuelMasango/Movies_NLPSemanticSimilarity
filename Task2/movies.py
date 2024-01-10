# ============= Importing Libraries ==============
import spacy

# Load the spaCy English language model
nlp_model = spacy.load('en_core_web_md')

# =====Reading in text file===========
movies_data = {}  # Create a dictionary to store movie data

# Read the movies.txt file
with open('movies.txt', 'r') as movies_file:
    for line in movies_file:
        # Split each line into movie title and description
        movie_title, description = line.strip('\n').split(" :")
        movies_data[movie_title] = description

# Define a dictionary for the movie just watched
just_watched_movies = {'Planet Hulk': '''Will he save their world or destroy it? When the Hulk becomes too dangerous for
 the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in 
 peace.Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''}


def watch_next(description):
    """
    Find the most similar movie to the given description.

    Parameters:
    - description (str): The description of the movie just watched.

    Returns:
    - str: The title of the most similar movie.
    """
    desc_doc = nlp_model(description)

    highest_similarity = 0
    most_similar_movie = ''

    # Iterate through the movies to find the most similar one
    for movieTitle, movieDescription in movies_data.items():
        movie_desc_doc = nlp_model(movieDescription)
        similarity = desc_doc.similarity(movie_desc_doc)

        # Update the most similar movie if the current one has higher similarity
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_movie = movieTitle

    return most_similar_movie


# Retrieve the description of the movie just watched
just_watched_description = just_watched_movies['Planet Hulk']

# Find the most similar movie
most_similar_movie_title = watch_next(just_watched_description)

# Print the result
print(f"The most similar film to 'Planet Hulk' is '{most_similar_movie_title}'.")
