import pandas as pd
import re
from user_agents import parse

log_file = 'sample-log.log'

log_pattern = re.compile(
    r'(?P<ip>\S+) - (?P<country>[A-Z]{2}) - \[(?P<timestamp>.*?)\] '  # note space at end
    r'"(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+) '  # space at end
    r'"-" "(?P<useragent>.*?)" (?P<responsetime>\d+)'
)

count = 0

with open(log_file, 'r') as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            entry = match.groupdict()
            ua = parse(entry['useragent'])
            is_bot = ua.is_bot
            browser = ua.browser.family
            if count == 0:
                print(f"User-Agent: {ua}\nIs bot: {is_bot}\nBrowser: {browser}")
                count += 1
