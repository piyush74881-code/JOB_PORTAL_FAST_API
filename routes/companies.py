from fastapi import APIRouter
from database import companies_collection

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/")
def create_company(name: str, location: str, industry: str):
    company = {
        "name": name,
        "location": location,
        "industry": industry
    }

    result = companies_collection.insert_one(company)

    return {
        "message": "Company created",
        "id": str(result.inserted_id)
    }


@router.get("/")
def get_companies():
    companies = list(companies_collection.find({}, {"_id": 0}))
    return companies