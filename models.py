from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum

# --- ENUMS ---
class ComplaintStatus(str, enum.Enum):
    pending = "pending"
    assigned = "assigned"
    in_progress = "in_progress"
    resolved = "resolved"

class EmployeeStatus(str, enum.Enum):
    free = "free"
    busy = "busy"

# --- EMPLOYEE TABLE ---
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)   # system ID
    login_id = Column(String, unique=True, index=True)   # unique login ID for login
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    status = Column(Enum(EmployeeStatus), default=EmployeeStatus.free)
    password = Column(String, nullable=True)             # optional login password

    # one-to-many relationship
    complaints = relationship("Complaint", back_populates="employee")


# --- COMPLAINT TABLE ---
class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    description = Column(String)
    name = Column(String)   # citizen name
    location = Column(String)
    status = Column(Enum(ComplaintStatus), default=ComplaintStatus.pending, nullable=False)
    photo_path = Column(String, nullable=True)

    # foreign key to employee
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    employee = relationship("Employee", back_populates="complaints")


