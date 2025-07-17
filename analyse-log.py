import pandas as pd
import re
from user_agents import parse

log_file = 'sample-log.log'

log_pattern = re.compile(
    r'(?P<ip>\S+) - (?P<country>[A-Z]{2}) - \[(?P<timestamp>.*?)\] '
    r'"(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+) ' 
    r'"-" "(?P<useragent>.*?)" (?P<responsetime>\d+)'
)

data = []

with open(log_file, 'r') as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            entry = match.groupdict()
            ua = parse(entry['useragent'])
            entry["is_bot"] = ua.is_bot
            entry["browser"] = ua.browser.family
            data.append(entry)

df = pd.DataFrame(data)

#Top IP addresses
print("\nTop 5 IP addresses by request counts:")
print(df["ip"].value_counts().head(5))

#Top Nations
print("\nTop 5 Nations by request counts:")
print(df["country"].value_counts().head(5))

#Top Status Codes that are not 200.
print("\nTop Status Codes that are not 200 OK")
print(df[df["status"] != "200"]["status"].value_counts())

#Getting error status codes
df["status"] = df["status"].astype(int)
error_logs = df[df["status"].between(400, 599)]

#Top Nations from error codes
print("\nTop 5 Nations by error logs request counts:")
print(error_logs["country"].value_counts().head(5))

#Top IP addresses
print("\nTop 5 IP addresses by error logs request counts:")
print(error_logs["ip"].value_counts().head(5))

print("\nLength - " +str(len(df.index)))