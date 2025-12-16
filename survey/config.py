'''
Created on 10. des. 2025

@author: joschua
'''

import os
import pandas as pd

import seaborn as sns 

pie_color_bright = sns.diverging_palette(350, 225, s=75, l=65, as_cmap=True)#cool"#sns.color_palette("viridis", as_cmap=True)#"cool"
pie_color_dark = sns.diverging_palette(350, 225, s=75, l=65, center="dark",as_cmap=True)
bar_color = sns.diverging_palette(350, 225, s=75, l=65, as_cmap=True)#"cool"#"Paired"

tasks_no = {
   
   "A": {
        "var": None,
        "sets": ["all"],
        "title": "Generell informasjon",
        "kind": "header",
        "niveau": 1
      },
      
   # 0. country as pie chart
   3: { 
         "var":   ["land"],
         "sets":  ["all"],
         "title": "Hvor bor du? (%)",
         "kind":  "barh",
         "cmap":  bar_color,
         "is-percentage": True
      },
   
   # 1. age as pie chart
   1: {
         "var":   ["alder"],
         "sets":  ["all"], 
         "title": "Hvor gammel er du?",
         "kind":  "pie",
         "cmap":  pie_color_bright,
         "text_bckgrd": True
      },

   # 2. gender as pie chart
   2: {
         "var": ["kjonn"],
         "sets":  ["all"],
         "title": "Hva er ditt kjønn?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   # 3. impairment as pie chart
   7: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["all"], 
         "title": "Har du en funksjonsnedsettelse eller tilstand som påvirker hvordan du gamer/spiller?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   # funksjonsnedsettelse-type-tekst er "Beskriv funksjonsnedsettelsen/tilstanden din:"
   8: {
         "var": ["funksjonsnedsettelse-type-kode"],
         "data-sep": ",",
         "sets": ["all"],
         "title": "Beskriv funskjonsnedsettelsen din:",
         "kind": "pie",
         "cmap": "Spectral",
         "text_bckgrd": True
      },
   
   # 4. gaming habits as pie chart separated by impairment (with, without, combined)
   4: {
         "var": ["spillevaner"],
         "sets":  ["all"], 
         "title": "Hvor ofte spiller du dataspill?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   
   400: {
         "var":     ["spillevaner"],
         "sets":    ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "Uansett funksjonsevne (%)",
               "is-percentage": True
               },
         },
         "title":    "Hvor ofte spiller du dataspill?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 5. plattform preferances as pie chart separated by impairment (with, without, combined)
   5: {
         "var": ["plattformpreferanser-kort"],
         "data-sep": ";",
         "sets":  ["all"], 
         "title": "Hvilke spillplattformer bruker du mest? (Total #)",
         "kind":  "barh",
         "cmap":  bar_color,
         "text_bckgrd": True,
         #"is-percentage":  True
      },
   
   # 6. genrepreferances as pie chart separated by impairment (with, without, combined)
   6: {
         "var": ["sjangerpreferanser-kort"],
         "sets":  ["all"],
         "data-sep": ";",
         "title": "Hvilke spillsjangere foretrekker du? (Total #)",
         "kind":  "barh",
         "cmap":  pie_color_dark,
         "text_bckgrd": True,
         #"is-percentage":  True
      },
   
   "B": {
        "var": None,
        "sets": ["all"],
        "title": "Svar fra gamere med funksjonsnedsettelser",
        "kind": "header",
        "niveau": 1
      },
   
    # 7. genre wishesas pie chart separated by impairment (with, without, combined)
   10: {
         "var": ["sjangeronsker-kort"],
         "sets":  ["all"],
         "data-sep": ";",
         "title": "Hvilke spillsjangere skulle du ønske du kunne spille mer,\nhvis de var bedre tilgjengelige for deg? (Total #)",
         "kind":  "barh",
         "cmap":  pie_color_dark,
         "text_bckgrd": True,
         #"is-percentage":  True
      },
   
   # 8. gaming habits as pie chart separated by impairment (with, without, combined)
   9: {
         "var": ["opplevde-utfordringer"],
         "sets":  ["all"], 
         "title": "Hvor ofte opplever du at det er vanskelig å spille med dine behov? (%)",
         "kind":  "bar",
         "cmap":  bar_color,
         "text_bckgrd": True,
         "is-percentage": True,
      },
   
   11: { 
         "var":   ["bruk-av-tilgjengelighetsfunksjoner_with-impair"],
         "sets":  ["all"],
         "title": "Hvilke tilgjengelighetsfunksjoner bruker du når du gamer/spiller?",
         "kind":  "text"
      },
   
   12: { 
         "var":   ["savnete-tilgjengelighetsfunksjoner"],
         "sets":  ["all"],
         "title": "Hvilke tilgjengelighetsfunksjoner savner du i spillene du spiller?",
         "kind":  "text"
      },
   
   13: {
         "var": ["personlig-opplevd-curb-cut_with-impair"],
         "sets":  ["all"], 
         "title": "Har du brukt tilgjengelighetsfunksjoner\nsom ikke var laget for dine behov,\nmen som likevel hjalp deg?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   14: { 
         "var":   ["personlig-opplevd-curb-cut-tekst_with-impair"],
         "sets":  ["all"],
         "title": "Hvilke funksjoner gjaldt det?",
         "kind":  "text"
      },
   
   15: {
         "var": ["generell-opplevd-curb-cut_with-impair"],
         "sets":  ["all"], 
         "title": "Har du lagt merke til at funksjoner\nlaget for én gruppe\nbrukes av andre spillere?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   16: { 
         "var":   ["generell-opplevd-curb-cut-tekst_with-impair"],
         "sets":  ["all"],
         "title": "Hvilke funksjoner har du lagt merke til?",
         "kind":  "text"
      },
   
   "C": {
        "var": None,
        "sets": ["all"],
        "title": "Svar fra gamere uten funksjonsnedsettelser",
        "kind": "header",
        "niveau": 1
      },
   
   17: {
         "var": ["holdning-til-tilgjengelighet"],
         "sets":  ["all"], 
         "title": "Tenker du på tilgjengelighet som noe som angår deg?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   18: {
         "var": ["kjennskap-til-tilgjengelighetsfunksjoner"],
         "sets":  ["all"], 
         "title": "Har du lagt merke til tilgjengelighetsinnstillinger\neller -funskjoner i spill du har spilt?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   19: { 
         "var":   ["kjennskap-til-tilgjengelighetsfunksjoner-tekst"],
         "sets":  ["all"],
         "title": "Hvilke funksjoner har du lagt merke til?",
         "kind":  "text"
      },
   
   20: {
         "var": ["interesse-for-tilgjengelighetsfunksjoner"],
         "sets":  ["all"], 
         "title": "Er du nysgjerrig på tilgjengelighetsfunksjoner\nnår du ser dem i spill eller på plattformen du bruker?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   21: {
         "var": ["bruk-av-tilgjengelighetsfunksjoner_without-impair"],
         "sets":  ["all"], 
         "title": "Har du noen gang brukt slike funksjoner selv –\nfor eksempel teksting, fargejustering, zoom,\nkontrolltilpasning eller assistansemoduser?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   22: { 
         "var":   ["bruk-av-tilgjengelighetsfunksjoner-tekst_without-impair"],
         "sets":  ["all"],
         "title": "Hvilke tilgjengelighetsfunksjoner har du brukt?",
         "kind":  "text"
      },
   
   23: { 
         "var":   ["motivasjon-for-bruk-av-tilgjengelighetsfunksjoner"],
         "sets":  ["all"],
         "title": "Hva fikk deg til å bruke disse funksjonene?",
         "kind":  "text"
      },
   
   24: {
         "var": ["personlig-opplevd-curb-cut_without-impair"],
         "sets":  ["all"], 
         "title": "Har du opplevd at funksjoner laget for tilgjengelighet\nhar forbedret din egen spillopplevelse?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   25: { 
         "var":   ["personlig-opplevd-curb-cut-tekst_without-impair"],
         "sets":  ["all"],
         "title": "Har du eksempler på funksjoner der dette har vært tydelig?",
         "kind":  "text"
      },
}

vanskelighetsgrad_no = {
   -1: "-1 - Svarte ikke",
   1: "1 - Veldig lett",
   2: "2 - Ganske lett",
   3: "3 - Verken lett/\neller vanskelig",
   4: "4 - Ganske vanskelig",
   5: "5 - Veldig vanskelig" 
   }

# The data sets are determined programmatically in the main module under key "data_set"
lookup_no = {
   "file-app": {},
   #   "no": "norway-only",
   #   "se": "sweden-only",
   #   "all": "all-countries"
   #   },
   "title-app": {},
   #   "no": "Kun Norge",
   #   "se": "Kun Sverige",
   #   "all": "Alle land"
   #   },
   "answers-repl": {
      "default-valg": {
         "Jeg ignorerer dem.": "Ignorere",
         "Jeg godtar alle cookies uten å lese informasjonsteksten.": "Godta",
         "Jeg avviser alle cookies, hvis mulig.": "Avvise",
         "Jeg leser informasjonsteksten og deretter bestemmer jeg hva jeg skal avvise eller akseptere.": "Tilpasse",
         },
      "vanskelighetsgrad-generell": vanskelighetsgrad_no,
      "vanskelighetsgrad-tekst": vanskelighetsgrad_no,
      "vanskelighetsgrad-valg": vanskelighetsgrad_no,
      }
   }

alder_en = {
   "19 - 30 år": "19 - 30 years",
   "31 - 49 år": "31 - 49 years",
   "50 - 65 år": "50 - 65 years",
   "66 og eldre": "66 years and older"
   }

kjonn_en = {
   "Mann": "Male",
   "Kvinne": "Female",
   "Ikke-binær": "Non-Binary"
   }

bool_en = {
   "Ja": "Yes",
   "Nei": "No",
   "Ønsker ikke å oppgi": "Prefer not to say"
   }

vanskelighetsgrad_en = {
   -1: "-1 - No answer",
   1: "1 - Very easy",
   2: "2 - Quite easy",
   3: "3 - Neither easy/\nnor difficult",
   4: "4 - Quite difficutl",
   5: "5 - Very difficult" 
   }

funksjonsnedsettelse_type_en = {
   "hørsel": "hearing",
   "kognisjon": "cognition",
   "mobilitet": "mobility",
   "motorikk": "motor",
   "syn": "vision",
   "syn (blind)": "vision (blind)",
   "ubestemt": "unknown"
   }

internettvaner_en = {
   "Daglig": "Daily",
   "Flere ganger om dagen": "Multiple times a day",
   "Ukentlig": "Weekly"
   }

# The data sets are determined programmatically in the main module under key "data_set"
lookup_en = {
   "file-app": {},
   #   "no": "norway-only",
   #   "se": "sweden-only",
   #   "all": "all-countries"
   #   },
   "title-app": {},
   #   "no": "Norway only",
   #   "se": "Sweden only",
   #   "all": "All countries combined" #wech
   #   },
   "answers-repl": {
      "alder": alder_en,
      "kjonn": kjonn_en,
      "funksjonsnedsettelse": bool_en,
      "funksjonsnedsettelse-type-kode": funksjonsnedsettelse_type_en,
      "internettvaner": internettvaner_en,
      "default-valg": {
         "Jeg ignorerer dem.": "Ignore",
         "Jeg godtar alle cookies uten å lese informasjonsteksten.": "Accept",
         "Jeg avviser alle cookies, hvis mulig.": "Reject",
         "Jeg leser informasjonsteksten og deretter bestemmer jeg hva jeg skal avvise eller akseptere.": "Adjust"
         },
      "vanskelighetsgrad-generell": vanskelighetsgrad_en,
      "vanskelighetsgrad-tekst": vanskelighetsgrad_en,
      "vanskelighetsgrad-valg": vanskelighetsgrad_en,
      }
   }

"""
Setting tasks for each language
"""

tasks = {
   "no": tasks_no,
#   "en": tasks_en
   }

#tasks = tasks_no

lookup = {
   "no": lookup_no,
   "en": lookup_en
   }