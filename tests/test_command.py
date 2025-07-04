from nl2bash.utils import is_command


ALLOWED_COMMANDS = {"ls", "cd", "grep", "find", "cat"}
KNOWN_COMMANDS = {"echo", "touch", "mkdir", "pwd", "chmod"}

def test_valid_command_from_allowed():
    assert is_command("ls -la") is True

def test_valid_command_from_known():
    assert is_command("mkdir new_folder") is True

def test_valid_one_line_with_symbols():
    assert is_command("./script.sh") is True
    assert is_command("grep 'test' file.txt | sort") is True

def test_empty_string():
    assert is_command("") is False

def test_paragraph_not_command():
    assert is_command("This is a sentence. It has a period.") is False

def test_spaces_only():
    assert is_command("     ") is False