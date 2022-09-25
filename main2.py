from rich import print, pretty
from rich.console import Console
from rich import inspect

console = Console()
# console.print("Hello", "World!", style="blink bold green")
# console.print("Error #4s04ce", style="blink bold purple")

# print("Hello, [bold green]World[/bold green]!", ":fire:")
# print("Hello, [bold green]World[/bold green]!", ":fire:")
# print("Hello, [italic yellow]World[/italic yellow]!", ":dance:")

# my_list = ["foo", "bar"]
# inspect(my_list, methods=False)

# console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")


# from rich.console import Console
# console = Console()
#
# test_data = [
#     {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
#     {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
#     {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
# ]
#
# def test_log():
#     enabled = False
#     context = {
#         "foo": "bar",
#     }
#     movies = ["Deadpool", "Rise of the Skywalker"]
#     console.log("Hello from", console, "!")
#     console.log(test_data, log_locals=True)
#
# test_log()


# from rich.progress import track
# import time
#
# for i in track(range(20), description="Скачивание..."):
#     time.sleep(0.7)  # Simulate work being done
#

# import time
#
# from rich.progress import Progress
#
# with Progress() as progress:
#
#     task1 = progress.add_task("[red]Скачивание...", total=1000)
#     task2 = progress.add_task("[green]Установка...", total=1000)
#     task3 = progress.add_task("[cyan]Подготовка...", total=1000)
#
#     while not progress.finished:
#         progress.update(task1, advance=0.65)
#         progress.update(task2, advance=0.4)
#         progress.update(task3, advance=0.8)
#         time.sleep(0.02)


# from rich.console import Console
# console = Console()
#
# try:
#     do_something()
# except Exception:
#     console.print_exception(show_locals=True)


# from rich.console import Console
# from rich.syntax import Syntax
#
# my_code = '''
# def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
#     """Iterate and generate a tuple with a flag for first and last value."""
#     iter_values = iter(values)
#     try:
#         previous_value = next(iter_values)
#     except StopIteration:
#         return
#     first = True
#     for value in iter_values:
#         yield first, False, previous_value
#         first = False
#         previous_value = value
#     yield first, True, previous_value
# '''
#
# my_code2 = '''
# public class Main {
#     public static void main(String[] args){
#         System.out.println("Hello World!");
#     }
# }
# '''
# syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
# syntax2 = Syntax(my_code2, "java", theme="dracula", line_numbers=True)
# console = Console()
# console.print(syntax2)