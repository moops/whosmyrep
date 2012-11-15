import json, datetime, urllib2, sys

limit = '600'
if len(sys.argv) == 2:
	limit = str(sys.argv[1])
data_url = 'http://www.govtrack.us/api/v1/person?roles__current=true&limit=' + limit

json_data = urllib2.urlopen(data_url)
data = json.load(json_data)

reps = []
for i,rep in enumerate(data['objects']):
	r = {
		'model' : 'reps.rep',
		'pk' : i+1,
		'fields' : {
			'first_name' : rep['firstname'],
			'middle_name' : rep['middlename'],
			'last_name' : rep['lastname'],
			'birth_on' : rep['birthday'],
			'twitter' : rep['twitterid'],
			'link' : rep['link'],
			'youtube' : rep['youtubeid'],
			'created_on' : datetime.date.today().strftime('%Y-%m-%d')
		}
	}
	reps.append(r)

with open('../whosmyrep/reps/fixtures/us_house.json', 'w') as outfile:
	json.dump(reps, outfile, indent=4)
