# medical Terms
medical_terms_lst_definitions_names = [
    "medical_terms",
    "pulimonary_respiratory",
    "renal_kidney",
    "cardiovascular",
    "gastrointestinal",
    "eyes_ears",
    "nuerologic",
    "misc_medical_terms",
    "medical_terms_extended"
]


medical_terms = {
    "cancer":["carcin-","carcino-"],
    "tumor":["onc-", "onco","-oma"],
    "muscle":["my-","myo-"],
    "new":["neo"],
    "tissue":["sarc-","sarco"],
    "front":["anter-","antero-","vent-","ventro-"],
    "side": ["latero-","later-"],
    "middle":["medi-","medio"],
    "back or behind":["poster-","postero-"],
    "below":["infer","infero-"],
    "above":["super-","supero"],
    "back":["dors-","dorse-"],
    "less than normal":["hypo"],
    "greater than normal":["hyper"],
    "intra":["within"],
    "endo":["within"],
    "epi":["upon","on","over"],
    "sub":["under"],
    "skin":["cutane-","cutaneo", "derm-","dermo-","dermato"],
    "nail":["onych- onycho-"],
    "joint":["arth-","artho-"],
    "bone":["oste-","osteo-"],
    "cells":["-cyters"],
    "study of":["ology"],
    "mouth":["oral"]
    }

pulimonary_respiratory = {
    "lung":["pulmon-", "pulmono", "pneum","pneumo"],
    "nose":["nas","naso-", "rhino-"],
    "breathing":["spir-","spiro", "-pnea"],
    "bronchus large airways":["bronch-","broncho"],
    "larnynx(voicebox)":["laryng-","laryngo"],
    "treachea(windpipe)":["trachea","trache"],
    "chestcavity":["thorac-","thoraco","-thorax"],
}

renal_kidney = {
    "bladder":["cyst-","cysto"],
    "kidney":["neph-","nephron"],
    "pertaining to urinary organs":["-ur","uri"]
}

cardiovascular = {
    "slow":["brady"],
    "fast rapid":["tachy-"],
    "blood vessel":["angi-","angio-"],
    "artery":["arter-","arterio"],
    "vein":["ven-","veno-","phleb-","phlebo-"],
    "heart":["cardi-","cardio-"],
    "blood clot":["thromb-","thrombo-"],
    "stop control(bloodflow)":["-stasis"],
    "abnormal condition of the blood":["-emina"],
    "abnormal reduction":["-penia"],
    "flow discharge":["-rrhea"],
    "rapid flow of blood":["-rrhagia"],
    "hardening of arteries":["-sclerosis"]
}

gastrointestinal = {
    "stomach":["gastr-","gastro-"],
    "colon":["col-","colo-"],
    "dueodenum":["duoden-","duodeno-"],
    "intestines":["enter-","entero-"],
    "esophagus":["esophag-","esophago"],
    "gums":["gingiv","gingiva"],
    "toungue":["gloss","glosso-"],
    "liver":["hepat-","hepato"],
    "gallbladder":["chol-","chole-"],
    "digestion":["-peps-","pepso-"],
    "swallowing":["-phag","phago"]
}

eyes_ears = {
    "eye":["ophthalm-","ophthalmo-"],
    "vision":["opt-","opto-"],
    "ear":["ot-","oto"],
}

nuerologic = {
    "brain":["cereb-","cerebro-"],
    "meninges(outer brain layer)":["mening-","meningo-"],
    "nerves and nervous system":["neur-","neuro-"],
    "pain":["-algia"],
    "paralysis":["-pleg"],
    "speech":["-phas"]
}

misc_medical_terms = {
    "difficult or abnormal":["dys"],
    "absent or without":["a-","an-"],
    "pus(infected)":["py-","pyo"],
    "thirst":["dips-","dipso-"],
    "blood sugar glucose":["glyc-","glycol-"],
    "inflamation":["-itis"],
    "abnormal condition":["-oisis"],
    "surigical removal of":["-ectomy"],
    "visual examinations":["-scopy"],
    "enlarged":["-megaly"]    
}

