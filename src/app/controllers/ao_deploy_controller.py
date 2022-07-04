# command /ao_deploy
from src.app.views.ao_deploy_alert.deploy_vars_input_modal_view import DeployVarsInputModalView


def show_modal_select_service(ack, body, client, logger):
    print("show_modal")
    print(client)
    client.views_open(
        trigger_id=body["trigger_id"],
        view=DeployVarsInputModalView().select_service_view()
    )
    ack()

def append_modal_select_deploy_vars(ack, body, client, logger):
    print("append_modal")
    selected_service = body["actions"][0]["selected_option"]["value"]
    print(f"selected service is {selected_service}")
    client.views_update(
        view_id=body["view"]["id"],
        view=DeployVarsInputModalView().select_deploy_vars_view(selected_service)
    )
    ack()
