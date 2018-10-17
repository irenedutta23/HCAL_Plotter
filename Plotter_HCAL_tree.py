import os,sys,re,fileinput,string,shutil
import numpy as np
import ROOT as rt
from array import array
from ROOT import TCanvas, TFile, TPaveText
from ROOT import TLorentzVector
import math

rt.gROOT.SetBatch()
rt.gStyle.SetPalette(55)
#rt.gStyle.SetOptStat(0)
rt.gStyle.SetOptFit()

#name='tree_Mmumu_ieta27_MC_NoPU'
#name='tree_Mmumu_ieta27_MC_wPU'
name= 'tree_ieta27_data2018_ABCD'
out_file =  rt.TFile.Open(name+"_plots_v3.root","recreate")

t = rt.TTree( 'tree', 'tree' )
run = array( 'i', [ 0 ] )
evt = array( 'i',[ 0 ] )
e4_o = array( 'f', [ 0.] )
e5_o = array( 'f', [ 0.] )
e6_o = array( 'f', [ 0.] )
e7_o = array( 'f', [ 0.] )
Z_mass = array( 'f', [ 0.] )

t.Branch('run', run,'run/I')
t.Branch('event',evt ,'event/I')
t.Branch('e4_o',e4_o,'e4_o/F')
t.Branch('e5_o',e5_o,'e5_o/F')
t.Branch('e6_o',e6_o,'e6_o/F')
t.Branch('e7_o',e7_o,'e7_o/F')
t.Branch('Z_mass',Z_mass,'Z_mass/F')





in_file = rt.TFile.Open(name+".root")
in_tree = in_file.Get("tree")


for event in in_tree:
   
    phi_m2=event.phi-math.pi;
    while (phi_m2 > math.pi):
        phi_m2 -= 2 * math.pi
    while (phi_m2 <= -math.pi):
        phi_m2 += 2 * math.pi
        
    m1 = TLorentzVector()
    m1.SetPtEtaPhiM(event.pt,event.eta,event.phi,0.1057)
    if(event.eta>0.):
        m2 = TLorentzVector()
        m2.SetPtEtaPhiM(45.31,2.575,phi_m2,0.1057)
    else:
        m2 = TLorentzVector()
        m2.SetPtEtaPhiM(45.31,-2.575,phi_m2,0.1057)
        
    Z=m1+m2
    
    if event.pt>25. and event.eEcal_o<0.5 and event.e7_o>0.0 and  event.e6_o>0.0 and event.e5_o>0.0 and event.e4_o>0.0 and event.e3_o>0.1 and event.e2_o>0.05 and event.e1_o>0. and  event.e4_o<0.8 and  event.e3_o<0.8:
        
        evt[0]=event.event
        run[0]=event.run
        e4_o[0]=event.e4_o
        e5_o[0]=event.e5_o
        e6_o[0]=event.e6_o
        e7_o[0]=event.e7_o
        Z_mass[0]=Z.M()
        t.Fill()
        
in_file.Close()
out_file.cd()

out_file.Write()
out_file.Close()
