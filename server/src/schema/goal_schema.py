from marshmallow import Schema, fields, validates, ValidationError


class CreateGoalSchema(Schema):
    title = fields.String(
        required=True,
        validate=lambda x: 3 <= len(x) <= 50,
        error_messages={
            "required": "Title is required",
            "validator_failed": "Title must be between 3 and 50 characters",
        },
    )
    description = fields.String(
        required=True,
        error_messages={
            "required": "Description is required",
            "invalid": "Invalid description format",
        },
    )
    category = fields.String(
        required=True, error_messages={"required": "Category is required"}
    )
    start_date = fields.Date(
        required=True, error_messages={"required": "Start date is required"}
    )
    end_date = fields.Date(
        required=True, error_messages={"required": "End date is required"}
    )

