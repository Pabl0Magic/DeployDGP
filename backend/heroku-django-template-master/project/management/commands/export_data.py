import pandas as pd
from django.core.management.base import BaseCommand
from project.models import Room, Window, Door, Ventilator, Light
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = os.path.join(BASE_DIR, 'room_data.csv')

        try:
            rooms = Room.objects.all()
            room_lists = []
            
            for room in rooms:
                doors = Door.objects.filter(rooms__pk=room.name)
                door_list = []
                for door in doors:
                    door_list.append(door.name)

                windows = Window.objects.filter(room__pk=room.name)
                window_list = []
                for window in windows:
                    window_list.append(window.name)

                ligths = Light.objects.filter(room__pk=room.name)
                ligths_list = []
                for light in ligths:
                    ligths_list.append(light.name)

                ventilators = Ventilator.objects.filter(room__pk=room.name)
                ventilator_list = []
                for ventilator in ventilators:
                    ventilator_list.append(ventilator.name)
                
                room_lists.append((room.name, room.size, door_list, window_list, ligths_list, ventilator_list))


            df = pd.DataFrame({'Rooms': room_lists})
            df.to_csv(file_path, index=False)

            self.stdout.write(self.style.SUCCESS('Data exported completed successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Data export failed: {str(e)}'))
        
        return
        
        