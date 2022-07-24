import pymongo
from appConfig import CONFIG
import mongoSchema
# declare global variables
def dbConnect():
    client = pymongo.MongoClient(CONFIG['database']['url'])
    db = client[CONFIG['database']['name']]
    return db

def dbDisconnect(db):
    db.client.close()
    return True

# CRUD Methods
# create issuer pymongo in certisign database
def createIssuer(db, issuer):
    # validate issuer schema
    # if not validateIssuerSchema(issuer):
    #     return False
    # insert issuer into database

    try:
        db.issuers.insert_one(issuer)
        return True
    except Exception as e:
        print(e)
        return False

def validateSchema(schema, data):
    # validate schema
    # check every key in data is in schema.properties
    # check every key in data is of type in schema.properties
    # check every key in data is not empty
    for key in data:
        print (key)
        print (type(data[key]))
        print (data[key])
        
        if key not in schema['properties']:
            return False
        if schema['properties'][key]['type'] != type(data[key]):
            return False
        if data[key] == '':
            return False            
    return True

testIssuer={
    "name": "Test Issuer",
    "description": "Test Issuer Description",
    "issuer_id": "Test Issuer ID",
    "issuer_type": "Test Issuer Type",
}

print("\n",validateSchema(mongoSchema.ISSUER_SCHEMA, testIssuer))