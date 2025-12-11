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
      
   # 0. country as pie chart
   0: { 
         "var":   ["land"],
         "sets":  ["all"],
         "title": "Hvor bor du?",
         "kind":  "pie",
         "cmap":  "Spectral"
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
   3: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["all"], 
         "title": "Har du en funksjonsnedsettelse eller tilstand som påvirker hvordan du gamer/spiller?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   # funksjonsnedsettelse-type-tekst er "Beskriv funksjonsnedsettelsen/tilstanden din:"
   300: {
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
   
   # 5. plattform preferances as pie chart separated by impairment (with, without, combined)
   5: {
         "var": ["plattformpreferanser-kort"],
         "data-sep": ";",
         "sets":  ["all"], 
         "title": "Hvilke spillplattformer bruker du mest?",
         "kind":  "barh",
         "cmap":  bar_color,
         "text_bckgrd": True,
         "is-percentage":  True
      },
   
   # 6. genrepreferances as pie chart separated by impairment (with, without, combined)
   6: {
         "var": ["sjangerpreferanser-kort"],
         "sets":  ["all"],
         "data-sep": ";",
         "title": "Hvilke spillsjangere foretrekker du?",
         "kind":  "barh",
         "cmap":  pie_color_dark,
         "text_bckgrd": True,
         "is-percentage":  True
      },
   
    # 7. genre wishesas pie chart separated by impairment (with, without, combined)
   7: {
         "var": ["sjangeronsker-kort"],
         "sets":  ["all"],
         "data-sep": ";",
         "title": "Hvilke spillsjangere skulle du ønske du kunne spille mer, hvis de var bedre tilgjengelige for deg?",
         "kind":  "barh",
         "cmap":  pie_color_dark,
         "text_bckgrd": True,
         "is-percentage":  True
      },
   
   # 8. gaming habits as pie chart separated by impairment (with, without, combined)
   8: {
         "var": ["opplevde-utfordringer"],
         "sets":  ["all"], 
         "title": "Hvor ofte opplever du at det er vanskelig å spille med dine behov?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   9: { 
         "var":   ["bruk-av-tilgjengelighetsfunksjoner_with-impair"],
         "sets":  ["all"],
         "title": "Hvilke tilgjengelighetsfunksjoner bruker du når du gamer/spiller?",
         "kind":  "text"
      },
   
   10: { 
         "var":   ["savnete-tilgjengelighetsfunksjoner"],
         "sets":  ["all"],
         "title": "Hvilke tilgjengelighetsfunksjoner savner du i spillene du spiller?",
         "kind":  "text"
      },
   
   11: {
         "var": ["personlig-opplevd-curb-cut_with-impair"],
         "sets":  ["all"], 
         "title": "Har du brukt tilgjengelighetsfunksjoner som ikke var laget for dine behov, men som likevel hjalp deg?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   12: { 
         "var":   ["personlig-opplevd-curb-cut-tekst_with-impair"],
         "sets":  ["all"],
         "title": "Hvilke funksjoner gjaldt det?",
         "kind":  "text"
      },
   
   13: {
         "var": ["generell-opplevd-curb-cut_with-impair"],
         "sets":  ["all"], 
         "title": "Har du lagt merke til at funksjoner laget for én gruppe brukes av andre spillere?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   14: { 
         "var":   ["generell-opplevd-curb-cut-tekst_with-impair"],
         "sets":  ["all"],
         "title": "Hvilke funksjoner har du lagt merke til?",
         "kind":  "text"
      },
   
   15: {
         "var": ["holdning-til-tilgjengelighet"],
         "sets":  ["all"], 
         "title": "Tenker du på tilgjengelighet som noe som angår deg?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   16: {
         "var": ["kjennskap-til-tilgjengelighetsfunksjoner"],
         "sets":  ["all"], 
         "title": "Har du lagt merke til tilgjengelighetsinnstillinger eller -funskjoner i spill du har spilt?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   17: { 
         "var":   ["kjennskap-til-tilgjengelighetsfunksjoner-tekst"],
         "sets":  ["all"],
         "title": "Hvilke funksjoner har du lagt merke til?",
         "kind":  "text"
      },
   
   18: {
         "var": ["interesse-for-tilgjengelighetsfunksjoner"],
         "sets":  ["all"], 
         "title": "Er du nysgjerrig på tilgjengelighetsfunksjoner når du ser dem i spill eller på plattformen du bruker?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   19: {
         "var": ["bruk-av-tilgjengelighetsfunksjoner_without-impair"],
         "sets":  ["all"], 
         "title": "Har du noen gang brukt slike funksjoner selv – for eksempel teksting, fargejustering, zoom, kontrolltilpasning eller assistansemoduser?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   20: { 
         "var":   ["bruk-av-tilgjengelighetsfunksjoner-tekst_without-impair"],
         "sets":  ["all"],
         "title": "Hvilke tilgjengelighetsfunksjoner har du brukt?",
         "kind":  "text"
      },
   
   21: { 
         "var":   ["motivasjon-for-bruk-av-tilgjengelighetsfunksjoner"],
         "sets":  ["all"],
         "title": "Hva fikk deg til å bruke disse funksjonene?",
         "kind":  "text"
      },
   
   22: {
         "var": ["personlig-opplevd-curb-cut_without-impair"],
         "sets":  ["all"], 
         "title": "Har du opplevd at funksjoner laget for tilgjengelighet har forbedret din egen spillopplevelse?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   23: { 
         "var":   ["personlig-opplevd-curb-cut-tekst_without-impair"],
         "sets":  ["all"],
         "title": "Har du eksempler på funksjoner der dette har vært tydelig?",
         "kind":  "text"
      },
}
"""
   # 5. default choices as bar chart separated by impairment (with, without, combined)
   5: {
         "var":     ["default-valg"],
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
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hvordan håndterer du varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 5. default choices as bar chart separated by impairment (with, without, combined)
   50: {
         "var":     ["default-valg"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hvordan håndterer du varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 6. general difficulty as bar chart separated by impairment (with, without, combined)
   6: {
         "var":     ["vanskelighetsgrad-generell"],
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
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hvordan opplever du generelt sett å håndtere varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 6. general difficulty as bar chart separated by impairment (with, without, combined)
   60: {
         "var":     ["vanskelighetsgrad-generell"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hvordan opplever du generelt sett å håndtere varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   7: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["all"],
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
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hva synes du generelt om teksten i varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (11,6),
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   70: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Hva synes du generelt om teksten i varsler om informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (11,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   8: {
         "var":     ["vanskelighetsgrad-valg"],
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
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Er det generelt lett eller vanskelig å ta valg for informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   80: {
         "var":     ["vanskelighetsgrad-valg"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "Med vs. Uten funksjonsnedsettelse (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "Med vs. Uten funksjonsnedsettelse (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "uansett funksjonsevne",
               "is-percentage": True
               },
         },
         "title":    "Er det generelt lett eller vanskelig å ta valg for informasjonskapsler?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   9: { 
         "var":   ["eksempler-paa-utfordringer"],
         "sets":  ["all"],
         "title": "Kan du gi et eksempel på noe du synes er vanskelig med cookies?",
         "kind":  "text"
      },
   10: { 
         "var":   ["forbedringsforslag"],
         "sets":  ["all"],
         "title": "Har du en idé om hvordan cookie-bannere kan gjøres enklere å forstå og administrere?",
         "kind":  "text"
      },
"""
   #}

tasks_en = {
      
   # 0. country as pie chart
   0: { 
         "var":   ["land"],
         "sets":  ["se"],
         "title": "From which country did the answers come in?",
         "kind":  "pie",
         "cmap":  "Spectral"
      },
   
   # 1. age as pie chart
   1: {
         "var":   ["alder"],
         "sets":  ["all"], 
         "title": "How old are you?",
         "kind":  "pie",
         "cmap":  pie_color_bright,
         "text_bckgrd": True
      },

   # 10. age as pie chart
   10: {
         "var":           ["alder"],
         "sets":          ["se"], #wech: no
         "title":         "How old are you?",
         "kind":          "pie",
         "target-folder": "sverige",
         "cmap":  pie_color_bright,
         "text_bckgrd": True
      },
   
   # 2. gender as pie chart
   2: {
         "var": ["kjonn"],
         "sets":  ["all"],
         "title": "Are you ...?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
    # 20. gender as pie chart
   20: {
         "var": ["kjonn"],
         "sets":  ["se"],
         "title": "Are you ...?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   # 3. impairment as pie chart
   3: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["all"], 
         "title": "Do you have an impairment or other condition?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   9: {
         "var": ["funksjonsnedsettelse-type-kode"],
         "data-sep": ",",
         "sets": ["all"],
         "title": "Describe your impairment or condition. It is related to …",
         "kind": "pie",
         "cmap": "Spectral",
         "text_bckgrd": True
      },
      
   # 3. impairment as pie chart
   30: {
         "var": ["funksjonsnedsettelse"],
         "sets":  ["se"], 
         "title": "Do you have an impairment or other condition that affects how you use the internet?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   # 4. internet habits as pie chart separated by impairment (with, without, combined)
   4: {
         "var": ["internettvaner"],
         "sets":  ["all"], 
         "title": "How often do you use the internet?",
         "kind":  "pie",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   # 4. internet habits as pie chart separated by impairment (with, without, combined)
   40: {
         "var": ["internettvaner"],
         "sets":  ["se"], 
         "title": "How often do you use the internet?",
         "kind":  "pie",
         "target-folder": "sverige",
         "cmap":  pie_color_dark,
         "text_bckgrd": True
      },
   
   # 5. default choices as bar chart separated by impairment (with, without, combined)
   5: {
         "var":     ["default-valg"],
         "sets":    ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "How do you generally handle cookie notifications?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 5. default choices as bar chart separated by impairment (with, without, combined)
   50: {
         "var":     ["default-valg"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "How do you generally handle cookie notifications?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 6. general difficulty as bar chart separated by impairment (with, without, combined)
   6: {
         "var":     ["vanskelighetsgrad-generell"],
         "sets":    ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "How do you generally find managing cookie notifications?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 6. general difficulty as bar chart separated by impairment (with, without, combined)
   60: {
         "var":     ["vanskelighetsgrad-generell"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "How do you generally find managing cookie notifications?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   7: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "What do you generally think about the text in cookie notifications?",
         "kind":     "bar",
         "fig_size": (11,6),
         "cmap":  bar_color
      },
   
   # 7. text difficulty a bar chart separated by impairment (with, without, combined)
   70: {
         "var": ["vanskelighetsgrad-tekst"],
         "sets":  ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "What do you generally think about the text in cookie notifications?",
         "kind":     "bar",
         "fig_size": (11,6),
         "target-folder": "sverige",
         "cmap":  bar_color
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   8: {
         "var":     ["vanskelighetsgrad-valg"],
         "sets":    ["all"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("equal to","Nei","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Is it generally easy or difficult to make choices for cookies?",
         "kind":     "bar",
         "fig_size": (10,6),
         "cmap":  bar_color
      },
   
   # 8. choice difficulty as bar chart separated by impairment (with, without, combined)
   80: {
         "var":     ["vanskelighetsgrad-valg"],
         "sets":    ["se"],
         "subsets": {
            1: {
               "var":            "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":       "with-v-withou-impair-pct",
               "title-app":      "With vs. Without Impairment (%)",
               "is-percentage":  True
               },
            2: {
               "var":           "funksjonsnedsettelse",
               "operators":     [("not equal to","Ja","without-impair"),("equal to","Ja","with-impair")],
               "file-app":      "with-v-without-impair-num",
               "title-app":     "With vs. Without Impairment (Total #)",
               "is-percentage": False,
               "target-folder": "total"
               },
            3: {
               "var":           "funksjonsnedsettelse",
               "operators":     [],
               "file-app":      "all-abilities",
               "title-app":     "all abilities",
               "is-percentage": True
               },
         },
         "title":    "Is it generally easy or difficult to make choices for cookies?",
         "kind":     "bar",
         "fig_size": (10,6),
         "target-folder": "sverige",
         "cmap":  bar_color
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
   "file-app": {
      "no": "norway-only",
      "se": "sweden-only",
      "all": "all-countries"
      },
   "title-app": {
      "no": "Kun Norge",
      "se": "Kun Sverige",
      "all": "Alle land"
      },
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
   "file-app": {
      "no": "norway-only",
      "se": "sweden-only",
      "all": "all-countries"
      },
   "title-app": {
      "no": "Norway only",
      "se": "Sweden only",
      "all": "All countries combined" #wech
      },
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
   "en": tasks_en
   }

lookup = {
   "no": lookup_no,
   "en": lookup_en
   }