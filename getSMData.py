import requests
import datetime
import time
from requests.auth import HTTPBasicAuth
import json
import threading

json_location = "..\..\Dropbox\SURVEY MONKEY TOUCHDESIGNER [SHARE]\data\surveyMonkeyData.json"
#json_location = "surveyMonkeyData.json"

def downloadAndSave():
	threading.Timer(60.0*15.0, downloadAndSave).start()
	api_url = "https://api.surveymonkey.net/v3/internal/art/locale?slices=96&sum=false&geos=timezones"
	key = 'bearer DBFO7wTXGJgnUjIVlznq.3oNuZmvT5SCHvtyyCl8OGpkA-1tdPyTMgnkb1uuOEfZkZEOdbX8MPkw9-g7jy74g8UL0B-dpfdDfrJqv0Xt4KdwBcGm8sF7LehlaUdE0JG2'
	try:
		print "DOWNLOADING"
		print ""
		response = requests.get(api_url, headers={'Authorization': key})
	except:
		print "THERE WAS A PROBLEM DOWNLOADING"
		print ""
		return
	json_data = json.loads(response.content)
	print "CONTENT"
	print json.dumps(json_data, indent=4, sort_keys=True)
	print ""
	print "WRITTING TO FILE"
	print ""
	with open(json_location, "w") as f:
			json.dump(json_data, f)
	print "FINISHED WRITTING"
	print ""
	return

downloadAndSave()

