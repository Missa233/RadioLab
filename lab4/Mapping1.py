
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import astropy
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import FK5
import time
import numpy as np
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from datetime import datetime

def getGalacticPointing(StartL,EndL,StartB,EndB):
    l_range = EndL-StartL
    b_range = EndB-StartB
    l_inc = 4
    b_inc = 2

    N= int(b_range/b_inc)
    M= int(l_range/l_inc)
    

    POINTS_l = np.empty((N+1,M+1))
    POINTS_b = np.empty((N+1,M+1))

    for i in range (0,N+1):
        for j in range (0,M+1):
            coord_l = Start+j*4
            coord_b = -20+i*2
            POINTS_l[N-i,j] = coord_l
            POINTS_b[N-i,j] = coord_b
    return POINTS_l, POINTS_b


def PointingPlan(PointsL,PointsB):
    '''
    Parameters: 
    PointsL =  Galactic Longitudes for each point
    PointsB = Galactic Latitudes for each point
    Returns: 
    
    Ra = Right ascension for each point
    Dec = Declination for each point'''
    l = PointsL

    b = PointsB
    

    gal = SkyCoord(l=l*u.degree, b=b*u.degree, frame='galactic')
    eq  = gal.fk5
    eq.transform_to(FK5(equinox='J2019'))
    Ra = eq.ra.degree
    Dec = eq.dec.degree
    #print(Ra)
    #print(Dec)
    
    return Ra, Dec

