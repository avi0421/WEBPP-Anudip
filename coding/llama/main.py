import os

# write a function to add two numbers
def sum(a, b): return a + b

print("The result is", sum(5, 6))

# connect to mongodb using pymongo
def connect_mongodb(): 
    from pymongo import MongoClient # create connection with mongo db client = MC('localhost', 27027) MongoClient as MC # create connection with mongo db client = MC('localhost', 27017) return client.db("llama")
    client = MongoClient() # connect to mongodb using pymongo def sum(a, b): return a + b print("The result is", sum(5, 6))
