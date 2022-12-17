import csv
from Neuroshima_Character_Creator.Engine.models import Origins

def run():
    file = open('Database_Sources/database_origins.csv')
    read_file = csv.reader(file, delimiter=';')

    Origins.objects.all().delete()

    count=1

    for record in read_file:
        if count==1:
            pass
        else:
            print(record)
            Origins.objects.create(origin_name=record[0],
                                   origin_description=record[1],
                                   origin_agility_bonus=record[2],
                                   origin_perception_bonus=record[3],
                                   origin_character_bonus=record[4],
                                   origin_guile_bonus=record[5],
                                   origin_build_bonus=record[6])
        count=count+1