def ConstPointing(PointsL,PointsB):
    L = PointsL

    B = PointsB
    
    N = L.shape[0]
    M = L.shape[1]
    
    

    Ra,Dec = PointingPlan(L,B)
    print(Ra.shape[0])
    print(L.shape[1])

    
    AurigaRa = []
    PerseusRa = []
    AurigaDec = []
    PerseusDec = []
    CassiopeiaRa = []
    CepheusRa = []
    LacertaRa = []
    CygnusRa = []
    AquilaRa = []
    ScutumRa = []
    SagittariusRa = []
    ScorpiusRa = []
    LupusRa = []
    CenterausRa = []
    CruxRa = []
    VelaRa = []
    PuppisRa = []
    CanisMajorRa = []
    MonocerosRa = []
    GeminiRa = []
    
    AurigaDec = []
    PerseusDec = []
    CassiopeiaDec = []
    CepheusDec = []
    LacertaDec = []
    CygnusDec = []
    AquilaDec = []
    ScutumDec = []
    SagittariusDec = []
    ScorpiusDec = []
    LupusDec = []
    CenterausDec = []
    CruxDec = []
    VelaDec = []
    PuppisDec = []
    CanisMajorDec = []
    MonocerosDec = []
    GeminiDec = []
    
    for i in range (0,N):
        for j in range (0,M):
        
            if (L[i,j]<180) and (L[i,j]>160):
                AurigaRa.append(Ra[i,j])
                AurigaDec.append(Dec[i,j])
            
            
            if (L[i,j]<160) and (L[i,j]>140):
                PerseusRa.append(Ra[i,j])
                PerseusDec.append(Dec[i,j])
                
            if (L[i,j]<140) and (L[i,j]>120):
                CassiopeiaRa.append(Ra[i,j])
                CassiopeiaDec.append(Dec[i,j])
                
            if (L[i,j]<120) and (L[i,j]>100):
                CepheusRa.append(Ra[i,j])
                CepheusDec.append(Dec[i,j])
                
            if (L[i,j]<100) and (L[i,j]>80):
                LacertaRa.append(Ra[i,j])
                LacertaDec.append(Dec[i,j])
                
            if (L[i,j]<80) and (L[i,j]>60):
                CygnusRa.append(Ra[i,j])
                CygnusDec.append(Dec[i,j])
                
            if (L[i,j]<60) and (L[i,j]>40):
                AquilaRa.append(Ra[i,j])
                AquilaDec.append(Dec[i,j])
                
            if (L[i,j]<40) and (L[i,j]>20):
                ScutumRa.append(Ra[i,j])
                ScutumDec.append(Dec[i,j])
            
            if (L[i,j]<20) and (L[i,j]>0):
                SagittariusRa.append(Ra[i,j])
                SagittariusDec.append(Dec[i,j])
            
            if (L[i,j]<360) and (L[i,j]>340):
                ScorpiusRa.append(Ra[i,j])
                ScorpiusDec.append(Dec[i,j])
                
            if (L[i,j]<340) and (L[i,j]>320):
                LupusRa.append(Ra[i,j])
                LupusDec.append(Dec[i,j])
            
            if (L[i,j]<320) and (L[i,j]>300):
                CenterausRa.append(Ra[i,j])
                CenterausDec.append(Dec[i,j])
            
            if (L[i,j]<300) and (L[i,j]>280):
                CruxRa.append(Ra[i,j])
                CruxDec.append(Dec[i,j])
            
            if (L[i,j]<280) and (L[i,j]>260):
                VelaRa.append(Ra[i,j])
                VelaDec.append(Dec[i,j])
            
            if (L[i,j]<260) and (L[i,j]>240):
                PuppisRa.append(Ra[i,j])
                PuppisDec.append(Dec[i,j])
            
            if (L[i,j]<240) and (L[i,j]>220):
                CanisMajorRa.append(Ra[i,j])
                CanisMajorDec.append(Dec[i,j])
            
            if (L[i,j]<220) and (L[i,j]>200):
                MonocerosRa.append(Ra[i,j])
                MonocerosDec.append(Dec[i,j])
            
            if (L[i,j]<200) and (L[i,j]>180):
                GeminiRa.append(Ra[i,j])
                GeminiDec.append(Dec[i,j])
            
    
    Ara = np.array(AurigaRa)
    Adec = np.array(AurigaDec)
    if (len(AurigaRa) !=0):
        Ara.shape = (N,-1)
        Adec.shape = (N,-1)
        print('Auriga')
                
                
    Pra = np.array(PerseusRa)
    Pdec = np.array(PerseusDec)
    if (len(PerseusRa) !=0):
        Pra.shape = (N,-1)
        Pdec.shape = (N,-1)
        print('Perseus')
        
    Casra = np.array(CassiopeiaRa)
    Casdec = np.array(CassiopeiaDec)
    if (len(CassiopeiaRa) !=0):
        Casra.shape = (N,-1)
        Casdec.shape = (N,-1)
        print('Cassiopeia')
        
    Cephra = np.array(CepheusRa)
    Cephdec = np.array(CepheusDec)
    if (len(CepheusRa) !=0):
        Cephra.shape = (N,-1)
        Cephdec.shape = (N,-1)
        print('Cepheus')
        
    Lacra = np.array(LacertaRa)
    Lacdec = np.array(LacertaDec)
    if (len(LacertaRa) !=0):
        Lacra.shape = (N,-1)
        Lacdec.shape = (N,-1)
        print('Lacerta')
        
    Cygra = np.array(CygnusRa)
    Cygdec = np.array(CygnusDec)
    if (len(CygnusRa) !=0):
        Cygra.shape = (N,-1)
        Cygdec.shape = (N,-1)
        print('Cygnus')
        
    Aqra = np.array(AquilaRa)
    Aqdec = np.array(AquilaDec)
    if (len(AquilaRa) !=0):
        Aqra.shape = (N,-1)
        Aqdec.shape = (N,-1)
        print('Aquila')
        
    
    Scra = np.array(ScutumRa)
    Scdec = np.array(ScutumDec)
    if (len(ScutumRa) !=0):
        Scra.shape = (N,-1)
        Scdec.shape = (N,-1)
        print('Scutum')
        
    if (len(SagittariusRa) !=0):
        Sagra = np.array(SagittariusRa)
        Sagdec = np.array(SagittariusDec)
        Sagra.shape = (N,-1)
        Sagdec.shape = (N,-1)
        print('Sagittarius')
        
    Scora = np.array(ScorpiusRa)
    Scodec = np.array(ScorpiusDec)
    if (len(ScorpiusRa) !=0):
        Scora.shape = (N,-1)
        Scodec.shape = (N,-1)
        print('Scorpius')
        
    Lupra = np.array(LupusRa)
    Lupdec = np.array(LupusDec)
    if (len(LupusRa) !=0):
        Lupra.shape = (N,-1)
        Lupdec.shape = (N,-1)
        print('Lupus')
        
    Cenra = np.array(CenterausRa)
    Cendec = np.array(CenterausDec)
    if (len(CenterausRa) !=0):
        Cenra.shape = (N,-1)
        Cendec.shape = (N,-1)
        print('Centeraus')
        
    Cxra = np.array(CruxRa)
    Cxdec = np.array(CruxDec)
    if (len(CruxRa) !=0):
        Cxra.shape = (N,-1)
        Cxdec.shape = (N,-1)
        print('Crux')
    
    Vra = np.array(VelaRa)
    Vdec = np.array(VelaDec)    
    if (len(VelaRa) !=0):
        Vra.shape = (N,-1)
        Vdec.shape = (N,-1)
        print('Vela')
        
    Pura = np.array(PuppisRa)
    Pudec = np.array(PuppisDec)
    if (len(PuppisRa) !=0):
        Pura.shape = (N,-1)
        Pudec.shape = (N,-1)
        print('Puppis')
        
    CMra = np.array(CanisMajorRa)
    CMdec = np.array(CanisMajorDec)
    if (len(CanisMajorRa) !=0):
        CMra.shape = (N,-1)
        CMdec.shape = (N,-1)
        print('CanisMajor')
        
    Mra = np.array(MonocerosRa)
    Mdec = np.array(MonocerosDec)
    if (len(MonocerosRa) !=0):
        Mra.shape = (N,-1)
        Mdec.shape = (N,-1)
        print('Monoceros')
    
    Gra = np.array(GeminiRa)
    Gdec = np.array(GeminiDec)
    if (len(GeminiRa) !=0): 
        Gra.shape = (N,-1)
        Gdec.shape = (N,-1)
        print('Gemini')
    
    return [Ara,Adec,Pra,Pdec,Casra,Casdec,Cephra,Cephdec,Lacra,Lacdec,Cygra,Cygdec,Aqra,Aqdec,Scra,Scdec,Sagra,Sagdec,Scora,Scodec,Lupra,Lupdec,Cenra,Cendec,Cxra,Cxdec,Vra,Vdec,Pura,Pudec,CMra,CMdec,Mra,Mdec,Gra,Gdec]

