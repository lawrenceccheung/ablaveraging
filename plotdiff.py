#!/usr/bin/env python
#

from pylab import *
import plotABLstats

statsfile = 'abl_statistics.nc'
tlims     = [0, 100]
# Load the netcdf data
data      = plotABLstats.ABLStatsFileClass(stats_file=statsfile)

print("")

# Velocity differences
Vprof, header  = plotABLstats.plotvelocityprofile(data, None, tlims=tlims, exportdata=True)
Vprof2, header = plotABLstats.plotveltavgprofile(data, None, tlims=tlims, exportdata=True)
Vdat           = loadtxt('abl_velocity_stats.dat')
print("<Umag> diff L2: %e"%linalg.norm(Vprof2[:,4] - Vprof[:,4]))

# Temperature differences
Tprof, header  = plotABLstats.plottemperatureprofile(data, None, tlims=tlims, exportdata=True)
Tprof2, header = plotABLstats.plotttavgprofile(data, None, tlims=tlims, exportdata=True)
Tdat           = loadtxt('abl_temperature_stats.dat')
print("<T> diff L2:    %e"%linalg.norm(Tprof2[:,1] - Tprof[:,1]))

# TKE differences
TKEprof, header  = plotABLstats.plottkeprofile(data, None, tlims=tlims, exportdata=True)
TKEdat           = loadtxt('abl_resolved_stress_stats.dat')
print("<uu> diff L2:   %e"%linalg.norm(TKEprof[:,1] - TKEdat[:,1]))
print("<vv> diff L2:   %e"%linalg.norm(TKEprof[:,2] - TKEdat[:,4]))
print("<ww> diff L2:   %e"%linalg.norm(TKEprof[:,3] - TKEdat[:,6]))

# Temperature flux differences
Tfluxprof, header  = plotABLstats.plottfluxprofile(data, None, tlims=tlims, exportdata=True)
TuAvgprof, header  = plotABLstats.plottfluxtavgprofile(data, None, tlims=tlims, exportdata=True)
print("<Tu> diff L2:   %e"%linalg.norm(Tfluxprof[:,1] - TuAvgprof[:,1]))
print("<Tv> diff L2:   %e"%linalg.norm(Tfluxprof[:,2] - TuAvgprof[:,2]))
print("<Tw> diff L2:   %e"%linalg.norm(Tfluxprof[:,3] - TuAvgprof[:,3]))

print("")
# --- make some plots --- 
figure(figsize=(14,8), facecolor='white')
Nplots=4

subplot(1,Nplots,1)
plot(Vprof[:,4], Vprof[:,0],  '+-',  label='manual tavg')
plot(Vprof2[:,4]-0*Vprof[:,4], Vprof2[:,0], '.-', label='netcdf tavg')
plot(sqrt(Vdat[:,1]**2 + Vdat[:,2]**2 + Vdat[:,3]**2)-0*Vprof[:,4], Vdat[:,0], '-', label='Stats file', marker='o', fillstyle='none')
ylabel('z [m]')
xlabel('U [m/s]')
legend(loc='best')

subplot(1,Nplots,2)
plot(Tprof[:,1],  Tprof[:,0],  '+-', label='manual tavg')
plot(Tprof2[:,1]-0*Tprof[:,1], Tprof2[:,0], '.-', label='netcdf tavg')
plot(Tdat[:,1]-0*Tprof[:,1],   Tdat[:,0],   '-',  label='stats file', marker='o', fillstyle='none')
xlabel('T [K]')
legend(loc='best')

subplot(1,Nplots,3)
plot(TKEprof[:,1], TKEprof[:,0],  '.-',  label='manual tavg')  # uu
plot(TKEdat[:,1],  TKEdat[:,0],  '+-',   label='stats file')   
#plot(TKEprof[:,2], TKEprof[:,0],  '.-',  label='manual tavg')  # vv
#plot(TKEdat[:,4],  TKEdat[:,0],  '+-',   label='stats file')
#plot(TKEprof[:,3], TKEprof[:,0],  '.-',  label='manual tavg')  # ww
#plot(TKEdat[:,6],  TKEdat[:,0],  '+-',   label='stats file')
legend(loc='best')

subplot(1,Nplots,4)
plot(Tfluxprof[:,1], Tfluxprof[:,0],  '.-',  label='manual tavg')  # Tu
plot(TuAvgprof[:,1], Tfluxprof[:,0],  '.-',  label='netcdf tavg')  # Tu
legend(loc='best')

# Make the final plot
tight_layout()
show()
