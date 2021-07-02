import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')

mydb = myclient["test"] # select the database
mycol = mydb["testcol"] # select the collection

# Look into: https://docs.mongodb.com/manual/reference/operator/update-field/

# Function to insert multiple documents with sub documents at once
def insert_multiple():
   # create a dummy document
    mylist = []

    mylist.append({ "name": "Andreas", "address": "Appartement 45", "garage": {"car1" : "Audi", "car2":"BMW"} })
    mylist.append({ "name": "Manuely", "address": "Appartement 45", "garage": {"car1" : "BMW", "car2":"VW"} })

    # write the document to the collection
    x = mycol.insert_many(mylist)

    # this is the id field of the new document
    print(x.inserted_ids) 

insert_multiple()

def query_sub_document():
    # find these documents where the car1 in garage is an Audi
    myquery = {"garage.car1": "Audi"}
    mydoc = mycol.find( myquery)

    # return only specific parts of the document
    #myreturnonly = { "_id": 0, "name": 1}
    #mydoc = mycol.find( myquery, myreturnonly )

    #print out doucument
    for x in mydoc:
        print(x)

query_sub_document()


# add a car to a garage attributes of a document
def update_sub_document():
    myquery = { "name": "Andreas", "address": "Appartement 45"}
    newvalues = { "$set": { "garage.car3": "Porsche" } }

    x = mycol.update_one(myquery, newvalues)   

    for x in mycol.find():
        print(x) 

update_sub_document()