"""Import all routers and add them to routers_list."""
from .admin import admin_router
from .echo import echo_router
from .user import user_router
from .other_handlers import router

routers_list = [
    admin_router,
    user_router,
    router,
    echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]
