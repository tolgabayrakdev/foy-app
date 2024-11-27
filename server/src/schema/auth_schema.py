from marshmallow import Schema, fields, validates, ValidationError
import re


class UserRegistrationSchema(Schema):
    username = fields.String(
        required=True,
        error_messages={'required': 'Username is required'}
    )
    email = fields.String(
        required=True,
        error_messages={'required': 'Email is required'}
    )
    password = fields.String(
        required=True,
        error_messages={
            'required': 'Password is required',
        }
    )

    @validates('username')
    def validate_username(self, value):
        if not (3 <= len(value) <= 15):
            raise ValidationError("Username must be between 3 and 15 characters")

    @validates('email')
    def validate_email(self, value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValidationError("Invalid email format")

    @validates('password')
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters")


class LoginSchema(Schema):
    email = fields.String(
        required=True,
        error_messages={'required': 'Email is required'}
    )
    password = fields.String(
        required=True,
        error_messages={'required': 'Password is required'}
    )

    @validates('email')
    def validate_email(self, value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValidationError("Invalid email format")
