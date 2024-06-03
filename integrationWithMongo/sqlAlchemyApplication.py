import datetime
import pymongo as pyM

client = pyM.MongoClient('mongodb+srv://renanfrancadev:password@cluster0.5pjzvgg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.pymongo
collection = db.DIO

print(db.list_collections)

post = {
    "name":"renan",
    "email":"renan@email.com",
    "cpf":12345678900,
    "number":"001",
    "type":"corrente",
    "date": datetime.datetime.now(datetime.UTC)
}

# Infos submit
posts = db.post
post_id = posts.insert_one(post).inserted_id
print(post_id)