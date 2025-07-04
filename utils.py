import bashlex
import re


DANGEROUS_KEYWORDS = ['rm', 'shutdown', 'reboot', ':(){', 'mkfs', 'dd', 'chmod 777', 'chown', 'sudo', ':()']

# Add a whitelist of common safe commands
ALLOWED_COMMANDS = {
    'ls', 'cat', 'echo', 'grep', 'find', 'head', 'tail', 'df', 'ps', 'mkdir',
    'cp', 'mv', 'chmod', 'touch', 'which', 'whoami', 'pwd', 'date', 'wc',
    'sort', 'uniq', 'cut', 'awk', 'sed', 'less', 'more', 'file', 'stat',
    'du', 'free', 'top', 'htop', 'uptime', 'uname', 'id', 'groups'
}


def is_safe(command: str) -> bool:
    # Handle empty or whitespace-only commands
    if not command or command.isspace():
        print("Empty or whitespace-only command - unsafe.")
        return False

    lowered = command.lower()

    # Quick substring check for dangerous keywords anywhere in the string
    for dangerous in DANGEROUS_KEYWORDS:
        if dangerous in lowered:
            print("Sorry, the command is not safe (dangerous keyword found).")
            return False  # <-- return immediately!

    # Parsing: fail safe on parse errors
    try:
        parts = bashlex.parse(command)
    except bashlex.errors.ParsingError:
        print("Parsing error - unsafe command.")
        return False

    def check_nodes(nodes):
        for node in nodes:
            if node.kind == 'command':
                if node.parts:
                    cmd_name = node.parts[0].word.lower()

                    # Check if command is in whitelist
                    if cmd_name not in ALLOWED_COMMANDS:
                        print(f"Command '{cmd_name}' not in allowed list - rejecting.")
                        return False

                    # Additional check: reject suspicious commands (non-alphanumeric except common chars)
                    if not cmd_name.isalnum() and cmd_name not in ['.', '..', ':']:
                        print(f"Suspicious command name '{cmd_name}' - rejecting.")
                        return False  # <-- return immediately!
            if hasattr(node, 'parts') and node.parts:
                if not check_nodes(node.parts):
                    return False
        return True

    return check_nodes(parts)


KNOWN_COMMANDS = {
    'ls', 'cat', 'echo', 'grep', 'find', 'head', 'tail', 'df', 'ps', 'mkdir',
    'cp', 'mv', 'chmod', 'touch', 'which', 'whoami', 'pwd', 'date', 'wc',
    'sort', 'uniq', 'cut', 'awk', 'sed', 'less', 'more', 'file', 'stat',
    'du', 'free', 'top', 'htop', 'uptime', 'uname', 'id', 'groups'
}



def is_command(output: str) -> bool:
    output = output.strip()
    if not output:
        return False

    # Reject if it looks like a sentence (has a period not at the end)
    if re.search(r'\.\s', output):  # e.g., "No output. The command..."
        return False

    # Accept if it starts with a known bash command
    first_word = output.split()[0].lower()
    if first_word in ALLOWED_COMMANDS:
        return True

    if first_word in KNOWN_COMMANDS:
        return True

    # Accept if it's a short one-liner with symbols and no complete sentences
    if len(output.splitlines()) == 1 and re.search(r'[\/\.\-\$><|&]', output):
        return True

    return False

