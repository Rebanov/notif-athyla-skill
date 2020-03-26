from mycroft import MycroftSkill, intent_file_handler
from mycroft import intent_handler
from mycroft_bus_client import MessageBusClient, Message
from adapt.intent import IntentBuilder
from flask import Flask, escape, request

notif = Flask(__name__)

from notif import routes

class NotifAthyla(MycroftSkill):

    client = MessageBusClient()

    def __init__(self):
        MycroftSkill.__init__(self)

    def result(self, message):
        messsageEntrant = request.form['data']
        self.speak_dialog('Test : {}'.format(message.data.get('notifWeb')))

    client.on('speak', result)

#    @intent_handler(IntentBuilder('athyla.notif.intent').require("messageBus"))
#    def handle_athyla_notif_intent(self, message):
#        self.speak_dialog('Nouvelle notification reçu : {}'.format(newNotif))



def create_skill():
    return NotifAthyla()

