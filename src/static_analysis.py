import re

def parse_diff(diff):
    changed_functions = []
    current_function = None
    in_function = False
    
    # Regex to identify function definitions
    function_def_regex = re.compile(r'^\s*def\s+(\w+)\s*\(')
    
    lines = diff.split('\n')
    for line in lines:
        # Check for function definitions
        print(line)
        match = function_def_regex.match(line)
        if match:
            current_function = match.group(1)
            in_function = True
            print(f"Detected function definition: {current_function}")
            changed_functions.append(current_function)
        
        # Check for changes within a function
        if in_function:
            if line.startswith('@@'):
                # Function boundaries indicated by diff context
                in_function = False
                current_function = None
            elif line.startswith('+') or line.startswith('-'):
                # Track changes within the function
                if current_function and current_function not in changed_functions:
                    changed_functions.append(current_function)
    
    return changed_functions
