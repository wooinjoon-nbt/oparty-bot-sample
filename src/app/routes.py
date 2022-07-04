from src.app.controllers.ao_deploy_controller import show_modal_select_service, append_modal_select_deploy_vars
from src.app.controllers.sample_controller import SampleController


def register_routes_and_controllers(app):
    sample_controller = SampleController()
    app.message("hello")(sample_controller.message_hello)
    app.action("wow/button_click")(sample_controller.action_button_click)

    app.command("/ao_deploy")(show_modal_select_service)
    app.action("action_target_service_select")(append_modal_select_deploy_vars)


def init(app):
    print("bot init start~!")
    register_routes_and_controllers(app)
