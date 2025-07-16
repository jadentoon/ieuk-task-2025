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
            is_bot = ua.is_bot
            browser = ua.browser.family
            data.append(entry)

df = pd.DataFrame(data)
print(df.head(30))
