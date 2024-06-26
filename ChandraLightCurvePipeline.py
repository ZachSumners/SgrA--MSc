import subprocess
import os

#Runs the first part of MEGA's "Guide to analyzing flares" (the part before DS9 stuff). Prompts will show up in the terminal but you should just be able to hit enter each time to continue.

#Should just have to change Chandra observation ID and working directory. It should be the directory with the primary and secondary folders in it.

#Change here
observationID = 28232
wd = f'/home/zach/Desktop/McGill-MSc/Chandra/data/{observationID}'

subprocess.call('punlearn ardlib', shell=True, cwd=wd)
subprocess.call('chandra_repro', shell=True, cwd=wd)

#Change here
repro_wd = f'/home/zach/Desktop/McGill-MSc/Chandra/data/{observationID}/repro'

subprocess.call('punlearn dmcopy', shell=True, cwd=repro_wd)
subprocess.call(f'dmcopy infile="acisf{observationID}_repro_evt2.fits[EVENTS][bin x=3992.71:4174.71:1,y=3991.24:4173.24:1][energy=2000:8000]" outfile="{observationID}_repro_2-8keV_cropped.fits" clobber=yes', shell=True, cwd=repro_wd)
subprocess.call('punlearn mkpsfmap', shell=True, cwd=repro_wd)
subprocess.call(f'mkpsfmap infile="{observationID}_repro_2-8keV_cropped.fits" outfile="{observationID}_repro_2-8keV_psfmap.fits" energy=3.8 ecf=0.393 clobber=yes', shell=True, cwd=repro_wd)

subprocess.call('punlearn wavdetect', shell=True, cwd=repro_wd)
subprocess.call(f'pset wavdetect infile="{observationID}_repro_2-8keV_cropped.fits"', shell=True, cwd=repro_wd)
subprocess.call(f'pset wavdetect psffile="{observationID}_repro_2-8keV_psfmap.fits"', shell=True, cwd=repro_wd)
subprocess.call('pset wavdetect outfile="src.fits"', shell=True, cwd=repro_wd)
subprocess.call(f'pset wavdetect scellfile="{observationID}_repro_2-8keV_scell.fits"', shell=True, cwd=repro_wd)
subprocess.call(f'pset wavdetect imagefile="{observationID}_repro_2-8keV_img.fits"', shell=True, cwd=repro_wd)
subprocess.call(f'pset wavdetect defnbkgfile="{observationID}_repro_2-8keV_nbkg.fits"', shell=True, cwd=repro_wd)
subprocess.call('pset wavdetect regfile="src.reg"', shell=True, cwd=repro_wd)
subprocess.call('pset wavdetect scales="1.0 2.0 4.0 8.0 16.0"', shell=True, cwd=repro_wd)
subprocess.call('pset wavdetect sigthresh=1.e-06', shell=True, cwd=repro_wd)
subprocess.call('pset wavdetect clobber=yes', shell=True, cwd=repro_wd)
subprocess.call('wavdetect', shell=True, cwd=repro_wd)







