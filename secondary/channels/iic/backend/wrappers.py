from django.db.models import Q
import re, json
from django.utils.encoding import smart_str
from xml.sax.saxutils import escape, unescape

class Wrappers:
	def fill_input_variables(self, input_variable, payload, node_info):

		lgr = node_info.log

		lgr.info('Filler input: %s' % input_variable)

	

		default_value5 = input_variable[5]
		if default_value5:
			#if input_variable[5] in payload.keys():
			variables = re.findall("\[(.*?)\]", default_value5)
			lgr.info("Found Variables: %s" % variables)
			for v in variables:
				not_json = True
				try: 
					p = '['+v+']'
					json.loads(p)
					not_json = False
				except Exception as e: lgr.info('Default Value not JSON: %s' % default_value5)


				if v in payload.keys() and not_json:
					default_value5 = default_value5.replace('['+v+']',str(payload[v]))
				elif not_json:
					default_value5 = default_value5.replace('['+v+']',"")
				else: pass


			#Replace values in {} as well
			try: default_value5 = default_value5.strip().format(**payload)
			except: pass
			#Escape html entities
			#default_value5 = unescape(default_value5)
			#default_value5 = smart_str(default_value5)
			#default_value5 = escape(default_value5)		

			#new vaiable 5 value
			input_variable[5] = default_value5

		default_value8 = input_variable[8]
		if default_value8:
			#if input_variable[8] in payload.keys():
			variables = re.findall("\[(.*?)\]", default_value8)
			lgr.info("Found Variables: %s" % variables)

			for v in variables:
				not_json = True
				try: 
					p = '['+v+']'
					json.loads(p)
					not_json = False
				except Exception as e: lgr.info('Default Value not JSON: %s' % default_value8)

				if v in payload.keys() and not_json:
					default_value8 = default_value8.replace('['+v+']',str(payload[v]))
				elif not_json:
					default_value8 = default_value8.replace('['+v+']',"")
				else: pass

			#Replace values in {} as well
			try: default_value8 = default_value8.strip().format(**payload)
			except: pass
			#Escape html entities
			#default_value8 = unescape(default_value8)
			#default_value8 = smart_str(default_value8)
			#default_value8 = escape(default_value8)		

			#new vaiable 5 value
			input_variable[8] = default_value8
		
		return input_variable

