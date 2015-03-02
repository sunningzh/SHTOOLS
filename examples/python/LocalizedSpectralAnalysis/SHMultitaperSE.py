#!/usr/bin/env python
"""
This script tests the conversions between real and complex spherical harmonics
coefficients
"""

#standard imports:
import os, sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#import shtools:
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
import pyshtools as shtools

#set shtools plot style:
sys.path.append(os.path.join(os.path.dirname(__file__), "../Common"))
from FigStyle import style_shtools
mpl.rcParams.update(style_shtools)

def main():
    test_MultitaperSE()

def test_MultitaperSE():
    print '\n---- testing SHReturnTapersM ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    lmax       = 10
    orderM     = 2
    print 'creating spherical cap tapers with:',
    print 'size {:1.0f}deg, bandwidth {:d}, order {:d}'.format(theta0_deg,lmax,orderM)
    tapers,concentrations,shannon = shtools.SHReturnTapersM(theta0,lmax,orderM)
    print 'first 3 taper concentrations:'
    print concentrations[:3]

    print '\n---- testing SHReturnTapers ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    lmax       = 10
    print 'creating spherical cap tapers of',
    print 'size {:1.0f}deg with bandwidth {:d}'.format(theta0_deg,lmax)
    tapers,concentrations,taperorder = shtools.SHReturnTapers(theta0,lmax)
    print 'first 3 taper concentrations:'
    print concentrations[:3]

    print '\n---- testing SHMultiTaperSE ----'
    lmax = 80
    ntapers = 3
    tapers = tapers[:,:ntapers]
    torders = taperorder[:ntapers]
    coeffs = np.random.normal(size = 2*(lmax+1)*(lmax+1)).reshape(2,lmax+1,lmax+1)
    localpower,localpower_sd = shtools.SHMultiTaperSE(coeffs,tapers,torders)
    print 'total power:',np.sum(localpower)

    print '\n---- testing SHMultiTaperCSE ----'
    lmax = 80
    ntapers = 3
    coeffs1 = np.random.normal(size = 2*(lmax+1)*(lmax+1)).reshape(2,lmax+1,lmax+1)
    coeffs2 = 0.5*(coeffs1+np.random.normal(size = 2*(lmax+1)*(lmax+1)).reshape(2,lmax+1,lmax+1))
    localpower,localpower_sd = shtools.SHMultiTaperCSE(coeffs1,coeffs2,tapers,torders)
    print 'total power:',np.sum(localpower)

    print '\n---- testing SHLocalizedAdmitCorr ----'
    admit,corr,dadmit,dcorr = shtools.SHLocalizedAdmitCorr(tapers,torders,coeffs1,coeffs2)
    print admit

    print '\n---- testing ComputeD0 ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    lmax       = 10
    D0 = shtools.ComputeD0(lmax,theta0)
    print D0[0,:3]

    print '\n---- testing ComputeDm ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    lmax       = 10
    m          = 2
    Dm = shtools.ComputeDm(lmax,m,theta0)
    print Dm[:3,:3]

    print '\n---- testing ComputeDG82 ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    lmax       = 10
    m          = 2
    DG82 = shtools.ComputeDG82(lmax,m,theta0)
    print DG82[:3,:3]

    print '\n---- testing SHFindLWin ----'
    theta0_deg = 20.
    theta0     = np.radians(theta0_deg)
    m          = 2
    ntapers    = 3
    minconcentration = 0.8
    lmax = shtools.SHFindLWin(theta0,m,minconcentration,taper_number=ntapers)
    print lmax

    print '\n---- testing SHBiasK ----'
    lmax = 80
    power_unbiased = 1./(1.+np.arange(lmax+1))**2
    power_biased = shtools.SHBiasK(tapers,power_unbiased)
    print (power_biased[:lmax+1]/power_unbiased)[:5]

    print '\n---- testing SHBias ----'
    lmax = 80
    power_unbiased = 1./(1.+np.arange(lmax+1))**2
    power_biased = shtools.SHBias(tapers[:,2],power_unbiased)
    print tapers.shape
    print (power_biased[:lmax+1]/power_unbiased)[:5]

    print '\n---- testing SHBiasAdmitCorr ----'
    lmax = 80
    Stt = 1./(1.+np.arange(lmax+1))**2
    Sgg = 1./(1.+np.arange(lmax+1))**2
    Sgt = 0.5/(1.+np.arange(lmax+1))**2
    admit,corr = shtools.SHBiasAdmitCorr(Sgt,Sgg,Stt,tapers[:,2])
    print corr

    print '\n---- testing SHMTDebias ----'
    print 'THIS FUNCTION THROWS AN ERROR'
    print '(uncomment in file to see it)'
    #lmax = 80
    #lwin,ntapers = tapers.shape
    #mtspectra = np.zeros( (2,lmax+lwin-1) )
    #mtspectra[0] = power_biased
    #mtspectra[1] = 1e-1*power_biased
    #print mtspectra.shape
    #mtdebias,lmid = shtools.SHMTDebias(mtspectra,tapers[:,:2],nl=2*lwin)
    #print mtdebias

#==== EXECUTE SCRIPT ====
if __name__ == "__main__":
    main()
