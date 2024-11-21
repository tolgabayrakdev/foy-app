from marshmallow import Schema, fields, validates, ValidationError
import re

class UserRegistrationSchema(Schema):
    username = fields.String(
        required=True,
        validate=lambda x: 3 <= len(x) <= 15,
        error_messages={
            'required': 'Username is required',
            'validator_failed': 'Username must be between 3 and 15 characters'
        }
    )
    email = fields.String(
        required=True,
        error_messages={
            'required': 'Email is required',
            'invalid': 'Invalid email format'
        }
    )
    password = fields.String(
        required=True,
        validate=lambda x: len(x) >= 8,
        error_messages={
            'required': 'Password is required',
            'validator_failed': 'Password must be at least 8 characters'
        }
    )

    @validates('email')
    def validate_email(self, value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value.lower()):
            raise ValidationError("Invalid email format")

    @validates('username')
    def validate_username(self, value):
        if len(value) < 3 or len(value) > 15:
            raise ValidationError("Username must be between 3 and 15 characters")

class LoginSchema(Schema):
    email = fields.String(
        required=True,
        error_messages={
            'required': 'Email is required',
            'invalid': 'Invalid email format'
        }
    )
    password = fields.String(
        required=True,
        error_messages={
            'required': 'Password is required'
        }
    )

    @validates('email')
    def validate_email(self, value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value.lower()):
            raise ValidationError("Invalid email format")
