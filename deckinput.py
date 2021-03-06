#!/usr/bin/python

#===================================
# Inputs for QuickPIC Deck Generator
#===================================

from numpy import *

#-------------------
# Verbosity Level of rpinput File
#-------------------
verbose    = 1        # 1:on, 0:off

#-------------------
# Verbosity Level of QPIC Debugger
# (not guaranteed to work)
#-------------------
qpic_debug = 0        # 1:on, 0:off

#-------------------
# Restart Runs
#-------------------
# is this a restart run?
is_restart = False    # boolean
# restart file number
# if this is a restart run
RST_START  = 1200     # dt
# reset file dump period
# (in units of sim. timestep)
DRST_STEP  = 100      # dt

#-------------------
# Number of Processors
#-------------------
# total number of processors
# you plan to use
# (must be power of 2)
#   8: good for fast jobs
#  64: good for medium jobs
# 128: good for long jobs
TOT_PROC     = 128    # processors

#-------------------
# Box Dimensions
#-------------------
# simulation box length
# default: 2.5 x L_bubble or
#          6.0 x sig_z
# set to '0' for automatic setting
box_length   = 0      # um
# simulation box height/width
# default: 4.0 x R_bubble or
#          5.0 x sig_x/y
# set to '0' for automatic setting
box_width    = 0      # um

#-------------------
# Multi-Step Simulation?
#-------------------
is_multistep = True   # boolean

#-------------------
# Simulation Length
#-------------------
L_sim        = 35.0   # cm



# #-------------------
# # Initialize Plasma Parameters
# # (Do not touch.)
# #-------------------
# nplas=0
# plas_dens=[]
# plas_np_cell=[]
# plas_rad_geom=[]
# plas_rad_geom_param=[]
# plas_long_geom=[]
# plas_long_geom_param=[]
# 
# nneut=0
# neut_z=[]
# neut_ion_lv=[]
# neut_dens=[]
# neut_np_cell=[]
# neut_rad_geom=[]
# neut_rad_geom_param=[]
# neut_long_geom=[]
# neut_long_geom_param=[]
# 
# #-------------------
# # Plasma Parameters - Argon Filament
# #-------------------
# # increment number of plasmas
# nplas+=1
# # nominal or maximum density
# dens_plas.append    (2.2E17  )   # cm^-3
# # min macro-particle density
# np_cell.append      (4       )   # per cell
# # radial geometry profile
# plas_rad_geom.append('circle')
# # radial geometry parameters
# plas_rad_geom_param1.append(10.0) # um
# plas_rad_geom_param2.append(1.0)
# plas_rad_geom_param3.append(1)



#-------------------
# Plasma Parameters
#-------------------
# (flat-top) plasma density
np         = 3.0E16   # cm^-3
# min plasma macro-particle density
np_cell    = 4        # per cell
# pre-formed/pre-ionized?
preformed  = True     # boolean
# plasma spiecies atomic number
# Note: only used if plasma is
# not pre-formed
# --------
# H : 1
# Li: 3
# He: 2
# Ar: 18
# Cs: 55
# --------
plasma_z   = 1
# maximum ionization level
max_ion_lv = 1

# --------
# transverse plasma geometry
# --------
#  'flat'  : constant density
#  'gauss' : gaussian ramps
#  'circle': circular filament
# --------
plasma_trans_geom = 'flat'

# --------
# longitudinal plasma geometry
# --------
#  'flat'  : constant density
#  'gauss' : gaussian ramps
# --------
plasma_long_geom = 'gauss'

# --------
# longitudinal plasma params 
# for gaussian ramps
# --------
# upramp length (sigma)
upramp_sig  = 15.0E4  # um
# flat-top start
flat_start  = 30.0E4  # um
# flat-top end
flat_end    = 60.0E4  # um
# downramp length (sigma)
dnramp_sig  = 15.0E4  # um

#-------------------
# Initialize Beam Parameters
#-------------------
nbeam=0
sig_x_matched=[]
sig_y_matched=[]
en_x_matched=[]
en_y_matched=[]
gam=[]
Q=[]
waist=[]
sig_z=[]
sig_x=[]
sig_y=[]
beta_x=[]
beta_y=[]
en_x=[]
en_y=[]
dp=[]
v_x=[]
v_y=[]
v_z=[]
off_x=[]
off_y=[]
off_z=[]
sig_x0=[]
sig_y0=[]
beta_x0=[]
beta_y0=[]
alpha_x0=[]
alpha_y0=[]

