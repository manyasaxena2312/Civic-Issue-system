# seed.py
from database import SessionLocal, engine, Base
from models import Employee, EmployeeStatus

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Add employees with login_id (unique username for login)
employees = [
    {"login_id": "emp001", "name": "Shikhar", "department": "Electricity"},
    {"login_id": "emp002", "name": "Yash", "department": "Water"},
    {"login_id": "emp003", "name": "Lakshit", "department": "Transport"},
    {"login_id": "emp004", "name": "Shubham", "department": "Cleanliness"},
    {"login_id": "emp005", "name": "Ayush", "department": "Cleanliness"},
    {"login_id": "emp006", "name": "Shashwat", "department": "Electricity"},
    {"login_id": "emp007", "name": "Dibyansh", "department": "Water"},
    {"login_id": "emp008", "name": "Aditya", "department": "Transport"},
    {"login_id": "emp009", "name": "Akshat", "department": "Cleanliness"},
]

for e in employees:
    # Check if employee already exists (avoid duplicates)
    existing = db.query(Employee).filter_by(login_id=e["login_id"]).first()
    if not existing:
        emp = Employee(
            login_id=e["login_id"],
            name=e["name"],
            department=e["department"],
            status=EmployeeStatus.free
        )
        db.add(emp)

db.commit()
db.close()
print("✅ Employees seeded successfully (no duplicates, with login IDs)")


