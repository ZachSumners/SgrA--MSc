import os
import subprocess
from pycrates import read_file
import matplotlib.pylab as plt
import numpy as np
from astropy.time import Time

#Runs the second part of MEGA's "Guide to analyzing flares" (the part after the DS9 stuff but before the Bayesian blocks). Prompts will show up in the terminal but you should just be able to hit enter each time to continue.

#Should just have to change Chandra observation ID, chip ID and working directory.

#Change here
observationID = 28232
chipID = 7
repro_wd = f'/home/zach/Desktop/McGill-MSc/Chandra/data/Barycentric/{observationID}'

#All just terminal commands from the guide to analyzing flares document. 
subprocess.call('punlearn dmextract', shell=True, cwd=repro_wd)
subprocess.call(f'pset dmextract infile="acisf{observationID}_bary_evt2.fits[ccd_id={chipID}, energy=2000:8000,sky=region(sgra.reg)][bin time=::300]"', shell=True, cwd=repro_wd)
subprocess.call(f'pset dmextract outfile="{observationID}_sgra_2-8keV_lc300.fits"', shell=True, cwd=repro_wd)
subprocess.call(f'pset dmextract bkg="acisf{observationID}_bary_evt2.fits[ccd_id={chipID},sky=region(bkg.reg)]"', shell=True, cwd=repro_wd)
subprocess.call('pset dmextract opt="ltc1"', shell=True, cwd=repro_wd)
subprocess.call('dmextract', shell=True, cwd=repro_wd)

subprocess.call('punlearn dmcopy', shell=True, cwd=repro_wd)
subprocess.call(f'pset dmcopy infile="acisf{observationID}_bary_evt2.fits[EVENTS][sky=region(sgra.reg)][energy=2000:8000]"', shell=True, cwd=repro_wd)
subprocess.call(f'pset dmcopy outfile="{observationID}_sgra_2-8keV_evt.fits"', shell=True, cwd=repro_wd)
subprocess.call('pset dmcopy option="all"', shell=True, cwd=repro_wd)
subprocess.call('dmcopy', shell=True, cwd=repro_wd)

#Plots the light curve - Commented out right now because I was plotting elsewhere with Bayesian Blocks.
#tab = read_file(f"{repro_wd}/{observationID}_sgra_2-8keV_lc300.fits")


#dt = tab.get_column("dt").values
#rate = tab.get_column("net_rate").values
#erate = tab.get_column("err_rate").values
#plt.errorbar(dt, rate, yerr=erate, marker="o", color="red", mfc="black",mec="black", ecolor="grey")
#plt.xlabel("$\Delta$ T (sec)")
#plt.ylabel("Net Count Rate (counts/sec)")

#print(dt[0])

#t = Time(times, format='isot')
#textstr = '\n'.join(())
#ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#plt.title(f"{observationID}_sgra_2-8keV_lc300.fits")
#plt.show()
