from marshmallow import Schema, fields, validate
import re

# Email regex pattern (basit bir email doğrulaması)
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


class UserRegistrationSchema(Schema):
    first_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(
        required=True,
        validate=[
            validate.Length(min=6, max=100),  # Email uzunluğu kontrolü
            validate.Regexp(
                EMAIL_REGEX, error="Invalid email format"
            ),  # Regex kontrolü
        ],
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(
            min=6, error="Password must be at least 6 characters"
        ),  # Minimum 6 karakter
    )


class LoginSchema(Schema):
    email = fields.Email(
        required=True,
        validate=[
            validate.Length(min=6, max=100),  # Email uzunluğu kontrolü
            validate.Regexp(
                EMAIL_REGEX, error="Invalid email format"
            ),  # Regex kontrolü
        ],
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(
            min=6, error="Password must be at least 6 characters"
        ),  # Minimum 6 karakter
    )
