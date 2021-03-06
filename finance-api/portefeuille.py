from re import M
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as  px
import statistics as cs
from pandas.plotting import scatter_matrix
from numpy.linalg import inv

Attijari = pd.read_excel('/home/tareq/Attijarii.xlsx', index_col='Séance',engine='openpyxl') 
Itissalat = pd.read_excel('/home/tareq/Attissalat.xlsx', index_col='Séance',engine='openpyxl')
BCP = pd.read_excel('/home/tareq/BCP.xlsx', index_col='Séance',engine='openpyxl')
Lafarge = pd.read_excel('/home/tareq/Lafarge.xlsx', index_col='Séance',engine='openpyxl')
BOA = pd.read_excel('/home/tareq/BMCE.xlsx', index_col='Séance',engine='openpyxl')
Cosumar = pd.read_excel('/home/tareq/Cosumar.xlsx', index_col='Séance',engine='openpyxl')
Ciment_Maroc = pd.read_excel('/home/tareq/Cim_Maroc.xlsx', index_col='Séance',engine='openpyxl')
Marsa_Maroc = pd.read_excel('/home/tareq/Marsa_Marooc.xlsx', index_col='Séance',engine='openpyxl')
Label_Vie = pd.read_excel('/home/tareq/LABEL_VIE.xlsx', index_col='Séance',engine='openpyxl')
Taqa_Maroc = pd.read_excel('/home/tareq/Taqa_Maroc.xlsx', index_col='Séance',engine='openpyxl')
HPS = pd.read_excel('/home/tareq/HPS.xlsx', index_col='Séance',engine='openpyxl')
Total_Maroc = pd.read_excel('/home/tareq/Total_MAROC.xlsx', index_col='Séance',engine='openpyxl')
Miniere = pd.read_excel('/home/tareq/M_touiss.xlsx', index_col='Séance',engine='openpyxl')
Mutandis = pd.read_excel('/home/tareq/Mutandis.xlsx', index_col='Séance',engine='openpyxl')
Lesieur = pd.read_excel('/home/tareq/Lesieur.xlsx', index_col='Séance',engine='openpyxl')
Addoha = pd.read_excel('/home/tareq/Addoha.xlsx', index_col='Séance',engine='openpyxl')
Atlanta = pd.read_excel('/home/tareq/Atlanta.xlsx', index_col='Séance',engine='openpyxl')
Auto_Hall = pd.read_excel('/home/tareq/Auto_Hall.xlsx', index_col='Séance',engine='openpyxl')
Snep = pd.read_excel('/home/tareq/Snepp.xlsx', index_col='Séance',engine='openpyxl')
Dar_sadaa = pd.read_excel('/home/tareq/DAR_SADAA.xlsx', index_col='Séance',engine='openpyxl')
MSI = pd.read_excel('/home/tareq/mm.xlsx', index_col='Séance',engine='openpyxl')


data_names = {'Attijari': Attijari, 'Itissalat': Itissalat, 'BCP': BCP, 'Lafarge': Lafarge, 'BOA': BOA, 'Cosumar': Cosumar, 'Ciment_Maroc': Ciment_Maroc, 'Marsa_Maroc': Marsa_Maroc, 'Label_Vie': Label_Vie, 'Taqa_Maroc': Taqa_Maroc,
              'HPS': HPS, 'Total_Maroc': Total_Maroc, 'Miniere': Miniere, 'Mutandis': Mutandis, 'Lesieur': Lesieur, 'Addoha': Addoha, 'Atlanta': Atlanta, 'Auto_Hall': Auto_Hall, 'Snep': Snep, 'Dar_Sadaa': Dar_sadaa, 'MSI': MSI}

Cours_cible=[520,140,300,2350,240,280,2100,310,5400,1280,7000,1900,1850,280,190,12,150,120,900,35]
d=['Attijari','Itissalat','BCP','Lafarge','BOA','Cosumar','Ciment_Maroc','Marsa_Maroc','Label_Vie','Taqa_Maroc','HPS','Total_Maroc','Miniere','Mutandis','Lesieur','Addoha','Atlanta','Auto_Hall','Snep','Dar_Sadaa']


 
 
