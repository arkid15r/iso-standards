"""ISO 3166-2 SI standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:SI
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "SI-001": (Entity("Ajdovščina", "SI-001", "MUNICIPALITY", "sl", ""),),
        "SI-002": (Entity("Beltinci", "SI-002", "MUNICIPALITY", "sl", ""),),
        "SI-003": (Entity("Bled", "SI-003", "MUNICIPALITY", "sl", ""),),
        "SI-004": (Entity("Bohinj", "SI-004", "MUNICIPALITY", "sl", ""),),
        "SI-005": (Entity("Borovnica", "SI-005", "MUNICIPALITY", "sl", ""),),
        "SI-006": (Entity("Bovec", "SI-006", "MUNICIPALITY", "sl", ""),),
        "SI-007": (Entity("Brda", "SI-007", "MUNICIPALITY", "sl", ""),),
        "SI-008": (Entity("Brezovica", "SI-008", "MUNICIPALITY", "sl", ""),),
        "SI-009": (Entity("Brežice", "SI-009", "MUNICIPALITY", "sl", ""),),
        "SI-010": (Entity("Tišina", "SI-010", "MUNICIPALITY", "sl", ""),),
        "SI-011": (Entity("Celje", "SI-011", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-012": (Entity("Cerklje na Gorenjskem", "SI-012", "MUNICIPALITY", "sl", ""),),
        "SI-013": (Entity("Cerknica", "SI-013", "MUNICIPALITY", "sl", ""),),
        "SI-014": (Entity("Cerkno", "SI-014", "MUNICIPALITY", "sl", ""),),
        "SI-015": (Entity("Črenšovci", "SI-015", "MUNICIPALITY", "sl", ""),),
        "SI-016": (Entity("Črna na Koroškem", "SI-016", "MUNICIPALITY", "sl", ""),),
        "SI-017": (Entity("Črnomelj", "SI-017", "MUNICIPALITY", "sl", ""),),
        "SI-018": (Entity("Destrnik", "SI-018", "MUNICIPALITY", "sl", ""),),
        "SI-019": (Entity("Divača", "SI-019", "MUNICIPALITY", "sl", ""),),
        "SI-020": (Entity("Dobrepolje", "SI-020", "MUNICIPALITY", "sl", ""),),
        "SI-021": (Entity("Dobrova-Polhov Gradec", "SI-021", "MUNICIPALITY", "sl", ""),),
        "SI-022": (Entity("Dol pri Ljubljani", "SI-022", "MUNICIPALITY", "sl", ""),),
        "SI-023": (Entity("Domžale", "SI-023", "MUNICIPALITY", "sl", ""),),
        "SI-024": (Entity("Dornava", "SI-024", "MUNICIPALITY", "sl", ""),),
        "SI-025": (Entity("Dravograd", "SI-025", "MUNICIPALITY", "sl", ""),),
        "SI-026": (Entity("Duplek", "SI-026", "MUNICIPALITY", "sl", ""),),
        "SI-027": (Entity("Gorenja vas-Poljane", "SI-027", "MUNICIPALITY", "sl", ""),),
        "SI-028": (Entity("Gorišnica", "SI-028", "MUNICIPALITY", "sl", ""),),
        "SI-029": (Entity("Gornja Radgona", "SI-029", "MUNICIPALITY", "sl", ""),),
        "SI-030": (Entity("Gornji Grad", "SI-030", "MUNICIPALITY", "sl", ""),),
        "SI-031": (Entity("Gornji Petrovci", "SI-031", "MUNICIPALITY", "sl", ""),),
        "SI-032": (Entity("Grosuplje", "SI-032", "MUNICIPALITY", "sl", ""),),
        "SI-033": (Entity("Šalovci", "SI-033", "MUNICIPALITY", "sl", ""),),
        "SI-034": (Entity("Hrastnik", "SI-034", "MUNICIPALITY", "sl", ""),),
        "SI-035": (Entity("Hrpelje-Kozina", "SI-035", "MUNICIPALITY", "sl", ""),),
        "SI-036": (Entity("Idrija", "SI-036", "MUNICIPALITY", "sl", ""),),
        "SI-037": (Entity("Ig", "SI-037", "MUNICIPALITY", "sl", ""),),
        "SI-038": (Entity("Ilirska Bistrica", "SI-038", "MUNICIPALITY", "sl", ""),),
        "SI-039": (Entity("Ivančna Gorica", "SI-039", "MUNICIPALITY", "sl", ""),),
        "SI-040": (Entity("Izola", "SI-040", "MUNICIPALITY", "sl", ""),),
        "SI-041": (Entity("Jesenice", "SI-041", "MUNICIPALITY", "sl", ""),),
        "SI-042": (Entity("Juršinci", "SI-042", "MUNICIPALITY", "sl", ""),),
        "SI-043": (Entity("Kamnik", "SI-043", "MUNICIPALITY", "sl", ""),),
        "SI-044": (Entity("Kanal ob Soči", "SI-044", "MUNICIPALITY", "sl", ""),),
        "SI-045": (Entity("Kidričevo", "SI-045", "MUNICIPALITY", "sl", ""),),
        "SI-046": (Entity("Kobarid", "SI-046", "MUNICIPALITY", "sl", ""),),
        "SI-047": (Entity("Kobilje", "SI-047", "MUNICIPALITY", "sl", ""),),
        "SI-048": (Entity("Kočevje", "SI-048", "MUNICIPALITY", "sl", ""),),
        "SI-049": (Entity("Komen", "SI-049", "MUNICIPALITY", "sl", ""),),
        "SI-050": (Entity("Koper", "SI-050", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-051": (Entity("Kozje", "SI-051", "MUNICIPALITY", "sl", ""),),
        "SI-052": (Entity("Kranj", "SI-052", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-053": (Entity("Kranjska Gora", "SI-053", "MUNICIPALITY", "sl", ""),),
        "SI-054": (Entity("Krško", "SI-054", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-055": (Entity("Kungota", "SI-055", "MUNICIPALITY", "sl", ""),),
        "SI-056": (Entity("Kuzma", "SI-056", "MUNICIPALITY", "sl", ""),),
        "SI-057": (Entity("Laško", "SI-057", "MUNICIPALITY", "sl", ""),),
        "SI-058": (Entity("Lenart", "SI-058", "MUNICIPALITY", "sl", ""),),
        "SI-059": (Entity("Lendava", "SI-059", "MUNICIPALITY", "sl", ""),),
        "SI-060": (Entity("Litija", "SI-060", "MUNICIPALITY", "sl", ""),),
        "SI-061": (Entity("Ljubljana", "SI-061", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-062": (Entity("Ljubno", "SI-062", "MUNICIPALITY", "sl", ""),),
        "SI-063": (Entity("Ljutomer", "SI-063", "MUNICIPALITY", "sl", ""),),
        "SI-064": (Entity("Logatec", "SI-064", "MUNICIPALITY", "sl", ""),),
        "SI-065": (Entity("Loška dolina", "SI-065", "MUNICIPALITY", "sl", ""),),
        "SI-066": (Entity("Loški Potok", "SI-066", "MUNICIPALITY", "sl", ""),),
        "SI-067": (Entity("Luče", "SI-067", "MUNICIPALITY", "sl", ""),),
        "SI-068": (Entity("Lukovica", "SI-068", "MUNICIPALITY", "sl", ""),),
        "SI-069": (Entity("Majšperk", "SI-069", "MUNICIPALITY", "sl", ""),),
        "SI-070": (Entity("Maribor", "SI-070", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-071": (Entity("Medvode", "SI-071", "MUNICIPALITY", "sl", ""),),
        "SI-072": (Entity("Mengeš", "SI-072", "MUNICIPALITY", "sl", ""),),
        "SI-073": (Entity("Metlika", "SI-073", "MUNICIPALITY", "sl", ""),),
        "SI-074": (Entity("Mežica", "SI-074", "MUNICIPALITY", "sl", ""),),
        "SI-075": (Entity("Miren-Kostanjevica", "SI-075", "MUNICIPALITY", "sl", ""),),
        "SI-076": (Entity("Mislinja", "SI-076", "MUNICIPALITY", "sl", ""),),
        "SI-077": (Entity("Moravče", "SI-077", "MUNICIPALITY", "sl", ""),),
        "SI-078": (Entity("Moravske Toplice", "SI-078", "MUNICIPALITY", "sl", ""),),
        "SI-079": (Entity("Mozirje", "SI-079", "MUNICIPALITY", "sl", ""),),
        "SI-080": (Entity("Murska Sobota", "SI-080", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-081": (Entity("Muta", "SI-081", "MUNICIPALITY", "sl", ""),),
        "SI-082": (Entity("Naklo", "SI-082", "MUNICIPALITY", "sl", ""),),
        "SI-083": (Entity("Nazarje", "SI-083", "MUNICIPALITY", "sl", ""),),
        "SI-084": (Entity("Nova Gorica", "SI-084", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-085": (Entity("Novo Mesto", "SI-085", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-086": (Entity("Odranci", "SI-086", "MUNICIPALITY", "sl", ""),),
        "SI-087": (Entity("Ormož", "SI-087", "MUNICIPALITY", "sl", ""),),
        "SI-088": (Entity("Osilnica", "SI-088", "MUNICIPALITY", "sl", ""),),
        "SI-089": (Entity("Pesnica", "SI-089", "MUNICIPALITY", "sl", ""),),
        "SI-090": (Entity("Piran", "SI-090", "MUNICIPALITY", "sl", ""),),
        "SI-091": (Entity("Pivka", "SI-091", "MUNICIPALITY", "sl", ""),),
        "SI-092": (Entity("Podčetrtek", "SI-092", "MUNICIPALITY", "sl", ""),),
        "SI-093": (Entity("Podvelka", "SI-093", "MUNICIPALITY", "sl", ""),),
        "SI-094": (Entity("Postojna", "SI-094", "MUNICIPALITY", "sl", ""),),
        "SI-095": (Entity("Preddvor", "SI-095", "MUNICIPALITY", "sl", ""),),
        "SI-096": (Entity("Ptuj", "SI-096", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-097": (Entity("Puconci", "SI-097", "MUNICIPALITY", "sl", ""),),
        "SI-098": (Entity("Rače-Fram", "SI-098", "MUNICIPALITY", "sl", ""),),
        "SI-099": (Entity("Radeče", "SI-099", "MUNICIPALITY", "sl", ""),),
        "SI-100": (Entity("Radenci", "SI-100", "MUNICIPALITY", "sl", ""),),
        "SI-101": (Entity("Radlje ob Dravi", "SI-101", "MUNICIPALITY", "sl", ""),),
        "SI-102": (Entity("Radovljica", "SI-102", "MUNICIPALITY", "sl", ""),),
        "SI-103": (Entity("Ravne na Koroškem", "SI-103", "MUNICIPALITY", "sl", ""),),
        "SI-104": (Entity("Ribnica", "SI-104", "MUNICIPALITY", "sl", ""),),
        "SI-105": (Entity("Rogašovci", "SI-105", "MUNICIPALITY", "sl", ""),),
        "SI-106": (Entity("Rogaška Slatina", "SI-106", "MUNICIPALITY", "sl", ""),),
        "SI-107": (Entity("Rogatec", "SI-107", "MUNICIPALITY", "sl", ""),),
        "SI-108": (Entity("Ruše", "SI-108", "MUNICIPALITY", "sl", ""),),
        "SI-109": (Entity("Semič", "SI-109", "MUNICIPALITY", "sl", ""),),
        "SI-110": (Entity("Sevnica", "SI-110", "MUNICIPALITY", "sl", ""),),
        "SI-111": (Entity("Sežana", "SI-111", "MUNICIPALITY", "sl", ""),),
        "SI-112": (Entity("Slovenj Gradec", "SI-112", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-113": (Entity("Slovenska Bistrica", "SI-113", "MUNICIPALITY", "sl", ""),),
        "SI-114": (Entity("Slovenske Konjice", "SI-114", "MUNICIPALITY", "sl", ""),),
        "SI-115": (Entity("Starše", "SI-115", "MUNICIPALITY", "sl", ""),),
        "SI-116": (Entity("Sveti Jurij ob Ščavnici", "SI-116", "MUNICIPALITY", "sl", ""),),
        "SI-117": (Entity("Šenčur", "SI-117", "MUNICIPALITY", "sl", ""),),
        "SI-118": (Entity("Šentilj", "SI-118", "MUNICIPALITY", "sl", ""),),
        "SI-119": (Entity("Šentjernej", "SI-119", "MUNICIPALITY", "sl", ""),),
        "SI-120": (Entity("Šentjur", "SI-120", "MUNICIPALITY", "sl", ""),),
        "SI-121": (Entity("Škocjan", "SI-121", "MUNICIPALITY", "sl", ""),),
        "SI-122": (Entity("Škofja Loka", "SI-122", "MUNICIPALITY", "sl", ""),),
        "SI-123": (Entity("Škofljica", "SI-123", "MUNICIPALITY", "sl", ""),),
        "SI-124": (Entity("Šmarje pri Jelšah", "SI-124", "MUNICIPALITY", "sl", ""),),
        "SI-125": (Entity("Šmartno ob Paki", "SI-125", "MUNICIPALITY", "sl", ""),),
        "SI-126": (Entity("Šoštanj", "SI-126", "MUNICIPALITY", "sl", ""),),
        "SI-127": (Entity("Štore", "SI-127", "MUNICIPALITY", "sl", ""),),
        "SI-128": (Entity("Tolmin", "SI-128", "MUNICIPALITY", "sl", ""),),
        "SI-129": (Entity("Trbovlje", "SI-129", "MUNICIPALITY", "sl", ""),),
        "SI-130": (Entity("Trebnje", "SI-130", "MUNICIPALITY", "sl", ""),),
        "SI-131": (Entity("Tržič", "SI-131", "MUNICIPALITY", "sl", ""),),
        "SI-132": (Entity("Turnišče", "SI-132", "MUNICIPALITY", "sl", ""),),
        "SI-133": (Entity("Velenje", "SI-133", "URBAN MUNICIPALITY", "sl", ""),),
        "SI-134": (Entity("Velike Lašče", "SI-134", "MUNICIPALITY", "sl", ""),),
        "SI-135": (Entity("Videm", "SI-135", "MUNICIPALITY", "sl", ""),),
        "SI-136": (Entity("Vipava", "SI-136", "MUNICIPALITY", "sl", ""),),
        "SI-137": (Entity("Vitanje", "SI-137", "MUNICIPALITY", "sl", ""),),
        "SI-138": (Entity("Vodice", "SI-138", "MUNICIPALITY", "sl", ""),),
        "SI-139": (Entity("Vojnik", "SI-139", "MUNICIPALITY", "sl", ""),),
        "SI-140": (Entity("Vrhnika", "SI-140", "MUNICIPALITY", "sl", ""),),
        "SI-141": (Entity("Vuzenica", "SI-141", "MUNICIPALITY", "sl", ""),),
        "SI-142": (Entity("Zagorje ob Savi", "SI-142", "MUNICIPALITY", "sl", ""),),
        "SI-143": (Entity("Zavrč", "SI-143", "MUNICIPALITY", "sl", ""),),
        "SI-144": (Entity("Zreče", "SI-144", "MUNICIPALITY", "sl", ""),),
        "SI-146": (Entity("Železniki", "SI-146", "MUNICIPALITY", "sl", ""),),
        "SI-147": (Entity("Žiri", "SI-147", "MUNICIPALITY", "sl", ""),),
        "SI-148": (Entity("Benedikt", "SI-148", "MUNICIPALITY", "sl", ""),),
        "SI-149": (Entity("Bistrica ob Sotli", "SI-149", "MUNICIPALITY", "sl", ""),),
        "SI-150": (Entity("Bloke", "SI-150", "MUNICIPALITY", "sl", ""),),
        "SI-151": (Entity("Braslovče", "SI-151", "MUNICIPALITY", "sl", ""),),
        "SI-152": (Entity("Cankova", "SI-152", "MUNICIPALITY", "sl", ""),),
        "SI-153": (Entity("Cerkvenjak", "SI-153", "MUNICIPALITY", "sl", ""),),
        "SI-154": (Entity("Dobje", "SI-154", "MUNICIPALITY", "sl", ""),),
        "SI-155": (Entity("Dobrna", "SI-155", "MUNICIPALITY", "sl", ""),),
        "SI-156": (Entity("Dobrovnik", "SI-156", "MUNICIPALITY", "sl", ""),),
        "SI-157": (Entity("Dolenjske Toplice", "SI-157", "MUNICIPALITY", "sl", ""),),
        "SI-158": (Entity("Grad", "SI-158", "MUNICIPALITY", "sl", ""),),
        "SI-159": (Entity("Hajdina", "SI-159", "MUNICIPALITY", "sl", ""),),
        "SI-160": (Entity("Hoče-Slivnica", "SI-160", "MUNICIPALITY", "sl", ""),),
        "SI-161": (Entity("Hodoš", "SI-161", "MUNICIPALITY", "sl", ""),),
        "SI-162": (Entity("Horjul", "SI-162", "MUNICIPALITY", "sl", ""),),
        "SI-163": (Entity("Jezersko", "SI-163", "MUNICIPALITY", "sl", ""),),
        "SI-164": (Entity("Komenda", "SI-164", "MUNICIPALITY", "sl", ""),),
        "SI-165": (Entity("Kostel", "SI-165", "MUNICIPALITY", "sl", ""),),
        "SI-166": (Entity("Križevci", "SI-166", "MUNICIPALITY", "sl", ""),),
        "SI-167": (Entity("Lovrenc na Pohorju", "SI-167", "MUNICIPALITY", "sl", ""),),
        "SI-168": (Entity("Markovci", "SI-168", "MUNICIPALITY", "sl", ""),),
        "SI-169": (Entity("Miklavž na Dravskem polju", "SI-169", "MUNICIPALITY", "sl", ""),),
        "SI-170": (Entity("Mirna Peč", "SI-170", "MUNICIPALITY", "sl", ""),),
        "SI-171": (Entity("Oplotnica", "SI-171", "MUNICIPALITY", "sl", ""),),
        "SI-172": (Entity("Podlehnik", "SI-172", "MUNICIPALITY", "sl", ""),),
        "SI-173": (Entity("Polzela", "SI-173", "MUNICIPALITY", "sl", ""),),
        "SI-174": (Entity("Prebold", "SI-174", "MUNICIPALITY", "sl", ""),),
        "SI-175": (Entity("Prevalje", "SI-175", "MUNICIPALITY", "sl", ""),),
        "SI-176": (Entity("Razkrižje", "SI-176", "MUNICIPALITY", "sl", ""),),
        "SI-177": (Entity("Ribnica na Pohorju", "SI-177", "MUNICIPALITY", "sl", ""),),
        "SI-178": (Entity("Selnica ob Dravi", "SI-178", "MUNICIPALITY", "sl", ""),),
        "SI-179": (Entity("Sodražica", "SI-179", "MUNICIPALITY", "sl", ""),),
        "SI-180": (Entity("Solčava", "SI-180", "MUNICIPALITY", "sl", ""),),
        "SI-181": (Entity("Sveta Ana", "SI-181", "MUNICIPALITY", "sl", ""),),
        "SI-182": (
            Entity("Sveti Andraž v Slovenskih goricah", "SI-182", "MUNICIPALITY", "sl", ""),
        ),
        "SI-183": (Entity("Šempeter-Vrtojba", "SI-183", "MUNICIPALITY", "sl", ""),),
        "SI-184": (Entity("Tabor", "SI-184", "MUNICIPALITY", "sl", ""),),
        "SI-185": (Entity("Trnovska Vas", "SI-185", "MUNICIPALITY", "sl", ""),),
        "SI-186": (Entity("Trzin", "SI-186", "MUNICIPALITY", "sl", ""),),
        "SI-187": (Entity("Velika Polana", "SI-187", "MUNICIPALITY", "sl", ""),),
        "SI-188": (Entity("Veržej", "SI-188", "MUNICIPALITY", "sl", ""),),
        "SI-189": (Entity("Vransko", "SI-189", "MUNICIPALITY", "sl", ""),),
        "SI-190": (Entity("Žalec", "SI-190", "MUNICIPALITY", "sl", ""),),
        "SI-191": (Entity("Žetale", "SI-191", "MUNICIPALITY", "sl", ""),),
        "SI-192": (Entity("Žirovnica", "SI-192", "MUNICIPALITY", "sl", ""),),
        "SI-193": (Entity("Žužemberk", "SI-193", "MUNICIPALITY", "sl", ""),),
        "SI-194": (Entity("Šmartno pri Litiji", "SI-194", "MUNICIPALITY", "sl", ""),),
        "SI-195": (Entity("Apače", "SI-195", "MUNICIPALITY", "sl", ""),),
        "SI-196": (Entity("Cirkulane", "SI-196", "MUNICIPALITY", "sl", ""),),
        "SI-197": (Entity("Kostanjevica na Krki", "SI-197", "MUNICIPALITY", "sl", ""),),
        "SI-198": (Entity("Makole", "SI-198", "MUNICIPALITY", "sl", ""),),
        "SI-199": (Entity("Mokronog-Trebelno", "SI-199", "MUNICIPALITY", "sl", ""),),
        "SI-200": (Entity("Poljčane", "SI-200", "MUNICIPALITY", "sl", ""),),
        "SI-201": (Entity("Renče-Vogrsko", "SI-201", "MUNICIPALITY", "sl", ""),),
        "SI-202": (Entity("Središče ob Dravi", "SI-202", "MUNICIPALITY", "sl", ""),),
        "SI-203": (Entity("Straža", "SI-203", "MUNICIPALITY", "sl", ""),),
        "SI-204": (
            Entity("Sveta Trojica v Slovenskih goricah", "SI-204", "MUNICIPALITY", "sl", ""),
        ),
        "SI-205": (Entity("Sveti Tomaž", "SI-205", "MUNICIPALITY", "sl", ""),),
        "SI-206": (Entity("Šmarješke Toplice", "SI-206", "MUNICIPALITY", "sl", ""),),
        "SI-207": (Entity("Gorje", "SI-207", "MUNICIPALITY", "sl", ""),),
        "SI-208": (Entity("Log-Dragomer", "SI-208", "MUNICIPALITY", "sl", ""),),
        "SI-209": (Entity("Rečica ob Savinji", "SI-209", "MUNICIPALITY", "sl", ""),),
        "SI-210": (Entity("Sveti Jurij v Slovenskih goricah", "SI-210", "MUNICIPALITY", "sl", ""),),
        "SI-211": (Entity("Šentrupert", "SI-211", "MUNICIPALITY", "sl", ""),),
        "SI-212": (Entity("Mirna", "SI-212", "MUNICIPALITY", "sl", ""),),
        "SI-213": (Entity("Ankaran", "SI-213", "MUNICIPALITY", "sl", ""),),
    }
