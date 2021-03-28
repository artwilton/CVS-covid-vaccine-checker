'''
This is a python script that requires you have python installed, or in a cloud environment.

This script scrapes the CVS website looking for vaccine appointments in the cities you list.
To update for your area, update the locations marked with ### below.

If you receive an error that says something is not install, type

pip install beepy

in your terminal.
'''



import requests
import time
import beepy


def findAVaccine():
    hours_to_run = 3 ###Update this to set the number of hours you want the script to run.
    max_time = time.time() + hours_to_run*60*60
    while time.time() < max_time:

        state = 'NJ' ###Update with your state abbreviation. Be sure to use all CAPS, e.g. RI

        response = requests.get("https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.{}.json?vaccineinfo".format(state.lower()), headers={"Referer":"https://www.cvs.com/immunizations/covid-19-vaccine"})
        payload = response.json()

        mappings = {}
        for item in payload["responsePayloadData"]["data"][state]:
            mappings[item.get('city')] = item.get('status')

        print(time.ctime())

        ###Update with your cities nearby
        cities = [
            'ABSECON',
            'ATLANTIC CITY',
            'BARNEGAT',
            'BAYONNE',
            'BEACHWOOD',
            'BELLE MEAD',
            'BERKELEY HEIGHTS',
            'BERLIN',
            'BERNARDSVILLE',
            'BLACKWOOD',
            'BLOOMFIELD',
            'BRICK',
            'BRIDGEWATER',
            'BRIGANTINE',
            'BROWNS MILLS',
            'BURLINGTON',
            'BURLINGTON TOWNSHIP',
            'CAMDEN',
            'CARTERET',
            'CEDAR GROVE',
            'CHATHAM',
            'CHERRY HILL',
            'CHESTER',
            'CLEMENTON',
            'CLIFTON',
            'CLOSTER',
            'CRESSKILL',
            'DELRAN',
            'DENVILLE',
            'DEPTFORD',
            'DUMONT',
            'EAST BRUNSWICK',
            'EAST HANOVER',
            'EAST ORANGE',
            'EAST WINDSOR',
            'EASTAMPTON',
            'EDGEWATER',
            'EDISON',
            'ELIZABETH',
            'ELMWOOD PARK',
            'ENGLEWOOD',
            'EWING',
            'FAIR LAWN',
            'FAIRFIELD',
            'FAIRLAWN',
            'FAIRVIEW',
            'FLEMINGTON',
            'FLORHAM PARK',
            'FORT LEE',
            'FRANKLIN PARK',
            'FREEHOLD',
            'GARFIELD',
            'GIBBSBORO',
            'GLASSBORO',
            'GREEN BROOK',
            'HACKENSACK',
            'HACKETTSTOWN',
            'HADDON HEIGHTS',
            'HADDON TOWNSHIP',
            'HADDONFIELD',
            'HAMILTON',
            'HASKELL',
            'HAZLET',
            'HAZLET TOWNSHIP',
            'HIGHLANDS',
            'HOBOKEN',
            'HOWELL',
            'JACKSON',
            'JERSEY CITY',
            'KEARNY',
            'KENDALL PARK',
            'LAKEWOOD',
            'LAMBERTVILLE',
            'LAWRENCEVILLE',
            'LEDGEWOOD',
            'LEONIA',
            'LINCOLN PARK',
            'LINDEN',
            'LITTLE FERRY',
            'LITTLE SILVER',
            'LODI',
            'LONG BRANCH',
            'LUMBERTON',
            'MAHWAH',
            'MALAGA',
            'MANAHAWKIN',
            'MANALAPAN',
            'MANASQUAN',
            'MANVILLE',
            'MAPLE SHADE',
            'MARGATE CITY',
            'MARLTON',
            'MARMORA',
            'MATAWAN',
            'MAYS LANDING',
            'MEDFORD',
            'MENDHAM',
            'MERCHANTVILLE',
            'METUCHEN',
            'MIDDLESEX',
            'MIDDLETOWN',
            'MILLTOWN',
            'MILLVILLE',
            'MONMOUTH JUNCTION',
            'MONTCLAIR',
            'MOORESTOWN',
            'MORRISTOWN',
            'MOUNT LAUREL',
            'MULLICA HILL',
            'NEPTUNE',
            'NEW EGYPT',
            'NEW MILFORD',
            'NEWARK',
            'NORTH ARLINGTON',
            'NORTH BRUNSWICK',
            'NORTH PLAINFIELD',
            'NORTH WILDWOOD',
            'NORTHVALE',
            'OAKHURST',
            'OAKLYN',
            'OCEAN',
            'OCEAN CITY',
            'OCEAN VIEW',
            'OLD TAPPAN',
            'PARAMUS',
            'PARSIPPANY',
            'PAULSBORO',
            'PENNSAUKEN',
            'PHILLIPSBURG',
            'PLAINSBORO',
            'PLEASANTVILLE',
            'POMONA',
            'PRINCETON',
            'RINGWOOD',
            'RIVER EDGE',
            'ROBBINSVILLE',
            'ROCHELLE PARK',
            'ROCKAWAY',
            'ROSELLE',
            'SADDLE BROOK',
            'SCOTCH PLAINS',
            'SEA ISLE CITY',
            'SEASIDE HEIGHTS',
            'SEWELL',
            'SICKLERVILLE',
            'SMITHVILLE',
            'SOUTH PLAINFIELD',
            'STANHOPE',
            'STRATFORD',
            'SWEDESBORO',
            'TABERNACLE',
            'TEANECK',
            'TENAFLY',
            'TOMS RIVER',
            'TRENTON',
            'TURNERSVILLE',
            'UNION',
            'UNION CITY',
            'UPPER MONTCLAIR',
            'VAUXHALL',
            'VENTNOR CITY',
            'VERNON',
            'VILLAS',
            'VINELAND',
            'VOORHEES',
            'WALL',
            'WARETOWN',
            'WASHINGTON',
            'WATCHUNG',
            'WEST CALDWELL',
            'WEST CAPE MAY',
            'WEST NEW YORK',
            'WEST ORANGE',
            'WEST WINDSOR',
            'WESTAMPTON',
            'WHIPPANY',
            'WHITING',
            'WILDWOOD',
            'WILLIAMSTOWN',
            'WILLINGBORO',
            'WOOD RIDGE',
            'WOODBRIDGE',
            'WOODBURY',
            'WYCKOFF'
        ]
        
        for city in cities:
            print(city, mappings[city])

        for key in mappings.keys():
            if (key in cities) and (mappings[key] != 'Fully Booked'):
                beepy.beep(sound = 'coin')
                break
            else:
                pass

        time.sleep(60) ##This runs every 60 seconds. Update here if you'd like it to go every 10min (600sec)
        print('\n -------------- RUNNING SCRIPT AGAIN --------------')

findAVaccine() ###this final line runs the function. Your terminal will output the cities every 60seconds

