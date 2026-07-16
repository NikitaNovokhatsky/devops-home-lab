from flask import Blueprint

from services.system_service import SystemService

system_bp = Blueprint(
    "system",
    __name__
)


@system_bp.route("/system")
def system():

    return SystemService.get_system_info()