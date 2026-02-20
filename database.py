from pymongo import MongoClient

MONGO_URL = "mongodb+srv://kumarpiyush7121_db_user:kumarpiyush7121_db_user@cluster0.4vpheqq.mongodb.net/"

client = MongoClient(MONGO_URL)

db = client["job_portal_db"]

companies_collection = db["companies"]
jobs_collection = db["jobs"]
applications_collection = db["applications"]