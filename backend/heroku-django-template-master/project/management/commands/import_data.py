""" Command to import data from a file to the DB """

# yourapp/management/commands/import_data.py
import os
import pandas as pd
from django.core.management.base import BaseCommand
from project.models import Room, Window, Door, Ventilator

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        )
    )
)


class Command(BaseCommand):
    """Command to import data from a file"""

    def handle(self, *args, **options):
        excel_file_path = os.path.join(BASE_DIR, "smartroom_exampledata.xlsx")

        try:
            # Read data from the Excel file
            data = pd.read_excel(excel_file_path, sheet_name=None)
            # for sheet_name, sheet_data in data.items():

            # Import data for the Room model
            if "Room" in data:
                room_data = data["Room"]
                for index, row in room_data.iterrows():
                    Room.objects.create(name=row["roomName"], size=row["roomSize"])

            # Import data for the Door model
            if "Door" in data:
                window_data = data["Door"]
                for index, row in window_data.iterrows():
                    Door.objects.create(id=row["ID"])

            # Import data for the Ventilator model
            if "Ventilator" in data:
                window_data = data["Ventilator"]
                for index, row in window_data.iterrows():
                    room_id = row["roomID"]

                    try:
                        room = Room.objects.get(name=room_id)
                        Ventilator.objects.create(id=row["ID"], room=room)
                    except Room.DoesNotExist:
                        print(f"Room with name {room_id} not found.")
                    except Exception as e:
                        print(f"Error creating Ventilator: {str(e)}")

            # Import data for the Window model
            if "Window" in data:
                window_data = data["Window"]
                for index, row in window_data.iterrows():
                    room_id = row["roomID"]

                    try:
                        room = Room.objects.get(name=room_id)
                        Window.objects.create(id=row["ID"], room=room)
                    except Room.DoesNotExist:
                        print(f"Room with name {room_id} not found.")
                    except Exception as e:
                        print(f"Error creating Window: {str(e)}")

            self.stdout.write(self.style.SUCCESS("Data import completed successfully"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Data import failed: {str(e)}"))
