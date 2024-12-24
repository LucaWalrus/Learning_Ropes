# Write your solution here
def find_movies(database: list, search_term: str):
    # Convert the search term to lowercase to make the search case-insensitive
    search_term = search_term.lower()
    
    # Create a new list to hold the movies that match the search term
    matching_movies = []
    
    # Loop through each movie in the database
    for movie in database:
        # Convert the movie name to lowercase and check if the search term is in the name
        if search_term in movie["name"].lower():
            matching_movies.append(movie)
    
    # Return the list of matching movies
    return matching_movies
