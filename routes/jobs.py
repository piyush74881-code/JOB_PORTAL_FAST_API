from fastapi import APIRouter
from database import jobs_collection

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/")
def create_job(title: str, salary: int, location: str, role: str, company_id: str):
    job = {
        "title": title,
        "salary": salary,
        "location": location,
        "role": role,
        "company_id": company_id
    }

    result = jobs_collection.insert_one(job)

    return {
        "message": "Job created",
        "id": str(result.inserted_id)
    }


@router.get("/")
def get_jobs(location: str = None, role: str = None, salary: int = None):
    query = {}

    if location:
        query["location"] = location

    if role:
        query["role"] = role

    if salary:
        query["salary"] = {"$gte": salary}

    jobs = list(jobs_collection.find(query, {"_id": 0}))
    return jobs