medical_terms_extended = {
    "localize collection of pus":["abscess"],
    "to remove part of a tissue for analysis":["biopsy"],
    "inflammation of the skin tissues":["cellunitis"],
    "tissue swelling due to fluid accumulation":["edema"],
    "redness":["erythema"],
    "disease cayse by bacterial, viral, fungal, parasitic pathogens":["infection"],
    "yellow color of the tissues":["jaundice"],
    "ragged tear in skin":["laceration"],
    "abnormal visual change in tissue appearance":["lesion"],
    "repiratory disease caused by inflammation and narrowing of the airways": ["asthma"],
    "chronic respitory disease caused by inflammation and destruction of lung tissue; usualy due to smoking":["chronic obstructive pulmonary disease (COPD)"],
    "infection within nasal cavity, larynx, pharynx":["upper respiratory infection"],
    "kidney":["renal"],
    "inability to control bowel and bladder functions":["incontinence"],
    "procedure to remove toxic substances from the blood (ie in patients with severe kidney failure)":["dialysis"],
    "UTI (kidney-bladder)":["urinary tract infection"],
    "to eliminate(ie urnination)":["void"],
    "reduction in number of red blood cells(important to carry oxygen to tissues":["anemia"],
    "reduction in number of white blood cells(important to fight infections)":["leukopenia"],
    "reduction in number of platelets(important for blood clot formation)":["thombocytopenia"],
    "low blood pressure":["hypotension"],
    "high blood pressure":["hypertension"],
    "rapid blood loss":["hemorrhage"],
    "heart attack(typically caused by blood clot interrupting blood flow to the heart)":["myocardial infarction"],
    "puncture to vein(to obtain blood)":["venipuncture"],
    "difficulty and or infrequent elimination of stool":["constipation"],
    "frequent elimination of liquid stool":["diarrhea"],
    "swollen distended veins in rectal/anal area":["hermorriods"], 
    "ringing of the ears":["tinnitus"],
    "inflammation of middle ear":["otitus media"],
    "eye condition associated with increased pressure within the eyes":["glaucoma"],
    "eye condition associated with clouding of the eye lens":["cataract"],
    "inflammatory disease of joints caused by uric acid crystals deposition":["gout"],
    "inflammatory disease of joints and tissue caused by abnormal immune system":["rheumatoid arthritis"],
    "loss of counciousness; pass out":["syncope"],
    "abnormal electrical activity in the brain causing impaired conciousness and or involantary muscle movements":["siezure"],
    "decrease in blood supply to brain that results in neurologic damage":["stroke"],
    "sudden decrease in blood supply to brain that resolves (within 1 hour) without permanent neurologic damage":["transient ischemic attack"],
    "intense throbbing heacache disorder that can be accompanied by altered sensations nausea and vommiting":["migraine"],
    "progressive neurologic degeneration causing fatigue impaired balance coordination and vision changes":["multiple sclerosis"],
    "chronic neurologic degeneration causing muscle rigidity tremors (shaking extremities) at rest, loss of facial expression, shuffled gait(walking pattern)":["parkinsons disease"],
    "disease characterized by mood swings from depression to mania":["bipolar disorder"],
    "disease characterized by high blood sugar caused by insufficent amount of insulin or bodys resistance to insulin effects":["diabetes mellitus"],
    "low or high amount of thyroid hormones":["hypo- hyper-thyroidism"]
}


medical_terms_lst_definitions = [
    medical_terms,
    pulimonary_respiratory,
    renal_kidney,
    cardiovascular,
    gastrointestinal,
    eyes_ears,
    nuerologic,
    misc_medical_terms,
    medical_terms_extended
]


#Prescription abbreviations

prescription_abbr_lst_names = [
    "frequency",
    "routes_of_administration",
    "dosage_forms",
    "measurement",
    "prescription_preperation_instruction",
]


frequency = {
    "every":["q"],
    "day":["d"],
    "hour":["hr","h"],
    "once a day":["qd"],
    "every other day":["qod"],
    "twice a day":["bid"],
    "three times a day":["tid"],
    "four times a day":["qid"],
    "every morning":["qam"],
    "every evening":["qpm"],
    "at bedtime":["qhs"],
    "every _ hour":["q _ h(q4h every four hours)"],
    "around the clock":["atc"],
    "before meals":["ac"],
    "after meals":["pc"],
    "as needed":["prn"],
    "immediatley":["stat"],
    "as soon as possible":["asap"],
    "as directed":["utd"]
}

routes_of_administration = {
    "by mouth":["po"],
    "nothing by mouth":["npo"],
    "sublingual(under the tounge)":["sl"],
    "nasogastric tube":["ngt"],
    "gatric tube":["gt"],
    "left ear":["as"],
    "right ear":["ad"],
    "both ears":["au"],
    "left eye":["os"],
    "right eye":["od"],
    "both eyes":["ou"],
    "right":["r"],
    "left":["l"],
    "per rectum":["pr","rect"],
    "inhalation":["inh"],
    "intravenous":["iv"],
    "intramuscular":["im"],
    "intranasal":["in","nas"],
    "subcutaneous(under the skin)":["sc","sq"],
    "intrathecal(into the spinal fluid)":["it"],
    "intraosseus(into the bone)":["io"],
    "topically":["top"],
    "intradermal":["id"],
    "vaginally":["v","pv"]
}

dosage_forms = {
    "tablet":["tab","t"],
    "capsule":["cap","c"],
    "solution":["sol"],
    "suspension":["susp"],
    "syrup":["syr"],
    "elixir":["elix"],
    "lozenge":["loz","trouch"],
    "ointment":["oint","ungt"],
    "suppository":["supp"],
    "IV push":["ivp"],
    "IV piggy back":["ivpb"],
    "injection":["inj"],
    "ampule":["amp"],
    "extended release":["er","xr"],
    "delayed release":["dr"],
    "enteric coated":["ec"],
    "immediate release":["ir"],
    "controlled release":["cr"],
    "long acting":["la"],
    "metered dose inhaler":["mdi"],
    "nebulizer":["neb"]
}

