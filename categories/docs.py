from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

category_list_docs = swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of categories.",
    responses={
        200: openapi.Response(description="List of categories retrieved successfully")
    }
)

category_create_docs = swagger_auto_schema(
    method='post',
    operation_description="Create a new category (admin only).",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, example="Technology")
        },
        required=["name"]
    ),
    responses={
        201: openapi.Response(description="Category created successfully"),
        403: openapi.Response(description="Unauthorized"),
        400: openapi.Response(description="Validation error")
    }
)

category_delete_docs = swagger_auto_schema(
    method='delete',
    operation_description="Delete a category (admin only).",
    responses={
        204: openapi.Response(description="Category deleted successfully"),
        403: openapi.Response(description="Unauthorized"),
        404: openapi.Response(description="Category not found")
    }
)