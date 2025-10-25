from database import SessionLocal, engine
import models
from sqlalchemy import text

db = SessionLocal()

# Delete all complaints
db.query(models.Complaint).delete()

# Reset complaint ID sequence
with engine.connect() as conn:
    conn.execute(text("ALTER SEQUENCE complaints_id_seq RESTART WITH 1;"))
    conn.commit()

# Reset employees
for emp in db.query(models.Employee).all():
    emp.status = models.EmployeeStatus.free

db.commit()
db.close()
print("✅ Complaints cleared, IDs reset, employees set to free")
