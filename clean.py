
from database import SessionLocal
from models import Employee

db = SessionLocal()

# Fetch unique (name, department) combinations
seen = set()
for emp in db.query(Employee).order_by(Employee.id).all():
    key = (emp.name, emp.department)
    if key in seen:
        db.delete(emp)  # delete duplicates
    else:
        seen.add(key)

db.commit()
db.close()

print("✅ Duplicate employees removed")
