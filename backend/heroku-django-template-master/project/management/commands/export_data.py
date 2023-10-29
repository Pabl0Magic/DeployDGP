import pandas as pd
from django.core.management.base import BaseCommand
from project.models import Room, Window, Door, Ventilator
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = os.path.join(BASE_DIR, 'room_data.csv')

        try:
            rooms = Room.objects.all()
            room_lists = []
            
            for room in rooms:
                room_lists.append((room.name, room.size, room.co2, room.temperatura, room.luz, room.NOPeopleInRoom))


            df = pd.DataFrame({'Rooms': room_lists})
            df.to_csv(file_path, index=False)

            self.stdout.write(self.style.SUCCESS('Data exported completed successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Data export failed: {str(e)}'))
        
        return
        
        