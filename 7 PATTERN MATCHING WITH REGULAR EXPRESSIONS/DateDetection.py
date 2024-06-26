import re

# Define the regular expression pattern for DD/MM/YYYY
date_pattern = re.compile(r'''
    (\d{1,2})   # Day, 1 or 2 digits
    /           # Slash
    (\d{1,2})   # Month, 1 or 2 digits
    /           # Slash
    (\d{4})     # Year, 4 digits
''', re.VERBOSE)

# Sample text to search for dates
text = "Today is 12/04/2023, and my birthday is 31/01/1990."

# Find all matches in the text
matches = date_pattern.findall(text)

# Check if the dates are valid and print them
for match in matches:
    day, month, year = match
    day, month, year = int(day), int(month), int(year)
    
    # Check if it's a leap year
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    # Check the validity of the date based on the month and leap year status
    if month in [4, 6, 9, 11]:  # April, June, September, November
        if day > 30:
            continue
    elif month == 2:  # February
        if is_leap:
            if day > 29:
                continue
        elif day > 28:
            continue
    elif day > 31:
        continue
    
    # Print the valid date
    print(f"{day:02d}/{month:02d}/{year}")