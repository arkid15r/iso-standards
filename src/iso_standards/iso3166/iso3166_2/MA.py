"""ISO 3166-2 MA standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:MA
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "MA-01": (Entity("Tanger-Tétouan-Al Hoceïma", "MA-01", "REGION", "ar", ""),),
        "MA-02": (Entity("L'Oriental", "MA-02", "REGION", "ar", ""),),
        "MA-03": (Entity("Fès-Meknès", "MA-03", "REGION", "ar", ""),),
        "MA-04": (Entity("Rabat-Salé-Kénitra", "MA-04", "REGION", "ar", ""),),
        "MA-05": (Entity("Béni Mellal-Khénifra", "MA-05", "REGION", "ar", ""),),
        "MA-06": (Entity("Casablanca-Settat", "MA-06", "REGION", "ar", ""),),
        "MA-07": (Entity("Marrakech-Safi", "MA-07", "REGION", "ar", ""),),
        "MA-08": (Entity("Drâa-Tafilalet", "MA-08", "REGION", "ar", ""),),
        "MA-09": (Entity("Souss-Massa", "MA-09", "REGION", "ar", ""),),
        "MA-10": (Entity("Guelmim-Oued Noun", "MA-10", "REGION", "ar", ""),),
        "MA-11": (Entity("Laâyoune-Sakia El Hamra", "MA-11", "REGION", "ar", ""),),
        "MA-12": (Entity("Dakhla-Oued Ed-Dahab", "MA-12", "REGION", "ar", ""),),
        "MA-AGD": (Entity("Agadir-Ida-Ou-Tanane", "MA-AGD", "PREFECTURE", "ar", "MA-09"),),
        "MA-AOU": (Entity("Aousserd", "MA-AOU", "PROVINCE", "ar", "MA-12"),),
        "MA-ASZ": (Entity("Assa-Zag", "MA-ASZ", "PROVINCE", "ar", "MA-10"),),
        "MA-AZI": (Entity("Azilal", "MA-AZI", "PROVINCE", "ar", "MA-05"),),
        "MA-BEM": (Entity("Béni Mellal", "MA-BEM", "PROVINCE", "ar", "MA-05"),),
        "MA-BER": (Entity("Berkane", "MA-BER", "PROVINCE", "ar", "MA-02"),),
        "MA-BES": (Entity("Benslimane", "MA-BES", "PROVINCE", "ar", "MA-06"),),
        "MA-BOD": (Entity("Boujdour", "MA-BOD", "PROVINCE", "ar", "MA-11"),),
        "MA-BOM": (Entity("Boulemane", "MA-BOM", "PROVINCE", "ar", "MA-03"),),
        "MA-BRR": (Entity("Berrechid", "MA-BRR", "PROVINCE", "ar", "MA-06"),),
        "MA-CAS": (Entity("Casablanca", "MA-CAS", "PREFECTURE", "ar", "MA-06"),),
        "MA-CHE": (Entity("Chefchaouen", "MA-CHE", "PROVINCE", "ar", "MA-01"),),
        "MA-CHI": (Entity("Chichaoua", "MA-CHI", "PROVINCE", "ar", "MA-07"),),
        "MA-CHT": (Entity("Chtouka-Ait Baha", "MA-CHT", "PROVINCE", "ar", "MA-06"),),
        "MA-DRI": (Entity("Driouch", "MA-DRI", "PROVINCE", "ar", "MA-02"),),
        "MA-ERR": (Entity("Errachidia", "MA-ERR", "PROVINCE", "ar", "MA-08"),),
        "MA-ESI": (Entity("Essaouira", "MA-ESI", "PROVINCE", "ar", "MA-07"),),
        "MA-ESM": (Entity("Es-Semara", "MA-ESM", "PROVINCE", "ar", "MA-11"),),
        "MA-FAH": (Entity("Fahs-Anjra", "MA-FAH", "PROVINCE", "ar", "MA-01"),),
        "MA-FES": (Entity("Fès", "MA-FES", "PREFECTURE", "ar", "MA-03"),),
        "MA-FIG": (Entity("Figuig", "MA-FIG", "PROVINCE", "ar", "MA-02"),),
        "MA-FQH": (Entity("Fquih Ben Salah", "MA-FQH", "PROVINCE", "ar", "MA-05"),),
        "MA-GUE": (Entity("Guelmim", "MA-GUE", "PROVINCE", "ar", "MA-10"),),
        "MA-GUF": (Entity("Guercif", "MA-GUF", "PROVINCE", "ar", "MA-02"),),
        "MA-HAJ": (Entity("El Hajeb", "MA-HAJ", "PROVINCE", "ar", "MA-03"),),
        "MA-HAO": (Entity("Al Haouz", "MA-HAO", "PROVINCE", "ar", "MA-07"),),
        "MA-HOC": (Entity("Al Hoceïma", "MA-HOC", "PROVINCE", "ar", "MA-01"),),
        "MA-IFR": (Entity("Ifrane", "MA-IFR", "PROVINCE", "ar", "MA-03"),),
        "MA-INE": (Entity("Inezgane-Ait Melloul", "MA-INE", "PREFECTURE", "ar", "MA-09"),),
        "MA-JDI": (Entity("El Jadida", "MA-JDI", "PROVINCE", "ar", "MA-06"),),
        "MA-JRA": (Entity("Jerada", "MA-JRA", "PROVINCE", "ar", "MA-02"),),
        "MA-KEN": (Entity("Kénitra", "MA-KEN", "PROVINCE", "ar", "MA-04"),),
        "MA-KES": (Entity("El Kelâa des Sraghna", "MA-KES", "PROVINCE", "ar", "MA-07"),),
        "MA-KHE": (Entity("Khémisset", "MA-KHE", "PROVINCE", "ar", "MA-04"),),
        "MA-KHN": (Entity("Khénifra", "MA-KHN", "PROVINCE", "ar", "MA-05"),),
        "MA-KHO": (Entity("Khouribga", "MA-KHO", "PROVINCE", "ar", "MA-05"),),
        "MA-LAA": (Entity("Laâyoune", "MA-LAA", "PROVINCE", "ar", "MA-11"),),
        "MA-LAR": (Entity("Larache", "MA-LAR", "PROVINCE", "ar", "MA-01"),),
        "MA-MAR": (Entity("Marrakech", "MA-MAR", "PREFECTURE", "ar", "MA-07"),),
        "MA-MDF": (Entity("M’diq-Fnideq", "MA-MDF", "PREFECTURE", "ar", "MA-01"),),
        "MA-MED": (Entity("Médiouna", "MA-MED", "PROVINCE", "ar", "MA-06"),),
        "MA-MEK": (Entity("Meknès", "MA-MEK", "PREFECTURE", "ar", "MA-03"),),
        "MA-MID": (Entity("Midelt", "MA-MID", "PROVINCE", "ar", "MA-08"),),
        "MA-MOH": (Entity("Mohammadia", "MA-MOH", "PREFECTURE", "ar", "MA-06"),),
        "MA-MOU": (Entity("Moulay Yacoub", "MA-MOU", "PROVINCE", "ar", "MA-03"),),
        "MA-NAD": (Entity("Nador", "MA-NAD", "PROVINCE", "ar", "MA-02"),),
        "MA-NOU": (Entity("Nouaceur", "MA-NOU", "PROVINCE", "ar", "MA-04"),),
        "MA-OUA": (Entity("Ouarzazate", "MA-OUA", "PROVINCE", "ar", "MA-08"),),
        "MA-OUD": (Entity("Oued Ed-Dahab", "MA-OUD", "PROVINCE", "ar", "MA-12"),),
        "MA-OUJ": (Entity("Oujda-Angad", "MA-OUJ", "PREFECTURE", "ar", "MA-02"),),
        "MA-OUZ": (Entity("Ouezzane", "MA-OUZ", "PROVINCE", "ar", "MA-01"),),
        "MA-RAB": (Entity("Rabat", "MA-RAB", "PREFECTURE", "ar", "MA-04"),),
        "MA-REH": (Entity("Rehamna", "MA-REH", "PROVINCE", "ar", "MA-07"),),
        "MA-SAF": (Entity("Safi", "MA-SAF", "PROVINCE", "ar", "MA-07"),),
        "MA-SAL": (Entity("Salé", "MA-SAL", "PREFECTURE", "ar", "MA-04"),),
        "MA-SEF": (Entity("Sefrou", "MA-SEF", "PROVINCE", "ar", "MA-03"),),
        "MA-SET": (Entity("Settat", "MA-SET", "PROVINCE", "ar", "MA-06"),),
        "MA-SIB": (Entity("Sidi Bennour", "MA-SIB", "PROVINCE", "ar", "MA-06"),),
        "MA-SIF": (Entity("Sidi Ifni", "MA-SIF", "PROVINCE", "ar", "MA-10"),),
        "MA-SIK": (Entity("Sidi Kacem", "MA-SIK", "PROVINCE", "ar", "MA-04"),),
        "MA-SIL": (Entity("Sidi Slimane", "MA-SIL", "PROVINCE", "ar", "MA-04"),),
        "MA-SKH": (Entity("Skhirate-Témara", "MA-SKH", "PREFECTURE", "ar", "MA-04"),),
        "MA-TAF": (Entity("Tarfaya", "MA-TAF", "PROVINCE", "ar", "MA-11"),),
        "MA-TAI": (Entity("Taourirt", "MA-TAI", "PROVINCE", "ar", "MA-02"),),
        "MA-TAO": (Entity("Taounate", "MA-TAO", "PROVINCE", "ar", "MA-03"),),
        "MA-TAR": (Entity("Taroudannt", "MA-TAR", "PROVINCE", "ar", "MA-09"),),
        "MA-TAT": (Entity("Tata", "MA-TAT", "PROVINCE", "ar", "MA-09"),),
        "MA-TAZ": (Entity("Taza", "MA-TAZ", "PROVINCE", "ar", "MA-03"),),
        "MA-TET": (Entity("Tétouan", "MA-TET", "PROVINCE", "ar", "MA-01"),),
        "MA-TIN": (Entity("Tinghir", "MA-TIN", "PROVINCE", "ar", "MA-08"),),
        "MA-TIZ": (Entity("Tiznit", "MA-TIZ", "PROVINCE", "ar", "MA-09"),),
        "MA-TNG": (Entity("Tanger-Assilah", "MA-TNG", "PREFECTURE", "ar", "MA-01"),),
        "MA-TNT": (Entity("Tan-Tan", "MA-TNT", "PROVINCE", "ar", "MA-10"),),
        "MA-YUS": (Entity("Youssoufia", "MA-YUS", "PROVINCE", "ar", "MA-07"),),
        "MA-ZAG": (Entity("Zagora", "MA-ZAG", "PROVINCE", "ar", "MA-08"),),
    }