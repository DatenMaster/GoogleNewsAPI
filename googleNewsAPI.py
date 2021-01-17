'''
Created on 17 Jan 2021

@author: Daten Master
'''
from GoogleNews import GoogleNews

googlenews = GoogleNews()

##############################################################
################ Definition der Suche ########################
##############################################################

googlenews.set_encode('utf-8')
# Sprache definieren (z.B. 'de'=deutsch; 'en'=englisch; ...)
googlenews.set_lang('de')
# nach Periode Filtern (z.B. News nicht älter als 1 Tag)
googlenews.set_period('1d')
#googlenews.set_time_range('15/01/2021','17/01/2021')

# Suche ausfuehren
googlenews.get_news('Wetter Hamburg')

##############################################################
######################## Ausgabe #############################
##############################################################

# Alle Infos (Titel, Beschreibung, Zeit, Datum, Link, Quelle)
#print(googlenews.results())

# News-Kopfzeile iterative durchlaufen
#for i in googlenews.results():
#    print(i['title'])
#print('Anzahl Ergebnisse: ', len(googlenews.results()))

# Liste mit allen News-Kopfzeilen
#print(googlenews.get_texts())

# Links zu den Quellen
print(googlenews.get_links())