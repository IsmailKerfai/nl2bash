from nl2bash.utils import is_safe

def test_safe_commands():
    safe_cmds = [
        'ls -la',
        'find . -name "*.py"',
        'cat log.txt',
        'echo "Hello World"',
        'grep "error" /var/log/syslog',
        'tail -n 10 /var/log/messages',
        'head -5 myfile.txt',
        'df -h',
        'ps aux | grep python',
        'mkdir myfolder',
        'cp file1.txt file2.txt',
        'mv oldname.txt newname.txt',
        'chmod 755 script.sh',  # Note: chmod without 777 is safe here
    ]

    for cmd in safe_cmds:
        assert is_safe(cmd), f"Safe command rejected: {cmd}"

def test_unsafe_commands():
    unsafe_cmds = [
        'rm -rf /',
        'sudo rm -rf /',
        'shutdown now',
        'reboot',
        ':(){ :|:& };:',  # fork bomb
        'mkfs.ext4 /dev/sda1',
        'dd if=/dev/zero of=/dev/sda',
        'chmod 777 /etc/passwd',
        'chown root:root /etc/shadow',
        'sudo reboot',
        'sudo mkfs',
        'rm -rf ~/important_files',
        'chmod 777 somefile',
    ]

    for cmd in unsafe_cmds:
        assert not is_safe(cmd), f"Unsafe command accepted: {cmd}"

def test_invalid_syntax():
    invalid_cmds = [
        'some random text',
        '12345',
        'ls | | grep',
        'echo "unclosed string',
        '&&&&&',
        '',
        '    ',
    ]

    for cmd in invalid_cmds:
        assert not is_safe(cmd), f"Invalid syntax accepted: {cmd}"
