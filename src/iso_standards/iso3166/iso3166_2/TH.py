"""ISO 3166-2 TH standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:TH
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "TH-10": (
            Entity("Krung Thep Maha Nakhon", "TH-10", "METROPOLITAN ADMINISTRATION", "th", ""),
        ),
        "TH-11": (Entity("Samut Prakan", "TH-11", "PROVINCE", "th", ""),),
        "TH-12": (Entity("Nonthaburi", "TH-12", "PROVINCE", "th", ""),),
        "TH-13": (Entity("Pathum Thani", "TH-13", "PROVINCE", "th", ""),),
        "TH-14": (Entity("Phra Nakhon Si Ayutthaya", "TH-14", "PROVINCE", "th", ""),),
        "TH-15": (Entity("Ang Thong", "TH-15", "PROVINCE", "th", ""),),
        "TH-16": (Entity("Lop Buri", "TH-16", "PROVINCE", "th", ""),),
        "TH-17": (Entity("Sing Buri", "TH-17", "PROVINCE", "th", ""),),
        "TH-18": (Entity("Chai Nat", "TH-18", "PROVINCE", "th", ""),),
        "TH-19": (Entity("Saraburi", "TH-19", "PROVINCE", "th", ""),),
        "TH-20": (Entity("Chon Buri", "TH-20", "PROVINCE", "th", ""),),
        "TH-21": (Entity("Rayong", "TH-21", "PROVINCE", "th", ""),),
        "TH-22": (Entity("Chanthaburi", "TH-22", "PROVINCE", "th", ""),),
        "TH-23": (Entity("Trat", "TH-23", "PROVINCE", "th", ""),),
        "TH-24": (Entity("Chachoengsao", "TH-24", "PROVINCE", "th", ""),),
        "TH-25": (Entity("Prachin Buri", "TH-25", "PROVINCE", "th", ""),),
        "TH-26": (Entity("Nakhon Nayok", "TH-26", "PROVINCE", "th", ""),),
        "TH-27": (Entity("Sa Kaeo", "TH-27", "PROVINCE", "th", ""),),
        "TH-30": (Entity("Nakhon Ratchasima", "TH-30", "PROVINCE", "th", ""),),
        "TH-31": (Entity("Buri Ram", "TH-31", "PROVINCE", "th", ""),),
        "TH-32": (Entity("Surin", "TH-32", "PROVINCE", "th", ""),),
        "TH-33": (Entity("Si Sa Ket", "TH-33", "PROVINCE", "th", ""),),
        "TH-34": (Entity("Ubon Ratchathani", "TH-34", "PROVINCE", "th", ""),),
        "TH-35": (Entity("Yasothon", "TH-35", "PROVINCE", "th", ""),),
        "TH-36": (Entity("Chaiyaphum", "TH-36", "PROVINCE", "th", ""),),
        "TH-37": (Entity("Amnat Charoen", "TH-37", "PROVINCE", "th", ""),),
        "TH-38": (Entity("Bueng Kan", "TH-38", "PROVINCE", "th", ""),),
        "TH-39": (Entity("Nong Bua Lam Phu", "TH-39", "PROVINCE", "th", ""),),
        "TH-40": (Entity("Khon Kaen", "TH-40", "PROVINCE", "th", ""),),
        "TH-41": (Entity("Udon Thani", "TH-41", "PROVINCE", "th", ""),),
        "TH-42": (Entity("Loei", "TH-42", "PROVINCE", "th", ""),),
        "TH-43": (Entity("Nong Khai", "TH-43", "PROVINCE", "th", ""),),
        "TH-44": (Entity("Maha Sarakham", "TH-44", "PROVINCE", "th", ""),),
        "TH-45": (Entity("Roi Et", "TH-45", "PROVINCE", "th", ""),),
        "TH-46": (Entity("Kalasin", "TH-46", "PROVINCE", "th", ""),),
        "TH-47": (Entity("Sakon Nakhon", "TH-47", "PROVINCE", "th", ""),),
        "TH-48": (Entity("Nakhon Phanom", "TH-48", "PROVINCE", "th", ""),),
        "TH-49": (Entity("Mukdahan", "TH-49", "PROVINCE", "th", ""),),
        "TH-50": (Entity("Chiang Mai", "TH-50", "PROVINCE", "th", ""),),
        "TH-51": (Entity("Lamphun", "TH-51", "PROVINCE", "th", ""),),
        "TH-52": (Entity("Lampang", "TH-52", "PROVINCE", "th", ""),),
        "TH-53": (Entity("Uttaradit", "TH-53", "PROVINCE", "th", ""),),
        "TH-54": (Entity("Phrae", "TH-54", "PROVINCE", "th", ""),),
        "TH-55": (Entity("Nan", "TH-55", "PROVINCE", "th", ""),),
        "TH-56": (Entity("Phayao", "TH-56", "PROVINCE", "th", ""),),
        "TH-57": (Entity("Chiang Rai", "TH-57", "PROVINCE", "th", ""),),
        "TH-58": (Entity("Mae Hong Son", "TH-58", "PROVINCE", "th", ""),),
        "TH-60": (Entity("Nakhon Sawan", "TH-60", "PROVINCE", "th", ""),),
        "TH-61": (Entity("Uthai Thani", "TH-61", "PROVINCE", "th", ""),),
        "TH-62": (Entity("Kamphaeng Phet", "TH-62", "PROVINCE", "th", ""),),
        "TH-63": (Entity("Tak", "TH-63", "PROVINCE", "th", ""),),
        "TH-64": (Entity("Sukhothai", "TH-64", "PROVINCE", "th", ""),),
        "TH-65": (Entity("Phitsanulok", "TH-65", "PROVINCE", "th", ""),),
        "TH-66": (Entity("Phichit", "TH-66", "PROVINCE", "th", ""),),
        "TH-67": (Entity("Phetchabun", "TH-67", "PROVINCE", "th", ""),),
        "TH-70": (Entity("Ratchaburi", "TH-70", "PROVINCE", "th", ""),),
        "TH-71": (Entity("Kanchanaburi", "TH-71", "PROVINCE", "th", ""),),
        "TH-72": (Entity("Suphan Buri", "TH-72", "PROVINCE", "th", ""),),
        "TH-73": (Entity("Nakhon Pathom", "TH-73", "PROVINCE", "th", ""),),
        "TH-74": (Entity("Samut Sakhon", "TH-74", "PROVINCE", "th", ""),),
        "TH-75": (Entity("Samut Songkhram", "TH-75", "PROVINCE", "th", ""),),
        "TH-76": (Entity("Phetchaburi", "TH-76", "PROVINCE", "th", ""),),
        "TH-77": (Entity("Prachuap Khiri Khan", "TH-77", "PROVINCE", "th", ""),),
        "TH-80": (Entity("Nakhon Si Thammarat", "TH-80", "PROVINCE", "th", ""),),
        "TH-81": (Entity("Krabi", "TH-81", "PROVINCE", "th", ""),),
        "TH-82": (Entity("Phangnga", "TH-82", "PROVINCE", "th", ""),),
        "TH-83": (Entity("Phuket", "TH-83", "PROVINCE", "th", ""),),
        "TH-84": (Entity("Surat Thani", "TH-84", "PROVINCE", "th", ""),),
        "TH-85": (Entity("Ranong", "TH-85", "PROVINCE", "th", ""),),
        "TH-86": (Entity("Chumphon", "TH-86", "PROVINCE", "th", ""),),
        "TH-90": (Entity("Songkhla", "TH-90", "PROVINCE", "th", ""),),
        "TH-91": (Entity("Satun", "TH-91", "PROVINCE", "th", ""),),
        "TH-92": (Entity("Trang", "TH-92", "PROVINCE", "th", ""),),
        "TH-93": (Entity("Phatthalung", "TH-93", "PROVINCE", "th", ""),),
        "TH-94": (Entity("Pattani", "TH-94", "PROVINCE", "th", ""),),
        "TH-95": (Entity("Yala", "TH-95", "PROVINCE", "th", ""),),
        "TH-96": (Entity("Narathiwat", "TH-96", "PROVINCE", "th", ""),),
        "TH-S": (Entity("Phatthaya", "TH-S", "SPECIAL ADMINISTRATIVE CITY", "th", ""),),
    }