measurement = {
    "teaspoon (5ml)":["tsp"],
    "tablespoon (15ml)":["tbsp"],
    "cubic centimeter (= to ml)":["cc"],
    "milliliter":["ml"],
    "liter (1000ml)":["l"],
    "ounce (30ml)":["oz"],
    "gallon":["gal"],
    "pint":["pt"],
    "drop":["gtt"],
    "microgram":["mcg"],
    "milligram":["mg"],
    "gram":["g","gm"],
    "kilogram":["kg"],
    "pound":["lb"],
    "milliequivalent":["mEq"],
    "international unit":["iu"],
    "milliosmoles":["mOsm"],
    "body surface area":["bsa"],
    "one half":["ss"]
}

prescription_preperation_instruction = {
    "dispense":["disp"],
    "of each":["aa"],
    "apply to the affected area":["aaa"],
    "water":["aq"],
    "to make up to":["ad"],
    "to make sufficent quantity":["qs"],
    "number":["no."],
    "and":["et"],
    "apply":["appl"],
    "make":["ft"],
    "mix":["m"],
    "write directions (on label)":["sig"],
    "with":["c"],
    "without":["s"],
    "dilute":["dil"],
    "dispense as written":["daw"]
}

prescription_abbr_lst = [
    frequency,
    routes_of_administration,
    dosage_forms,
    measurement,
    prescription_preperation_instruction
]


#clinical

clinical_definitions_lst_names = [
    "clinical_cardiovascular",
    "clinical_gastrointestinal",
    "misc_medical_terms_clinical",
    "common_medication_abbr"
]

clinical_cardiovascular = {
    "hypertension":["HTN"],
    "blood pressure":["BP"],
    "systolic blood pressure":["SBP"],
    "diastolic blood pressure":["DBP"],
    "heart rate(pulse)":["HR"],
    "respiratory rate":["RR"],
    "coronary artery disease":["CAD"],
    "coronary heart disease":["CHD"],
    "heart failure":["HF"],
    "myocardinal infarction":["MI"],
    "cardiopulmonary resuscitation":["CPR"],
    "Coronary artery bypass graft (surgical procedure)":["CABG"],
    "Electrocardiogram (measurement of heart electrical activity":["EKG or ECG"]
}

clinical_gastrointestinal = {
    "bowel movement":["BM"],
    "Nausea":["N"],
    "Vomiting":["V"],
    "peptic ulcer disease":["PUD"],
    "Gastroesophageal reflux disease":["GERD"],
}

misc_medical_terms_clinical = {
    "headache":["HA"],
    "upper respatory":["URI"],
    "Urinary tract infection":["UTI"],
    "urine analysis":["UA"],
    "intraocular pressure(pressure in the eye)":["IOP"],
    "chronic obstrutive pulomary disease":["COPD"],
    "status post":["s/p"],
    "shortness of breath":["SOB"],
    "blood sugar":["BS"],
    "fasting blood sugar":["FBS"],
    "benign prostatic hypertrophy": ["BPH"],
    "deep venous thrombosis":["DVT"],
    "culture and sensitivity":["C&S"],
    "chest x-ray":["CXR"],
    "no known allergies":["NKA"],
    "no known drug allergies":["NKDA"],
    "red blood cell (erythrocyte)":["RBC"],
    "white blood cell (leukocyte)":["WBC"],
    "tuberculosis":["TB"],
    "electroencephalogram (tracing of the electrical activity of the brain)":["EEG"],
    "cerebrovascularaccident (stroke)":["CVA"],
    "central nervous system":["CNS"],
    "obstructive sleep apnea":["OSA"]
}

common_medication_abbr = {
    "Acetaminophen":["APAP"],
    "Aspirin":["ASA"],
    "Erythromycin (ethyl succinate)":["EES"],
    "trimethoprim":["TMP"],
    "sulfamethoxazole":["SMZ"],
    "hydrocortisone":["HC"],
    "hydrochlorothiazide":["HCTZ"],
    "medrol dosepack":["MDP"],
    "nonsteroidal anti-inflammatory":["NSAID"],
    "over the counter":["OTC"],
    "Normal saline":["NS"],
    "lactated ringers":["LR"],
    "Dextrose 5 percent in water":["D5W"],
    "iron":["Fe"]
}

clinical_definitions_lst = [
    clinical_cardiovascular,
    clinical_gastrointestinal,
    misc_medical_terms_clinical,
    common_medication_abbr
]


#Key definitions

key_definitions = {
    'plist': ' plist is the mdeications that have been identified as being acutley toxic if disposed of incorrectly',
    'garbing': ' Garbing the process of putting on the proper clothing in a specific order',
    'bio hazardous': ' Bio Hazardous is any waste that could possibly contain infectious material such as blood',
    'aseptic techniques': ' Aseptic Technique is a procedure designed to remove the potential for the contamination of drugs ',
    'ulist': ' ulist is the list of medications that are toxic, flammable, or reactive and are considered hazardous'
}
