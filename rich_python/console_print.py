from rich.console import Console

console = Console()

console.print("This is some text.")
console.print("This is some bold text.", style="bold")
console.print("This is some bold underline text.", style="bold underline")
console.print("This is bold [yellow]some[/yellow] bold underline red text with a dash of yellow.", style="bold underline red")
console.print("This is some bold underline red on magenta text.", style="bold underline red on magenta")
console.print("This is some bold underline green on blue text.", style="bold underline green on blue")

console.print("[#a93dc2]192.168.1.229[/#a93dc2] is currently down or doesn't exist", style="bold red")