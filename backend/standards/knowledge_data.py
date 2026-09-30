import datetime as dt

LAST_VERIFIED = dt.date(2026, 9, 28)

BIS_KYS = "https://standards.bis.gov.in/website/know-your-standards"

FAMILIES = [
    {
        "slug": "tmt-steel-bars",
        "name": "TMT / Reinforcement Steel Bars (HYSD)",
        "description": "High strength deformed steel bars and wires used as concrete reinforcement.",
        "keywords": (
            "TMT,rebar,reinforcement bar,reinforcement steel,HYSD,deformed bar,"
            "concrete reinforcement,Fe415,Fe500,Fe550,Fe600,"
            "ribbed bar,ribbed steel,CTD bar,cold twisted bar,tor steel,tor bar,"
            "steel bar for concrete,bar reinforcement,high yield bar,"
            "sariya,saria,lohiya,steel rod,RCC bar,reinforced bar,"
            "deformed steel,high strength bar,structural steel bar"
        ),
    },
    {
        "slug": "cement-opc",
        "name": "Cement (OPC / PPC / PSC)",
        "description": "Ordinary Portland, Portland Pozzolana and Portland Slag cement for construction.",
        "keywords": (
            "cement,OPC,portland cement,PPC,PSC,pozzolana,slag cement,"
            "portland pozzolana,portland slag,hydraulic cement,building cement,"
            "construction cement,binding material,cementitious,binding agent,"
            "siment,simant,chuna"
        ),
    },
    {
        "slug": "gold-hallmarking",
        "name": "Gold Jewellery / Artefacts (Hallmarking)",
        "description": "Gold jewellery and artefacts covered by BIS mandatory hallmarking.",
        "keywords": (
            "gold jewellery,gold artefact,hallmark,hallmarking,karat,carat,HUID,"
            "gold ornament,jeweller,gold chain,gold ring,gold bangle,gold coin,"
            "gold bar,gold bullion,sona,swarna,sunna,sonar,jewellery shop,"
            "assaying centre,hallmarking centre"
        ),
    },
    {
        "slug": "aluminium-utensils",
        "name": "Wrought and Cast Aluminium Utensils / Cookware",
        "description": "Aluminium utensils and cookware, covered by a Quality Control Order.",
        "keywords": (
            "aluminium utensil,aluminium cookware,aluminium vessel,wrought aluminium,"
            "cookware,kitchen utensil,aluminium pan,aluminium pot,aluminium tray,"
            "aluminium plate,aluminium bowl,aluminium pressure cooker,"
            "aluminium kadai,aluminium handi,bartan,aluminium bartan,"
            "cast aluminium,anodized aluminium cookware"
        ),
    },
    {
        "slug": "led-lamps-crs",
        "name": "Self-Ballasted LED Lamps (CRS)",
        "description": "LED lamps for general lighting, covered by the Compulsory Registration Scheme.",
        "keywords": (
            "LED lamp,LED bulb,self-ballasted LED,LED light,general lighting,"
            "LED luminaire,LED tube,LED fitting,energy saving lamp,LED batten,"
            "LED panel,LED downlight,LED spotlight,LED strip,solid state lighting,"
            "LED driver,LED module"
        ),
    },
]

