"""ISO 3166-2 UG standard representation.

References:
  - https://en.wikipedia.org/wiki/ISO_3166-2
  - https://www.iso.org/obp/ui/#iso:code:3166:UG
"""

from iso_standards.base import EntityCollection
from iso_standards.iso3166.types import Iso3166_2 as Entity


class Iso3166_2(EntityCollection):
    __slots__ = ()

    entities = {
        "UG-101": (Entity("Kalangala", "UG-101", "DISTRICT", "en", "UG-C"),),
        "UG-102": (Entity("Kampala", "UG-102", "CITY", "en", "UG-C"),),
        "UG-103": (Entity("Kiboga", "UG-103", "DISTRICT", "en", "UG-C"),),
        "UG-104": (Entity("Luwero", "UG-104", "DISTRICT", "en", "UG-C"),),
        "UG-105": (Entity("Masaka", "UG-105", "DISTRICT", "en", "UG-C"),),
        "UG-106": (Entity("Mpigi", "UG-106", "DISTRICT", "en", "UG-C"),),
        "UG-107": (Entity("Mubende", "UG-107", "DISTRICT", "en", "UG-C"),),
        "UG-108": (Entity("Mukono", "UG-108", "DISTRICT", "en", "UG-C"),),
        "UG-109": (Entity("Nakasongola", "UG-109", "DISTRICT", "en", "UG-C"),),
        "UG-110": (Entity("Rakai", "UG-110", "DISTRICT", "en", "UG-C"),),
        "UG-111": (Entity("Sembabule", "UG-111", "DISTRICT", "en", "UG-C"),),
        "UG-112": (Entity("Kayunga", "UG-112", "DISTRICT", "en", "UG-C"),),
        "UG-113": (Entity("Wakiso", "UG-113", "DISTRICT", "en", "UG-C"),),
        "UG-114": (Entity("Lyantonde", "UG-114", "DISTRICT", "en", "UG-C"),),
        "UG-115": (Entity("Mityana", "UG-115", "DISTRICT", "en", "UG-C"),),
        "UG-116": (Entity("Nakaseke", "UG-116", "DISTRICT", "en", "UG-C"),),
        "UG-117": (Entity("Buikwe", "UG-117", "DISTRICT", "en", "UG-C"),),
        "UG-118": (Entity("Bukomansibi", "UG-118", "DISTRICT", "en", "UG-C"),),
        "UG-119": (Entity("Butambala", "UG-119", "DISTRICT", "en", "UG-C"),),
        "UG-120": (Entity("Buvuma", "UG-120", "DISTRICT", "en", "UG-C"),),
        "UG-121": (Entity("Gomba", "UG-121", "DISTRICT", "en", "UG-C"),),
        "UG-122": (Entity("Kalungu", "UG-122", "DISTRICT", "en", "UG-C"),),
        "UG-123": (Entity("Kyankwanzi", "UG-123", "DISTRICT", "en", "UG-C"),),
        "UG-124": (Entity("Lwengo", "UG-124", "DISTRICT", "en", "UG-C"),),
        "UG-125": (Entity("Kyotera", "UG-125", "DISTRICT", "en", "UG-C"),),
        "UG-126": (Entity("Kasanda", "UG-126", "DISTRICT", "en", "UG-C"),),
        "UG-201": (Entity("Bugiri", "UG-201", "DISTRICT", "en", "UG-E"),),
        "UG-202": (Entity("Busia", "UG-202", "DISTRICT", "en", "UG-E"),),
        "UG-203": (Entity("Iganga", "UG-203", "DISTRICT", "en", "UG-E"),),
        "UG-204": (Entity("Jinja", "UG-204", "DISTRICT", "en", "UG-E"),),
        "UG-205": (Entity("Kamuli", "UG-205", "DISTRICT", "en", "UG-E"),),
        "UG-206": (Entity("Kapchorwa", "UG-206", "DISTRICT", "en", "UG-E"),),
        "UG-207": (Entity("Katakwi", "UG-207", "DISTRICT", "en", "UG-E"),),
        "UG-208": (Entity("Kumi", "UG-208", "DISTRICT", "en", "UG-E"),),
        "UG-209": (Entity("Mbale", "UG-209", "DISTRICT", "en", "UG-E"),),
        "UG-210": (Entity("Pallisa", "UG-210", "DISTRICT", "en", "UG-E"),),
        "UG-211": (Entity("Soroti", "UG-211", "DISTRICT", "en", "UG-E"),),
        "UG-212": (Entity("Tororo", "UG-212", "DISTRICT", "en", "UG-E"),),
        "UG-213": (Entity("Kaberamaido", "UG-213", "DISTRICT", "en", "UG-E"),),
        "UG-214": (Entity("Mayuge", "UG-214", "DISTRICT", "en", "UG-E"),),
        "UG-215": (Entity("Sironko", "UG-215", "DISTRICT", "en", "UG-E"),),
        "UG-216": (Entity("Amuria", "UG-216", "DISTRICT", "en", "UG-E"),),
        "UG-217": (Entity("Budaka", "UG-217", "DISTRICT", "en", "UG-E"),),
        "UG-218": (Entity("Bududa", "UG-218", "DISTRICT", "en", "UG-E"),),
        "UG-219": (Entity("Bukedea", "UG-219", "DISTRICT", "en", "UG-E"),),
        "UG-220": (Entity("Bukwo", "UG-220", "DISTRICT", "en", "UG-E"),),
        "UG-221": (Entity("Butaleja", "UG-221", "DISTRICT", "en", "UG-E"),),
        "UG-222": (Entity("Kaliro", "UG-222", "DISTRICT", "en", "UG-E"),),
        "UG-223": (Entity("Manafwa", "UG-223", "DISTRICT", "en", "UG-E"),),
        "UG-224": (Entity("Namutumba", "UG-224", "DISTRICT", "en", "UG-E"),),
        "UG-225": (Entity("Bulambuli", "UG-225", "DISTRICT", "en", "UG-E"),),
        "UG-226": (Entity("Buyende", "UG-226", "DISTRICT", "en", "UG-E"),),
        "UG-227": (Entity("Kibuku", "UG-227", "DISTRICT", "en", "UG-E"),),
        "UG-228": (Entity("Kween", "UG-228", "DISTRICT", "en", "UG-E"),),
        "UG-229": (Entity("Luuka", "UG-229", "DISTRICT", "en", "UG-E"),),
        "UG-230": (Entity("Namayingo", "UG-230", "DISTRICT", "en", "UG-E"),),
        "UG-231": (Entity("Ngora", "UG-231", "DISTRICT", "en", "UG-E"),),
        "UG-232": (Entity("Serere", "UG-232", "DISTRICT", "en", "UG-E"),),
        "UG-233": (Entity("Butebo", "UG-233", "DISTRICT", "en", "UG-E"),),
        "UG-234": (Entity("Namisindwa", "UG-234", "DISTRICT", "en", "UG-E"),),
        "UG-235": (Entity("Bugweri", "UG-235", "DISTRICT", "en", "UG-E"),),
        "UG-236": (Entity("Kapelebyong", "UG-236", "DISTRICT", "en", "UG-E"),),
        "UG-237": (Entity("Kalaki", "UG-237", "DISTRICT", "en", "UG-E"),),
        "UG-301": (Entity("Adjumani", "UG-301", "DISTRICT", "en", "UG-N"),),
        "UG-302": (Entity("Apac", "UG-302", "DISTRICT", "en", "UG-N"),),
        "UG-303": (Entity("Arua", "UG-303", "DISTRICT", "en", "UG-N"),),
        "UG-304": (Entity("Gulu", "UG-304", "DISTRICT", "en", "UG-N"),),
        "UG-305": (Entity("Kitgum", "UG-305", "DISTRICT", "en", "UG-N"),),
        "UG-306": (Entity("Kotido", "UG-306", "DISTRICT", "en", "UG-N"),),
        "UG-307": (Entity("Lira", "UG-307", "DISTRICT", "en", "UG-N"),),
        "UG-308": (Entity("Moroto", "UG-308", "DISTRICT", "en", "UG-N"),),
        "UG-309": (Entity("Moyo", "UG-309", "DISTRICT", "en", "UG-N"),),
        "UG-310": (Entity("Nebbi", "UG-310", "DISTRICT", "en", "UG-N"),),
        "UG-311": (Entity("Nakapiripirit", "UG-311", "DISTRICT", "en", "UG-N"),),
        "UG-312": (Entity("Pader", "UG-312", "DISTRICT", "en", "UG-N"),),
        "UG-313": (Entity("Yumbe", "UG-313", "DISTRICT", "en", "UG-N"),),
        "UG-314": (Entity("Abim", "UG-314", "DISTRICT", "en", "UG-N"),),
        "UG-315": (Entity("Amolatar", "UG-315", "DISTRICT", "en", "UG-N"),),
        "UG-316": (Entity("Amuru", "UG-316", "DISTRICT", "en", "UG-N"),),
        "UG-317": (Entity("Dokolo", "UG-317", "DISTRICT", "en", "UG-N"),),
        "UG-318": (Entity("Kaabong", "UG-318", "DISTRICT", "en", "UG-N"),),
        "UG-319": (Entity("Koboko", "UG-319", "DISTRICT", "en", "UG-N"),),
        "UG-320": (Entity("Maracha", "UG-320", "DISTRICT", "en", "UG-N"),),
        "UG-321": (Entity("Oyam", "UG-321", "DISTRICT", "en", "UG-N"),),
        "UG-322": (Entity("Agago", "UG-322", "DISTRICT", "en", "UG-N"),),
        "UG-323": (Entity("Alebtong", "UG-323", "DISTRICT", "en", "UG-N"),),
        "UG-324": (Entity("Amudat", "UG-324", "DISTRICT", "en", "UG-N"),),
        "UG-325": (Entity("Kole", "UG-325", "DISTRICT", "en", "UG-N"),),
        "UG-326": (Entity("Lamwo", "UG-326", "DISTRICT", "en", "UG-N"),),
        "UG-327": (Entity("Napak", "UG-327", "DISTRICT", "en", "UG-N"),),
        "UG-328": (Entity("Nwoya", "UG-328", "DISTRICT", "en", "UG-N"),),
        "UG-329": (Entity("Otuke", "UG-329", "DISTRICT", "en", "UG-N"),),
        "UG-330": (Entity("Zombo", "UG-330", "DISTRICT", "en", "UG-N"),),
        "UG-331": (Entity("Omoro", "UG-331", "DISTRICT", "en", "UG-N"),),
        "UG-332": (Entity("Pakwach", "UG-332", "DISTRICT", "en", "UG-N"),),
        "UG-333": (Entity("Kwania", "UG-333", "DISTRICT", "en", "UG-N"),),
        "UG-334": (Entity("Nabilatuk", "UG-334", "DISTRICT", "en", "UG-N"),),
        "UG-335": (Entity("Karenga", "UG-335", "DISTRICT", "en", "UG-N"),),
        "UG-336": (Entity("Madi-Okollo", "UG-336", "DISTRICT", "en", "UG-N"),),
        "UG-337": (Entity("Obongi", "UG-337", "DISTRICT", "en", "UG-N"),),
        "UG-401": (Entity("Bundibugyo", "UG-401", "DISTRICT", "en", "UG-W"),),
        "UG-402": (Entity("Bushenyi", "UG-402", "DISTRICT", "en", "UG-W"),),
        "UG-403": (Entity("Hoima", "UG-403", "DISTRICT", "en", "UG-W"),),
        "UG-404": (Entity("Kabale", "UG-404", "DISTRICT", "en", "UG-W"),),
        "UG-405": (Entity("Kabarole", "UG-405", "DISTRICT", "en", "UG-W"),),
        "UG-406": (Entity("Kasese", "UG-406", "DISTRICT", "en", "UG-W"),),
        "UG-407": (Entity("Kibaale", "UG-407", "DISTRICT", "en", "UG-W"),),
        "UG-408": (Entity("Kisoro", "UG-408", "DISTRICT", "en", "UG-W"),),
        "UG-409": (Entity("Masindi", "UG-409", "DISTRICT", "en", "UG-W"),),
        "UG-410": (Entity("Mbarara", "UG-410", "DISTRICT", "en", "UG-W"),),
        "UG-411": (Entity("Ntungamo", "UG-411", "DISTRICT", "en", "UG-W"),),
        "UG-412": (Entity("Rukungiri", "UG-412", "DISTRICT", "en", "UG-W"),),
        "UG-413": (Entity("Kamwenge", "UG-413", "DISTRICT", "en", "UG-W"),),
        "UG-414": (Entity("Kanungu", "UG-414", "DISTRICT", "en", "UG-W"),),
        "UG-415": (Entity("Kyenjojo", "UG-415", "DISTRICT", "en", "UG-W"),),
        "UG-416": (Entity("Buliisa", "UG-416", "DISTRICT", "en", "UG-W"),),
        "UG-417": (Entity("Ibanda", "UG-417", "DISTRICT", "en", "UG-W"),),
        "UG-418": (Entity("Isingiro", "UG-418", "DISTRICT", "en", "UG-W"),),
        "UG-419": (Entity("Kiruhura", "UG-419", "DISTRICT", "en", "UG-W"),),
        "UG-420": (Entity("Buhweju", "UG-420", "DISTRICT", "en", "UG-W"),),
        "UG-421": (Entity("Kiryandongo", "UG-421", "DISTRICT", "en", "UG-W"),),
        "UG-422": (Entity("Kyegegwa", "UG-422", "DISTRICT", "en", "UG-W"),),
        "UG-423": (Entity("Mitooma", "UG-423", "DISTRICT", "en", "UG-W"),),
        "UG-424": (Entity("Ntoroko", "UG-424", "DISTRICT", "en", "UG-W"),),
        "UG-425": (Entity("Rubirizi", "UG-425", "DISTRICT", "en", "UG-W"),),
        "UG-426": (Entity("Sheema", "UG-426", "DISTRICT", "en", "UG-W"),),
        "UG-427": (Entity("Kagadi", "UG-427", "DISTRICT", "en", "UG-W"),),
        "UG-428": (Entity("Kakumiro", "UG-428", "DISTRICT", "en", "UG-W"),),
        "UG-429": (Entity("Rubanda", "UG-429", "DISTRICT", "en", "UG-W"),),
        "UG-430": (Entity("Bunyangabu", "UG-430", "DISTRICT", "en", "UG-W"),),
        "UG-431": (Entity("Rukiga", "UG-431", "DISTRICT", "en", "UG-W"),),
        "UG-432": (Entity("Kikuube", "UG-432", "DISTRICT", "en", "UG-W"),),
        "UG-433": (Entity("Kazo", "UG-433", "DISTRICT", "en", "UG-W"),),
        "UG-434": (Entity("Kitagwenda", "UG-434", "DISTRICT", "en", "UG-W"),),
        "UG-435": (Entity("Rwampara", "UG-435", "DISTRICT", "en", "UG-W"),),
        "UG-C": (Entity("Central", "UG-C", "GEOGRAPHICAL REGION", "en", ""),),
        "UG-E": (Entity("Eastern", "UG-E", "GEOGRAPHICAL REGION", "en", ""),),
        "UG-N": (Entity("Northern", "UG-N", "GEOGRAPHICAL REGION", "en", ""),),
        "UG-W": (Entity("Western", "UG-W", "GEOGRAPHICAL REGION", "en", ""),),
    }
