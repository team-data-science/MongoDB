import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')

mydb = myclient["test"] # select the database
mycol = mydb["testcol"] # select the collection

# add more attributes to a document
def add_more_to_document():
    myquery = { "address": "Huettenmeister 8" }
    newvalues = { "$set": { "newcol": "Canyon 123" } }

    x = mycol.update_one(myquery, newvalues)   

    for x in mycol.find(myquery):
        print(x) 

#add_more_to_document()


# change attributes of a document
def update_document():
    myquery = { "newcol": "Canyon 123" }
    newvalues = { "$set": { "newcol": "Reset 123" } }

    x = mycol.update_one(myquery, newvalues)   

    for x in mycol.find():
        print(x) 

update_document()