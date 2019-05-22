import base64
import csv
import json
import logging
import operator
import time
from datetime import datetime
from decimal import Decimal, ROUND_DOWN

import pytz
import re
from django.apps import apps
from django.conf import settings
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.validators import validate_email
from django.db import IntegrityError
from django.db import transaction
from django.db.models import Count, Sum, Max, Min, Avg, Q, F, Func, Value, CharField, Case, Value, When, TextField
from django.db.models.functions import Cast
from django.db.models.functions import Concat, Substr
from django.shortcuts import render
from django.utils import timezone
from django.utils.timezone import localtime
from django.utils.timezone import utc
import numpy as np
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from .models import *

lgr = logging.getLogger('secondary.channels.notify')

class List:
    #def balance(self, payload, gateway_profile, profile_tz, data):

    def notifications_summary(self, payload, gateway_profile, profile_tz, data):
        params = {}
	params['rows'] = []
	params['cols'] = [{"label": "index", "type": "string"}, {"label": "name", "type": "string"},
                          {"label": "image", "type": "string"}, {"label": "checked", "type": "string"},
                          {"label": "selectValue", "type": "string"}, {"label": "description", "type": "string"},
                          {"label": "color", "type": "string"}]

	params['data'] = []
	params['lines'] = []
	
	max_id = 0
	min_id = 0
	ct = 0
	push = {}

	lgr.info('Started Notifications')

        try:
            outbound = Outbound.objects.filter(
                    contact__product__notification__code__institution=gateway_profile.institution). \
                values('state__name'). \
                annotate(state_count=Count('state__name'))

            for o in outbound:
                item = {}
                item['name'] = o['state__name']
                item['count'] = '%s' % '{0:,.2f}'.format(o['state_count'])
                params['rows'].append(item)
        except Exception, e:
            lgr.info('Error on notifications: %s' % e)
        return params,max_id,min_id,ct,push


