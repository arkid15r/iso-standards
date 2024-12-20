"""ISO 3166-2 CZ standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:CZ
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "CZ-10": (Entity("Praha", "CZ-10", "CAPITAL CITY", "cs", ""),),
        "CZ-20": (Entity("Středočeský kraj", "CZ-20", "REGION", "cs", ""),),
        "CZ-201": (Entity("Benešov", "CZ-201", "DISTRICT", "cs", "CZ-20"),),
        "CZ-202": (Entity("Beroun", "CZ-202", "DISTRICT", "cs", "CZ-20"),),
        "CZ-203": (Entity("Kladno", "CZ-203", "DISTRICT", "cs", "CZ-20"),),
        "CZ-204": (Entity("Kolín", "CZ-204", "DISTRICT", "cs", "CZ-20"),),
        "CZ-205": (Entity("Kutná Hora", "CZ-205", "DISTRICT", "cs", "CZ-20"),),
        "CZ-206": (Entity("Mělník", "CZ-206", "DISTRICT", "cs", "CZ-20"),),
        "CZ-207": (Entity("Mladá Boleslav", "CZ-207", "DISTRICT", "cs", "CZ-20"),),
        "CZ-208": (Entity("Nymburk", "CZ-208", "DISTRICT", "cs", "CZ-20"),),
        "CZ-209": (Entity("Praha-východ", "CZ-209", "DISTRICT", "cs", "CZ-20"),),
        "CZ-20A": (Entity("Praha-západ", "CZ-20A", "DISTRICT", "cs", "CZ-20"),),
        "CZ-20B": (Entity("Příbram", "CZ-20B", "DISTRICT", "cs", "CZ-20"),),
        "CZ-20C": (Entity("Rakovník", "CZ-20C", "DISTRICT", "cs", "CZ-20"),),
        "CZ-31": (Entity("Jihočeský kraj", "CZ-31", "REGION", "cs", ""),),
        "CZ-311": (Entity("České Budějovice", "CZ-311", "DISTRICT", "cs", "CZ-31"),),
        "CZ-312": (Entity("Český Krumlov", "CZ-312", "DISTRICT", "cs", "CZ-31"),),
        "CZ-313": (Entity("Jindřichův Hradec", "CZ-313", "DISTRICT", "cs", "CZ-31"),),
        "CZ-314": (Entity("Písek", "CZ-314", "DISTRICT", "cs", "CZ-31"),),
        "CZ-315": (Entity("Prachatice", "CZ-315", "DISTRICT", "cs", "CZ-31"),),
        "CZ-316": (Entity("Strakonice", "CZ-316", "DISTRICT", "cs", "CZ-31"),),
        "CZ-317": (Entity("Tábor", "CZ-317", "DISTRICT", "cs", "CZ-31"),),
        "CZ-32": (Entity("Plzeňský kraj", "CZ-32", "REGION", "cs", ""),),
        "CZ-321": (Entity("Domažlice", "CZ-321", "DISTRICT", "cs", "CZ-32"),),
        "CZ-322": (Entity("Klatovy", "CZ-322", "DISTRICT", "cs", "CZ-32"),),
        "CZ-323": (Entity("Plzeň-město", "CZ-323", "DISTRICT", "cs", "CZ-32"),),
        "CZ-324": (Entity("Plzeň-jih", "CZ-324", "DISTRICT", "cs", "CZ-32"),),
        "CZ-325": (Entity("Plzeň-sever", "CZ-325", "DISTRICT", "cs", "CZ-32"),),
        "CZ-326": (Entity("Rokycany", "CZ-326", "DISTRICT", "cs", "CZ-32"),),
        "CZ-327": (Entity("Tachov", "CZ-327", "DISTRICT", "cs", "CZ-32"),),
        "CZ-41": (Entity("Karlovarský kraj", "CZ-41", "REGION", "cs", ""),),
        "CZ-411": (Entity("Cheb", "CZ-411", "DISTRICT", "cs", "CZ-41"),),
        "CZ-412": (Entity("Karlovy Vary", "CZ-412", "DISTRICT", "cs", "CZ-41"),),
        "CZ-413": (Entity("Sokolov", "CZ-413", "DISTRICT", "cs", "CZ-41"),),
        "CZ-42": (Entity("Ústecký kraj", "CZ-42", "REGION", "cs", ""),),
        "CZ-421": (Entity("Děčín", "CZ-421", "DISTRICT", "cs", "CZ-42"),),
        "CZ-422": (Entity("Chomutov", "CZ-422", "DISTRICT", "cs", "CZ-42"),),
        "CZ-423": (Entity("Litoměřice", "CZ-423", "DISTRICT", "cs", "CZ-42"),),
        "CZ-424": (Entity("Louny", "CZ-424", "DISTRICT", "cs", "CZ-42"),),
        "CZ-425": (Entity("Most", "CZ-425", "DISTRICT", "cs", "CZ-42"),),
        "CZ-426": (Entity("Teplice", "CZ-426", "DISTRICT", "cs", "CZ-42"),),
        "CZ-427": (Entity("Ústí nad Labem", "CZ-427", "DISTRICT", "cs", "CZ-42"),),
        "CZ-51": (Entity("Liberecký kraj", "CZ-51", "REGION", "cs", ""),),
        "CZ-511": (Entity("Česká Lípa", "CZ-511", "DISTRICT", "cs", "CZ-51"),),
        "CZ-512": (Entity("Jablonec nad Nisou", "CZ-512", "DISTRICT", "cs", "CZ-51"),),
        "CZ-513": (Entity("Liberec", "CZ-513", "DISTRICT", "cs", "CZ-51"),),
        "CZ-514": (Entity("Semily", "CZ-514", "DISTRICT", "cs", "CZ-51"),),
        "CZ-52": (Entity("Královéhradecký kraj", "CZ-52", "REGION", "cs", ""),),
        "CZ-521": (Entity("Hradec Králové", "CZ-521", "DISTRICT", "cs", "CZ-52"),),
        "CZ-522": (Entity("Jičín", "CZ-522", "DISTRICT", "cs", "CZ-52"),),
        "CZ-523": (Entity("Náchod", "CZ-523", "DISTRICT", "cs", "CZ-52"),),
        "CZ-524": (Entity("Rychnov nad Kněžnou", "CZ-524", "DISTRICT", "cs", "CZ-52"),),
        "CZ-525": (Entity("Trutnov", "CZ-525", "DISTRICT", "cs", "CZ-52"),),
        "CZ-53": (Entity("Pardubický kraj", "CZ-53", "REGION", "cs", ""),),
        "CZ-531": (Entity("Chrudim", "CZ-531", "DISTRICT", "cs", "CZ-53"),),
        "CZ-532": (Entity("Pardubice", "CZ-532", "DISTRICT", "cs", "CZ-53"),),
        "CZ-533": (Entity("Svitavy", "CZ-533", "DISTRICT", "cs", "CZ-53"),),
        "CZ-534": (Entity("Ústí nad Orlicí", "CZ-534", "DISTRICT", "cs", "CZ-53"),),
        "CZ-63": (Entity("Kraj Vysočina", "CZ-63", "REGION", "cs", ""),),
        "CZ-631": (Entity("Havlíčkův Brod", "CZ-631", "DISTRICT", "cs", "CZ-63"),),
        "CZ-632": (Entity("Jihlava", "CZ-632", "DISTRICT", "cs", "CZ-63"),),
        "CZ-633": (Entity("Pelhřimov", "CZ-633", "DISTRICT", "cs", "CZ-63"),),
        "CZ-634": (Entity("Třebíč", "CZ-634", "DISTRICT", "cs", "CZ-63"),),
        "CZ-635": (Entity("Žďár nad Sázavou", "CZ-635", "DISTRICT", "cs", "CZ-63"),),
        "CZ-64": (Entity("Jihomoravský kraj", "CZ-64", "REGION", "cs", ""),),
        "CZ-641": (Entity("Blansko", "CZ-641", "DISTRICT", "cs", "CZ-64"),),
        "CZ-642": (Entity("Brno-město", "CZ-642", "DISTRICT", "cs", "CZ-64"),),
        "CZ-643": (Entity("Brno-venkov", "CZ-643", "DISTRICT", "cs", "CZ-64"),),
        "CZ-644": (Entity("Břeclav", "CZ-644", "DISTRICT", "cs", "CZ-64"),),
        "CZ-645": (Entity("Hodonín", "CZ-645", "DISTRICT", "cs", "CZ-64"),),
        "CZ-646": (Entity("Vyškov", "CZ-646", "DISTRICT", "cs", "CZ-64"),),
        "CZ-647": (Entity("Znojmo", "CZ-647", "DISTRICT", "cs", "CZ-64"),),
        "CZ-71": (Entity("Olomoucký kraj", "CZ-71", "REGION", "cs", ""),),
        "CZ-711": (Entity("Jeseník", "CZ-711", "DISTRICT", "cs", "CZ-71"),),
        "CZ-712": (Entity("Olomouc", "CZ-712", "DISTRICT", "cs", "CZ-71"),),
        "CZ-713": (Entity("Prostějov", "CZ-713", "DISTRICT", "cs", "CZ-71"),),
        "CZ-714": (Entity("Přerov", "CZ-714", "DISTRICT", "cs", "CZ-71"),),
        "CZ-715": (Entity("Šumperk", "CZ-715", "DISTRICT", "cs", "CZ-71"),),
        "CZ-72": (Entity("Zlínský kraj", "CZ-72", "REGION", "cs", ""),),
        "CZ-721": (Entity("Kroměříž", "CZ-721", "DISTRICT", "cs", "CZ-72"),),
        "CZ-722": (Entity("Uherské Hradiště", "CZ-722", "DISTRICT", "cs", "CZ-72"),),
        "CZ-723": (Entity("Vsetín", "CZ-723", "DISTRICT", "cs", "CZ-72"),),
        "CZ-724": (Entity("Zlín", "CZ-724", "DISTRICT", "cs", "CZ-72"),),
        "CZ-80": (Entity("Moravskoslezský kraj", "CZ-80", "REGION", "cs", ""),),
        "CZ-801": (Entity("Bruntál", "CZ-801", "DISTRICT", "cs", "CZ-80"),),
        "CZ-802": (Entity("Frýdek-Místek", "CZ-802", "DISTRICT", "cs", "CZ-80"),),
        "CZ-803": (Entity("Karviná", "CZ-803", "DISTRICT", "cs", "CZ-80"),),
        "CZ-804": (Entity("Nový Jičín", "CZ-804", "DISTRICT", "cs", "CZ-80"),),
        "CZ-805": (Entity("Opava", "CZ-805", "DISTRICT", "cs", "CZ-80"),),
        "CZ-806": (Entity("Ostrava-město", "CZ-806", "DISTRICT", "cs", "CZ-80"),),
    }
