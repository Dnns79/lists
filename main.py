# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
movies = ['The Poseidon Adventure', 'Cinderella Liberty', 'The River', 'The Accidental Tourist', 'Fahrenheit', 'The Seventh One']
movies.sort()

def alphabetical_order(movies):
        return movies.sort()
print(movies)

won_globe = ('Jaws', 'Star Wars: Episode IV – A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha')
won_globe = [each_string.lower() for each_string in won_globe]

def won_golden_globe(movie):
    if movie in won_globe:
        return True
    else:
        return False
print (won_golden_globe('jaws'))


toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', '35th Anniversary – Live in Poland',
    'Toto XIV', 'Old Is New', 'Tours Around the Sun - Live in Holland']

def remove_toto_albums(movies):
    if toto_albums[0] in movies:
        movies.remove(toto_albums[0]) 
    if toto_albums[1] in movies:
        movies.remove(toto_albums[1])
    if toto_albums[2] in movies:
        movies.remove(toto_albums[2])
    if toto_albums[3] in movies:
        movies.remove(toto_albums[3])
    if toto_albums[4] in movies:
        movies.remove(toto_albums[4])
    if toto_albums[5] in movies:
        movies.remove(toto_albums[5])
   


