import logging
from rich.logging import RichHandler
from rich.console import Console

console = Console()

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%d-%b-%Y (%H:%M:%S)]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")
log.warning("192.168.1.229 is currently down or doesn't exist")

console.print("[black on green]Success[/black on green] host is up", style = "bold black")