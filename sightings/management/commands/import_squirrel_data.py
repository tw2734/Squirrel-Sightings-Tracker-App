from django.core.management.base import BaseCommand
import csv
from sightings.models import Squirrel
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        def str_to_bool(s):
            if s == 'true':
                return True
            elif s == 'false':
                return False
        for item in data:
            s = Squirrel(
                    latitude = item['Y'],
                    longitude = item['X'],
                    unique_squirrel_id = item['Unique Squirrel ID'],
                    shift = item['Shift'],
                    date = datetime.datetime.strptime(item['Date'],'%m%d%Y'),
                    age = item['Age'],
                    primary_fur_color = item['Primary Fur Color'],
                    location = item['Location'],
                    specific_location = item['Specific Location'],
                    running = str_to_bool(item['Running']),
                    chasing = str_to_bool(item['Chasing']),
                    climbing = str_to_bool(item['Climbing']),
                    eating = str_to_bool(item['Eating']),
                    foraging = str_to_bool(item['Foraging']),
                    other_activities = item['Other Activities'],
                    kuks = str_to_bool(item['Kuks']),
                    quaas = str_to_bool(item['Quaas']),
                    moans = str_to_bool(item['Moans']),
                    tail_flags = str_to_bool(item['Tail flags']),
                    tail_twitches = str_to_bool(item['Tail twitches']),
                    approaches = str_to_bool(item['Approaches']),
                    indifferent = str_to_bool(item['Indifferent']),
                    runs_from = str_to_bool(item['Runs from']),
                    )
            s.save()