def mapper(l,b,LO,MapName):
    Completed = []
    Skipped = []
    M = l.shape[0]
    N = l.shape[1]
    LeuschTelescope = ugradio.leusch.LeuschTelescope()
    spec = leuschner.Spectrometer('10.0.1.2')
    agilent = ugradio.agilent.SynthDirect()
    #LO = ugradio.agilent.SynthClient(host='127.0.0.1')
    #get coordinates
    agilent.set_frequency(LO, 'MHz')
    spec.check_connected()
    #spec.read_spec('Calibrateupper.fits',20,(120,0),'ga')
    for i in range (0,M):
        for j in range (0,N):
            L = l[i,j]
            B = b[i,j]
            Leuschner = EarthLocation(lat=37.34*u.deg, lon=-121.64*u.deg, height=390*u.m)
            ut = Time(datetime.utcnow(), scale='utc')
            gal = SkyCoord(l=L*u.degree, b=B*u.degree, frame='galactic')
            eq  = gal.fk5
            altaz = gal.transform_to(AltAz(obstime=ut,location=Leuschner))
            alt = altaz.alt.degree
            az = altaz.az.degree
            try:
                LeuschTelescope.point(alt,az)
                spec.read_spec(MapName+'_'+str(i)+'_'str(j)'.fits',20,(L,B),'ga')
                Completed.append((L,B))
            except:
                print(L,B)
                Skipped.append((L,B))
                continue
            
    return Completed, Skipped
            
