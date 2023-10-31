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


class RoomTemperatureConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("temperature", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("temperature", self.channel_name)

    def receive(self, temperature_data):
        async_to_sync(self.channel_layer.group_send)(
            "temperature",
            {
                "type": "temperature.message",
                "temperature": temperature_data,
            },
        )

    def temperature_message(self, event):
        self.send(text_data=event["temperature"])


class RoomCO2Consumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("co2", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("co2", self.channel_name)

    def receive(self, co2_data):
        async_to_sync(self.channel_layer.group_send)(
            "co2",
            {
                "type": "co2.message",
                "co2": co2_data,
            },
        )

    def co2_message(self, event):
        self.send(text_data=event["co2"])