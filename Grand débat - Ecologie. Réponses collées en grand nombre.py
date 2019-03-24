
# coding: utf-8

# ## ECO

# RESUME
# 
# 5 questions dans le débat 'ecologie' sont complètement libres (ni qcm, ni suite à une question fermée): ce que j'appelle les questions 2, 6, 7, 16, 17. Les réponses qui reviennent à plusieurs réprises face à ces questions *SEMBLENT* provenir de ces sites / associations:
# 
# https://forums.automobile-propre.com/topic/dire-stop-au-80-kmh-sur-route-sur-le-granddebatfr-13520/
# 
# https://welfarm.fr/grand-debat-national
# 
# https://savoie-antinucleaire.fr/2019/02/13/participons-au-grand-debat-pour-denoncer-larme-nucleaire/
# 
# https://www.animal-cross.org/petition-sanctionnons-les-chasseurs-avec-un-permis-de-chasser-a-points/
# 
# https://www.facebook.com/34207477994/posts/le-comit%C3%A9-scientifique-pro-anima-partage-le-projet-dantidote-davoir-un-grand-d%C3%A9b/10158282873392995/
# 
# 

# In[4]:


# importer et forcer une visibilité de 30 colonnes

import pandas as pd
import os

pd.options.display.max_columns = 30


# In[5]:


# import le ficher csv du site grand débat 

path_to_file = ("CHEMIN ET NOM DE FICHIER ICI")
eco = pd.read_csv(path_to_file)


# In[6]:


# c'est quoi la taille?

print (eco.shape)

raw = os.path.getsize("CHEMIN ET NOM DE FICHIER ICI")
size_mb = raw / 1000000
size_mb


# In[9]:


eco.head(3)


# In[10]:


# renommer les colonnes par rapport au dépliant (https://granddebat.fr/media/default/0001/01/39520feb60078392ddde45ddf9e29873e2ca8070.pdf)
# pour rendre les noms de colonnes plus maniables

eco.rename(columns = {eco.columns[11]: 'q1_plus_gnd_pb'}, inplace = True) # qcm (inc 'autre'. Une réponse permise)

# QUESTION 2
eco.rename(columns = {eco.columns[12]: 'q2_que_faire'}, inplace = True) # LIBRE
# Que faudrait-il faire selon vous pour apporter des réponses à ce problème ?

eco.rename(columns = {eco.columns[13]: 'q3_touché_par_CC'}, inplace = True) # binaire

eco.rename(columns = {eco.columns[14]: 'q3bis_touché_comment'}, inplace = True) # LIBRE (si oui)

eco.rename(columns = {eco.columns[15]: 'q4_pvz_vs_aider'}, inplace = True) # binaire

eco.rename(columns = {eco.columns[16]: 'q4bis_q_faites_feriez_vs'}, inplace = True) # LIBRE (si oui)

# q5 du dépliant n'était pas présent

# QUESTION 6
eco.rename(columns = {eco.columns[17]: 'q6_comment_inciter'}, inplace = True) # LIBRE
# Qu’est-ce qui pourrait vous inciter à changer vos comportements comme par exemple mieux entretenir et régler 
# votre chauffage, modifier votre manière de conduire ou renoncer à prendre votre véhicule pour de très petites 
# distances ?

# QUESTION 7
eco.rename(columns = {eco.columns[18]: 'q7_solutions_abordable_enfric'}, inplace = True) # LIBRE
# Quelles seraient pour vous les solutions les plus simples et les plus supportables sur un plan financier pour 
# vous inciter à changer vos comportements ?

eco.rename(columns = {eco.columns[19]: 'q8_meilleure_chauffage'}, inplace = True) # binaire

eco.rename(columns = {eco.columns[20]: 'q8bis_comment_convaincre'}, inplace = True) # LIBRE (si oui)

# q9 du dépliant n'était pas présent

eco.rename(columns = {eco.columns[21]: 'q10_mobilite_alt'}, inplace = True) # triple

eco.rename(columns = {eco.columns[22]: 'q10bis_comment_convaincre'}, inplace = True) # LIBRE (si oui)

eco.rename(columns = {eco.columns[23]: 'q10ter_vzvoulez_quoi'}, inplace = True) # qcm

eco.rename(columns = {eco.columns[24]: 'q10quat_qui_propose'}, inplace = True) # LIBRE (si non)

