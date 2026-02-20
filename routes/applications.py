from fastapi import APIRouter, UploadFile, File, Form
import shutil
from database import applications_collection

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("/")
def apply_job(
    job_id: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    resume: UploadFile = File(...)
):
    file_path = f"uploads/{resume.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    application = {
        "job_id": job_id,
        "name": name,
        "email": email,
        "resume": file_path
    }

    applications_collection.insert_one(application)

    return {"message": "Application submitted successfully"}


@router.get("/")
def get_applications():
    return list(applications_collection.find({}, {"_id": 0}))