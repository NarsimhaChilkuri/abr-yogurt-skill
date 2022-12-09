from mycroft import MycroftSkill, intent_file_handler


class AbrYogurt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('yogurt.abr.intent')
    def handle_yogurt_abr(self, message):
        self.speak_dialog('yogurt.abr')


def create_skill():
    return AbrYogurt()

