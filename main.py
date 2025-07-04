from translator import translate_to_bash
from utils import is_safe, is_command

from rich.console import Console
from rich.prompt import Prompt
from translator import translate_to_bash
from utils import is_safe, is_command

console = Console()

def main():
    console.print("[bold green]NL -> bash, type 'exit' to quit[/bold green]")

    while True:
        user_input = Prompt.ask("Enter your natural language command").strip()
        if user_input.lower() == 'exit':
            break

        command = translate_to_bash(user_input)
        if is_command(command):
            if is_safe(command):
                console.print(f"[bold blue]bash ->[/bold blue] [yellow]{command}[/yellow]")
            else:
                console.print("[bold red]Unsafe command detected![/bold red]")
        else:
            console.print(f"[red]{command}[/red]")

if __name__ == '__main__':
    main()
