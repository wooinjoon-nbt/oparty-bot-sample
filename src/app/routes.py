from src.app.reactors.sample_reactor import SampleReactor


def register_reactors(app):
    sample_reactor = SampleReactor()
    app.message("hello")(sample_reactor.message_hello)
    app.action("wow/button_click")(sample_reactor.action_button_click)


def init(app):
    print("bot init start~!")
    register_reactors(app)
