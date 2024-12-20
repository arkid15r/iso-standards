"""ISO 3166-2 BD standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:BD
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "BD-01": (Entity("Bandarban", "BD-01", "DISTRICT", "bn", "BD-B"),),
        "BD-02": (Entity("Barguna", "BD-02", "DISTRICT", "bn", "BD-A"),),
        "BD-03": (Entity("Bogura", "BD-03", "DISTRICT", "bn", "BD-E"),),
        "BD-04": (Entity("Brahmanbaria", "BD-04", "DISTRICT", "bn", "BD-B"),),
        "BD-05": (Entity("Bagerhat", "BD-05", "DISTRICT", "bn", "BD-D"),),
        "BD-06": (Entity("Barishal", "BD-06", "DISTRICT", "bn", "BD-A"),),
        "BD-07": (Entity("Bhola", "BD-07", "DISTRICT", "bn", "BD-A"),),
        "BD-08": (Entity("Cumilla", "BD-08", "DISTRICT", "bn", "BD-B"),),
        "BD-09": (Entity("Chandpur", "BD-09", "DISTRICT", "bn", "BD-B"),),
        "BD-10": (Entity("Chattogram", "BD-10", "DISTRICT", "bn", "BD-B"),),
        "BD-11": (Entity("Cox's Bazar", "BD-11", "DISTRICT", "bn", "BD-B"),),
        "BD-12": (Entity("Chuadanga", "BD-12", "DISTRICT", "bn", "BD-D"),),
        "BD-13": (Entity("Dhaka", "BD-13", "DISTRICT", "bn", "BD-C"),),
        "BD-14": (Entity("Dinajpur", "BD-14", "DISTRICT", "bn", "BD-F"),),
        "BD-15": (Entity("Faridpur", "BD-15", "DISTRICT", "bn", "BD-C"),),
        "BD-16": (Entity("Feni", "BD-16", "DISTRICT", "bn", "BD-B"),),
        "BD-17": (Entity("Gopalganj", "BD-17", "DISTRICT", "bn", "BD-C"),),
        "BD-18": (Entity("Gazipur", "BD-18", "DISTRICT", "bn", "BD-C"),),
        "BD-19": (Entity("Gaibandha", "BD-19", "DISTRICT", "bn", "BD-F"),),
        "BD-20": (Entity("Habiganj", "BD-20", "DISTRICT", "bn", "BD-G"),),
        "BD-21": (Entity("Jamalpur", "BD-21", "DISTRICT", "bn", "BD-H"),),
        "BD-22": (Entity("Jashore", "BD-22", "DISTRICT", "bn", "BD-D"),),
        "BD-23": (Entity("Jhenaidah", "BD-23", "DISTRICT", "bn", "BD-D"),),
        "BD-24": (Entity("Joypurhat", "BD-24", "DISTRICT", "bn", "BD-E"),),
        "BD-25": (Entity("Jhalakathi", "BD-25", "DISTRICT", "bn", "BD-A"),),
        "BD-26": (Entity("Kishoreganj", "BD-26", "DISTRICT", "bn", "BD-C"),),
        "BD-27": (Entity("Khulna", "BD-27", "DISTRICT", "bn", "BD-D"),),
        "BD-28": (Entity("Kurigram", "BD-28", "DISTRICT", "bn", "BD-F"),),
        "BD-29": (Entity("Khagrachhari", "BD-29", "DISTRICT", "bn", "BD-B"),),
        "BD-30": (Entity("Kushtia", "BD-30", "DISTRICT", "bn", "BD-D"),),
        "BD-31": (Entity("Lakshmipur", "BD-31", "DISTRICT", "bn", "BD-B"),),
        "BD-32": (Entity("Lalmonirhat", "BD-32", "DISTRICT", "bn", "BD-F"),),
        "BD-33": (Entity("Manikganj", "BD-33", "DISTRICT", "bn", "BD-C"),),
        "BD-34": (Entity("Mymensingh", "BD-34", "DISTRICT", "bn", "BD-H"),),
        "BD-35": (Entity("Munshiganj", "BD-35", "DISTRICT", "bn", "BD-C"),),
        "BD-36": (Entity("Madaripur", "BD-36", "DISTRICT", "bn", "BD-C"),),
        "BD-37": (Entity("Magura", "BD-37", "DISTRICT", "bn", "BD-D"),),
        "BD-38": (Entity("Moulvibazar", "BD-38", "DISTRICT", "bn", "BD-G"),),
        "BD-39": (Entity("Meherpur", "BD-39", "DISTRICT", "bn", "BD-D"),),
        "BD-40": (Entity("Narayanganj", "BD-40", "DISTRICT", "bn", "BD-C"),),
        "BD-41": (Entity("Netrakona", "BD-41", "DISTRICT", "bn", "BD-H"),),
        "BD-42": (Entity("Narsingdi", "BD-42", "DISTRICT", "bn", "BD-C"),),
        "BD-43": (Entity("Narail", "BD-43", "DISTRICT", "bn", "BD-D"),),
        "BD-44": (Entity("Natore", "BD-44", "DISTRICT", "bn", "BD-E"),),
        "BD-45": (Entity("Chapai Nawabganj", "BD-45", "DISTRICT", "bn", "BD-E"),),
        "BD-46": (Entity("Nilphamari", "BD-46", "DISTRICT", "bn", "BD-F"),),
        "BD-47": (Entity("Noakhali", "BD-47", "DISTRICT", "bn", "BD-B"),),
        "BD-48": (Entity("Naogaon", "BD-48", "DISTRICT", "bn", "BD-E"),),
        "BD-49": (Entity("Pabna", "BD-49", "DISTRICT", "bn", "BD-E"),),
        "BD-50": (Entity("Pirojpur", "BD-50", "DISTRICT", "bn", "BD-A"),),
        "BD-51": (Entity("Patuakhali", "BD-51", "DISTRICT", "bn", "BD-A"),),
        "BD-52": (Entity("Panchagarh", "BD-52", "DISTRICT", "bn", "BD-F"),),
        "BD-53": (Entity("Rajbari", "BD-53", "DISTRICT", "bn", "BD-C"),),
        "BD-54": (Entity("Rajshahi", "BD-54", "DISTRICT", "bn", "BD-E"),),
        "BD-55": (Entity("Rangpur", "BD-55", "DISTRICT", "bn", "BD-F"),),
        "BD-56": (Entity("Rangamati", "BD-56", "DISTRICT", "bn", "BD-B"),),
        "BD-57": (Entity("Sherpur", "BD-57", "DISTRICT", "bn", "BD-H"),),
        "BD-58": (Entity("Satkhira", "BD-58", "DISTRICT", "bn", "BD-D"),),
        "BD-59": (Entity("Sirajganj", "BD-59", "DISTRICT", "bn", "BD-E"),),
        "BD-60": (Entity("Sylhet", "BD-60", "DISTRICT", "bn", "BD-G"),),
        "BD-61": (Entity("Sunamganj", "BD-61", "DISTRICT", "bn", "BD-G"),),
        "BD-62": (Entity("Shariatpur", "BD-62", "DISTRICT", "bn", "BD-C"),),
        "BD-63": (Entity("Tangail", "BD-63", "DISTRICT", "bn", "BD-C"),),
        "BD-64": (Entity("Thakurgaon", "BD-64", "DISTRICT", "bn", "BD-F"),),
        "BD-A": (Entity("Barishal", "BD-A", "DIVISION", "bn", ""),),
        "BD-B": (Entity("Chattogram", "BD-B", "DIVISION", "bn", ""),),
        "BD-C": (Entity("Dhaka", "BD-C", "DIVISION", "bn", ""),),
        "BD-D": (Entity("Khulna", "BD-D", "DIVISION", "bn", ""),),
        "BD-E": (Entity("Rajshahi", "BD-E", "DIVISION", "bn", ""),),
        "BD-F": (Entity("Rangpur", "BD-F", "DIVISION", "bn", ""),),
        "BD-G": (Entity("Sylhet", "BD-G", "DIVISION", "bn", ""),),
        "BD-H": (Entity("Mymensingh", "BD-H", "DIVISION", "bn", ""),),
    }
