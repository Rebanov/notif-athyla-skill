from mycroft import MycroftSkill, intent_file_handler


class NotifAthyla(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('athyla.notif.intent')
    def handle_athyla_notif(self, message):
        self.speak_dialog('athyla.notif')


def create_skill():
    return NotifAthyla()

