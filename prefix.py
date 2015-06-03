#! /usr/bin/python

###########################
#	RIPE announced-prefixes  
###########################


import requests
import sys
import json

# We take the first argument of the prompt data. Put the AS number in here 
URL = (sys.argv)
print str(URL[1])


# We use the RIPE API to get the announced-prefixes data
r = requests.get("https://stat.ripe.net/data/announced-prefixes/data.json\?resource=%s" % str(URL[1]))

# We transform the json data in dictionnary data
ann_pref_dict = json.loads(r.text)
ann_pref_list_data_prefixes = ann_pref_dict["data"]["prefixes"]

# We go accross the list and print the prefixes
j=0
for i in ann_pref_list_data_prefixes:
	print ann_pref_list_data_prefixes[j]['prefix']
	j+=1
