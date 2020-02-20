from config import BOOSTING
from objects.library import Library


def highest_scan_capacity(library: Library) -> int:
    return library.scan_capacity * -1


def lowest_sign_up_time(library: Library) -> int:
    return library.time


def capacity_per_sign_up_time(library: Library) -> int:
    return library.scan_capacity / (library.time or 1) * -1


def boosted_capacity_per_sign_up_time(library: Library) -> int:
    return ((library.scan_capacity / (library.time or 1)) + library.scan_capacity * BOOSTING) * -1
