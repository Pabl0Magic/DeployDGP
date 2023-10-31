from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class RoomPeopleConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("people", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("people", self.channel_name)

    def receive(self, people_data):
        async_to_sync(self.channel_layer.group_send)(
            "people",
            {
                "type": "people.message",
                "people": people_data,
            },
        )

    def people_message(self, event):
        print("Received")
        self.send(text_data=event["people"])