"""ISO 3166-2 IT standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:IT
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "IT-21": (Entity("Piemonte", "IT-21", "REGION", "it", ""),),
        "IT-23": (
            Entity("Val d'Aoste", "IT-23", "AUTONOMOUS REGION", "fr", ""),
            Entity("Valle d'Aosta", "IT-23", "AUTONOMOUS REGION", "it", ""),
        ),
        "IT-25": (Entity("Lombardia", "IT-25", "REGION", "it", ""),),
        "IT-32": (
            Entity("Trentino-Alto Adige", "IT-32", "AUTONOMOUS REGION", "it", ""),
            Entity("Trentino-Südtirol", "IT-32", "AUTONOMOUS REGION", "de", ""),
        ),
        "IT-34": (Entity("Veneto", "IT-34", "REGION", "it", ""),),
        "IT-36": (Entity("Friuli Venezia Giulia", "IT-36", "AUTONOMOUS REGION", "it", ""),),
        "IT-42": (Entity("Liguria", "IT-42", "REGION", "it", ""),),
        "IT-45": (Entity("Emilia-Romagna", "IT-45", "REGION", "it", ""),),
        "IT-52": (Entity("Toscana", "IT-52", "REGION", "it", ""),),
        "IT-55": (Entity("Umbria", "IT-55", "REGION", "it", ""),),
        "IT-57": (Entity("Marche", "IT-57", "REGION", "it", ""),),
        "IT-62": (Entity("Lazio", "IT-62", "REGION", "it", ""),),
        "IT-65": (Entity("Abruzzo", "IT-65", "REGION", "it", ""),),
        "IT-67": (Entity("Molise", "IT-67", "REGION", "it", ""),),
        "IT-72": (Entity("Campania", "IT-72", "REGION", "it", ""),),
        "IT-75": (Entity("Puglia", "IT-75", "REGION", "it", ""),),
        "IT-77": (Entity("Basilicata", "IT-77", "REGION", "it", ""),),
        "IT-78": (Entity("Calabria", "IT-78", "REGION", "it", ""),),
        "IT-82": (Entity("Sicilia", "IT-82", "AUTONOMOUS REGION", "it", ""),),
        "IT-88": (Entity("Sardegna", "IT-88", "AUTONOMOUS REGION", "it", ""),),
        "IT-AG": (Entity("Agrigento", "IT-AG", "FREE MUNICIPAL CONSORTIUM", "it", "IT-82"),),
        "IT-AL": (Entity("Alessandria", "IT-AL", "PROVINCE", "it", "IT-21"),),
        "IT-AN": (Entity("Ancona", "IT-AN", "PROVINCE", "it", "IT-57"),),
        "IT-AP": (Entity("Ascoli Piceno", "IT-AP", "PROVINCE", "it", "IT-57"),),
        "IT-AQ": (Entity("L'Aquila", "IT-AQ", "PROVINCE", "it", "IT-65"),),
        "IT-AR": (Entity("Arezzo", "IT-AR", "PROVINCE", "it", "IT-52"),),
        "IT-AT": (Entity("Asti", "IT-AT", "PROVINCE", "it", "IT-21"),),
        "IT-AV": (Entity("Avellino", "IT-AV", "PROVINCE", "it", "IT-72"),),
        "IT-BA": (Entity("Bari", "IT-BA", "METROPOLITAN CITY", "it", "IT-75"),),
        "IT-BG": (Entity("Bergamo", "IT-BG", "PROVINCE", "it", "IT-25"),),
        "IT-BI": (Entity("Biella", "IT-BI", "PROVINCE", "it", "IT-21"),),
        "IT-BL": (Entity("Belluno", "IT-BL", "PROVINCE", "it", "IT-34"),),
        "IT-BN": (Entity("Benevento", "IT-BN", "PROVINCE", "it", "IT-72"),),
        "IT-BO": (Entity("Bologna", "IT-BO", "METROPOLITAN CITY", "it", "IT-45"),),
        "IT-BR": (Entity("Brindisi", "IT-BR", "PROVINCE", "it", "IT-75"),),
        "IT-BS": (Entity("Brescia", "IT-BS", "PROVINCE", "it", "IT-25"),),
        "IT-BT": (Entity("Barletta-Andria-Trani", "IT-BT", "PROVINCE", "it", "IT-75"),),
        "IT-BZ": (
            Entity("Bolzano", "IT-BZ", "AUTONOMOUS PROVINCE", "it", "IT-32"),
            Entity("Bozen", "IT-BZ", "AUTONOMOUS PROVINCE", "de", "IT-32"),
        ),
        "IT-CA": (Entity("Cagliari", "IT-CA", "METROPOLITAN CITY", "it", "IT-88"),),
        "IT-CB": (Entity("Campobasso", "IT-CB", "PROVINCE", "it", "IT-67"),),
        "IT-CE": (Entity("Caserta", "IT-CE", "PROVINCE", "it", "IT-72"),),
        "IT-CH": (Entity("Chieti", "IT-CH", "PROVINCE", "it", "IT-65"),),
        "IT-CL": (Entity("Caltanissetta", "IT-CL", "FREE MUNICIPAL CONSORTIUM", "it", "IT-82"),),
        "IT-CN": (Entity("Cuneo", "IT-CN", "PROVINCE", "it", "IT-21"),),
        "IT-CO": (Entity("Como", "IT-CO", "PROVINCE", "it", "IT-25"),),
        "IT-CR": (Entity("Cremona", "IT-CR", "PROVINCE", "it", "IT-25"),),
        "IT-CS": (Entity("Cosenza", "IT-CS", "PROVINCE", "it", "IT-78"),),
        "IT-CT": (Entity("Catania", "IT-CT", "METROPOLITAN CITY", "it", "IT-82"),),
        "IT-CZ": (Entity("Catanzaro", "IT-CZ", "PROVINCE", "it", "IT-78"),),
        "IT-EN": (Entity("Enna", "IT-EN", "FREE MUNICIPAL CONSORTIUM", "it", "IT-82"),),
        "IT-FC": (Entity("Forlì-Cesena", "IT-FC", "PROVINCE", "it", "IT-45"),),
        "IT-FE": (Entity("Ferrara", "IT-FE", "PROVINCE", "it", "IT-45"),),
        "IT-FG": (Entity("Foggia", "IT-FG", "PROVINCE", "it", "IT-75"),),
        "IT-FI": (Entity("Firenze", "IT-FI", "METROPOLITAN CITY", "it", "IT-52"),),
        "IT-FM": (Entity("Fermo", "IT-FM", "PROVINCE", "it", "IT-57"),),
        "IT-FR": (Entity("Frosinone", "IT-FR", "PROVINCE", "it", "IT-62"),),
        "IT-GE": (Entity("Genova", "IT-GE", "METROPOLITAN CITY", "it", "IT-42"),),
        "IT-GO": (Entity("Gorizia", "IT-GO", "DECENTRALIZED REGIONAL ENTITY", "it", "IT-36"),),
        "IT-GR": (Entity("Grosseto", "IT-GR", "PROVINCE", "it", "IT-52"),),
        "IT-IM": (Entity("Imperia", "IT-IM", "PROVINCE", "it", "IT-42"),),
        "IT-IS": (Entity("Isernia", "IT-IS", "PROVINCE", "it", "IT-67"),),
        "IT-KR": (Entity("Crotone", "IT-KR", "PROVINCE", "it", "IT-78"),),
        "IT-LC": (Entity("Lecco", "IT-LC", "PROVINCE", "it", "IT-25"),),
        "IT-LE": (Entity("Lecce", "IT-LE", "PROVINCE", "it", "IT-75"),),
        "IT-LI": (Entity("Livorno", "IT-LI", "PROVINCE", "it", "IT-52"),),
        "IT-LO": (Entity("Lodi", "IT-LO", "PROVINCE", "it", "IT-25"),),
        "IT-LT": (Entity("Latina", "IT-LT", "PROVINCE", "it", "IT-62"),),
        "IT-LU": (Entity("Lucca", "IT-LU", "PROVINCE", "it", "IT-52"),),
        "IT-MB": (Entity("Monza e Brianza", "IT-MB", "PROVINCE", "it", "IT-25"),),
        "IT-MC": (Entity("Macerata", "IT-MC", "PROVINCE", "it", "IT-57"),),
        "IT-ME": (Entity("Messina", "IT-ME", "METROPOLITAN CITY", "it", "IT-82"),),
        "IT-MI": (Entity("Milano", "IT-MI", "METROPOLITAN CITY", "it", "IT-25"),),
        "IT-MN": (Entity("Mantova", "IT-MN", "PROVINCE", "it", "IT-25"),),
        "IT-MO": (Entity("Modena", "IT-MO", "PROVINCE", "it", "IT-45"),),
        "IT-MS": (Entity("Massa-Carrara", "IT-MS", "PROVINCE", "it", "IT-52"),),
        "IT-MT": (Entity("Matera", "IT-MT", "PROVINCE", "it", "IT-77"),),
        "IT-NA": (Entity("Napoli", "IT-NA", "METROPOLITAN CITY", "it", "IT-72"),),
        "IT-NO": (Entity("Novara", "IT-NO", "PROVINCE", "it", "IT-21"),),
        "IT-NU": (Entity("Nuoro", "IT-NU", "PROVINCE", "it", "IT-88"),),
        "IT-OR": (Entity("Oristano", "IT-OR", "PROVINCE", "it", "IT-88"),),
        "IT-PA": (Entity("Palermo", "IT-PA", "METROPOLITAN CITY", "it", "IT-82"),),
        "IT-PC": (Entity("Piacenza", "IT-PC", "PROVINCE", "it", "IT-45"),),
        "IT-PD": (Entity("Padova", "IT-PD", "PROVINCE", "it", "IT-34"),),
        "IT-PE": (Entity("Pescara", "IT-PE", "PROVINCE", "it", "IT-65"),),
        "IT-PG": (Entity("Perugia", "IT-PG", "PROVINCE", "it", "IT-55"),),
        "IT-PI": (Entity("Pisa", "IT-PI", "PROVINCE", "it", "IT-52"),),
        "IT-PN": (Entity("Pordenone", "IT-PN", "DECENTRALIZED REGIONAL ENTITY", "it", "IT-36"),),
        "IT-PO": (Entity("Prato", "IT-PO", "PROVINCE", "it", "IT-52"),),
        "IT-PR": (Entity("Parma", "IT-PR", "PROVINCE", "it", "IT-45"),),
        "IT-PT": (Entity("Pistoia", "IT-PT", "PROVINCE", "it", "IT-52"),),
        "IT-PU": (Entity("Pesaro e Urbino", "IT-PU", "PROVINCE", "it", "IT-57"),),
        "IT-PV": (Entity("Pavia", "IT-PV", "PROVINCE", "it", "IT-25"),),
        "IT-PZ": (Entity("Potenza", "IT-PZ", "PROVINCE", "it", "IT-77"),),
        "IT-RA": (Entity("Ravenna", "IT-RA", "PROVINCE", "it", "IT-45"),),
        "IT-RC": (Entity("Reggio Calabria", "IT-RC", "METROPOLITAN CITY", "it", "IT-78"),),
        "IT-RE": (Entity("Reggio Emilia", "IT-RE", "PROVINCE", "it", "IT-45"),),
        "IT-RG": (Entity("Ragusa", "IT-RG", "FREE MUNICIPAL CONSORTIUM", "it", "IT-82"),),
        "IT-RI": (Entity("Rieti", "IT-RI", "PROVINCE", "it", "IT-62"),),
        "IT-RM": (Entity("Roma", "IT-RM", "METROPOLITAN CITY", "it", "IT-62"),),
        "IT-RN": (Entity("Rimini", "IT-RN", "PROVINCE", "it", "IT-45"),),
        "IT-RO": (Entity("Rovigo", "IT-RO", "PROVINCE", "it", "IT-34"),),
        "IT-SA": (Entity("Salerno", "IT-SA", "PROVINCE", "it", "IT-72"),),
        "IT-SI": (Entity("Siena", "IT-SI", "PROVINCE", "it", "IT-52"),),
        "IT-SO": (Entity("Sondrio", "IT-SO", "PROVINCE", "it", "IT-25"),),
        "IT-SP": (Entity("La Spezia", "IT-SP", "PROVINCE", "it", "IT-42"),),
        "IT-SR": (Entity("Siracusa", "IT-SR", "FREE MUNICIPAL CONSORTIUM", "it", "IT-82"),),
        "IT-SS": (Entity("Sassari", "IT-SS", "PROVINCE", "it", "IT-88"),),
        "IT-SU": (Entity("Sud Sardegna", "IT-SU", "PROVINCE", "it", "IT-88"),),
        "IT-SV": (Entity("Savona", "IT-SV", "PROVINCE", "it", "IT-42"),),
        "IT-TA": (Entity("Taranto", "IT-TA", "PROVINCE", "it", "IT-75"),),
        "IT-TE": (Entity("Teramo", "IT-TE", "PROVINCE", "it", "IT-65"),),
        "IT-TN": (Entity("Trento", "IT-TN", "AUTONOMOUS PROVINCE", "it", "IT-32"),),
        "IT-TO": (Entity("Torino", "IT-TO", "METROPOLITAN CITY", "it", "IT-21"),),
        "IT-TP": (Entity("Trapani", "IT-TP", "FREE MUNICIPAL CONSORTIUM", "it", "IT-82"),),
        "IT-TR": (Entity("Terni", "IT-TR", "PROVINCE", "it", "IT-55"),),
        "IT-TS": (Entity("Trieste", "IT-TS", "DECENTRALIZED REGIONAL ENTITY", "it", "IT-36"),),
        "IT-TV": (Entity("Treviso", "IT-TV", "PROVINCE", "it", "IT-34"),),
        "IT-UD": (Entity("Udine", "IT-UD", "DECENTRALIZED REGIONAL ENTITY", "it", "IT-36"),),
        "IT-VA": (Entity("Varese", "IT-VA", "PROVINCE", "it", "IT-25"),),
        "IT-VB": (Entity("Verbano-Cusio-Ossola", "IT-VB", "PROVINCE", "it", "IT-21"),),
        "IT-VC": (Entity("Vercelli", "IT-VC", "PROVINCE", "it", "IT-21"),),
        "IT-VE": (Entity("Venezia", "IT-VE", "METROPOLITAN CITY", "it", "IT-34"),),
        "IT-VI": (Entity("Vicenza", "IT-VI", "PROVINCE", "it", "IT-34"),),
        "IT-VR": (Entity("Verona", "IT-VR", "PROVINCE", "it", "IT-34"),),
        "IT-VT": (Entity("Viterbo", "IT-VT", "PROVINCE", "it", "IT-62"),),
        "IT-VV": (Entity("Vibo Valentia", "IT-VV", "PROVINCE", "it", "IT-78"),),
    }
