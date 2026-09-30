EXAMPLES = [
    {
        'id': 'tmt-conflict',
        'label': 'TMT bars — grade conflict',
        'description': (
            'The department intends to procure high strength deformed TMT reinforcement bars '
            'for RCC columns and beams of a new government office building under construction.\n'
            'Material shall be of grade Fe 500D conforming to the relevant Indian Standard.\n'
            'Mill test certificates must accompany each consignment and shall show a minimum '
            'yield strength of 415 MPa for all supplied bars.\n'
            'Diameter required is 12 mm and 16 mm. Total quantity is 50 MT.\n'
            'Supply shall be completed within 90 days of the purchase order date.\n'
            'Bidders must hold a valid BIS ISI Mark licence and furnish licence details in the bid.'
        ),
        'tender_date': None,
        'delivery_period_days': 90,
        'enterprise_size': 'large',
        'highlights': 'Fe 500D requires min 500 MPa yield strength — the 415 MPa stated in the tender is a direct contradiction.',
    },
    {
        'id': 'aluminium-live',
        'label': 'Aluminium utensils — live QCO',
        'description': (
            'This tender is for the supply of wrought aluminium cookware and kitchen utensils '
            'for use in the department\'s residential quarters and staff mess.\n'
            'The utensils shall be manufactured from wrought aluminium sheet and shall conform '
            'to IS 1660:2009 as specified in the indent.\n'
            'The supplier is a small enterprise registered under the Udyam portal.\n'
            'Delivery of the full quantity is required within 30 days of the award of contract.\n'
            'The tendering authority requires confirmation of the applicable BIS certification '
            'requirement and whether the cited standard edition is current.'
        ),
        'tender_date': None,
        'delivery_period_days': 30,
        'enterprise_size': 'small',
        'highlights': 'Cites withdrawn IS 1660:2009 (current: IS 1660:2024). Tests the full QCO order-chain for a small enterprise.',
    },
    {
        'id': 'cement-conflict',
        'label': 'Cement — strength conflict',
        'description': (
            'Supply of Ordinary Portland Cement of 43 grade (OPC) for general RCC construction '
            'work at the project site, in 50 kg HDPE-lined bags.\n'
            'The cement shall achieve a 28-day compressive strength of not less than 33 MPa '
            'as per the project specification.\n'
            'Testing of physical and chemical properties shall be carried out as per the '
            'applicable Indian Standard test methods.\n'
            'Delivery is required within 45 days of the supply order in three monthly instalments.\n'
            'The supplier shall hold a valid BIS certification for the supplied grade of cement.'
        ),
        'tender_date': None,
        'delivery_period_days': 45,
        'enterprise_size': 'large',
        'highlights': '43 grade OPC requires minimum 43 MPa at 28 days — stating 33 MPa is a parameter conflict.',
    },
    {
        'id': 'gold-hallmark',
        'label': 'Gold jewellery — caratage conflict',
        'description': (
            'The department requires the supply of hallmarked gold jewellery articles of '
            '21 karat purity for the departmental gift procurement scheme this festive season.\n'
            'All articles must carry a valid Hallmark Unique Identification (HUID) number '
            'as prescribed by BIS under the mandatory hallmarking scheme.\n'
            'The supplier shall be a BIS registered jeweller holding a valid hallmarking licence.\n'
            'Testing of gold purity shall be done at a BIS recognised Assaying and Hallmarking Centre.\n'
            'Please confirm whether IS 1417:2016 is the current applicable standard and whether '
            '21 karat is among the eligible caratages.'
        ),
        'tender_date': None,
        'delivery_period_days': 30,
        'enterprise_size': 'all',
        'highlights': '21 karat is not among the caratages currently covered by the mandatory hallmarking order.',
    },
    {
        'id': 'led-crs',
        'label': 'LED lamps — CRS scheme',
        'description': (
            'Procurement of self-ballasted LED lamps (LED bulbs) of 9W and 12W ratings '
            'for general lighting of office and corridor areas across the building.\n'
            'The lamps shall meet safety requirements and performance specifications for '
            'self-ballasted LED lamps used in general lighting services.\n'
            'Supplier must hold a valid Compulsory Registration under the BIS scheme '
            'for the supplied product models before the supply date.\n'
            'Delivery of 500 units (mixed ratings) is required within 20 days of the order.\n'
            'Lamps must be tested at a BIS recognised or NABL accredited laboratory.'
        ),
        'tender_date': None,
        'delivery_period_days': 20,
        'enterprise_size': 'large',
        'highlights': 'Tests the CRS scheme (Scheme-II, self-declaration) which is different from ISI Mark.',
    },
    {
        'id': 'vague-abstain',
        'label': 'Vague input — system abstains',
        'description': (
            'We need to purchase some good quality material for our upcoming construction work '
            'at the departmental site.\n'
            'Please suggest the appropriate standard to follow for this procurement process.\n'
            'Kindly ensure the specification is in line with current government norms.\n'
            'The supplier should provide all proper documentation and test certificates.\n'
            'This is a routine departmental requirement for the current financial year.'
        ),
        'tender_date': None,
        'delivery_period_days': None,
        'enterprise_size': 'large',
        'highlights': 'No product-specific keywords — the system abstains rather than guessing.',
    },
    {
        'id': 'hindi-transliteration',
        'label': 'Hindi input — transliteration',
        'description': (
            'Sariya ki supply ke liye tender: Fe 500D grade ke deformed reinforcement bars '
            'RCC columns aur beams ke liye chahiye.\n'
            'Mill test certificate mein yield strength 500 MPa se kam nahi honi chahiye.\n'
            'Delivery 90 din mein karni hai purchase order ke baad.\n'
            'Supplier ke paas valid BIS ISI licence hona chahiye.\n'
            'Sare bars IS 1786 ke anusar hone chahiye aur quality certificate dena hoga.'
        ),
        'tender_date': None,
        'delivery_period_days': 90,
        'enterprise_size': 'large',
        'highlights': 'Hindi transliteration (sariya = reinforcement bar) — system detects language and expands to English before matching.',
    },
    {
        'id': 'hindi-devanagari',
        'label': 'Hindi input — Devanagari script',
        'description': (
            'सरिया की आपूर्ति के लिए निविदा: Fe 500D ग्रेड के प्रबलित बार RCC कॉलम और बीम के लिए।\n'
            'मिल टेस्ट सर्टिफिकेट में yield strength 500 MPa से कम नहीं होनी चाहिए।\n'
            'डिलीवरी 90 दिनों में करनी है purchase order के बाद।\n'
            'आपूर्तिकर्ता के पास वैध BIS ISI लाइसेंस होना चाहिए।\n'
            'सभी बार IS 1786 के अनुसार होने चाहिए।'
        ),
        'tender_date': None,
        'delivery_period_days': 90,
        'enterprise_size': 'large',
        'highlights': 'Devanagari script input — Unicode script detection, synonym expansion to English, then standard pipeline.',
    },
]
