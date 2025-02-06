import re
import json

with open('data_log.txt', 'r') as file:
    content = file.readlines()

'''
1. Extract All IP Addresses 

Write a regex to extract all the IP addresses from the log. 
Print the unique IP addresses in sorted order.   
'''
ip_pattern = r'\b(\d[0-9]{1,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3})\b'
ip_list = re.findall(ip_pattern, "\n".join(content))
unique_ip_list = sorted(set(ip_list))
print(ip_list)

'''
2. Extract User Actions

For all log lines containing "INFO," extract:
The username (e.g., john_doe).
The action they performed (e.g., 'UPDATE' or 'created a new record').
Store the results in a dictionary where the key is the username and the value is a unique list of their actions.
'''
action_pattern = r'INFO: User (\w+) (performed action .*? on record \d+|created a new record|logged (?:in|out))'

user_actions = {}

for line in content:
    match = re.search(action_pattern, line)
    if match:
          user, action = match.groups()
          user_actions.setdefault(user, set()).add(action)

user_actions = {user: list(actions) for user, actions in user_actions.items()}
print(user_actions)

'''
3. Validate and Extract Email Addresses

Search for valid email addresses in the log file. 
Ensure the email address adheres to standard rules 
(e.g., contains @, valid domain, no special 
characters in the username).
Output the extracted email addresses.
'''
email_pattern2 = r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[?:a-z|A-Z]{2,3}\b'
emails2 = re.findall(email_pattern2, "\n".join(content))
print(emails2)

'''
4. Extract Phone Numbers

Find and extract all phone numbers in the log. Ensure the phone numbers:
Follow the format XXX-XXX-XXXX.
Contain exactly 10 digits.
Return the extracted numbers in a set.
'''
phno_pattern = r'\d{3}-\d{3}-\d{4}'
phno = re.findall(phno_pattern, "\n".join(content))
print(phno)

'''
5. Extract All URLs

Search for and extract all URLs from the log. Ensure that:
The URL starts with http:// or https://.
It includes a valid domain name.
Return the extracted URLs in a set.
'''
url_pattern = r'https?://[^\s]+'
urls = re.findall(url_pattern, "\n".join(content))
print(urls)

'''
6. Classify Log Levels

Using regex, classify each log entry by its severity level 
(INFO, WARNING, ERROR, or CRITICAL). 
Count the number of entries in each category and display the results 
in a dictionary.
'''
log_severity = {'INFO': 0, 'WARNING': 1, 'ERROR': 2, 'CRITICAL': 3}
for line in content:
     for severity in log_severity.keys():
          if f"{severity}:" in line:
               log_severity[severity] += 1
print(log_severity)
'''
7. Extract Timestamps

Extract all the timestamps (e.g., [2025-01-07 14:32:10]) from the log. 
Store the timestamps in a list and display them in ascending order.
'''
timestamp_pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]'
timestamps = sorted(re.findall(timestamp_pattern, "\n".join(content)))
print(timestamps)

'''
8. Mask Sensitive Information

Create a new version of the log where:
IP addresses are masked as ***.***.***.***.
Phone numbers are masked as XXX-XXX-XXXX.
Email addresses are masked as hidden@example.com.
Save the modified log to a new file named masked_data_log.txt.
'''
masked_logs = []

for log in content:
    log = re.sub(ip_pattern, "***.***.***.***", log)
    log = re.sub(phno_pattern, "XXX-XXX-XXXX", log)
    log = re.sub(email_pattern2, "hidden@example.com", log)
    masked_logs.append(log)

with open('masked_data_log.txt', 'w') as file:
    file.write("\n".join(masked_logs))
'''
9. Validate Error Codes

Identify and validate error codes from the log. Error codes should:
Start with DB_ERR_ followed by a 4-digit number.
Print all unique valid error codes in a list.
'''
error_pattern = r'[DB_ERR]+\d{4}'
error_codes = re.findall(error_pattern, "\n".join(content))
print(error_codes)

'''
10. Parse Log into Structured Format

Using regex, parse the log entries into a structured format 
(dictionary or JSON) with the following keys:
timestamp: The timestamp of the log entry.
level: The log level (INFO, WARNING, ERROR, CRITICAL).
message: The rest of the log message.
Write the parsed data to a file named parsed_log.json.
'''
log_entries = []
log_entry_pattern = r'\[(.*?)\] (\w+): (.*)'
for line in content:
    match = re.match(log_entry_pattern, line)
    if match:
         timestamp, severity, message = match.groups()
         log_entries.append({"timestamp": timestamp, "level": severity, "message": message})
with open("parsed_log.json", 'w') as json_file:
    json.dump(log_entries, json_file, indent = 7)