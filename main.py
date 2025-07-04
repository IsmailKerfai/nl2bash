from translator import translate_to_bash
from utils import is_safe, is_command

def main():
    print("NL -> bash, type 'exit' to quit")

    while True:
        user_input = input(">").strip()
        if user_input.lower() == 'exit':
            break

        command = translate_to_bash(user_input)
        if is_command(command):
            if is_safe(command):
                print(f"bash -> {command}")
            else:
                print("Unsafe command")
        else:
            print(command)



if __name__ == '__main__':
    main()