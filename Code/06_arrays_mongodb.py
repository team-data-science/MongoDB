import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')

mydb = myclient["test"] # select the database
mycol = mydb["testcol"] # select the collection

# Look into: https://docs.mongodb.com/manual/reference/operator/update-array/


# Function to insert multiple documents with sub documents at once
def insert_array():
   # create a dummy document

    myquery = { "name": "Sebastian", "address": "Appartement 45", "garage": [{"car" : "Audi", "model":"A4"},{"car" : "BMW", "model":"3 Series"} ]}


    # write the document to the collection
    x = mycol.insert_one(myquery)

    # this is the id field of the new document
    print(x.inserted_id) 

insert_array()

def query_subdocument():
    # find these documents where the car1 in garage is an Audi
    myquery = {"garage.car": "Audi"}
    mydoc = mycol.find( myquery)

    #print out doucument
    for x in mydoc:
        print(x)

query_subdocument()

def add_object_to_array():
    myquery =  {"name": "Sebastian"}
    newcar = { "$push": {"garage": {"car" : "Porsche", "model":"Cayman"}} }

    x = mycol.update_one(myquery,newcar)

    print( x.matched_count , "updated")

    for x in mycol.find():
        print(x) 

add_object_to_array()