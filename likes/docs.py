from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


like_unlike_docs = swagger_auto_schema(
    method='post',
    operation_description="Like or unlike a blog. If the blog is already liked, this will remove the like.",
    # request_body=openapi.Schema(
    #     type=openapi.TYPE_OBJECT,
    #     properties={
    #         "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the blog to like/unlike", example=5),
    #     },
    #     required=["id"]
    # ),
    responses={
        201: openapi.Response(
            description="Liked the blog",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "response": openapi.Schema(type=openapi.TYPE_STRING, example="Liked the blog"),
                }
            )
        ),
        200: openapi.Response(
            description="Unliked the blog",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "response": openapi.Schema(type=openapi.TYPE_STRING, example="Unliked the blog"),
                }
            )
        ),
        404: openapi.Response(
            description="Blog not found",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING, example="Blog not found"),
                }
            )
        )
    }
)


get_likes_docs = swagger_auto_schema(
    method='get',
    operation_description="Retrieve all likes in the system.",
    responses={
        200: openapi.Response(
            description="List of all likes",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                        "user": openapi.Schema(type=openapi.TYPE_STRING, example="djawad99"),
                        "blog": openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                    }
                )
            )
        )
    }
)


get_likes_by_user_docs = swagger_auto_schema(
    method='get',
    operation_description="Retrieve all likes by a specific user.",
    responses={
        200: openapi.Response(
            description="List of likes by the user",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                        "user": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),  
                        "blog": openapi.Schema(type=openapi.TYPE_INTEGER, example=5),  
                    }
                )
            )
        ),
        404: openapi.Response(
            description="User not found or has no likes",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING, example="The user doesn't exist or has never liked a blog"),
                }
            )
        )
    }
)

get_likes_by_blog_docs = swagger_auto_schema(
    method='get',
    operation_description="Retrieve all likes for a specific blog.",
    responses={
        200: openapi.Response(
            description="List of likes for the blog",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=3),
                        "user": openapi.Schema(type=openapi.TYPE_INTEGER, example=2),  
                        "blog": openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                    }
                )
            )
        ),
        404: openapi.Response(
            description="Blog not found or has no likes",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING, example="The blog doesn't exist or has no likes"),
                }
            )
        )
    }
)