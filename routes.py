from mycroft_bus_client import MessageBusClient, Message
from flask import Flask, request
from notif import notif
import json


@notif.route('/')
@notif.route('/notifAthyla', methods=['POST'])

def notifAthyla():
    entryData = request.args.get('data')
    client = MessageBusClient()
    client.run_in_thread()

    if request.method == "POST":
       notification = "Nouvelle notification : {}".format(entryData)
       client.emit(Message('speak', data={'utterance': notification}))

       notifsave = {"titre": "{}".format(entryData),}
       notifplain= "titre: {}".format(entryData)
       print(notifsave)
       print(notifplain)
       #json_string = json.dumps(['notification', {'titre': '{}'.format(entryData)}])
       #json_dict = json.loads(json_string)
       #print(json_string)
       with open("~/notif_save.json", 'a+', encoding='utf-8') as json_file:
         json.dump(notifsave, json_file, indent=4)

       #test = open("~/notif_save.txt", 'a+')
       #test.write(notifplain)
       #test.close()

       return "sending message : {}".format(entryData)
    return "Requête post obligatoire"
