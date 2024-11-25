import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy
from typing import List

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    password: Mapped[str]

    goals: Mapped[List["Goal"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    rewards: Mapped[List["Reward"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Goal(db.Model):
    __tablename__ = "goals"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    category: Mapped[str]  # Örneğin, Finansal, Sağlık, Kişisel vb.
    start_date: Mapped[str]
    end_date: Mapped[str]
    priority_level: Mapped[int] = mapped_column(default=1)  # 1: Low, 2: Medium, 3: High
    completion_percentage: Mapped[int] = mapped_column(default=0)  # Hedefin tamamlanma oranı
    status: Mapped[str]  # Durum: 'In Progress', 'Completed', 'Failed' vb.
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

    user: Mapped["User"] = relationship(back_populates="goals")
    milestones: Mapped[List["Milestone"]] = relationship(
        back_populates="goal", cascade="all, delete-orphan"
    )
    reminders: Mapped[List["Reminder"]] = relationship(
        back_populates="goal", cascade="all, delete-orphan"
    )
    rewards: Mapped[List["Reward"]] = relationship(
        back_populates="goal", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "priority_level": self.priority_level,
            "completion_percentage": self.completion_percentage,
            "status": self.status,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

class Milestone(db.Model):
    __tablename__ = "milestones"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    due_date: Mapped[datetime.datetime]
    status: Mapped[str]  # Durum: 'Not Started', 'In Progress', 'Completed'
    completion_percentage: Mapped[int] = mapped_column(default=0)
    goal_id: Mapped[int] = mapped_column(ForeignKey("goals.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

    goal: Mapped["Goal"] = relationship(back_populates="milestones")
    progress: Mapped[List["Progress"]] = relationship(
        back_populates="milestone", cascade="all, delete-orphan"
    )
    reminders: Mapped[List["Reminder"]] = relationship(
        back_populates="milestone", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "completion_percentage": self.completion_percentage,
            "goal_id": self.goal_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Progress(db.Model):
    __tablename__ = "progress"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    completion_percentage: Mapped[int]  # Kilometre taşının tamamlanma oranı
    progress_date: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    milestone_id: Mapped[int] = mapped_column(ForeignKey("milestones.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

    milestone: Mapped["Milestone"] = relationship(back_populates="progress")

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completion_percentage": self.completion_percentage,
            "progress_date": self.progress_date,
            "milestone_id": self.milestone_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Reminder(db.Model):
    __tablename__ = "reminders"

    id: Mapped[int] = mapped_column(primary_key=True)
    reminder_time: Mapped[datetime.datetime]  # Hatırlatıcı zamanı
    message: Mapped[str]  # Hatırlatıcı mesajı
    goal_id: Mapped[int] = mapped_column(ForeignKey("goals.id"))
    milestone_id: Mapped[int] = mapped_column(ForeignKey("milestones.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

    goal: Mapped["Goal"] = relationship(back_populates="reminders")
    milestone: Mapped["Milestone"] = relationship(back_populates="reminders")


    def to_dict(self):
        return {
            "id": self.id,
            "reminder_time": self.reminder_time,
            "message": self.message,
            "goal_id": self.goal_id,
            "milestone_id": self.milestone_id,
            "created_at": self.created_at
        }


class Reward(db.Model):
    __tablename__ = "rewards"

    id: Mapped[int] = mapped_column(primary_key=True)
    reward_name: Mapped[str]
    reward_description: Mapped[str]
    goal_id: Mapped[int] = mapped_column(ForeignKey("goals.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    achieved_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())

    goal: Mapped["Goal"] = relationship(back_populates="rewards")
    user: Mapped["User"] = relationship(back_populates="rewards")

    def to_dict(self):
        return {
            "id": self.id,
            "reward_name": self.reward_name,
            "reward_description": self.reward_description,
            "goal_id": self.goal_id,
            "user_id": self.user_id,
            "achieved_at": self.achieved_at
        }