HINDI_SYNONYMS = {
    "sariya": "reinforcement bar",
    "saria": "reinforcement bar",
    "lohiya": "reinforcement bar",
    "lohiya bar": "TMT",
    "steel rod": "TMT",
    "loh dand": "reinforcement bar",
    "sariyon": "reinforcement bar",
    "sariyen": "reinforcement bar",
    "\u0938\u0930\u093f\u092f\u093e": "reinforcement bar",
    "\u0938\u0930\u093f\u092f\u094b\u0902": "reinforcement bar",
    "\u0938\u0930\u093f\u092f\u0947\u0902": "reinforcement bar",
    "\u0932\u094b\u0939\u093e": "reinforcement bar",
    "\u0932\u094b\u0939\u0947 \u0915\u0940 \u0938\u0932\u093e\u0916": "reinforcement bar",
    "simant": "cement",
    "siment": "cement",
    "chuna": "cement",
    "nishadhar": "cement",
    "cement ki boriya": "cement",
    "\u0938\u0940\u092e\u0947\u0902\u091f": "cement",
    "\u0938\u093f\u092e\u0947\u0902\u091f": "cement",
    "\u0938\u0940\u092e\u0947\u0902\u091f \u0915\u0940 \u092c\u094b\u0930\u093f\u092f\u093e\u0902": "cement",
    "\u091a\u0942\u0928\u093e": "cement",
    "\u0928\u093f\u0936\u093e\u0927\u093e\u0930": "cement",
    "sona": "gold jewellery",
    "swarna": "gold jewellery",
    "sunna": "gold jewellery",
    "sonar": "gold jewellery",
    "sone ke gehne": "gold jewellery",
    "sone ka aabhushan": "gold jewellery",
    "gehna": "gold jewellery",
    "\u0938\u094b\u0928\u093e": "gold jewellery",
    "\u0938\u094b\u0928\u0947 \u0915\u0947 \u0917\u0939\u0928\u0947": "gold jewellery",
    "\u0938\u094b\u0928\u0947 \u0915\u0947 \u0906\u092d\u0942\u0937\u0923": "gold jewellery",
    "\u0938\u094d\u0935\u0930\u094d\u0923": "gold jewellery",
    "\u0906\u092d\u0942\u0937\u0923": "gold jewellery",
    "\u0917\u0939\u0928\u093e": "gold jewellery",
    "bartan": "aluminium cookware",
    "aluminium bartan": "aluminium cookware",
    "bartan ki supply": "aluminium cookware",
    "pakane ke bartan": "cookware",
    "rasoi bartan": "aluminium cookware",
    "stainless bartan": "aluminium cookware",
    "\u0935\u0930\u094d\u0924\u0928": "aluminium cookware",
    "\u090f\u0932\u0941\u092e\u093f\u0928\u093f\u092f\u092e \u0935\u0930\u094d\u0924\u0928": "aluminium cookware",
    "\u0930\u0938\u094b\u0908 \u0935\u0930\u094d\u0924\u0928": "aluminium cookware",
    "\u092a\u0915\u093e\u0928\u0947 \u0915\u0947 \u092c\u0930\u094d\u0924\u0928": "cookware",
    "\u0905\u0932\u0941\u092e\u093f\u0928\u093f\u092f\u092e": "aluminium cookware",
    "LED batti": "LED lamp",
    "batti": "LED lamp",
    "LED bulb": "LED lamp",
    "prakash": "LED lamp",
    "roshni": "LED lamp",
    "prakash vyavastha": "LED lamp",
    "lohiya sariya": "TMT",
    "\u092c\u0924\u094d\u0924\u0940": "LED lamp",
    "\u092a\u094d\u0930\u0915\u093e\u0936": "LED lamp",
    "\u0930\u094b\u0936\u0928\u0940": "LED lamp",
    "\u092a\u094d\u0930\u0915\u093e\u0936 \u0935\u094d\u092f\u0935\u0938\u094d\u0925\u093e": "LED lamp",
    "sone ki chain": "gold jewellery",
    "sone ki angoothi": "gold jewellery",
    "gehne": "gold jewellery",
    "swarn aabhushan": "gold jewellery",
}

LANG_PATTERNS = {
    "hi": [
        "sariya", "saria", "lohiya", "simant", "siment", "chuna",
        "sona", "swarna", "sunna", "sonar", "bartan", "batti",
        "gehna", "aabhushan", "prashashan", "nirdesh", "niyam",
        "vidyut", "prakash", "roshni", "nishadhar",
        "\u0938\u0930\u093f\u092f\u093e", "\u0938\u0940\u092e\u0947\u0902\u091f",
        "\u0938\u094b\u0928\u093e", "\u0905\u0932\u0941\u092e\u093f\u0928\u093f\u092f\u092e",
        "\u0935\u0930\u094d\u0924\u0928", "\u092c\u0924\u094d\u0924\u0940",
    ],
    "mr": [
        "\u0938\u0930\u093f\u092f\u093e", "\u0938\u093f\u092e\u0947\u0902\u091f",
        "\u0938\u094b\u0928\u0947", "\u092d\u093e\u0902\u0921\u0940",
    ],
    "gu": [
        "\u0ab8\u0ab0\u0abf\u092f\u093e", "\u0ab8\u093f\u092e\u0947\u0aa8\u0acd\u0aad",
        "\u0ab8\u094b\u0aa8\u0ac1", "\u0ab5\u093e\u0ab8\u0aa3",
    ],
    "ta": [
        "\u0b95\u0bae\u0bcd\u0baa\u0bbf", "\u0b9a\u0bbf\u0bae\u0bc6\u0ba3\u0bcd\u0b9f\u0bcd",
        "\u0ba4\u0b99\u0bcd\u0b95\u0bae\u0bcd", "\u0b8a\u0b9c\u0bbf\u0baf\u0bae\u0bcd",
    ],
    "te": [
        "\u0c38\u0c30\u0c3f\u0c2f\u0c3e", "\u0c38\u0c3f\u0c2e\u0c46\u0c02\u0c1f\u0c41",
        "\u0c2c\u0c02\u0c17\u0c3e\u0c30\u0c02", "\u0c35\u0c02\u0c1f\u0c2a\u0c3e\u0c24\u0c4d\u0c30\u0c3e\u0c32\u0c41",
    ],
    "kn": [
        "\u0cb8\u0cbf\u0cae\u0cc6\u0c82\u0c1f\u0cc1", "\u0c9a\u0cbf\u0ca8\u0ccd\u0ca8",
        "\u0caa\u0cbe\u0ca4\u0ccd\u0cb0\u0cc6", "\u0cb5\u0cbf\u0ca6\u0ccd\u0caf\u0cc1\u0ca4\u0ccd",
    ],
}

DEVANAGARI_RANGE = ('\u0900', '\u097F')
TAMIL_RANGE = ('\u0B80', '\u0BFF')
TELUGU_RANGE = ('\u0C00', '\u0C7F')
KANNADA_RANGE = ('\u0C80', '\u0CFF')
GUJARATI_RANGE = ('\u0A80', '\u0AFF')
MARATHI_RANGE = ('\u0900', '\u097F')

