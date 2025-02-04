from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

blog_list_docs = swagger_auto_schema(
    method='get',
    operation_description="Retrieve a list of blogs, optionally filtered by category or user.",
    manual_parameters=[
        openapi.Parameter('categoryId', openapi.IN_QUERY, description="Filter blogs by category ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('userId', openapi.IN_QUERY, description="Filter blogs by user ID", type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: openapi.Response(
            description="List of blogs retrieved successfully",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                        "title": openapi.Schema(type=openapi.TYPE_STRING),
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "content": openapi.Schema(type=openapi.TYPE_OBJECT),
                        "user": openapi.Schema(type=openapi.TYPE_INTEGER)
                    }
                )
            )
        )
    }
)

blog_create_docs = swagger_auto_schema(
    method='post',
    operation_description="Create a new blog (admin only).",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, example="My Blog Title"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, example="A short description"),
            "content": openapi.Schema(type=openapi.TYPE_OBJECT, example={"text": "This is my blog content"}),
            "categories": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_INTEGER))
        },
        required=["title", "content"]
    ),
    responses={
        201: openapi.Response(description="Blog created successfully"),
        403: openapi.Response(description="Unauthorized - only admins can create blogs"),
        400: openapi.Response(description="Validation error")
    }
)

blog_detail_docs = swagger_auto_schema(
    method='get',
    operation_description="Retrieve details of a specific blog.",
    responses={
        200: openapi.Response(description="Blog details retrieved successfully"),
        404: openapi.Response(description="Blog not found")
    }
)

blog_update_docs = swagger_auto_schema(
    method='put',
    operation_description="Update a specific blog (admin only).",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING),
            "description": openapi.Schema(type=openapi.TYPE_STRING),
            "content": openapi.Schema(type=openapi.TYPE_OBJECT),
            "categories": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_INTEGER))
        }
    ),
    responses={
        200: openapi.Response(description="Blog updated successfully"),
        403: openapi.Response(description="Unauthorized"),
        400: openapi.Response(description="Validation error")
    }
)

blog_delete_docs = swagger_auto_schema(
    method='delete',
    operation_description="Delete a specific blog (admin only).",
    responses={
        204: openapi.Response(description="Blog deleted successfully"),
        403: openapi.Response(description="Unauthorized"),
        404: openapi.Response(description="Blog not found")
    }
)

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