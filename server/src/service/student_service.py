from marshmallow import ValidationError
from ..schema.student_schema import StudentCreateSchema, StudentUpdateSchema
from ..model import db, Student
from ..exceptions import AppException
from sqlalchemy.exc import SQLAlchemyError

create_schema = StudentCreateSchema()
update_schema = StudentUpdateSchema()


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
            data = create_schema.load(data)

            # Dinamik olarak 'Student' modelinin alanlarıyla eşleşen veriyi al
            student_data = {
                key: data.get(key) for key in data if key in Student.__table__.columns
            }
            new_student = Student(**student_data)

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

            validated_data = update_schema.load(data)

            # Güncellenebilir alanları dinamik olarak atıyoruz
            for key, value in validated_data.items():
                if hasattr(student, key):  # Eğer öğrenci modelinde böyle bir alan varsa
                    setattr(student, key, value)  # Alanı güncelle

            with db.session.begin_nested():
                db.session.commit()

            return student
        except ValidationError as e:
            raise AppException(e.messages, 400)
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
