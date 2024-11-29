from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey, DateTime, Text
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(15))
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[str] = mapped_column(default="teacher")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "role": self.role,
        }


class Student(db.Model):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
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
    program: Mapped["Program"] = relationship(
        "Program", back_populates="student", uselist=False
    )  # Birebir ilişki

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

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"), nullable=False, unique=True
    )
    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )  # Örneğin, özel ders programı adı
    description: Mapped[str] = mapped_column(Text, nullable=True)  # Programın detayları
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=True)
    progress: Mapped[float] = mapped_column(default=0.0)  # İlerleme yüzdesi
    status: Mapped[str] = mapped_column(
        default="active"
    )  # Program durumu (Aktif, Tamamlandı, İptal)
    notes: Mapped[str] = mapped_column(Text)  # Öğretmen notları veya özel bilgiler

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
