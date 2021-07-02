import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')

mydb = myclient["test"] # select the database
mycol = mydb["testcol"] # select the collection

# Function to insert single document
def insert_single():
   # create a dummy document
    mydict = { "name": "Herbert", "address": "Highway 37" }

    # write the document to the collection
    x = mycol.insert_one(mydict)

    # this is the id field of the new document
    print(x.inserted_id) 

# insert single document
# insert_single()


# Function to insert multiple documents at once
def insert_multiple():
   # create a dummy document
    mylist = []

    mylist.append({ "name": "Andreas", "address": "Appartement 45" })
    mylist.append({ "name": "Manuela", "address": "Appartement 45" })

    # write the document to the collection
    x = mycol.insert_many(mylist)

    # this is the id field of the new document
    print(x.inserted_ids) 

insert_multiple()