from pymongo import MongoClient

# Kreiranje instance za MongoDBClient() kako bih se povezala sa serverom
client = MongoClient()

# Pristup bazi podataka my_database
db = client.movies_collection

# Unos dokumenata koje cu kasnije prikazati
movie_name = input("Enter movie name: ")
movie_genre = input("Enter movie genre: ")
movie_year = input("Enter movie year: ")

# Kreiranje kolekcije movies
movies = db.movies

# Ubacivanje dokumenta koje je korisnik uneo u recnik
movie = {
    'movie_name': movie_name,
    'movie_genre': movie_genre,
    'movie_year': movie_year
}

# Ubacivanje dokumenta u kolekciju movies
movies.insert_one(movie)

# Dobavljanje dokumenata iz kolekcije
result = movies.find()

# Prikaz svih dokumenata pomocu for petlje
print("All movies in the collection:")

for r in result:
    print("Movie name: {} | Movie genre: {} | Movie year: {}".format(r['movie_name'], r['movie_genre'], r['movie_year']))
