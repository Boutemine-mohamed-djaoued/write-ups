from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

register_docs = swagger_auto_schema(
    method='post',
    operation_description="Register a new user.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description="Username of the user", example="djawad99"),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description="Password of the user", example="hello123"),
        },
        required=['username', 'password']
    ),
    responses={
        200: openapi.Response(
            description="User registered successfully",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "username": openapi.Schema(type=openapi.TYPE_STRING, example="djawad"),
                }
            )
        ),
        400: openapi.Response(
            description="Invalid input",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "username": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING, example="This field is required.")),
                    "password": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING, example="This field is required.")),
                }
            )
        )
    }
)

login_docs = swagger_auto_schema(
    method='post',
    operation_description="Authenticate a user and return an access token.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description="Username of the user", example="djawad"),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description="Password of the user", example="hello123"),
        },
        required=['username', 'password']
    ),
    responses={
        200: openapi.Response(
            description="Login successful",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING, example="Login successful"),
                    "user": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                            "username": openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    )
                }
            )
        ),
        400: openapi.Response(
            description="Invalid input",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        401: openapi.Response(
            description="Invalid credentials",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        )
    }
)

logout_docs = swagger_auto_schema(
    method='post',
    operation_description="Logout the user by deleting the access token cookie.",
    responses={
        200: openapi.Response(
            description="Logout successful",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING, example="Logout successful")
                }
            )
        ),
        401: openapi.Response(
            description="Unauthorized",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING, example="Authentication credentials were not provided.")
                }
            )
        )
    }
)