#-------------------
# Beam Parameters - Drive Bunch
# (tri-gaussian)
#-------------------
# increment number of beams
nbeam+=1
# auto-match spot size to plasma?
sig_x_matched.append (False) # boolean
sig_y_matched.append (False) # boolean
# auto-match emittance to plasma?
en_x_matched.append  (False) # boolean
en_y_matched.append  (False) # boolean
# relativistic gamma factor
gam.append  ( 39823.87   ) # (unitless)
# bunch charge
Q.append    ( int(2.0E10)) # e
# bunch length
sig_z.append( 30.        ) # um
# bunch spot size at waist in vacuum
sig_x.append( 30.        ) # um
sig_y.append( 30.        ) # um
# bunch noralized emittance
en_x.append ( 100.       ) # mm-mrad
en_y.append ( 10.        ) # mm-mrad
# bunch waist location from start
waist.append( 15.        ) # cm
# bunch energy spread
# NOTE: Doesn't work! Set to '0'
dp.append   ( 0.00       ) # (unitless)
# bunch drift velocity
# (keep set to '0' for now)
v_x.append  ( 0.         ) # c
v_y.append  ( 0.         ) # c
v_z.append  ( 0.         ) # c
# bunch transverse & longitudinal offset
off_x.append( 0.         ) # um
off_y.append( 0.         ) # um
off_z.append( 0.         ) # um

#-------------------
# Beam Parameters - Witness Bunch
# (tri-gaussian)
#-------------------
# increment number of beams
nbeam+=1
# auto-match spot size to plasma?
sig_x_matched.append (False) # boolean
sig_y_matched.append (False) # boolean
# auto-match emittance to plasma?
en_x_matched.append  (False) # boolean
en_y_matched.append  (False) # boolean
# relativistic gamma factor
gam.append  ( 1000       ) # (unitless)
# bunch charge
Q.append    ( int(1.0E9) ) # e
# bunch length
sig_z.append( 10.        ) # um
# bunch spot size at waist in vacuum
sig_x.append( 10.        ) # um
sig_y.append( 10.        ) # um
# bunch noralized emittance
en_x.append ( 1.         ) # mm-mrad
en_y.append ( 1.         ) # mm-mrad
# bunch waist location from start
waist.append( 15.        ) # cm
# bunch energy spread
# NOTE: Doesn't work! Set to '0'
dp.append   ( 0.00       ) # (unitless)
# bunch drift velocity
# (keep set to '0' for now)
v_x.append  ( 0.         ) # c
v_y.append  ( 0.         ) # c
v_z.append  ( 0.         ) # c
# bunch transverse & longitudinal offset
off_x.append( 0.         ) # um
off_y.append( 0.         ) # um
off_z.append( 125.       ) # um

#-------------------
# Simulation Output Parameters
#-------------------
# 3-D sampling?
# Warning: Can drastically
# increase simulation time.
#-------------------
# E-field
samp_E_3D    = False # boolean
# B-field
samp_B_3D    = False # boolean
# Beam
samp_beam_3D = False # boolean
# Plasma
samp_plas_3D = False # boolean
#-------------------
# Sampling Plane(s)
# x0: x=0, y-z plane
# y0: y=0, x-z plane
# z0: z=0, x-y plane
#-------------------
# E-field
samp_E_x0     = True # boolean
samp_E_y0     = True  # boolean
samp_E_z0     = False # boolean
# B-field
samp_B_x0     = True # boolean
samp_B_y0     = True  # boolean
samp_B_z0     = False # boolean
# Beam
samp_beam_x0  = True # boolean
samp_beam_y0  = True  # boolean
samp_beam_z0  = False # boolean
# Plasma
samp_plas_x0  = True # boolean
samp_plas_y0  = True  # boolean
samp_plas_z0  = False # boolean
# Beam Phase Space
samp_beam_pha = True  # boolean
# Plasma Phase Space
samp_plas_pha = False # boolean
#-------------------
# Sampling Periods in Time
# (in units of sim. timestep)
#-------------------
# E-field
samp_E_dt        = 20   # dt (int)
# B-field
samp_B_dt        = 20   # dt (int)
# Beam
samp_beam_dt     = 20   # dt (int)
# Plasma
samp_plas_dt     = 20   # dt (int)
# Beam Phase Space
samp_beam_pha_dt = 20   # dt (int)
# Plasma Phase Space
samp_plas_pha_dt = 20   # dt (int)
#-------------------
# Phase Space Sampling Sizes & Resolution
#-------------------
# Beam Phase Space
samp_beam_pha_N = int(pow(2,17))   # particles
# Plasma Phase Space
samp_plas_pha_N = int(pow(2,17))   # particles
# Beam Centroid Resolution
beam_cent_res_dz = int(pow(2,6))   # z-slices


