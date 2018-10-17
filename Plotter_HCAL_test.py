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
#out_file =  rt.TFile.Open(name+"_plots.root","recreate")
h_depth1_o =rt.TH1F("h_depth1_o","",50,0.,2.)
h_depth2_o =rt.TH1F("h_depth2_o","",50,0.,2.)
h_depth3_o =rt.TH1F("h_depth3_o","",50,0.,2.)
h_depth4_o =rt.TH1F("h_depth4_o","",50,0.,2.)
h_depth5_o =rt.TH1F("h_depth5_o","",50,0.,2.)
h_depth6_o =rt.TH1F("h_depth6_o","",13,0.,2.)
h_depth7_o =rt.TH1F("h_depth7_o","",25,0.,2.)

h_depth7_o.GetXaxis().SetTitle("depth 7 (GeV)")
h_depth6_o.GetXaxis().SetTitle("depth 6 (GeV)")
h_depth5_o.GetXaxis().SetTitle("depth 5 (GeV)")
h_depth4_o.GetXaxis().SetTitle("depth 4 (GeV)")
h_depth3_o.GetXaxis().SetTitle("depth 3 (GeV)")
h_depth2_o.GetXaxis().SetTitle("depth 2 (GeV)")
h_depth1_o.GetXaxis().SetTitle("depth 1 (GeV)")

h_depth7_o.GetYaxis().SetTitle("Events")
h_depth6_o.GetYaxis().SetTitle("Events")
h_depth5_o.GetYaxis().SetTitle("Events")
h_depth4_o.GetYaxis().SetTitle("Events")
h_depth3_o.GetYaxis().SetTitle("Events")
h_depth2_o.GetYaxis().SetTitle("Events")
h_depth1_o.GetYaxis().SetTitle("Events")


in_file = rt.TFile.Open(name+".root")
in_tree = in_file.Get("tree")	
i=-1
for event in in_tree:
    i=i+1
    if i%100000==0: print "100000"
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
    if event.pt>25. and event.eEcal_o<0.5 and event.e7_o>0. and  event.e6_o>0. and event.e5_o>0.and event.e4_o>0. and event.e3_o>0. and event.e2_o>0. and event.e1_o>0. and Z.M()>80.:
        '''
        if event.e7_o<2.:
            h_depth7_o.Fill(event.e7_o)
        if event.e6_o<2.:
            h_depth6_o.Fill(event.e6_o)
        if event.e5_o<2.:
            h_depth5_o.Fill(event.e5_o)
        if event.e4_o<2.:
            h_depth4_o.Fill(event.e4_o)
        if event.e3_o<2.:
            h_depth3_o.Fill(event.e3_o)
        if event.e2_o<2.:
            h_depth2_o.Fill(event.e2_o)
        if event.e1_o<2.:
            h_depth1_o.Fill(event.e1_o)
'''
        if event.e7_o<2. and event.e7_o>0.3:
            h_depth7_o.Fill(event.e7_o)
        if event.e6_o<2.  and event.e6_o>0.2:
            h_depth6_o.Fill(event.e6_o)
        if event.e5_o<2. and event.e5_o>0.1:
            h_depth5_o.Fill(event.e5_o)
        if event.e4_o<2. and event.e4_o>0.05:
            h_depth4_o.Fill(event.e4_o)
        if event.e3_o<2. and event.e3_o>0.05:
            h_depth3_o.Fill(event.e3_o)
        if event.e2_o<2.  and event.e2_o>0.05:
            h_depth2_o.Fill(event.e2_o)
        if event.e1_o<2.  and event.e1_o>0.05:
            h_depth1_o.Fill(event.e1_o)

in_file.Close()
out_file.cd()

h_depth7_o.Fit("landau","R","",0.3,1.78)
h_depth6_o.Fit("landau","R","",0.3,1.5)
h_depth5_o.Fit("landau","R","",0.1,1.38)
h_depth4_o.Fit("landau","R","",0.05,1.2)
h_depth3_o.Fit("landau","R","",0.05,0.5)
h_depth2_o.Fit("landau","R","",0.05,1.32)
h_depth1_o.Fit("landau","R","",0.05,1.16)
"""
#--------------------------------
#No PU sample
#--------------------------------

h_depth1_o.Fit("landau","R","",0.06,1.16)
h_depth2_o.Fit("landau","R","",0.08,1.2)
h_depth3_o.Fit("landau","R","",0.1,1.2)
h_depth4_o.Fit("landau","R","",0.1,1.2)
h_depth5_o.Fit("landau","R","",0.26,1.38)
h_depth6_o.Fit("landau","R","",0.36,1.5)
h_depth7_o.Fit("landau","R","",0.26,1.78)
"""

c1 = TCanvas( 'c1', '', 200, 10, 700, 500 )
c1.GetFrame().SetBorderMode(-1 )
c1.GetFrame().SetBorderSize( 5 )
h_depth1_o.SetFillColor(17)
h_depth1_o.Draw()

c2 = TCanvas( 'c2', '', 200, 10, 700, 500 )
h_depth2_o.SetFillColor(17)

h_depth2_o.Draw()

c3 = TCanvas( 'c3', '', 200, 10, 700, 500 )
h_depth3_o.SetFillColor(17)

h_depth3_o.Draw()

c4 = TCanvas( 'c4', '', 200, 10, 700, 500 )
h_depth4_o.SetFillColor(17)

h_depth4_o.Draw()

c5 = TCanvas( 'c5', '', 200, 10, 700, 500 )
h_depth5_o.SetFillColor(17)

h_depth5_o.Draw()

c6 = TCanvas( 'c6', '', 200, 10, 700, 500 )
h_depth6_o.SetFillColor(17)

h_depth6_o.Draw()

c7 = TCanvas( 'c7', '', 200, 10, 700, 500 )
h_depth7_o.SetFillColor(17)

h_depth7_o.Draw()


#c1.SaveAs(name+"_depth1_o.png")
#c2.SaveAs(name+"_depth2_o.png")
#c3.SaveAs(name+"_depth3_o.png")
#c4.SaveAs(name+"_depth4_o.png")
#c5.SaveAs(name+"_depth5_o.png")
#c6.SaveAs(name+"_depth6_o.png")
#c7.SaveAs(name+"_depth7_o.png")


#h_depth7_o.Write()
#h_depth6_o.Write()
#h_depth5_o.Write()
#h_depth4_o.Write()
#h_depth3_o.Write()
#h_depth2_o.Write()
#h_depth1_o.Write()
#out_file.Close()
