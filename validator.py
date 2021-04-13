'''
Algorithm:

Iterate through the lines of the input.json 
Load the json line into a python dictionary
Iterate through each field of the dictionary and validate the field
Add the data line's increment to the report

'''

from config import *
from datetime import datetime
import json
import re
import sys

import logging
logging.basicConfig(level=logging.DEBUG, filename='validator.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

global event_report
global column_verification_ref

def check_number(column, value):
	# to check if the value is numberical
	try:
		int(value)
	except:
		return(False)
	else:
		return(True)


def check_timestamp(column, datetime_str):
	# to check if the timestamp is in the right format
	try:
		data = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
	except:
		try:
			data = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f%z')
		except:
			return(False)
		else:
			return(True)
	else:
		return(True)


def check_list(column, value):
	# to validate if the value of the field comes from a known list of possibilities
	if value in list_values[column]:
		return(True)
	elif value.lower() in list_values[column]:
		return(True)
	else:
		return(False)


def match_regex(column, value):
	# to validate if the value is of the right pattern
	if re.match(patterns[column], value):
		return(True)
	else:
		return(False)


def check_boolean(column, value):
	# check if the value is a boolean or not
	if str(value) in ['True', 'False']:
		return(True)
	else:
		return (False)


def report_event(data):
	# get event name
	event = data['event']
	# get date from the timestamp
	date = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
	date = date.date().strftime('%Y-%m-%d')
	# check if event field exists in the report
	if event in event_report.keys():
		# check if the date field exists in the event
		if date in event_report[event].keys():
			event_report[event][date] = event_report[event][date] + 1
		else:
			# add the date to the event 
			event_report[event][date] = 1
	else:
		# add event field to the report
		event_report[event] = { date: 1 }


def write_report():
	file_obj = open('report.json', 'a+')
	file_obj.write(json.dumps(event_report))
	file_obj.close()



# the main function will iterate through this dictionary's keys and will call the function specified in the value
column_validation_ref = {
	'received_at': check_timestamp, 
	'timestamp': check_timestamp, 
	'context_device_manufacturer': check_list, 
	'context_locale': check_list, 
	'context_network_wifi': check_boolean, 
	'id': match_regex, 
	'anonymous_id': match_regex, 
	'context_device_type': check_list, 
	'event': check_list, 
	'event_text': check_list, 
	'user_id': check_number, 
	'context_device_token': check_number, 
	'context_device_model': match_regex, 
	'context_os_name': check_list, 
	'original_timestamp': check_timestamp, 
	'context_network_carrier': check_list, 
	'sent_at': check_timestamp, 
	'context_device_ad_tracking_enabled': check_boolean, 
	'context_app_version': match_regex, 
	'context_traits_taxfix_language': check_list, 
	'context_library_version': match_regex, 
	'context_library_name': check_list, 
	'context_timezone': check_list}

# global report variable that the main function will change to reflect the event count for each date
event_report = {}


def validate(filepath):
	file_obj = open(filepath)
	logging.info('Reading from the file, input.json')
	while(1):
		data = file_obj.readlines(1)
		if data:
			logging.info('Validating line: ' + data[0])
			data = json.loads(data[0])
			for key, value in column_validation_ref.items():
				try:
					if not data[key] == '' and not str(data[key]) == 'null' and not data[key] is None:
						if value(key, data[key]):
							pass
						else:
							logging.error('Skipping line due to non-compliance in field: ' + key + ' value: ' + str(data[key]))
							break
					else:
						if key in nullables:
							pass
						else:
							logging.error('Skipping line due to null value/missing field in a non-nullable field: ' + key)
							break
				except KeyError:
					if key in nullables:
						# non mandatory field
						pass
					else:
						logging.error('Field not found: ' + key + '... Skipping line')
						break
			logging.info('The line was successfully validated')
			report_event(data)
		else:
			logging.info('Reached EoF')
			logging.info('Writing report to file')
			write_report()
			break
	return



if __name__ == "__main__":
	if len(sys.argv) > 1:
		validate(sys.argv[1])
	else:
		print('Please enter the input json file as a command line argument')






