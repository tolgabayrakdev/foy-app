from ..model import db, Student
from ..exceptions import AppException
from sqlalchemy.exc import SQLAlchemyError


class StudentService:
    @staticmethod
    def get_all_students(user_id):
        """
        Tüm öğrencileri getirir.
        """
        return Student.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_student_by_id(student_id):
        """
        ID ile bir öğrenciyi getirir.
        """
        student = Student.query.get(student_id)
        if not student:
            raise AppException("Öğrenci bulunamadı.")
        return student

    @staticmethod
    def create_student(data):
        """
        Yeni bir öğrenci oluşturur.
        Transaction kullanılarak kaydedilir.
        """
        try:
            new_student = Student(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                phone_number=data.get("phone_number"),
                email=data.get("email"),
                date_of_birth=data.get("date_of_birth"),
                gender=data.get("gender"),
                grade=data.get("grade"),
                parent_name=data.get("parent_name"),
                parent_contact=data.get("parent_contact"),
                special_conditions=data.get("special_conditions"),
                notes=data.get("notes"),
            )
            # Transaction başlangıcı
            with db.session.begin_nested():
                db.session.add(new_student)
                db.session.commit()
            return new_student
        except SQLAlchemyError as e:
            db.session.rollback()  # Hata durumunda geri al
            raise AppException(f"Öğrenci oluşturulamadı: {str(e)}", 500)

    @staticmethod
    def update_student(student_id, data):
        """
        Var olan bir öğrenciyi günceller.
        Transaction kullanılarak kaydedilir.
        """
        try:
            student = StudentService.get_student_by_id(student_id)
            for key, value in data.items():
                if hasattr(student, key):
                    setattr(student, key, value)

            # Transaction başlangıcı
            with db.session.begin_nested():
                db.session.commit()
            return student
        except SQLAlchemyError as e:
            db.session.rollback()  # Hata durumunda geri al
            raise AppException(f"Öğrenci güncellenemedi: {str(e)}", 500)

    @staticmethod
    def delete_student(student_id):
        """
        Bir öğrenciyi siler.
        """
        student = StudentService.get_student_by_id(student_id)
        db.session.delete(student)
        db.session.commit()