def _key(is_number, part, year):
    return f"{is_number}|{part or ''}|{year or ''}"

def S(is_number, year=None, part=None, title="", std_type="product", status="unknown", family=None,
      replaced_by=None, amendments=None, amendment_note="", source_url="", verification="public_data",
      notes="", triggers=None):
    return {
        "key": _key(is_number, part, year),
        "is_number": is_number,
        "part": part,
        "year": year,
        "title": title,
        "std_type": std_type,
        "status": status,
        "family": family,
        "replaced_by": replaced_by,
        "amendments": amendments or [],
        "amendment_note": amendment_note,
        "source_url": source_url,
        "verification": verification,
        "last_verified": LAST_VERIFIED,
        "notes": notes,
        "triggers": triggers or [],
    }

K = _key

STANDARDS = [
    S("IS 1786", 2008,
      title="High Strength Deformed Steel Bars and Wires for Concrete Reinforcement — Specification (Fourth Revision)",
      family="tmt-steel-bars", status="current",
      amendments=[
          {"no": 1, "date": "2012-11", "note": "Adds Fe 415S / Fe 500S categories, revised chemical composition, Table 3 and bend-test tables."},
          {"no": 2, "date": None, "note": "Issued between Nov 2012 and Mar 2017; exact date not confirmed."},
          {"no": 3, "date": "2017-03", "note": "Amends clause 1.1 to add grades Fe 650 and Fe 700."},
          {"no": 4, "date": "2019-07", "note": "Published 4 Jul 2019; implementation deadline 9 Sep 2019. IS 1608 replaced by IS 1608 (Part 1); IS 11587 deleted from references."},
      ],
      amendment_note="Amendment No. 4 (July 2019) is the latest confirmed from BIS documents. Check BIS for anything issued later.",
      source_url="https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf",
      verification="official_verified",
      notes="Terminology is defined inside the standard itself (clause 3), not in a separate terminology standard."),
    S("IS 228", None, title="Methods for Chemical Analysis of Steels (Parts 1 to 24)", std_type="test_method",
      source_url="https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf", verification="official_verified",
      notes="Listed in clause 2 of IS 1786:2008."),
    S("IS 1387", 1993, title="General Requirements for the Supply of Metallurgical Materials (Second Revision)",
      std_type="normative_reference", source_url="https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf",
      verification="official_verified"),
    S("IS 1599", 1985, title="Method for Bend Test (Second Revision)", std_type="test_method",
      source_url="https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf", verification="official_verified"),
    S("IS 1608", None, part="1",
      title="Metallic Materials — Tensile Testing — Part 1: Method of Test at Ambient Temperature",
      std_type="test_method", source_url="https://services.bis.gov.in/tmp/GG_IS_1786_06082019.pdf",
      verification="official_verified",
      notes="Amendment No. 4 to IS 1786 replaced the plain IS 1608 reference by IS 1608 (Part 1)."),
    S("IS 2062", 2006, title="Hot Rolled Low, Medium and High Tensile Structural Steel (Sixth Revision)",
      std_type="normative_reference", source_url="https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf",
      verification="official_verified"),
    S("IS 2770", 1967, part="1", title="Methods of Testing Bond in Reinforced Concrete — Part 1: Pull-out Test",
      std_type="test_method", source_url="https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf",
      verification="official_verified"),
    S("IS 9417", 1989,
      title="Recommendations for Welding Cold-Worked Steel Bars for Reinforced Concrete Construction (First Revision)",
      std_type="installation", source_url="https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf",
      verification="official_verified"),
    S("IS 456", 2000, title="Plain and Reinforced Concrete — Code of Practice", std_type="code_of_practice",
      status="unknown", source_url="https://law.resource.org/pub/in/bis/S03/is.456.2000.pdf",
      verification="public_data"),
    S("IS 13920", None,
      title="Ductile Design and Detailing of Reinforced Concrete Structures Subjected to Seismic Forces — Code of Practice",
      std_type="safety", source_url="https://infralens.in/term/fy", verification="public_data"),

    S("IS 269", 2015, title="Ordinary Portland Cement — Specification (Sixth Revision)", family="cement-opc",
      status="current",
      amendments=[{"no": 1, "date": None, "note": "One amendment recorded by BIS; exact date not confirmed."}],
      amendment_note="BIS Know Your Standard lists 1 amendment. Check BIS for its text and date.",
      source_url="https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEx",
      verification="official_verified",
      notes="Covers 33, 43, 53, 43S and 53S grades."),
    S("IS 1489", 2015, part="1", title="Portland Pozzolana Cement — Specification — Part 1: Fly Ash Based (Fourth Revision)",
      family="cement-opc", status="current",
      source_url="https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/",
      verification="official_verified", triggers=["ppc", "pozzolana", "pozzolanic", "fly ash cement", "portland pozzolana"]),
    S("IS 1489", 2015, part="2", title="Portland Pozzolana Cement — Specification — Part 2: Calcined Clay Based (Fourth Revision)",
      family="cement-opc", status="current",
      source_url="https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/",
      verification="official_verified", triggers=["calcined clay"]),
    S("IS 455", 2015, title="Portland Slag Cement — Specification (Fifth Revision)", family="cement-opc",
      status="current",
      source_url="https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/",
      verification="official_verified", triggers=["psc", "slag cement", "portland slag"]),
    S("IS 8112", 2013, title="43 Grade Ordinary Portland Cement — Specification", family="cement-opc",
      status="superseded", replaced_by=K("IS 269", None, 2015),
      source_url="https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/",
      verification="public_data"),
    S("IS 12269", 2013, title="53 Grade Ordinary Portland Cement — Specification", family="cement-opc",
      status="superseded", replaced_by=K("IS 269", None, 2015),
      source_url="https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/",
      verification="public_data"),
    S("IS 4031", None, title="Methods of Physical Tests for Hydraulic Cement (relevant parts)",
      std_type="test_method",
      source_url="https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEx",
      verification="official_verified"),
    S("IS 4032", 1985, title="Method of Chemical Analysis of Hydraulic Cement (First Revision)", std_type="test_method",
      source_url="https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEx",
      verification="official_verified"),
    S("IS 650", 1991, title="Standard Sand for Testing Cement — Specification (Second Revision)", std_type="test_method",
      source_url="https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEx",
      verification="official_verified"),
    S("IS 2580", 1995, title="Textiles — Jute Sacking Bags for Packing Cement — Specification (Third Revision)",
      std_type="packaging",
      source_url="https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEx",
      verification="official_verified"),
    S("IS 4905", 2015, title="Random Sampling and Randomization Procedures (First Revision)", std_type="sampling",
      source_url="https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEx",
      verification="official_verified"),

    S("IS 1417", 2016, title="Gold and Gold Alloys, Jewellery/Artefacts — Fineness and Marking — Specification",
      family="gold-hallmarking", status="current",
      amendment_note="Amendments not checked. Look up IS 1417 on the BIS Know Your Standard portal.",
      source_url="https://services.bis.gov.in/php/BIS_2.0/BISBlog/?p=560", verification="public_data"),
    S("IS 2112", 2014, title="Silver and Silver Alloys, Jewellery/Artefacts — Fineness and Marking — Specification",
      source_url="https://en.vikaspedia.in/viewcontent/social-welfare/social-awareness/consumer-education/hallmarking-of-gold-jewellery-consumer-education-1/hallmarking-of-gold-jewellery",
      verification="public_data", notes="Applies instead of IS 1417 if the article is silver, not gold."),
    S("IS 15820", 2009, title="General Requirements for Establishment and Operation of Assaying and Hallmarking Centres",
      std_type="code_of_practice", source_url="https://services.bis.gov.in/php/BIS_2.0/BISBlog/?p=560",
      verification="public_data"),

    S("IS 1660", 2024, title="Wrought and Cast Aluminium Utensils — Specification (Second Revision)",
      family="aluminium-utensils", status="current",
      amendment_note="A draft Amendment No. 1 was circulated by BIS in Sept 2024. Whether a final amendment has been issued is not confirmed — check BIS.",
      source_url="https://services.bis.gov.in/tmp/1733919988.pdf", verification="official_verified"),
    S("IS 1660", 2009, title="Wrought Aluminium Utensils — Specification (First Revision)", family="aluminium-utensils",
      status="superseded", replaced_by=K("IS 1660", None, 2024),
      amendments=[{"no": 1, "date": None, "note": "One amendment recorded; incorporated into the 2024 revision."}],
      source_url="https://services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/Indian_standards/isdetails/MjEyMzk=",
      verification="official_verified"),
    S("IS 21", 1992, title="Wrought Aluminium and Aluminium Alloys for Manufacture of Utensils — Specification (Fourth Revision)",
      std_type="normative_reference", status="current",
      source_url="https://services.bis.gov.in/tmp/1733919988.pdf", verification="official_verified"),
    S("IS 737", 2008, title="Wrought Aluminium and Aluminium Alloy Sheet and Strip — Specification (Fourth Revision)",
      std_type="normative_reference", status="superseded", replaced_by=K("IS 737", None, 2024),
      source_url="https://services.bis.gov.in/tmp/1733919988.pdf", verification="official_verified"),
    S("IS 737", 2024, title="Wrought Aluminium and Aluminium Alloy Sheet and Strip — Specification (Fifth Revision)",
      std_type="normative_reference", status="current",
      source_url="https://services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/Indian_standards/isdetails/MzM0NTE=",
      verification="official_verified"),
    S("IS 617", 1994, title="Cast Aluminium and its Alloys — Ingots and Castings for General Engineering Purposes — Specification (Third Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 734", 1975, title="Wrought Aluminium and Aluminium Alloy Forging Stock and Forgings — Specification (Second Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 739", 1992, title="Wrought Aluminium and Aluminium Alloys — Wire for General Engineering Purposes — Specification (Third Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 740", 1977, title="Wrought Aluminium and Aluminium Alloy Rivet Stock — Specification (Second Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 1868", 1996, title="Anodic Coatings on Aluminium and its Alloys — Specification (Third Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 5522", 2014, title="Stainless Steel Sheets and Strips for Utensils — Specification (Third Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 5523", 1983, title="Method of Testing Anodic Coating on Aluminium and its Alloys (First Revision)",
      std_type="test_method", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 6057", 1988, title="Specification for Hard Anodic Coatings on Aluminium and Aluminium Alloys (First Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 6527", 1995, title="Stainless Steel Wire Rods — Specification (First Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 6528", 1995, title="Stainless Steel Wire — Specification (First Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 6911", 2017, title="Stainless Steel Plate, Sheet and Strip — Specification (Second Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 9040", 1978, title="Method for Sampling of Utensils", std_type="sampling",
      source_url="https://services.bis.gov.in/tmp/1733919988.pdf", verification="official_verified"),
    S("IS 9730", 2008, title="Non-stick Unreinforced Plastics Coatings on Domestic Cooking Utensils — Specification (First Revision)",
      std_type="test_method", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 9806", 2001, title="Methods of Test for and Permissible Limits of Toxic Materials Released from Ceramicware in Contact with Food (First Revision)",
      std_type="test_method", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 13395", 2021, title="Performance of Handles and Handle Assemblies Attached to Cookware — Specification (First Revision)",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 15997", 2012, title="Low Nickel Austenitic Stainless Steel Sheet and Strip for Utensils — Specification",
      std_type="normative_reference", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),
    S("IS 101", 1986, part="2/Sec 2",
      title="Methods of Sampling and Test for Paints, Varnishes and Related Products — Part 2 Section 2: Volatile Matter",
      std_type="test_method", source_url="https://services.bis.gov.in/tmp/1733919988.pdf",
      verification="official_verified"),

    S("IS 16102", 2012, part="1",
      title="Self-Ballasted LED Lamps for General Lighting Services — Part 1: Safety Requirements",
      family="led-lamps-crs", status="current",
      amendment_note="Amendments not checked. Look up IS 16102 (Part 1) on the BIS Know Your Standard portal.",
      source_url="https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme",
      verification="official_verified"),
    S("IS 15885", 2012, part="2/Sec 13",
      title="Safety of Lamp Control Gear — Part 2 Section 13: d.c. or a.c. Supplied Electronic Control Gear for LED Modules",
      source_url="https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme",
      verification="official_verified"),
    S("IS 16103", 2012, part="1", title="LED Modules for General Lighting — Part 1: Safety Requirements",
      source_url="https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme",
      verification="official_verified"),
    S("IS 10322", None, part="5/Sec 1",
      title="Luminaires — Part 5: Particular Requirements — Section 1: Fixed General Purpose Luminaires",
      source_url="https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme",
      verification="official_verified"),
]


def E(src, dst, edge_type, mandatory=False, condition="", evidence="", source_url=""):
    return {"src": src, "dst": dst, "edge_type": edge_type, "mandatory": mandatory,
            "condition": condition, "evidence": evidence, "source_url": source_url}


TMT = K("IS 1786", None, 2008)
CEM = K("IS 269", None, 2015)
ALU = K("IS 1660", None, 2024)
GOLD = K("IS 1417", None, 2016)
LED = K("IS 16102", "1", 2012)

_T = "https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf"
_C = "https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/standard_review/Standard_review/Isdetails?ID=MTEx"
_A = "https://services.bis.gov.in/tmp/1733919988.pdf"

EDGES = [
    E(TMT, K("IS 228", None, None), "test_method", True, "", "Clause 4.2: ladle analysis by IS 228.", _T),
    E(TMT, K("IS 1608", "1", None), "test_method", True, "", "Clause 9.2: tensile strength per IS 1608 (Part 1).", _T),
    E(TMT, K("IS 1599", None, 1985), "test_method", True, "", "Clause 9.3: bend test per IS 1599.", _T),
    E(TMT, K("IS 2062", None, 2006), "normative_reference", True, "", "Clause 9.1: sample selection per IS 2062.", _T),
    E(TMT, K("IS 1387", None, 1993), "normative_reference", True, "", "Clause 12.1: general supply requirements per IS 1387.", _T),
    E(TMT, K("IS 2770", "1", 1967), "test_method", True, "when pull-out bond test route is used (cl. 5.1, 5.7)", "Pull-out test per IS 2770 (Part 1).", _T),
    E(TMT, K("IS 9417", None, 1989), "installation", True, "when bars are to be welded (cl. 4.2.2)", "Welding recommendations per IS 9417.", _T),
    E(TMT, K("IS 456", None, 2000), "code_of_practice", False, "", "RCC design code governing use of reinforcement.", "https://law.resource.org/pub/in/bis/S03/is.456.2000.pdf"),
    E(TMT, K("IS 13920", None, None), "safety", False, "", "Seismic ductility code for ductile (D) grades.", "https://infralens.in/term/fy"),

    E(CEM, K("IS 4031", None, None), "test_method", True, "", "Physical properties tested per IS 4031.", _C),
    E(CEM, K("IS 4032", None, 1985), "test_method", True, "", "Chemical requirements tested per IS 4032.", _C),
    E(CEM, K("IS 650", None, 1991), "test_method", True, "", "Standard sand for compressive strength test.", _C),
    E(CEM, K("IS 4905", None, 2015), "sampling", True, "", "Random sampling procedures.", _C),
    E(CEM, K("IS 2580", None, 1995), "packaging", False, "when jute sacking bags are used", "Jute bags for packing cement.", _C),
    E(CEM, K("IS 456", None, 2000), "code_of_practice", False, "", "IS 456 specifies minimum cement content by exposure class.", "https://law.resource.org/pub/in/bis/S03/is.456.2000.pdf"),
    E(CEM, K("IS 1489", "1", 2015), "co_cited", False, "", "Portland Pozzolana Cement, fly ash based.", "https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/"),
    E(CEM, K("IS 455", None, 2015), "co_cited", False, "", "Portland Slag Cement.", "https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/"),

    E(GOLD, K("IS 15820", None, 2009), "code_of_practice", True, "", "Hallmarking at BIS-recognised Assaying and Hallmarking Centres per IS 15820.", "https://services.bis.gov.in/php/BIS_2.0/BISBlog/?p=560"),
    E(GOLD, K("IS 2112", None, 2014), "co_cited", False, "", "IS 2112 applies instead of IS 1417 if the article is silver.", "https://en.vikaspedia.in/viewcontent/social-welfare/social-awareness/consumer-education/hallmarking-of-gold-jewellery-consumer-education-1/hallmarking-of-gold-jewellery"),

    E(ALU, K("IS 21", None, 1992), "normative_reference", True, "", "Cl. 4.1: main body per IS 21 or IS 737.", _A),
    E(ALU, K("IS 737", None, 2008), "normative_reference", True, "for body, strips and lids (cl. 4.1, 4.2, 4.6)", "Edition cited in Annex A. Fifth revision IS 737:2024 is now current.", _A),
    E(ALU, K("IS 617", None, 1994), "normative_reference", True, "for cast cookware only (cl. 4.1)", "Main body of cast cookware per IS 617.", _A),
    E(ALU, K("IS 734", None, 1975), "normative_reference", True, "for other aluminium parts (cl. 4.1)", "Other parts per IS 21, IS 617, IS 734 or IS 737.", _A),
    E(ALU, K("IS 739", None, 1992), "normative_reference", True, "for lunch-box clips (cl. 4.3)", "Clips per IS 739.", _A),
    E(ALU, K("IS 740", None, 1977), "normative_reference", True, "for rivets (cl. 4.5)", "Rivets per IS 739 / IS 740.", _A),
    E(ALU, K("IS 5522", None, 2014), "normative_reference", True, "when stainless steel lids, rims or rivet caps are used", "Stainless steel sheets and strips for utensils.", _A),
    E(ALU, K("IS 6527", None, 1995), "normative_reference", True, "for stainless steel handles and rivets", "Stainless steel wire rods.", _A),
    E(ALU, K("IS 6528", None, 1995), "normative_reference", True, "for stainless steel rivets (cl. 4.5)", "Stainless steel wire.", _A),
    E(ALU, K("IS 6911", None, 2017), "normative_reference", True, "for stainless steel lids, handles or induction plates", "Stainless steel plate, sheet and strip.", _A),
    E(ALU, K("IS 15997", None, 2012), "normative_reference", True, "for low-nickel stainless steel lids (cl. 4.1.1)", "Low nickel austenitic stainless steel.", _A),
    E(ALU, K("IS 1868", None, 1996), "normative_reference", True, "when the utensil is anodized (cl. 5.4.1, 8.3)", "Anodic coating grade AC 5 or above.", _A),
    E(ALU, K("IS 6057", None, 1988), "normative_reference", True, "for hard-anodized cookware (cl. 8.3)", "Hard anodic coatings.", _A),
    E(ALU, K("IS 5523", None, 1983), "test_method", True, "for hard-anodized cookware (cl. 8.3 note)", "Abrasion resistance test method.", _A),
    E(ALU, K("IS 9730", None, 2008), "test_method", True, "when non-stick or ceramic coating is used (cl. 8.5-8.7)", "Non-stick coatings test.", _A),
    E(ALU, K("IS 9806", None, 2001), "test_method", True, "for ceramic coatings (cl. 8.6, 8.7)", "Toxic material release limits for food-contact coatings.", _A),
    E(ALU, K("IS 13395", None, 2021), "normative_reference", True, "for cookware handles (cl. 7.3)", "Performance of handles attached to cookware.", _A),
    E(ALU, K("IS 9040", None, 1978), "sampling", True, "", "Cl. 13: sampling per IS 9040.", _A),
    E(ALU, K("IS 101", "2/Sec 2", 1986), "test_method", False, "", "Listed in Annex A.", _A),

    E(LED, K("IS 16103", "1", 2012), "co_cited", False, "", "CRS-listed: stand-alone LED modules.", "https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme"),
    E(LED, K("IS 15885", "2/Sec 13", 2012), "co_cited", False, "", "CRS-listed: electronic control gear for LED modules.", "https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme"),
    E(LED, K("IS 10322", "5/Sec 1", None), "co_cited", False, "", "CRS-listed: fixed general purpose LED luminaires.", "https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme"),
]

_seen = set()
_dedup = []
for _e in EDGES:
    _k = (_e["src"], _e["dst"], _e["edge_type"])
    if _k not in _seen:
        _seen.add(_k)
        _dedup.append(_e)
EDGES = _dedup


def C(family, is_number, scheme, order_ref, effective=None, since_year=None, size="all", state="in_force",
      notes="", source_url="", verification="public_data"):
    return {
        "family": family, "is_number": is_number, "scheme": scheme, "order_ref": order_ref,
        "effective_date": effective, "since_year": since_year, "enterprise_size": size, "state": state,
        "notes": notes, "source_url": source_url, "verification": verification,
        "last_verified": LAST_VERIFIED,
    }


_QCO_AL = "https://absoluteveritas.com/bis-qco-for-wrought-aluminium-utensils/"
_QCO_AL25 = "https://alephindia.in/bis-qco-for-the-wrought-aluminium-utensils.php"
_QCO_AL26 = "https://www.alcircle.com/news/a-fresh-qco-puts-aluminium-cans-and-cookware-under-the-compliance-spotlight-116959"
_QCO_AL26B = "https://www.intertek.com/products-retail/insight-bulletins/2026/1518-india-published-the-cookware-utensils-and-cans-for-foods-and-beverages-quality-control-order-2026/"
_HM = "https://en.vikaspedia.in/viewcontent/social-welfare/social-awareness/consumer-education/hallmarking-of-gold-jewellery-consumer-education-1/hallmarking-of-gold-jewellery"
_BISCRS = "https://www.bis.gov.in/product-certification/products-under-compulsory-certification/scheme-ii-registration-scheme"

CERTS = [
    C("tmt-steel-bars", "IS 1786:2008", "ISI Mark",
      "Steel and Steel Products (Quality Control) Order, 2024 (S.O. 574(E), 5 Feb 2024)",
      effective=dt.date(2024, 2, 5),
      notes="Standard Mark required under Scheme-I. Bars below 8 mm and goods made only for export are exempt.",
      source_url="https://alephindia.in/bis-qco-for-the-high-strength-deformed-steel-bars-and-wires-for-concrete-reinforcement.php"),
    C("cement-opc", "IS 269:2015", "ISI Mark", "Cement (Quality Control) Order, 2003",
      since_year=2003,
      notes="No person may manufacture, store for sale, sell or distribute cement without the Standard Mark.",
      source_url="https://www.bis.gov.in/standards/standard-formulation/international-standardization-activity/"),
    C("gold-hallmarking", "IS 1417:2016", "Hallmarking",
      "Hallmarking of Gold Jewellery and Gold Artefacts Order, 2020 — first phase",
      effective=dt.date(2021, 6, 16),
      notes="Mandatory hallmarking began 16 June 2021 in notified districts.",
      source_url=_HM),
    C("gold-hallmarking", "IS 1417:2016", "Hallmarking",
      "HUID-only sale mandate (Department of Consumer Affairs)",
      effective=dt.date(2023, 4, 1),
      notes="Sale of hallmarked gold jewellery without a 6-digit HUID is prohibited since this date.",
      source_url="https://www.tribuneindia.com/news/business/sale-of-gold-jewellery-hallmarked-without-6-digit-code-to-be-banned-after-march-31-14980"),
    C("gold-hallmarking", "IS 1417:2016", "Hallmarking",
      "Hallmarking Order amendments of 2026 — district coverage expansion",
      state="notified",
      notes="BIS lists 2026 amendments (2 Mar, 28 Apr, 3 Aug). Effective date per district not confirmed. Check whether the delivery district is covered.",
      source_url=_BISCRS),
    C("aluminium-utensils", "IS 1660:2024", "QCO", "Cookware, Utensils and Cans for Foods and Beverages (QCO), 2024",
      effective=dt.date(2024, 4, 1), size="large", state="superseded",
      notes="Original enforcement date for large enterprises under the 2024 order.", source_url=_QCO_AL),
    C("aluminium-utensils", "IS 1660:2024", "QCO", "Cookware, Utensils and Cans for Foods and Beverages (QCO), 2024",
      effective=dt.date(2025, 7, 1), size="small", state="superseded",
      notes="Small-enterprise phase-in date under the 2024 order.", source_url=_QCO_AL),
    C("aluminium-utensils", "IS 1660:2024", "QCO", "Cookware, Utensils and Cans for Foods and Beverages (QCO), 2024",
      effective=dt.date(2025, 10, 1), size="micro", state="superseded",
      notes="Micro-enterprise phase-in date under the 2024 order.", source_url=_QCO_AL),
    C("aluminium-utensils", "IS 1660:2024", "QCO",
      "Cookware, Utensils and Cans for Foods and Beverages (Quality Control) Extension Order, 2025",
      effective=dt.date(2025, 10, 1), state="superseded",
      notes="Extended and updated the referenced standard editions; replaced by the 2026 order.", source_url=_QCO_AL25),
    C("aluminium-utensils", "IS 1660:2024", "QCO",
      "Cookware, Utensils and Cans for Foods and Beverages (Quality Control) Order, 2026",
      effective=dt.date(2026, 10, 1), size="large",
      notes="Large enterprises: 1 Oct 2026. Micro enterprises: 1 Apr 2027. Small-enterprise date not confirmed.",
      source_url=_QCO_AL26),
    C("aluminium-utensils", "IS 1660:2024", "QCO",
      "Cookware, Utensils and Cans for Foods and Beverages (Quality Control) Order, 2026",
      effective=dt.date(2027, 4, 1), size="micro", state="notified",
      notes="Micro-enterprise compliance date.", source_url=_QCO_AL26B),
    C("aluminium-utensils", "IS 1660:2024", "QCO",
      "Cookware, Utensils and Cans for Foods and Beverages (Quality Control) Order, 2026",
      size="small", state="notified",
      notes="Exact small-enterprise date under the 2026 order not confirmed. Verify with DPIIT/BIS.",
      source_url=_QCO_AL26),
    C("led-lamps-crs", "IS 16102 (Part 1):2012", "CRS",
      "Electronics and Information Technology Goods (Requirement of Compulsory Registration) Order, 2021",
      since_year=2021,
      notes="BIS lists self-ballasted LED lamps under the Compulsory Registration Scheme (Scheme-II). The 2021 order replaced the earlier 2012 CRS order.",
      source_url=_BISCRS),
]


def P(family, std_key, grade, param, operator, value, unit, clause_ref, source_url="", verification="public_data"):
    return {"family": family, "std_key": std_key, "grade": grade, "param": param, "operator": operator,
            "value": value, "unit": unit, "clause_ref": clause_ref, "source_url": source_url,
            "verification": verification}


PARAMS = []
_T_SRC = "https://law.resource.org/pub/in/bis/S03/is.1786.2008.pdf"
for _g, _v in [("Fe 415", 415), ("Fe 415D", 415), ("Fe 415S", 415),
               ("Fe 500", 500), ("Fe 500D", 500), ("Fe 500S", 500),
               ("Fe 550", 550), ("Fe 550D", 550), ("Fe 600", 600),
               ("Fe 650", 650), ("Fe 700", 700)]:
    PARAMS.append(P("tmt-steel-bars", TMT, _g, "yield_strength", "min", _v, "MPa",
                    "cl. 1.1 Note 1 & Table 3: the figure after Fe is the minimum 0.2% proof/yield stress",
                    _T_SRC, "official_verified"))
PARAMS.append(P("tmt-steel-bars", TMT, "Fe 415S", "yield_strength", "max", 540, "MPa",
                "Table 3 as substituted by Amendment No. 1 (2012)", _T_SRC, "official_verified"))
PARAMS.append(P("tmt-steel-bars", TMT, "Fe 500S", "yield_strength", "max", 625, "MPa",
                "Table 3 as substituted by Amendment No. 1 (2012)", _T_SRC, "official_verified"))

_CS = "https://starcement.co.in/pdf/Pamphlet%20on%20Requirements%20of%20Ordinary%20Portland%20Cement%20as%20per%20IS%20269-2015.pdf"
for _g, _v in [("33", 33), ("43", 43), ("43S", 43), ("53", 53), ("53S", 53)]:
    PARAMS.append(P("cement-opc", CEM, _g, "compressive_strength_28d", "min", _v, "MPa",
                    "IS 269:2015 Table 3 (compressive strength at 672 h)", _CS))
PARAMS.append(P("cement-opc", CEM, "33", "compressive_strength_28d", "max", 48, "MPa",
                "IS 269:2015 Table 3 upper limit at 672 h", _CS))
PARAMS.append(P("cement-opc", CEM, "43", "compressive_strength_28d", "max", 58, "MPa",
                "IS 269:2015 Table 3 upper limit at 672 h", _CS))

PARAMS.append(P("aluminium-utensils", ALU, None, "sheet_thickness", "min", 0.70, "mm",
                "Table 1 and cl. 3.1.2", _A, "official_verified"))
PARAMS.append(P("aluminium-utensils", ALU, None, "toxic_metal_content", "max", 0.05, "%",
                "cl. 4.1 Note: not more than 0.05 percent of toxic metals (lead, cadmium, mercury, chromium VI)", _A, "official_verified"))
PARAMS.append(P("aluminium-utensils", ALU, None, "glass_lid_thickness", "min", 3.5, "mm",
                "cl. 4.1.2: minimum thickness of tempered glass lid", _A, "official_verified"))
PARAMS.append(P("aluminium-utensils", ALU, None, "stainless_lid_thickness", "min", 0.4, "mm",
                "cl. 4.1.1: minimum thickness of stainless steel lid", _A, "official_verified"))
PARAMS.append(P("aluminium-utensils", ALU, None, "powder_coating_thickness", "min", 30, "micron",
                "cl. 8.7: minimum thickness of powder coating", _A, "official_verified"))
PARAMS.append(P("aluminium-utensils", ALU, None, "ceramic_coating_thickness", "min", 15, "micron",
                "cl. 8.7: minimum thickness of ceramic coating", _A, "official_verified"))

SCHEME_LABELS = {
    "ISI Mark": "BIS Product Certification — Standard (ISI) Mark, Scheme-I",
    "QCO": "Quality Control Order — BIS Standard Mark required",
    "CRS": "Compulsory Registration Scheme (Scheme-II)",
    "Hallmarking": "BIS Mandatory Hallmarking (with HUID)",
}

ALLOWED_HALLMARK_KARATS = [14, 18, 20, 22, 23, 24]
