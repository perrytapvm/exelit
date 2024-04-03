from datetime import datetime

def convert_timestamp_to_utc(timestamp):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

# Example usage:
timestamp = 1710502379
print(convert_timestamp_to_utc(timestamp))
