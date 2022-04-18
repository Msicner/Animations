"""This specially named module makes the package runnable."""

from constants import *
from model import Model
from ViewController import ViewController


def main() -> None:
    """Entrypoint of simulation."""
    model = Model(CELL_COUNT, CELL_SPEED)
    vc = ViewController(model)
    vc.start_simulation()


if __name__ == "__main__":
    main()