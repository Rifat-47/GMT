# gmt/utils.py

import phonenumbers
import pytz
from phonenumbers import timezone
from datetime import datetime

def get_timezone_info(phone_number):
    try:
        if phone_number.startswith('+'):
            parsed_number = phonenumbers.parse(phone_number)
        else:
            parsed_number = phonenumbers.parse(f"+{phone_number}")
        if not phonenumbers.is_valid_number(parsed_number):
            return ("Invalid phone number", 'Invalid')

        timezone_str = timezone.time_zones_for_number(parsed_number)
        if timezone_str:
            timezone_info = timezone_str[0]
            tz = pytz.timezone(timezone_info)
            current_time = datetime.now(tz)
            offset_str = current_time.strftime('%z')
            gmt_offset = int(offset_str[:-2])
            if gmt_offset < 0:
                gmt_value = "GMT{}:{:02d}".format(gmt_offset, 0)
            else:
                gmt_value = "GMT+{}:{:02d}".format(abs(gmt_offset), 0)
            return timezone_info, gmt_value  
        else:
            return ("Timezone information not available for this number", 'Not available')
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return ("Error parsing phone number: {}".format(e), 'Error parsing phone number')
