#!/usr/bin/env python
#

from pylab import *
import plotABLstats

statsfile = 'abl_statistics.nc'
tlims     = [0, 100]
# Load the netcdf data
data = plotABLstats.ABLStatsFileClass(stats_file=statsfile)

figure(figsize=(12,8), facecolor='white')
Nplots=4

# Velocity differences
Vprof, header  = plotABLstats.plotvelocityprofile(data, None, tlims=tlims, exportdata=True)
Vprof2, header = plotABLstats.plotveltavgprofile(data, None, tlims=tlims, exportdata=True)
Vdat = loadtxt('abl_velocity_stats.dat')
subplot(1,Nplots,1)
#plot(Vprof[:,4], Vprof[:,0],  '+-',  label='manual tavg')
plot(Vprof2[:,4]-Vprof[:,4], Vprof2[:,0], '.-', label='netcdf tavg')
plot(sqrt(Vdat[:,1]**2 + Vdat[:,2]**2 + Vdat[:,3]**2)-Vprof[:,4], Vdat[:,0], '-', label='Stats file', marker='o', fillstyle='none')
legend(loc='best')
#show()

# Temperature differences
Tprof, header  = plotABLstats.plottemperatureprofile(data, None, tlims=tlims, exportdata=True)
Tprof2, header = plotABLstats.plotttavgprofile(data, None, tlims=tlims, exportdata=True)
Tdat = loadtxt('abl_temperature_stats.dat')
subplot(1,Nplots,2)
#plot(Tprof[:,1],  Tprof[:,0],  '+-', label='manual tavg')
plot(Tprof2[:,1]-Tprof[:,1], Tprof2[:,0], '.-', label='netcdf tavg')
plot(Tdat[:,1]-Tprof[:,1],   Tdat[:,0],   '-',  label='stats file', marker='o', fillstyle='none')
legend(loc='best')

# TKE differences
TKEprof, header  = plotABLstats.plottkeprofile(data, None, tlims=tlims, exportdata=True)
TKEdat = loadtxt('abl_resolved_stress_stats.dat')

subplot(1,Nplots,3)
plot(TKEprof[:,1], TKEprof[:,0],  '.-',  label='manual tavg')  # uu
plot(TKEdat[:,1],  TKEdat[:,0],  '+-',   label='stats file')   
plot(TKEprof[:,2], TKEprof[:,0],  '.-',  label='manual tavg')  # vv
plot(TKEdat[:,4],  TKEdat[:,0],  '+-',   label='stats file')
plot(TKEprof[:,3], TKEprof[:,0],  '.-',  label='manual tavg')  # ww
plot(TKEdat[:,6],  TKEdat[:,0],  '+-',   label='stats file')
legend(loc='best')

# Temperature flux differences
Tfluxprof, header  = plotABLstats.plottfluxprofile(data, None, tlims=tlims, exportdata=True)
TuAvgprof, header  = plotABLstats.plottfluxtavgprofile(data, None, tlims=tlims, exportdata=True)
subplot(1,Nplots,4)
plot(Tfluxprof[:,3], Tfluxprof[:,0],  '.-',  label='manual tavg')  # Tu
plot(TuAvgprof[:,3], Tfluxprof[:,0],  '.-',  label='netcdf tavg')  # Tu
legend(loc='best')

# Make the final plot
tight_layout()
show()
