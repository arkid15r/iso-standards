"""ISO 3166-2 LT standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:LT
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "LT-01": (Entity("Akmenė", "LT-01", "DISTRICT MUNICIPALITY", "lt", "LT-SA"),),
        "LT-02": (Entity("Alytaus miestas", "LT-02", "CITY MUNICIPALITY", "lt", "LT-AL"),),
        "LT-03": (Entity("Alytus", "LT-03", "DISTRICT MUNICIPALITY", "lt", "LT-AL"),),
        "LT-04": (Entity("Anykščiai", "LT-04", "DISTRICT MUNICIPALITY", "lt", "LT-UT"),),
        "LT-05": (Entity("Birštonas", "LT-05", "MUNICIPALITY", "lt", "LT-KU"),),
        "LT-06": (Entity("Biržai", "LT-06", "DISTRICT MUNICIPALITY", "lt", "LT-PN"),),
        "LT-07": (Entity("Druskininkai", "LT-07", "MUNICIPALITY", "lt", "LT-AL"),),
        "LT-08": (Entity("Elektrėnai", "LT-08", "MUNICIPALITY", "lt", "LT-VL"),),
        "LT-09": (Entity("Ignalina", "LT-09", "DISTRICT MUNICIPALITY", "lt", "LT-UT"),),
        "LT-10": (Entity("Jonava", "LT-10", "DISTRICT MUNICIPALITY", "lt", "LT-KU"),),
        "LT-11": (Entity("Joniškis", "LT-11", "DISTRICT MUNICIPALITY", "lt", "LT-SA"),),
        "LT-12": (Entity("Jurbarkas", "LT-12", "DISTRICT MUNICIPALITY", "lt", "LT-TA"),),
        "LT-13": (Entity("Kaišiadorys", "LT-13", "DISTRICT MUNICIPALITY", "lt", "LT-KU"),),
        "LT-14": (Entity("Kalvarija", "LT-14", "MUNICIPALITY", "lt", "LT-MR"),),
        "LT-15": (Entity("Kauno miestas", "LT-15", "CITY MUNICIPALITY", "lt", "LT-KU"),),
        "LT-16": (Entity("Kaunas", "LT-16", "DISTRICT MUNICIPALITY", "lt", "LT-KU"),),
        "LT-17": (Entity("Kazlų Rūdos", "LT-17", "MUNICIPALITY", "lt", "LT-MR"),),
        "LT-18": (Entity("Kėdainiai", "LT-18", "DISTRICT MUNICIPALITY", "lt", "LT-KU"),),
        "LT-19": (Entity("Kelmė", "LT-19", "DISTRICT MUNICIPALITY", "lt", "LT-SA"),),
        "LT-20": (Entity("Klaipėdos miestas", "LT-20", "CITY MUNICIPALITY", "lt", "LT-KL"),),
        "LT-21": (Entity("Klaipėda", "LT-21", "DISTRICT MUNICIPALITY", "lt", "LT-KL"),),
        "LT-22": (Entity("Kretinga", "LT-22", "DISTRICT MUNICIPALITY", "lt", "LT-KL"),),
        "LT-23": (Entity("Kupiškis", "LT-23", "DISTRICT MUNICIPALITY", "lt", "LT-PN"),),
        "LT-24": (Entity("Lazdijai", "LT-24", "DISTRICT MUNICIPALITY", "lt", "LT-AL"),),
        "LT-25": (Entity("Marijampolė", "LT-25", "DISTRICT MUNICIPALITY", "lt", "LT-MR"),),
        "LT-26": (Entity("Mažeikiai", "LT-26", "DISTRICT MUNICIPALITY", "lt", "LT-TE"),),
        "LT-27": (Entity("Molėtai", "LT-27", "DISTRICT MUNICIPALITY", "lt", "LT-UT"),),
        "LT-28": (Entity("Neringa", "LT-28", "MUNICIPALITY", "lt", "LT-KL"),),
        "LT-29": (Entity("Pagėgiai", "LT-29", "MUNICIPALITY", "lt", "LT-TA"),),
        "LT-30": (Entity("Pakruojis", "LT-30", "DISTRICT MUNICIPALITY", "lt", "LT-SA"),),
        "LT-31": (Entity("Palangos miestas", "LT-31", "CITY MUNICIPALITY", "lt", "LT-KL"),),
        "LT-32": (Entity("Panevėžio miestas", "LT-32", "CITY MUNICIPALITY", "lt", "LT-PN"),),
        "LT-33": (Entity("Panevėžys", "LT-33", "DISTRICT MUNICIPALITY", "lt", "LT-PN"),),
        "LT-34": (Entity("Pasvalys", "LT-34", "DISTRICT MUNICIPALITY", "lt", "LT-PN"),),
        "LT-35": (Entity("Plungė", "LT-35", "DISTRICT MUNICIPALITY", "lt", "LT-TE"),),
        "LT-36": (Entity("Prienai", "LT-36", "DISTRICT MUNICIPALITY", "lt", "LT-KU"),),
        "LT-37": (Entity("Radviliškis", "LT-37", "DISTRICT MUNICIPALITY", "lt", "LT-SA"),),
        "LT-38": (Entity("Raseiniai", "LT-38", "DISTRICT MUNICIPALITY", "lt", "LT-KU"),),
        "LT-39": (Entity("Rietavas", "LT-39", "MUNICIPALITY", "lt", "LT-TE"),),
        "LT-40": (Entity("Rokiškis", "LT-40", "DISTRICT MUNICIPALITY", "lt", "LT-PN"),),
        "LT-41": (Entity("Šakiai", "LT-41", "DISTRICT MUNICIPALITY", "lt", "LT-MR"),),
        "LT-42": (Entity("Šalčininkai", "LT-42", "DISTRICT MUNICIPALITY", "lt", "LT-VL"),),
        "LT-43": (Entity("Šiaulių miestas", "LT-43", "CITY MUNICIPALITY", "lt", "LT-SA"),),
        "LT-44": (Entity("Šiauliai", "LT-44", "DISTRICT MUNICIPALITY", "lt", "LT-SA"),),
        "LT-45": (Entity("Šilalė", "LT-45", "DISTRICT MUNICIPALITY", "lt", "LT-TA"),),
        "LT-46": (Entity("Šilutė", "LT-46", "DISTRICT MUNICIPALITY", "lt", "LT-KL"),),
        "LT-47": (Entity("Širvintos", "LT-47", "DISTRICT MUNICIPALITY", "lt", "LT-VL"),),
        "LT-48": (Entity("Skuodas", "LT-48", "DISTRICT MUNICIPALITY", "lt", "LT-KL"),),
        "LT-49": (Entity("Švenčionys", "LT-49", "DISTRICT MUNICIPALITY", "lt", "LT-VL"),),
        "LT-50": (Entity("Tauragė", "LT-50", "DISTRICT MUNICIPALITY", "lt", "LT-TA"),),
        "LT-51": (Entity("Telšiai", "LT-51", "DISTRICT MUNICIPALITY", "lt", "LT-TE"),),
        "LT-52": (Entity("Trakai", "LT-52", "DISTRICT MUNICIPALITY", "lt", "LT-VL"),),
        "LT-53": (Entity("Ukmergė", "LT-53", "DISTRICT MUNICIPALITY", "lt", "LT-VL"),),
        "LT-54": (Entity("Utena", "LT-54", "DISTRICT MUNICIPALITY", "lt", "LT-UT"),),
        "LT-55": (Entity("Varėna", "LT-55", "DISTRICT MUNICIPALITY", "lt", "LT-AL"),),
        "LT-56": (Entity("Vilkaviškis", "LT-56", "DISTRICT MUNICIPALITY", "lt", "LT-MR"),),
        "LT-57": (Entity("Vilniaus miestas", "LT-57", "CITY MUNICIPALITY", "lt", "LT-VL"),),
        "LT-58": (Entity("Vilnius", "LT-58", "DISTRICT MUNICIPALITY", "lt", "LT-VL"),),
        "LT-59": (Entity("Visaginas", "LT-59", "MUNICIPALITY", "lt", "LT-UT"),),
        "LT-60": (Entity("Zarasai", "LT-60", "DISTRICT MUNICIPALITY", "lt", "LT-UT"),),
        "LT-AL": (Entity("Alytaus apskritis", "LT-AL", "COUNTY", "lt", ""),),
        "LT-KL": (Entity("Klaipėdos apskritis", "LT-KL", "COUNTY", "lt", ""),),
        "LT-KU": (Entity("Kauno apskritis", "LT-KU", "COUNTY", "lt", ""),),
        "LT-MR": (Entity("Marijampolės apskritis", "LT-MR", "COUNTY", "lt", ""),),
        "LT-PN": (Entity("Panevėžio apskritis", "LT-PN", "COUNTY", "lt", ""),),
        "LT-SA": (Entity("Šiaulių apskritis", "LT-SA", "COUNTY", "lt", ""),),
        "LT-TA": (Entity("Tauragės apskritis", "LT-TA", "COUNTY", "lt", ""),),
        "LT-TE": (Entity("Telšių apskritis", "LT-TE", "COUNTY", "lt", ""),),
        "LT-UT": (Entity("Utenos apskritis", "LT-UT", "COUNTY", "lt", ""),),
        "LT-VL": (Entity("Vilniaus apskritis", "LT-VL", "COUNTY", "lt", ""),),
    }