from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey, Text, UUID
from datetime import datetime
import uuid
import enum

db = SQLAlchemy()


class RoleStatus(enum.Enum):
    teacher = "teacher"
    student = "student"


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, nullable=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[RoleStatus] = mapped_column(default=RoleStatus.teacher)

    students: Mapped[list["Student"]] = relationship(
        "Student", back_populates="user", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
        }


class Student(db.Model):
    __tablename__ = "students"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    date_of_birth: Mapped[datetime] = mapped_column()
    gender: Mapped[str] = mapped_column(String(10))
    grade: Mapped[str] = mapped_column(String(10))
    parent_name: Mapped[str] = mapped_column(String(100))
    parent_contact: Mapped[str] = mapped_column(String(15))
    status: Mapped[str] = mapped_column(default="active")
    special_conditions: Mapped[str] = mapped_column(Text)
    notes: Mapped[str] = mapped_column(String(160))

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )  # Öğrencinin bağlı olduğu öğretmeni belirtir
    user: Mapped["User"] = relationship("User", back_populates="students")

    program: Mapped["Program"] = relationship(
        "Program", back_populates="student", cascade="all, delete-orphan"
    )  # Öğrencinin programı

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "grade": self.grade,
            "parent_name": self.parent_name,
            "parent_contact": self.parent_contact,
            "status": self.status,
            "special_conditions": self.special_conditions,
            "notes": self.notes,
        }


class Program(db.Model):
    __tablename__ = "programs"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"), nullable=False
    )  # Programın bağlı olduğu öğrenci
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=True)
    progress: Mapped[float] = mapped_column(default=0.0)
    status: Mapped[str] = mapped_column(default="active")
    notes: Mapped[str] = mapped_column(Text)

    student: Mapped["Student"] = relationship("Student", back_populates="program")

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "progress": self.progress,
            "status": self.status,
            "notes": self.notes,
        }
