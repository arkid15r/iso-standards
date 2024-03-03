"""ISO 3166-2 MK standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:MK
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "MK-101": (Entity("Veles", "MK-101", "MUNICIPALITY", "mk", ""),),
        "MK-102": (Entity("Gradsko", "MK-102", "MUNICIPALITY", "mk", ""),),
        "MK-103": (Entity("Demir Kapija", "MK-103", "MUNICIPALITY", "mk", ""),),
        "MK-104": (Entity("Kavadarci", "MK-104", "MUNICIPALITY", "mk", ""),),
        "MK-105": (Entity("Lozovo", "MK-105", "MUNICIPALITY", "mk", ""),),
        "MK-106": (Entity("Negotino", "MK-106", "MUNICIPALITY", "mk", ""),),
        "MK-107": (Entity("Rosoman", "MK-107", "MUNICIPALITY", "mk", ""),),
        "MK-108": (Entity("Sveti Nikole", "MK-108", "MUNICIPALITY", "mk", ""),),
        "MK-109": (Entity("Čaška", "MK-109", "MUNICIPALITY", "mk", ""),),
        "MK-201": (Entity("Berovo", "MK-201", "MUNICIPALITY", "mk", ""),),
        "MK-202": (Entity("Vinica", "MK-202", "MUNICIPALITY", "mk", ""),),
        "MK-203": (Entity("Delčevo", "MK-203", "MUNICIPALITY", "mk", ""),),
        "MK-204": (Entity("Zrnovci", "MK-204", "MUNICIPALITY", "mk", ""),),
        "MK-205": (Entity("Karbinci", "MK-205", "MUNICIPALITY", "mk", ""),),
        "MK-206": (Entity("Kočani", "MK-206", "MUNICIPALITY", "mk", ""),),
        "MK-207": (Entity("Makedonska Kamenica", "MK-207", "MUNICIPALITY", "mk", ""),),
        "MK-208": (Entity("Pehčevo", "MK-208", "MUNICIPALITY", "mk", ""),),
        "MK-209": (Entity("Probištip", "MK-209", "MUNICIPALITY", "mk", ""),),
        "MK-210": (Entity("Češinovo-Obleševo", "MK-210", "MUNICIPALITY", "mk", ""),),
        "MK-211": (Entity("Štip", "MK-211", "MUNICIPALITY", "mk", ""),),
        "MK-301": (Entity("Vevčani", "MK-301", "MUNICIPALITY", "mk", ""),),
        "MK-303": (Entity("Debar", "MK-303", "MUNICIPALITY", "mk", ""),),
        "MK-304": (Entity("Debrca", "MK-304", "MUNICIPALITY", "mk", ""),),
        "MK-307": (Entity("Kičevo", "MK-307", "MUNICIPALITY", "mk", ""),),
        "MK-308": (Entity("Makedonski Brod", "MK-308", "MUNICIPALITY", "mk", ""),),
        "MK-310": (Entity("Ohrid", "MK-310", "MUNICIPALITY", "mk", ""),),
        "MK-311": (Entity("Plasnica", "MK-311", "MUNICIPALITY", "mk", ""),),
        "MK-312": (Entity("Struga", "MK-312", "MUNICIPALITY", "mk", ""),),
        "MK-313": (Entity("Centar Župa", "MK-313", "MUNICIPALITY", "mk", ""),),
        "MK-401": (Entity("Bogdanci", "MK-401", "MUNICIPALITY", "mk", ""),),
        "MK-402": (Entity("Bosilovo", "MK-402", "MUNICIPALITY", "mk", ""),),
        "MK-403": (Entity("Valandovo", "MK-403", "MUNICIPALITY", "mk", ""),),
        "MK-404": (Entity("Vasilevo", "MK-404", "MUNICIPALITY", "mk", ""),),
        "MK-405": (Entity("Gevgelija", "MK-405", "MUNICIPALITY", "mk", ""),),
        "MK-406": (Entity("Dojran", "MK-406", "MUNICIPALITY", "mk", ""),),
        "MK-407": (Entity("Konče", "MK-407", "MUNICIPALITY", "mk", ""),),
        "MK-408": (Entity("Novo Selo", "MK-408", "MUNICIPALITY", "mk", ""),),
        "MK-409": (Entity("Radoviš", "MK-409", "MUNICIPALITY", "mk", ""),),
        "MK-410": (Entity("Strumica", "MK-410", "MUNICIPALITY", "mk", ""),),
        "MK-501": (Entity("Bitola", "MK-501", "MUNICIPALITY", "mk", ""),),
        "MK-502": (Entity("Demir Hisar", "MK-502", "MUNICIPALITY", "mk", ""),),
        "MK-503": (Entity("Dolneni", "MK-503", "MUNICIPALITY", "mk", ""),),
        "MK-504": (Entity("Krivogaštani", "MK-504", "MUNICIPALITY", "mk", ""),),
        "MK-505": (Entity("Kruševo", "MK-505", "MUNICIPALITY", "mk", ""),),
        "MK-506": (Entity("Mogila", "MK-506", "MUNICIPALITY", "mk", ""),),
        "MK-507": (Entity("Novaci", "MK-507", "MUNICIPALITY", "mk", ""),),
        "MK-508": (Entity("Prilep", "MK-508", "MUNICIPALITY", "mk", ""),),
        "MK-509": (Entity("Resen", "MK-509", "MUNICIPALITY", "mk", ""),),
        "MK-601": (Entity("Bogovinje", "MK-601", "MUNICIPALITY", "mk", ""),),
        "MK-602": (Entity("Brvenica", "MK-602", "MUNICIPALITY", "mk", ""),),
        "MK-603": (Entity("Vrapčište", "MK-603", "MUNICIPALITY", "mk", ""),),
        "MK-604": (Entity("Gostivar", "MK-604", "MUNICIPALITY", "mk", ""),),
        "MK-605": (Entity("Želino", "MK-605", "MUNICIPALITY", "mk", ""),),
        "MK-606": (Entity("Jegunovce", "MK-606", "MUNICIPALITY", "mk", ""),),
        "MK-607": (Entity("Mavrovo i Rostuše", "MK-607", "MUNICIPALITY", "mk", ""),),
        "MK-608": (Entity("Tearce", "MK-608", "MUNICIPALITY", "mk", ""),),
        "MK-609": (Entity("Tetovo", "MK-609", "MUNICIPALITY", "mk", ""),),
        "MK-701": (Entity("Kratovo", "MK-701", "MUNICIPALITY", "mk", ""),),
        "MK-702": (Entity("Kriva Palanka", "MK-702", "MUNICIPALITY", "mk", ""),),
        "MK-703": (Entity("Kumanovo", "MK-703", "MUNICIPALITY", "mk", ""),),
        "MK-704": (Entity("Lipkovo", "MK-704", "MUNICIPALITY", "mk", ""),),
        "MK-705": (Entity("Rankovce", "MK-705", "MUNICIPALITY", "mk", ""),),
        "MK-706": (Entity("Staro Nagoričane", "MK-706", "MUNICIPALITY", "mk", ""),),
        "MK-801": (Entity("Aerodrom †", "MK-801", "MUNICIPALITY", "mk", ""),),
        "MK-802": (Entity("Aračinovo", "MK-802", "MUNICIPALITY", "mk", ""),),
        "MK-803": (Entity("Butel †", "MK-803", "MUNICIPALITY", "mk", ""),),
        "MK-804": (Entity("Gazi Baba †", "MK-804", "MUNICIPALITY", "mk", ""),),
        "MK-805": (Entity("Gjorče Petrov †", "MK-805", "MUNICIPALITY", "mk", ""),),
        "MK-806": (Entity("Zelenikovo", "MK-806", "MUNICIPALITY", "mk", ""),),
        "MK-807": (Entity("Ilinden", "MK-807", "MUNICIPALITY", "mk", ""),),
        "MK-808": (Entity("Karpoš †", "MK-808", "MUNICIPALITY", "mk", ""),),
        "MK-809": (Entity("Kisela Voda †", "MK-809", "MUNICIPALITY", "mk", ""),),
        "MK-810": (Entity("Petrovec", "MK-810", "MUNICIPALITY", "mk", ""),),
        "MK-811": (Entity("Saraj †", "MK-811", "MUNICIPALITY", "mk", ""),),
        "MK-812": (Entity("Sopište", "MK-812", "MUNICIPALITY", "mk", ""),),
        "MK-813": (Entity("Studeničani", "MK-813", "MUNICIPALITY", "mk", ""),),
        "MK-814": (Entity("Centar †", "MK-814", "MUNICIPALITY", "mk", ""),),
        "MK-815": (Entity("Čair †", "MK-815", "MUNICIPALITY", "mk", ""),),
        "MK-816": (Entity("Čučer-Sandevo", "MK-816", "MUNICIPALITY", "mk", ""),),
        "MK-817": (Entity("Šuto Orizari †", "MK-817", "MUNICIPALITY", "mk", ""),),
    }
