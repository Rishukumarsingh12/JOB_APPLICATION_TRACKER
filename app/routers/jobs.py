from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_db, get_current_user


router = APIRouter(prefix="/jobs", tags=["Jobs"])


# Create Job
@router.post("/")
def create_job(job: schemas.JobCreate,
               db: Session = Depends(get_db),
               current_user: models.User = Depends(get_current_user)):

    new_job = models.Job(
        company=job.company,
        role=job.role,
        status=job.status,
        notes=job.notes,
        user_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


# Get all jobs of current user
@router.get("/")
def get_jobs(db: Session = Depends(get_db),
             current_user: models.User = Depends(get_current_user)):

    jobs = db.query(models.Job).filter(
        models.Job.user_id == current_user.id
    ).all()

    return jobs


# Update job status
@router.put("/{job_id}")
def update_job(job_id: int,
               job: schemas.JobCreate,
               db: Session = Depends(get_db),
               current_user: models.User = Depends(get_current_user)):

    db_job = db.query(models.Job).filter(
        models.Job.id == job_id,
        models.Job.user_id == current_user.id
    ).first()

    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")

    db_job.company = job.company
    db_job.role = job.role
    db_job.status = job.status
    db_job.notes = job.notes

    db.commit()
    db.refresh(db_job)

    return db_job


# Delete job
@router.delete("/{job_id}")
def delete_job(job_id: int,
               db: Session = Depends(get_db),
               current_user: models.User = Depends(get_current_user)):

    db_job = db.query(models.Job).filter(
        models.Job.id == job_id,
        models.Job.user_id == current_user.id
    ).first()

    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")

    db.delete(db_job)
    db.commit()

    return {"message": "Job deleted successfully"}