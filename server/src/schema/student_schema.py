from marshmallow import Schema, fields, validate
from datetime import datetime


class StudentCreateSchema(Schema):
    first_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=2, max=50, error="First name must be between 2 and 50 characters"
        ),
    )
    last_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=2, max=50, error="Last name must be between 2 and 50 characters"
        ),
    )
    phone_number = fields.Str(
        required=True,
        validate=validate.Regexp(
            r"^\+?[0-9]{10,15}$", error="Phone number must be between 10 and 15 digits"
        ),
    )
    email = fields.Str(
        required=True,
        validate=[
            validate.Length(
                min=6, max=100, error="Email must be between 6 and 100 characters"
            ),
            validate.Regexp(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                error="Invalid email format",
            ),
        ],
    )
    date_of_birth = fields.Date(required=True, error="Date of birth is required")
    gender = fields.Str(
        required=True,
        validate=validate.OneOf(
            ["male", "female", "other"],
            error="Gender must be 'male', 'female', or 'other'",
        ),
    )
    grade = fields.Str(
        required=True,
        validate=validate.Length(
            min=1, max=10, error="Grade must be between 1 and 10 characters"
        ),
    )
    parent_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=2, max=100, error="Parent name must be between 2 and 100 characters"
        ),
    )
    parent_contact = fields.Str(
        required=True,
        validate=validate.Regexp(
            r"^\+?[0-9]{10,15}$",
            error="Parent contact number must be between 10 and 15 digits",
        ),
    )
    special_conditions = fields.Str(
        required=False,  # Optional field
        validate=validate.Length(
            max=500, error="Special conditions must be under 500 characters"
        ),
    )
    notes = fields.Str(
        required=False,  # Optional field
        validate=validate.Length(max=160, error="Notes must be under 160 characters"),
    )


class StudentUpdateSchema(Schema):
    first_name = fields.Str(
        required=False,
        validate=validate.Length(
            min=2, max=50, error="First name must be between 2 and 50 characters"
        ),
    )
    last_name = fields.Str(
        required=False,
        validate=validate.Length(
            min=2, max=50, error="Last name must be between 2 and 50 characters"
        ),
    )
    phone_number = fields.Str(
        required=False,
        validate=validate.Regexp(
            r"^\+?[0-9]{10,15}$", error="Phone number must be between 10 and 15 digits"
        ),
    )
    email = fields.Str(
        required=True,
        validate=[
            validate.Length(
                min=6, max=100, error="Email must be between 6 and 100 characters"
            ),
            validate.Regexp(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                error="Invalid email format",
            ),
        ],
    )
    date_of_birth = fields.Date(required=False, error="Date of birth is required")
    gender = fields.Str(
        required=False,
        validate=validate.OneOf(
            ["male", "female", "other"],
            error="Gender must be 'male', 'female', or 'other'",
        ),
    )
    grade = fields.Str(
        required=False,
        validate=validate.Length(
            min=1, max=10, error="Grade must be between 1 and 10 characters"
        ),
    )
    parent_name = fields.Str(
        required=False,
        validate=validate.Length(
            min=2, max=100, error="Parent name must be between 2 and 100 characters"
        ),
    )
    parent_contact = fields.Str(
        required=False,
        validate=validate.Regexp(
            r"^\+?[0-9]{10,15}$",
            error="Parent contact number must be between 10 and 15 digits",
        ),
    )
    special_conditions = fields.Str(
        required=False,
        validate=validate.Length(
            max=500, error="Special conditions must be under 500 characters"
        ),
    )
    notes = fields.Str(
        required=False,
        validate=validate.Length(max=160, error="Notes must be under 160 characters"),
    )