class Portefeuille:

  def __init__(self,data_names):
    self.data_names=data_names 
    

  def Plot_Actif_Line(self,actif:str):
    # Visualisation des prix d Actif

    if actif == 'MSI':
      return  self.data_names[actif]['Instrument'].plot(figsize=(17,7))
    else :
      return self.data_names[actif]['COURS_CLOTURE'].plot(figsize=(17,7))
    
  def Plot_Indicateur_MA(self,actif:str,longueur:list):

    # Visualisation : Prix + Indicateur Moyenne Mobile 
    # a=Portefeuille(data_names)
    # a.Plot_Indicateur_MA('Attijari',[100,50,133])
    
    d=pd.DataFrame()
    d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']

    for i in range(0,len(longueur)):
      d['MA : {} '.format(longueur[i])]=self.data_names[actif]['COURS_CLOTURE'].rolling(longueur[i]).mean()
    
    return d[list(d.columns)].plot(figsize=(17,7))

  def Plot_Indicateur_Drawdown(self,actif:str,tp):

    # Visualisation : Prix + Indicateur Max/Min Drawdown
    # a=Portefeuille(data_names)
    # a.Plot_Indicateur_Drawdown('MSI','Min')

    d=pd.DataFrame()

    if actif=='MSI':
      if tp in ['max','max'.title(),'max'.upper()] :
        d['cmMax']=self.data_names[actif]['Instrument'].cummax()
        d['COURS_CLOTURE']=self.data_names[actif]['Instrument']
        return d[['cmMax','COURS_CLOTURE']].plot(figsize=(17,7))

      elif tp in ['min','min'.title(),'min'.upper()]  :
        d['cmMin']=self.data_names[actif]['Instrument'].cummin()
        d['COURS_CLOTURE']=self.data_names[actif]['Instrument']
        return d[['cmMin','COURS_CLOTURE']].plot(figsize=(17,7))

    else :
      if tp in ['max','max'.title(),'max'.upper()] :
        d['cmMax']=self.data_names[actif]['COURS_CLOTURE'].cummax()
        d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']
        return   d[['cmMax','COURS_CLOTURE']].plot(figsize=(17,7))

      elif tp in ['min','min'.title(),'min'.upper()]  :
        d['cmMin']=self.data_names[actif]['COURS_CLOTURE'].cummin()
        d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']
        return d[['cmMin','COURS_CLOTURE']].plot(figsize=(17,7))


  def Combinaison_Indicateurs(self,actif,cible_indicateur:list,longueur_MA=None):
    
    # Combinaison entre deux Indicateurs : Moyenne Mobile + Max/Min Drawdown
    # a.Combinaison_Indicateurs('Attijari',['MA','Max','Min'],[100,200,50])  

    d=pd.DataFrame()
    d['COURS_CLOTURE']=self.data_names[actif]['COURS_CLOTURE']

    for i in cible_indicateur:

      if i in ['max','max'.title(),'max'.upper()]:
        d['cmMax']=self.data_names[actif]['COURS_CLOTURE'].cummax()
        
      elif i in ['min','min'.title(),'min'.upper()]  :
        d['cmMin']=self.data_names[actif]['COURS_CLOTURE'].cummin()
          
      elif i in ['Ma','ma','MA']:

        if longueur_MA == None :
          longueur_MA=[50]

        for i in range(0,len(longueur_MA)):
          d['MA : {} '.format(longueur_MA[i])]=self.data_names[actif]['COURS_CLOTURE'].rolling(longueur_MA[i]).mean()
      
    return d[list(d.columns)].plot(figsize=(17,7))

 
  def Calcul_Rendement_Actifs(self, actif:list , tp2:str , date_debut , date_fin ,tp=True ) :
    
    # Rendement des Actifs 
    # a=Portefeuille(data_names)
    # a.Calcul_Rendement_Actifs(['Attijari','BOA','Snep'],'2020-10-10','2022-01-01','Cumulatif',False)
    # tp est toujours = False ( pour ne pas changer la data originale )
    actif=np.array(actif)

    y=[]
    for i in range(0,len(actif)):
      #if i in list(self.data_names.keys()):
      y.append(self.data_names[actif[i]])
    
    if tp == True  :
      if tp2 == 'Quotidien':
        for i in range(0,len(y)):
          y[i]['Rendement']=(y[i]['COURS_CLOTURE'].pct_change())
       
          
      elif tp2 == 'Cumulatif':
        for i in range(0,len(y)):
          y[i]['Rendement_Cumul']=((y[i]['COURS_CLOTURE'].pct_change())+1).cumprod()
     
    elif tp == False:
      d=pd.DataFrame()

      if tp2=='Quotidien':
        for i in range(0,len(actif)):
          d['Rendement {}'.format(actif[i])]=(self.data_names[actif[i]]['COURS_CLOTURE'].loc[date_debut:date_fin]).pct_change()
        return d
        
      elif tp2 == 'Cumulatif':
        for i in range(0,len(actif)):
          d['Rendement_Cumul {}'.format(actif[i])]=(self.data_names[actif[i]].loc[date_debut:date_fin]['COURS_CLOTURE'].pct_change()+1).cumprod()
        return d

  def Plot_Histogramme(self,actif):
    
    # Visualisation du rendement des Actifs en Histogramme
    # a=Portefeuille(data_names)
    # a.Plot_Histogramme('MSI')


    if actif == 'MSI':
      return (self.data_names[actif]['Instrument'].pct_change()).hist(figsize=(13,7),bins=600)
    else :
      return (self.data_names[actif]['COURS_CLOTURE'].pct_change()).hist(figsize=(13,7),bins=600)


  def Risque_Actif(self,actif,date_debut,date_fin):

    # Calcul du Risque des Actif pendant la periode : date_debut et date_fin 
    # a=Portefeuille(data_names)
    # a.Risque_Actif('BCP','2021-01-01','2022-01-01')

    ee=pd.DataFrame()
    if actif == 'MSI':
      ee['Rendement']=self.data_names[actif]['Instrument'].loc[date_debut:date_fin].pct_change()
    else : 
      ee['Rendement']=self.data_names[actif]['COURS_CLOTURE'].loc[date_debut:date_fin].pct_change()
    
    
    return 'Risque_Actif {} : {} % '.format(actif,(ee.std()[0]*np.sqrt(252)*100))
    


  def Covariance_Matrice(self,actif:list,date_debut,date_fin,val):

      # Calcul de la matrice de variance covariance entre plusieurs actifs
      # Ploter la dispertion en cas de plot == True 
      # On va intégrer deux boutton , pour le calcul et pour la visualisation de la dispertion
      # a=Portefeuille(data_names)
      # a.Covariance_Matrice(['Attijari','BOA','Snep','Addoha'],'2020-01-01','2022-01-01',plot=True)


      if val=='Non':
        return self.Calcul_Rendement_Actifs(actif,'Quotidien',date_debut,date_fin,False).cov()
      else:
        from pandas.plotting import scatter_matrix
        return scatter_matrix(self.Calcul_Rendement_Actifs(actif,'Quotidien',date_debut,date_fin,False),hist_kwds={'bins':600},alpha=0.8,figsize=(17,9))
        # plt.show()
        # return plt
  