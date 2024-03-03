"""ISO 3166-2 IS standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:IS
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "IS-1": (Entity("Höfuðborgarsvæði", "IS-1", "REGION", "is", ""),),
        "IS-2": (Entity("Suðurnes", "IS-2", "REGION", "is", ""),),
        "IS-3": (Entity("Vesturland", "IS-3", "REGION", "is", ""),),
        "IS-4": (Entity("Vestfirðir", "IS-4", "REGION", "is", ""),),
        "IS-5": (Entity("Norðurland vestra", "IS-5", "REGION", "is", ""),),
        "IS-6": (Entity("Norðurland eystra", "IS-6", "REGION", "is", ""),),
        "IS-7": (Entity("Austurland", "IS-7", "REGION", "is", ""),),
        "IS-8": (Entity("Suðurland", "IS-8", "REGION", "is", ""),),
        "IS-AKN": (Entity("Akraneskaupstaður", "IS-AKN", "MUNICIPALITY", "is", "IS-3"),),
        "IS-AKU": (Entity("Akureyrarbær", "IS-AKU", "MUNICIPALITY", "is", "IS-6"),),
        "IS-ARN": (Entity("Árneshreppur", "IS-ARN", "MUNICIPALITY", "is", "IS-4"),),
        "IS-ASA": (Entity("Ásahreppur", "IS-ASA", "MUNICIPALITY", "is", "IS-8"),),
        "IS-BLA": (Entity("Bláskógabyggð", "IS-BLA", "MUNICIPALITY", "is", "IS-8"),),
        "IS-BOG": (Entity("Borgarbyggð", "IS-BOG", "MUNICIPALITY", "is", "IS-3"),),
        "IS-BOL": (Entity("Bolungarvíkurkaupstaður", "IS-BOL", "MUNICIPALITY", "is", "IS-4"),),
        "IS-DAB": (Entity("Dalabyggð", "IS-DAB", "MUNICIPALITY", "is", "IS-3"),),
        "IS-DAV": (Entity("Dalvíkurbyggð", "IS-DAV", "MUNICIPALITY", "is", "IS-6"),),
        "IS-EOM": (Entity("Eyja- og Miklaholtshreppur", "IS-EOM", "MUNICIPALITY", "is", "IS-3"),),
        "IS-EYF": (Entity("Eyjafjarðarsveit", "IS-EYF", "MUNICIPALITY", "is", "IS-6"),),
        "IS-FJD": (Entity("Fjarðabyggð", "IS-FJD", "MUNICIPALITY", "is", "IS-7"),),
        "IS-FJL": (Entity("Fjallabyggð", "IS-FJL", "MUNICIPALITY", "is", "IS-6"),),
        "IS-FLA": (Entity("Flóahreppur", "IS-FLA", "MUNICIPALITY", "is", "IS-8"),),
        "IS-FLR": (Entity("Fljótsdalshreppur", "IS-FLR", "MUNICIPALITY", "is", "IS-7"),),
        "IS-GAR": (Entity("Garðabær", "IS-GAR", "MUNICIPALITY", "is", "IS-1"),),
        "IS-GOG": (
            Entity("Grímsnes- og Grafningshreppur", "IS-GOG", "MUNICIPALITY", "is", "IS-8"),
        ),
        "IS-GRN": (Entity("Grindavíkurbær", "IS-GRN", "MUNICIPALITY", "is", "IS-2"),),
        "IS-GRU": (Entity("Grundarfjarðarbær", "IS-GRU", "MUNICIPALITY", "is", "IS-3"),),
        "IS-GRY": (Entity("Grýtubakkahreppur", "IS-GRY", "MUNICIPALITY", "is", "IS-6"),),
        "IS-HAF": (Entity("Hafnarfjarðarkaupstaður", "IS-HAF", "MUNICIPALITY", "is", "IS-1"),),
        "IS-HRG": (Entity("Hörgársveit", "IS-HRG", "MUNICIPALITY", "is", "IS-6"),),
        "IS-HRU": (Entity("Hrunamannahreppur", "IS-HRU", "MUNICIPALITY", "is", "IS-8"),),
        "IS-HUG": (Entity("Húnabyggð", "IS-HUG", "MUNICIPALITY", "is", "IS-5"),),
        "IS-HUV": (Entity("Húnaþing vestra", "IS-HUV", "MUNICIPALITY", "is", "IS-5"),),
        "IS-HVA": (Entity("Hvalfjarðarsveit", "IS-HVA", "MUNICIPALITY", "is", "IS-3"),),
        "IS-HVE": (Entity("Hveragerðisbær", "IS-HVE", "MUNICIPALITY", "is", "IS-8"),),
        "IS-ISA": (Entity("Ísafjarðarbær", "IS-ISA", "MUNICIPALITY", "is", "IS-4"),),
        "IS-KAL": (Entity("Kaldrananeshreppur", "IS-KAL", "MUNICIPALITY", "is", "IS-4"),),
        "IS-KJO": (Entity("Kjósarhreppur", "IS-KJO", "MUNICIPALITY", "is", "IS-1"),),
        "IS-KOP": (Entity("Kópavogsbær", "IS-KOP", "MUNICIPALITY", "is", "IS-1"),),
        "IS-LAN": (Entity("Langanesbyggð", "IS-LAN", "MUNICIPALITY", "is", "IS-6"),),
        "IS-MOS": (Entity("Mosfellsbær", "IS-MOS", "MUNICIPALITY", "is", "IS-1"),),
        "IS-MUL": (Entity("Múlaþing", "IS-MUL", "MUNICIPALITY", "is", "IS-7"),),
        "IS-MYR": (Entity("Mýrdalshreppur", "IS-MYR", "MUNICIPALITY", "is", "IS-8"),),
        "IS-NOR": (Entity("Norðurþing", "IS-NOR", "MUNICIPALITY", "is", "IS-6"),),
        "IS-RGE": (Entity("Rangárþing eystra", "IS-RGE", "MUNICIPALITY", "is", "IS-8"),),
        "IS-RGY": (Entity("Rangárþing ytra", "IS-RGY", "MUNICIPALITY", "is", "IS-8"),),
        "IS-RHH": (Entity("Reykhólahreppur", "IS-RHH", "MUNICIPALITY", "is", "IS-4"),),
        "IS-RKN": (Entity("Reykjanesbær", "IS-RKN", "MUNICIPALITY", "is", "IS-2"),),
        "IS-RKV": (Entity("Reykjavíkurborg", "IS-RKV", "MUNICIPALITY", "is", "IS-1"),),
        "IS-SBT": (Entity("Svalbarðsstrandarhreppur", "IS-SBT", "MUNICIPALITY", "is", "IS-6"),),
        "IS-SDN": (Entity("Suðurnesjabær", "IS-SDN", "MUNICIPALITY", "is", "IS-2"),),
        "IS-SDV": (Entity("Súðavíkurhreppur", "IS-SDV", "MUNICIPALITY", "is", "IS-4"),),
        "IS-SEL": (Entity("Seltjarnarnesbær", "IS-SEL", "MUNICIPALITY", "is", "IS-1"),),
        "IS-SFA": (Entity("Sveitarfélagið Árborg", "IS-SFA", "MUNICIPALITY", "is", "IS-8"),),
        "IS-SHF": (Entity("Sveitarfélagið Hornafjörður", "IS-SHF", "MUNICIPALITY", "is", "IS-7"),),
        "IS-SKF": (Entity("Skaftárhreppur", "IS-SKF", "MUNICIPALITY", "is", "IS-8"),),
        "IS-SKG": (Entity("Skagabyggð", "IS-SKG", "MUNICIPALITY", "is", "IS-5"),),
        "IS-SKO": (Entity("Skorradalshreppur", "IS-SKO", "MUNICIPALITY", "is", "IS-3"),),
        "IS-SKR": (Entity("Skagafjörður", "IS-SKR", "MUNICIPALITY", "is", "IS-5"),),
        "IS-SNF": (Entity("Snæfellsbær", "IS-SNF", "MUNICIPALITY", "is", "IS-3"),),
        "IS-SOG": (Entity("Skeiða- og Gnúpverjahreppur", "IS-SOG", "MUNICIPALITY", "is", "IS-8"),),
        "IS-SOL": (Entity("Sveitarfélagið Ölfus", "IS-SOL", "MUNICIPALITY", "is", "IS-8"),),
        "IS-SSS": (Entity("Sveitarfélagið Skagaströnd", "IS-SSS", "MUNICIPALITY", "is", "IS-5"),),
        "IS-STR": (Entity("Strandabyggð", "IS-STR", "MUNICIPALITY", "is", "IS-4"),),
        "IS-STY": (Entity("Stykkishólmsbær", "IS-STY", "MUNICIPALITY", "is", "IS-3"),),
        "IS-SVG": (Entity("Sveitarfélagið Vogar", "IS-SVG", "MUNICIPALITY", "is", "IS-2"),),
        "IS-TAL": (Entity("Tálknafjarðarhreppur", "IS-TAL", "MUNICIPALITY", "is", "IS-4"),),
        "IS-THG": (Entity("Þingeyjarsveit", "IS-THG", "MUNICIPALITY", "is", "IS-6"),),
        "IS-TJO": (Entity("Tjörneshreppur", "IS-TJO", "MUNICIPALITY", "is", "IS-6"),),
        "IS-VEM": (Entity("Vestmannaeyjabær", "IS-VEM", "MUNICIPALITY", "is", "IS-8"),),
        "IS-VER": (Entity("Vesturbyggð", "IS-VER", "MUNICIPALITY", "is", "IS-4"),),
        "IS-VOP": (Entity("Vopnafjarðarhreppur", "IS-VOP", "MUNICIPALITY", "is", "IS-7"),),
    }
