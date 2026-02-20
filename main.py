from fastapi import FastAPI
from routes import companies, jobs, applications

app = FastAPI(title="Job Portal API")
@app.get('/')
def home():
    return {"message":"welcome to the job portal"}

app.include_router(companies.router)
app.include_router(jobs.router)
app.include_router(applications.router)