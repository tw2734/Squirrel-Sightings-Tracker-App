# Squirrel Sightings Tracker

## Application link:
home page: https://squirrel-hunter-007.appspot.com/
sightings (list all the squirrels): https://squirrel-hunter-007.appspot.com/sightings/
Add a squirrel: https://squirrel-hunter-007.appspot.com/sightings/add/
Squirrel stats: https://squirrel-hunter-007.appspot.com/sightings/stats/
Squirrel map: https://squirrel-hunter-007.appspot.com/map/

## Discription:
This is a web application built with Django. The aim of the app is to keep track of all the known squirrels in Central Park. Current squirrel records are imported from NYC Open Data [2018 Central Park Squirrel Census - Squirrel Data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).

The application mainly provides two functions, which could be accessed through our application home page.
1. Check Squirrel List
  - Listing all squirrel sightings with links to edit each
  - Updating a particular sighting
  - Creating a new sighting
  - General stats about the sightings
2. Go to Squirrel Map
  - Showing a map that displays the locations of the squirrel sightings on an OpenStreets map
  
  
Each squirrel record includes 23 fields:
-	Latitude
-	Longitude
-	Unique Squirrel ID
-	Shift
-	Date
-	Age
-	Primary Fur Color
-	Location
-	Specific Location
-	Running
-	Chasing
-	Climbing
-	Eating
-	Foraging
-	Other Activities
-	Kuks
-	Quaas
-	Moans
-	Tail flags
-	Tail twitches
-	Approaches
-	Indifferent
-	Runs from

Data import and export are enabled by running in the command line:
```
$ python manage.py import_squirrel_data /path/to/data.csv
```
```
$ python manage.py export_squirrel_data /path/to/export.csv
```

## Group Information:

Project Group 23, Section 1


## Contributors:
Name: Jiaming Xie, Tianling Wang
UNIs: [jx2389, tw2734]



