import re

def regex_strip(input_string, chars_to_remove=None):
    # If chars_to_remove is not provided, remove whitespace
    if chars_to_remove is None:
        # Regex pattern to match leading and trailing whitespace
        pattern = r'^\s+|\s+$'
    else:
        # Escape special regex characters in chars_to_remove to treat them as literals
        escaped_chars = re.escape(chars_to_remove)
        # Regex pattern to match leading and trailing specified characters
        pattern = rf'^[{escaped_chars}]+|[{escaped_chars}]+$'
    
    # Use sub() to replace the matched patterns with an empty string
    stripped_string = re.sub(pattern, '', input_string)
    
    return stripped_string

# Test the function
print(regex_strip("  Hello, World!  "))  # Output: "Hello, World!"
print(regex_strip("...Hello, World!...", "."))  # Output: "Hello, World!"
print(regex_strip("xyxHello, World!xyx", "xy"))  # Output: "Hello, World!"