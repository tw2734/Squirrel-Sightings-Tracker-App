from django.core.management.base import BaseCommand
import csv
from sightings.models import Squirrel
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        field_names = [f.name for f in Squirrel._meta.fields]
        with open(options['csv_file'], 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(['Y','X','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
            for obj in Squirrel.objects.all():
                row = []
                for field in field_names:
                    attr = getattr(obj, field)
                    if field == 'date':
                        attr = datetime.datetime.strftime(attr,'%m%d%Y')
                    row.append(attr)
                writer.writerow(row)
                
