import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')
mydb = myclient["test"]
mycol = mydb["testcol"]

# find these documents where the address equals Highway 37
myquery = {"address": "Appartement 45"}
mydoc = mycol.find( myquery )

# return only specific parts of the document
#myreturnonly = { "_id": 0, "name": 1}
#mydoc = mycol.find( myquery, myreturnonly )

#print out doucument
for x in mydoc:
  print(x)

# how to sort the data that you will retrieve
# find order ASC .sort("name") or .sort("name", 1)
# find order DSC .sort("name",-1)  