# q11 - 15 du dépliant n'était pas présent finalement

# QUESTION 16
eco.rename(columns = {eco.columns[25]: 'q16_q_doit_laFrance'}, inplace = True) # LIBRE
# Que pourrait faire la France pour faire partager ses choix en matière d’environnement au 
# niveau européen et international ?

# QUESTION 17
eco.rename(columns = {eco.columns[26]: 'q17_autre_chose'}, inplace = True) # LIBRE
# Y a-t-il d’autres points sur la transition écologique sur lesquels vous souhaiteriez vous exprimer ?


# In[11]:


eco.columns


# ## réponses repétées aux questions 2, 6, 7, 16, 17

# In[12]:


# répétition dans les réponses à la question 2

eco.q2_que_faire.value_counts()
#vcq2.value_counts().head(5)


# # provenance des réponses multiples à la question 2
# 
# SOURCES
# 
# 117, 33
# https://welfarm.fr/grand-debat-national
# 
# 44, 12, 12
# https://welfarm.fr/grand-debat-national
# 
# 33
# https://savoie-antinucleaire.fr/2019/02/13/participons-au-grand-debat-pour-denoncer-larme-nucleaire/
# 
# 28
# ?
# 
# 26
# ?
# 
# 22
# https://www.animal-cross.org/petition-sanctionnons-les-chasseurs-avec-un-permis-de-chasser-a-points/
# 
# 19, 16, 13
# https://www.facebook.com/34207477994/posts/le-comit%C3%A9-scientifique-pro-anima-partage-le-projet-dantidote-davoir-un-grand-d%C3%A9b/10158282873392995/
#     
#  

# ## répétition dans les réponses à la question 6

# In[28]:


# répétition dans les réponses à la question 6

eco.q6_comment_inciter.value_counts()

# Les 'doublons' viennent surtout des réponses 'c'est fait, j'ai fait etc. Avec l'exception de la réponse 
# qui paraît 154 fois. Il vient de: https://welfarm.fr/grand-debat-national 
# et quelques réponses qui paraissent 9 ou 10 fois pour lesquels j'ai pas trouvé de provenance.


# ## répétition dans les réponses à la question 7

# In[16]:


# repétition dans la question 7 -  cf la réponse qui paraît 177 fois. SOURCE PAS ENCORE TROUVE

eco.q7_solutions_abordable_enfric.value_counts()


# ## répétition dans les réponses à la question 16

# In[17]:


# repétition dans la question 16 - notons la réponse qui revient 146 fois (provenance: welfarm.fr)

eco.q16_q_doit_laFrance.value_counts()


# ## repétition dans la question 17

# In[18]:


# repétition dans la question 17 - une réponse revient 216 fois, SOURCE PAS ENCORE TROUVE
# réponse revenant 35 fois, 20 fois, 12 fois, 11 fois, 3 fois : facebook (pro-anima), voir ci-dessus

# réponse sur la limitation de vitesse, 12 fois:
''' ici, on voit la réponse revenant 12 fois sur la limitation de vitesse:
"Il faut revenir sur l’abaissement de la limitation de vitesse à 80 km/h sur le réseau secondaire. 
Cette mesure a été imposée sans concertation, après une expérimentation biaisée aux résultats peu probants, 
contre l’avis des Français. Cela pénalise injustement les conducteurs : temps de trajet rallongés, dépassements 
dangereux, camions collés aux voitures… Sans parler des radars qui flashent à tout va ! Le Gouvernement doit 
veiller à l’entretien des routes, au lieu d’y baisser la limitation de vitesse ! Le Gouvernement doit mettre 
la politique de sécurité routière au service des conducteurs, au lieu d’en faire une politique fiscale et un 
véritable racket par les radars ! Le Gouvernement doit traiter les conducteurs en citoyens responsables, acteurs 
indispensables de la sécurité routière : laissez-nous adapter notre vitesse aux conditions de circulation, au 
lieu de détourner notre attention de la route, en nous obligeant à rouler à une vitesse inutilement réduite, 
les yeux rivés sur le compteur !""

SOURCE : https://forums.automobile-propre.com/topic/dire-stop-au-80-kmh-sur-route-sur-le-granddebatfr-13520/
'''

eco.q17_autre_chose.value_counts()

