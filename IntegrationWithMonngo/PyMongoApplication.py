import datetime
import pprint
from pymongo import *

client = MongoClient('localhost', 27017)

db = client.test
colletion = db.test_collection
print(colletion)

# Definição de informação para compor o documento
post = {
    "author" : "Manuel",
    "text" : "Minha primeira aplicação de MongoDB baseado em Python",
    "tags" : ["mongodb", "python3", "pymongo"],
    "date" : datetime.datetime.utcnow()
}

# Preparando para submeter as informações
posts = db.posts
# post_id = posts.insert_one(post).inserted_id

# pprint.pprint(posts.find_one())

# Bulk inserts 

new_posts = [{
        "author" : "John",
        "text" : "Another post",
        "tags" : ["bulk", "post", "insert"],
        "date" : datetime.datetime.utcnow()
    },
    {
        "author" : "Michael",
        "text" : "Another text",
        "title" : "Mongo is fun.",
        "data" : datetime.datetime.utcnow()        
    }]

# result = posts.insert_many(new_posts)

# Printa todos os documentos do banco
for post in posts.find():
    # pprint.pprint(post)
    pass

# Printa quantas documentos tem no banco
print(posts.count_documents({}))

# Printa quantas documentos tem no banco como o nome do autor = Manuel
print(posts.count_documents({"author" : "Manuel"}))

# Printa qunatas documentos tem no banco, ordenando pelo nome do autor
for post in posts.find({}).sort("author"):
    # pprint.pprint(post)
    pass

result = db.profiles.create_index([("author", ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {"user_id" : 211, "name" : "João"},
    {"user_id" : 212, "name" : "Jorge"}
]

# result = db.profiles_user.insert_many(user_profile_user)

#Coleções armazenadas no MongoDB
print(db.list_collection_names())

# Removendo uma coleção
# db['profiles'].drop()

#Deletando um documento com o nome do autor = Manuel
print(posts.delete_one({"author" : "Manuel"}))

# Deletando um banco de dados
client.drop_database("test")
