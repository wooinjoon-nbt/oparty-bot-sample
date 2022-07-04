from src.app.utils.view_builder.actions.check_boxes import CheckBoxes
from src.app.utils.view_builder.divider import Divider
from src.app.utils.view_builder.modal_view import ModalView
from src.app.utils.view_builder.blocks.section import Section
from src.app.utils.view_builder.actions.static_select import StaticSelect


class DeployVarsInputModalView:
    def __init__(self):
        pass

    def select_service_view(self):
        return ModalView(callback_id="modal_deploy_alert",
                  title="배포 알림 도우미",
                  submit="Submit",
                  blocks=[
                      Section(id="target_service_select",
                              text="배포를 진행할 서비스를 선택해주세요",
                              action=StaticSelect(id="target_service_select",
                                                  placeholder="서버를 선택하세요",
                                                  options=self.__target_services()))
                  ]).render()


    def select_deploy_vars_view(self, selected_service):
        return ModalView(callback_id="modal_deploy_alert",
                         title="배포 알림 도우미",
                         submit="Submit",
                         blocks=[
                             Section(id="target_service_select",
                                     text="배포를 진행할 서비스를 선택해주세요",
                                     action=StaticSelect(id="target_service_select",
                                                         placeholder="서버를 선택하세요",
                                                         options=self.__target_services())),
                             Divider(),
                             Section(id="target_env_select",
                                     text="배포를 진행할 환경을 선택해주세요",
                                     action=CheckBoxes(id="checkbox_action",
                                                       options=self.__target_envs(selected_service)))
                         ]).render()


    # def select_deploy_vars_view(self, selected_service):
        # return ModalView(callback_id="modal_deploy_alert",
        #           title="배포 알림 도우미",
        #           submit="Submit",
        #           blocks=[
        #               Section(id="target_service_select",
        #                       text="배포를 진행할 서비스를 선택해주세요",
        #                       action=Action(id="target_service_select",
        #                              StaticSelect(placeholder="서버를 선택하세요",
        #                                           options=self.__target_services()))),
        #               Divider(),
        #               Section(id="target_env_select",
        #                       text="배포를 진행할 환경을 선택해주세요",
        #                       action=Action(id="target_env_select",
        #                              CheckBoxes(id="checkbox_action",
        #                                         option=self.__target_envs(selected_service))),
        #               Section(id="target_server_select",
        #                       text="배포를 진행할 서버를 선택해주세요",
        #                       action=Action(id="target_server_select",
        #                              CheckBoxes(id="checkbox_action",
        #                                         option=self.__target_servers(selected_service))),
        #               Input(id="deploy_branch_select",
        #                     action=Action(StaticSelect(placeholder="서버를 선택하세요",
        #                                  options=self.__target_branches(selected_service))),
        #               Input(id="deploy_desc_input",
        #                     action=Action(PlainTextInput(placeholder="배포 설명을 입력해주세요",
        #                                           optional=True)))
        #           ])
        # ]).render()

        # return {
        #     "type": "modal",
        #     "callback_id": "modal_deploy_alert",
        #     "title": {"type": "plain_text", "text": "배포 알림 도우미"},
        #     "submit": {"type": "plain_text", "text": "Submit"},
        #     "blocks": [
        #         {
        #             "type": "section",
        #             "text": {"type": "mrkdwn", "text": "배포를 진행할 서버를 선택해주세요"},
        #             "block_id": "block_target_service_select",
        #             "accessory": {
        #                 "action_id": "action_target_service_select",
        #                 "type": "static_select",
        #                 "placeholder": {
        #                     "type": "plain_text",
        #                     "text": "서버를 선택하세요",
        #                 },
        #                 "options": [
        #                     {
        #                         "text": {
        #                             "type": "plain_text",
        #                             "text": "[AO] AdiSON Offerwall",
        #                         },
        #                         "value": "ao"
        #                     },
        #                     {
        #                         "text": {
        #                             "type": "plain_text",
        #                             "text": "[AP] AdiSON Points",
        #                         },
        #                         "value": "ap"
        #                     },
        #                     {
        #                         "text": {
        #                             "type": "plain_text",
        #                             "text": "[DSP] AdiSON DSP",
        #                         },
        #                         "value": "dsp"
        #                     },
        #                     {
        #                         "text": {
        #                             "type": "plain_text",
        #                             "text": "[Event] AdiSON Event",
        #                         },
        #                         "value": "event"
        #                     }
        #                 ]
        #             }
        #         },
        #         {"type": "divider"},
        #         {
        #             "block_id": "env_checkbox",
        #             "type": "section",
        #             "text": {
        #                 "type": "mrkdwn",
        #                 "text": "배포할 환경을 선택해주세요"
        #             },
        #             "accessory": {
        #                 "type": "checkboxes",
        #                 "options": [
        #                     {
        #                         "text": {
        #                             "type": "mrkdwn",
        #                             "text": "Sandbox"
        #                         },
        #                         "value": "sandbox"
        #                     },
        #                     {
        #                         "text": {
        #                             "type": "mrkdwn",
        #                             "text": "Stage"
        #                         },
        #                         "value": "stage"
        #                     },
        #                     {
        #                         "text": {
        #                             "type": "mrkdwn",
        #                             "text": "Production"
        #                         },
        #                         "value": "production"
        #                     }
        #                 ],
        #                 "action_id": "checkbox_action"
        #             }
        #         },
        #         {
        #             "block_id": "server_type_checkbox",
        #             "type": "section",
        #             "text": {
        #                 "type": "mrkdwn",
        #                 "text": "배포할 서버를 선택해주세요"
        #             },
        #             "accessory": {
        #                 "type": "checkboxes",
        #                 "options": [
        #                     {
        #                         "text": {
        #                             "type": "plain_text",
        #                             "text": f"[DSP] AdiSON DSP{selected_service}"
        #                         },
        #                         "value": "dsp"
        #                     }
        #                 ],
        #                 "action_id": "checkbox_action"
        #             }
        #         },
        #         {
        #
        #             "block_id": "deploy_branch_select",
        #             "dispatch_action": True,
        #             "type": "input",
        #             "element": {
        #                 "type": "static_select",
        #                 "placeholder": {
        #                     "type": "plain_text",
        #                     "text": "브랜치를 선택",
        #                 },
        #                 "options": [
        #                     {
        #                         "text": {
        #                             "type": "plain_text",
        #                             "text": "[DSP] AdiSON DSP"
        #                         },
        #                         "value": "dsp"
        #                     }
        #                 ],
        #                 "action_id": "deploy_branch_select_action"
        #             },
        #             "label": {
        #                 "type": "plain_text",
        #                 "text": "배포 대상 브랜치를 선택해주세요",
        #             }
        #         },
        #         {
        #             "block_id": "deploy_desc_input",
        #             "type": "input",
        #             "element": {
        #                 "type": "plain_text_input",
        #                 "action_id": "text_input_action"
        #             },
        #             "label": {
        #                 "type": "plain_text",
        #                 "text": "배포 내용을 입력해주세요",
        #             },
        #             "optional": True
        #         }
        #     ]
        # }

    def __target_services(self):
        return [
            {
                "text": {
                    "type": "plain_text",
                    "text": "[AO] AdiSON Offerwall",
                },
                "value": "ao"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": "[AP] AdiSON Points",
                },
                "value": "ap"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": "[DSP] AdiSON DSP",
                },
                "value": "dsp"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": "[Event] AdiSON Event",
                },
                "value": "event"
            }
        ]

    def __target_envs(self, selected_service):
        env_dict = {
            "ao": [
                    {
                        "text": {
                            "type": "mrkdwn",
                            "text": "Sandbox"
                        },
                        "value": "sandbox"
                    },
                        {
                            "text": {
                               "type": "mrkdwn",
                               "text": "Stage"
                           },
                           "value": "stage"
                       },
                       {
                           "text": {
                               "type": "mrkdwn",
                               "text": "Production"
                           },
                           "value": "production"
                       }
            ]
        }

        return env_dict[selected_service]
