class AppException(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code




'''

@app.errorhandler(Exception)
def handle_global_error(error):
    if isinstance(error, SQLAlchemyError):
        return {"message": "Veritabanı hatası meydana geldi."}, 500
    elif isinstance(error, AppException):
        return {"message": str(error)}, 400
    return {"message": "Bilinmeyen bir hata oluştu."}, 500

'''