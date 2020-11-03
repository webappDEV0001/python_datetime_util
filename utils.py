from datetime import datetime, timedelta

def datetime_converter(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def normalize_seconds(seconds):
    seconds = int(seconds)
    (days, remainder) = divmod(seconds, 86400)
    (hours, remainder) = divmod(remainder, 3600)
    (minutes, seconds) = divmod(remainder, 60)
    
    if days > 0:
        return f'{days} days {hours} hrs'
    elif hours > 0:
        return f'{hours} hrs {minutes} minutes'
    elif minutes > 0:
        return f'{minutes} minutes {seconds} seconds'
    else:
        return f'{seconds} seconds'
