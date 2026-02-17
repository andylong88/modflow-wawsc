Publication
[Citation will go here]

Data Release
[Citation will go here]

MODEL ARCHIVE
-------------

Archive created: 2022-08-04

--------------------------------------------------------------------------
DISCLAIMER-                                                                       
                                                                          
  THE FILES CONTAINED HEREIN ARE PROVIDED AS A CONVENIENCE TO THOSE
  WHO WISH TO REPLICATE SIMULATIONS OF GROUNDWATER FLOW THAT ARE
  DESCRIBED IN U.S. GEOLOGICAL SURVEY SCIENTIFIC INVESTIGATIONS
  REPORT 20XX-XXXX.                                                    
  ANY CHANGES MADE TO THESE FILES COULD HAVE UNINTENDED, UNDESIRABLE      
  CONSEQUENCES. THESE CONSEQUENCES COULD INCLUDE, BUT MAY NOT BE 
  NOT LIMITED TO: ERRONEOUS MODEL OUTPUT, NUMERICAL INSTABILITIES, 
  AND VIOLATIONS OF UNDERLYING ASSUMPTIONS ABOUT THE SUBJECT HYDROLOGIC       
  SYSTEM THAT ARE INHERENT IN RESULTS PRESENTED IN U.S. GEOLOGICAL SURVEY 
  SCIENTIFIC INVESTIGATIONS REPORT 20XX-XXXX. 
  THE U.S. GEOLOGICAL SURVEY ASSUMES NO RESPONSIBILITY FOR THE            
  CONSEQUENCES OF ANY CHANGES MADE TO THESE FILES. IF CHANGES ARE MADE
  TO THE MODEL, THE USER IS RESPONSIBLE FOR DOCUMENTING THE CHANGES AND
  JUSTIFYING THE RESULTS AND CONCLUSIONS.   

--------------------------------------------------------------------------

SIR20XX-XXXX/

The underlying directories contain all the input files, output files, and source 
code for the simulations described in the report.
         
The model simulations were run with MODFLOW-NWT. MODFLOW-NWT was compiled 
using the Intel Fortran Compiler for 64-bit operating systems and downloaded from 
https://www.usgs.gov/software/modflow-nwt-a-newton-formulation-modflow-2005. 
The model was run on Microsoft Windows 10 Enterprise Version 1909 (64-bit) 
operating system.

Reconstructing the model archive from the online data release:

        The model archive is available as a data release from:
        
            https://doi.org/10.xxxx/xxxxx
        
        The models will run successfully only if the correct directory 
        structure is correctly restored. The model archive is broken into 
        several pieces to reduce the likelihood of download timeouts. 
        Small files (readme.txt and modelgeoref.txt) are available as 
        uncompressed files. All other files are zipped at the subdirectory 
        level. For example, the files in the "georef" subdirectory are zipped
        into a zip file named "georef.zip". All zip files should be unzipped
        into a directory with the same name as the zip file name without the
        .zip extension. 
        
        The highest-level directory structure of the original model archive is:
        
            SIR2022-XXXX/
                ancillary/
                bin/
                georef/
                model/
                output/
                source/
                
        The full directory structure of the model archive and the files  
        within each subdirectory are listed below.                  
         


Running the models:
Each model in this archive can be run by opening a command window/terminal in 
the model’s subdirectory and typing:

..\..\bin\MODFLOW-NWT_64.exe <sim_name>.nam
         
where "<sim_name>" is replaced with the simulation name. Possible simulation 
names are: 
   
1. SES_ss
2. SES_tr
3. SES_Scenario1a
4. SES_Scenario1b
5. SES_Scenario1c
6. SES_Scenario1d
7. SES_Scenario2
8. SES_Scenario3a
9. SES_Scenario3b
10. SES_Scenario3c
11. SES_Scenario3d
12. SES_Scenario3e

For the user’s convenience, batch files have been included in each simulation 
directories. Double click on the Run_<sim_name>.bat file or type the batch file 
name into a command window to initiate the run.


 
ancillary/

Description: 
----------------
This directory contains the Groundwater Vistas files, the python script used to 
generate the transient recharge file, and instructions and MATLAB scripts to run 
the sensitivity analysis.


     ChapterG_Tables/

     Description: 
     ----------------
     This directory contains the Chapter G tables.
     
          Files: 
          -------
          ChapterG_tables.xlsx: Excel file containing Tables G-1 through G-14
          
          CSV/

     			Description: 
     			----------------
     			This directory contains the Chapter G tables in comma-separated-value format.
     
          		Files: 
          		-------
          		TableG-1_TRheads.csv: Table G-1 containing transient head values
          		TableG-2_SSheads.csv: Table G-2 containing steady-state head values
          		TableG-3_SSheaddiff.csv: Table G-3 containing steady-state head difference values
          		TableG-4_SS_GWflood.csv: Table G-4 containing steady-state head targets equal to the land surface
          		TableG-5_LakeLevels.csv: Table G-5 containing measured lake water levels
          		TableG-6_LakeMonthly.csv: Table G-6 containing monthly average lake water levels
          		TableG-7_TRbaseflow.csv: Table G-7 containing monthly average baseflow values
          		TableG-8_TR_SFRinflows_ChC.csv: Table G-8 containing monthly average baseflow where selected streams enter the active model area
          		TableG-9_TR_SFRinflows_ChD.csv: Table G-9 containing monthly average baseflow where selected streams enter the active model area, inflow to Lake Tapps (the Buckley diversion), and outflow from Lake Tapps
          		TableG-10_SSbaseflow.csv: Table G-10 containing steady-state baseflow values
          		TableG-11_SFRreaches.csv: Table G-11 containing streamflow routing (SFR) package specifications by reach
          		TableG-12_parameters.csv: Table G-12 containing the model calibration parameters
          		TableG-13_TRbudget.csv: Table G-13 containing the transient groundwater budget
          		TableG-14_Scenario3.csv: Table G-14 containing the groundwater use applied to Scenario 3
	
	
     GroundwaterVistas/

     Description: 
     ----------------
     This directory contains the Groundwater Vistas files for the steady-state 
     and transient models. These Groundwater Vistas files contain all the model 
     boundary conditions and inputs for the steady-state model and everything 
     except for the recharge package for the transient model. All model input 
     files can be generated from these Groundwater Vistas files except for the 
     transient recharge file. The recharge file for the transient model was 
     generated outside of Groundwater Vistas and can be found in the recharge 
     directory of this ancillary folder. 

          Files: 
          -------
          SES_ss.gwv: Steady-state model Groundwater Vistas file
          SES_tr.gwv: Transient model Groundwater Vistas file
          Lakes_named.map: Map file of lakes read by Groundwater Vistas
          Lyr3_active.map: Map file of layer 3 active area read by Groundwater Vistas
          Streams.map: Map file of streams read by Groundwater Vistas
          
                   
     Heads/

     Description: 
     ----------------
     This directory contains images of the head values for every layer in the 
     model.    
     
          Files: 
          -------
          Heads_Layer1.png: Image of head values in Layer 1
          Heads_Layer2.png: Image of head values in Layer 2
          Heads_Layer3.png: Image of head values in Layer 3
          Heads_Layer4.png: Image of head values in Layer 4
          Heads_Layer5.png: Image of head values in Layer 5
          Heads_Layer6.png: Image of head values in Layer 6
          Heads_Layer7.png: Image of head values in Layer 7
          Heads_Layer8.png: Image of head values in Layer 8
          Heads_Layer9.png: Image of head values in Layer 9
          Heads_Layer10.png: Image of head values in Layer 10
          Heads_Layer11.png: Image of head values in Layer 11
          Heads_Layer12.png: Image of head values in Layer 12
          Heads_Layer13.png: Image of head values in Layer 13
          
          
     Kh/

     Description: 
     ----------------
     This directory contains images of the horizontal hydraulic conductivity 
     values for every layer in the model.    
     
          Files: 
          -------
          Kh_Layer1.png: Image of Kh values in Layer 1
          Kh_Layer2.png: Image of Kh values in Layer 2
          Kh_Layer3.png: Image of Kh values in Layer 3
          Kh_Layer4.png: Image of Kh values in Layer 4
          Kh_Layer5.png: Image of Kh values in Layer 5
          Kh_Layer6.png: Image of Kh values in Layer 6
          Kh_Layer7.png: Image of Kh values in Layer 7
          Kh_Layer8.png: Image of Kh values in Layer 8
          Kh_Layer9.png: Image of Kh values in Layer 9
          Kh_Layer10.png: Image of Kh values in Layer 10
          Kh_Layer11.png: Image of Kh values in Layer 11
          Kh_Layer12.png: Image of Kh values in Layer 12
          Kh_Layer13.png: Image of Kh values in Layer 13


     PEST/

     Description: 
     ----------------
     This directory contains the files needed to run PEST and PEST_HP.

          Files: 
          -------
	        ses_ss.pst: PEST control file
	        pest_gv.bat: Batch file used when running PEST
          PEST_HP_instructions.docx: Instructions for running PEST_HP
          open_agent_folders.bat: Batch file to open multiple agent folders to run PEST_HP
          run_master.bat: Batch file to begin PEST_HP process in Master folder
          a.bat: Batch file to start PEST_HP process in agent folders	
          UpdateModel_AfterCalibration.docx: Document describing how to update model after PEST calibration
          
          
          PilotPoints/

     			Description: 
     			----------------
     			This directory contains the pilot point files used in the PEST calibration.
     			
     			     Files: 
          		 -------
          		 readme_pilotpoint.txt: Text file describing the contents of the pilot point files
          		 points1.dat: Zone 1 Kh pilot points file
          		 points2.dat: Zone 2 Kh pilot points file
          		 points3.dat: Zone 3 Kh pilot points file
          		 points4.dat: Zone 4 Kh pilot points file
          		 points5.dat: Zone 5 Kh pilot points file
          		 points6.dat: Zone 6 Kh pilot points file
          		 points7.dat: Zone 7 Kh pilot points file
          		 points8.dat: Zone 8 Kh pilot points file
          		 points9.dat: Zone 9 Kh pilot points file
          		 points10.dat: Zone 10 Kh pilot points file
          		 points11.dat: Zone 11 Kh pilot points file
          		 points12.dat: Zone 12 Kh pilot points file
          		 points13.dat: Zone 13 Kh pilot points file
          		 points14.dat: Zone 14 Kh pilot points file
          		 points15.dat: Zone 15 Kh pilot points file
          		 points16.dat: Zone 16 Kh pilot points file
          		 points17.dat: Zone 17 Kh pilot points file
          		 pointz1.dat: Zone 1 Kh/Kv pilot points file
          		 pointz2.dat: Zone 2 Kh/Kv pilot points file
          		 pointz3.dat: Zone 3 Kh/Kv pilot points file
          		 pointz4.dat: Zone 4 Kh/Kv pilot points file
          		 pointz5.dat: Zone 5 Kh/Kv pilot points file
          		 pointz6.dat: Zone 6 Kh/Kv pilot points file
          		 pointz7.dat: Zone 7 Kh/Kv pilot points file
          		 pointz8.dat: Zone 8 Kh/Kv pilot points file
          		 pointz9.dat: Zone 9 Kh/Kv pilot points file
          		 pointz10.dat: Zone 10 Kh/Kv pilot points file
          		 pointz11.dat: Zone 11 Kh/Kv pilot points file
          		 pointz12.dat: Zone 12 Kh/Kv pilot points file
          		 pointz13.dat: Zone 13 Kh/Kv pilot points file
          		 pointz14.dat: Zone 14 Kh/Kv pilot points file
          		 pointz15.dat: Zone 15 Kh/Kv pilot points file
          		 pointz16.dat: Zone 16 Kh/Kv pilot points file
          		 pointz17.dat: Zone 17 Kh/Kv pilot points file


     Recharge/

     Description: 
     ----------------
	   This directory contains the python script used to generate the transient 
	   recharge file. 

          Files: 
          -------
          rch_script.py: Python script to generate the transient recharge file
          ModGrid_rech_20200128.csv: Spreadsheet containing recharge inputs used by rch_script.py
          rch_script_output.txt: Output from rch_script.py to be used as a MODFLOW input file for the transient model after changing file extension to .rch. NOTE: the python script or recharge input file can be edited to add a recharge multiplier if needed. The transient recharge file in this archive was edited to have a multiplier of 1.25.


     S/

     Description: 
     ----------------
     This directory contains images of the specific storage values for every 
     layer in the model.    
     
          Files: 
          -------
          S_Layer1.png: Image of S values in Layer 1
          S_Layer2.png: Image of S values in Layer 2
          S_Layer3.png: Image of S values in Layer 3
          S_Layer4.png: Image of S values in Layer 4
          S_Layer5.png: Image of S values in Layer 5
          S_Layer6.png: Image of S values in Layer 6
          S_Layer7.png: Image of S values in Layer 7
          S_Layer8.png: Image of S values in Layer 8
          S_Layer9.png: Image of S values in Layer 9
          S_Layer10.png: Image of S values in Layer 10
          S_Layer11.png: Image of S values in Layer 11
          S_Layer12.png: Image of S values in Layer 12
          S_Layer13.png: Image of S values in Layer 13
          
          
     SENSAN/

     Description: 
     ----------------
     This directory contains all the MATLAB scripts, text files of the MATLAB 
     scripts, SENSAN input and output files, and instructions for generating the 
     input files and processing the output.

          Files: 
          -------
          SENSANinput_instructions.docx: Instructions for generating sensitivity analysis input files
          SENSANoutput_instructions.docx: Instructions for processing sensitivity analysis output
          get_parametervariability.m: MATLAB file used to generate parameter variability file
          get_parametervariability.txt: Text file copy of get_parametervariability.m for viewing outside of MATLAB
          parameters_v20.csv: Spreadsheet containing a parameter list used by get_parametervariability.m
          pilotpoint_groups_v20.csv: Spreadsheet containing pilot point group names used by get_parametervariability.m
          parameter_variability_sensgroup2_v20.dat: Parameter variability file generated by get_parametervariability.m
          group_names_v20.mat: MATLAB data file containing list of parameter group names generated by get_parametervariability.m and used by sensan_out.m
          ses_ss.sns: SENSAN control file
          abs_out.dat: Lists the parameter values and model output for each SENSAN run
          rel_out.dat: Lists the parameter values and the difference between the base model output and the varied model output using the parameter sets specified in the parameter variability file. rel = (varied model output – base model output)/base model output
          sens_out.dat: Lists the parameter values and provides “sensitivities” of varied model output relative to base model output
          sensan_out.m: MATLAB script to process SENSAN output
          sensan_out.txt: Text file copy of sensan_out.m for viewing outside of MATLAB
          observations_v20.xlsx: List of observation values, weights, and names obtained from the pest control file that is used by sensan_out.m
          tau_sensangroups_ChpD8table.csv: Spreadsheet of sensitivity metric tau values for each SENSAN group calculated in sensan_out.m


     Zonebudget/

     Description: 
     ----------------
     This directory contains the Zonebudget input and output files for each of 
     the MODFLOW simulations in this archive. To start Zonebudget following a 
     simulation run, double-click on the RunZonebudget_<sim_name>.Bat batch file 
     or type the batch file name in a command window. <sim_name> is replaced by 
     the simulation name: SES_ss, SES_tr, SES_Scenario1, SES_Scenario2, 
     SES_Scenario3a, SES_Scenario3b, SES_Scenario3c, SES_Scenario3d, or 
     SES_Scenario3e.
     
          Files: 
          -------
          RunZonebudget_SES_ss.Bat: Batch file to run steady-state zonebudget
          RunZonebudget_SES_tr.Bat: Batch file to run transient zonebudget
          RunZonebudget_SES_Scenario1a.Bat: Batch file to run Scenario 1a zonebudget
          RunZonebudget_SES_Scenario1b.Bat: Batch file to run Scenario 1b zonebudget
          RunZonebudget_SES_Scenario1c.Bat: Batch file to run Scenario 1c zonebudget
          RunZonebudget_SES_Scenario1d.Bat: Batch file to run Scenario 1d zonebudget
          RunZonebudget_SES_Scenario2.Bat: Batch file to run Scenario 2 zonebudget
          RunZonebudget_SES_Scenario3a.Bat: Batch file to run Scenario 3a zonebudget
          RunZonebudget_SES_Scenario3b.Bat: Batch file to run Scenario 3b zonebudget
          RunZonebudget_SES_Scenario3c.Bat: Batch file to run Scenario 3c zonebudget
          RunZonebudget_SES_Scenario3d.Bat: Batch file to run Scenario 3d zonebudget
          RunZonebudget_SES_Scenario3e.Bat: Batch file to run Scenario 3e zonebudget
          RunZonebudget_SES_ss.in: Input file for steady-state zonebudget batch file
          RunZonebudget_SES_tr.in: Input file for transient zonebudget batch file
          RunZonebudget_SES_Scenario1a.in: Input file for Scenario 1a zonebudget batch file
          RunZonebudget_SES_Scenario1b.in: Input file for Scenario 1b zonebudget batch file
          RunZonebudget_SES_Scenario1c.in: Input file for Scenario 1c zonebudget batch file
          RunZonebudget_SES_Scenario1d.in: Input file for Scenario 1d zonebudget batch file
          RunZonebudget_SES_Scenario2.in: Input file for Scenario 2 zonebudget batch file
          RunZonebudget_SES_Scenario3a.in: Input file for Scenario 3a zonebudget batch file
          RunZonebudget_SES_Scenario3b.in: Input file for Scenario 3b zonebudget batch file
          RunZonebudget_SES_Scenario3c.in: Input file for Scenario 3c zonebudget batch file
          RunZonebudget_SES_Scenario3d.in: Input file for Scenario 3d zonebudget batch file
          RunZonebudget_SES_Scenario3e.in: Input file for Scenario 3e zonebudget batch file
	        Zonebudget_in.zon: Zonebudget input file
	        zonbud_SES_ss.lst: Zonebudget output file for steady-state simulation
	        zonbud_SES_tr.lst: Zonebudget output file for transient simulation
	        zonbud_SES_Scenario1a.lst: Zonebudget output file for Scenario 1a simulation
	        zonbud_SES_Scenario1b.lst: Zonebudget output file for Scenario 1b simulation
	        zonbud_SES_Scenario1c.lst: Zonebudget output file for Scenario 1c simulation
	        zonbud_SES_Scenario1d.lst: Zonebudget output file for Scenario 1d simulation
	        zonbud_SES_Scenario2.lst: Zonebudget output file for Scenario 2 simulation
	        zonbud_SES_Scenario3a.lst: Zonebudget output file for Scenario 3a simulation
	        zonbud_SES_Scenario3b.lst: Zonebudget output file for Scenario 3b simulation
	        zonbud_SES_Scenario3c.lst: Zonebudget output file for Scenario 3c simulation
	        zonbud_SES_Scenario3d.lst: Zonebudget output file for Scenario 3d simulation
	        zonbud_SES_Scenario3e.lst: Zonebudget output file for Scenario 3e simulation
                       
  

bin/
  
Description:    
----------------
This directory contains the executables used to run the MODFLOW simulations, 
PEST calibration, and SENSAN sensitivity analysis.

     Files: 
     -------
     agent_hp.exe: Executable used to start agent folders in PEST HP process
     fac2real.exe: Executable used for spatial interpolation of pilot points in PEST process
     inschek.exe: Executable used to check instruction files before running PEST
     kmakr.exe: Executable used to obtain hydraulic conductivities at pilot points in PEST process
     MODFLOW-NWT_64.exe: MODFLOW-NWT (version 1.1.4) 64-bit Windows executable
     parm3d.exe: Executable used in pilot point parameterization in PEST
     parrep.exe: Executable used to generate a new PEST control file with updated PEST parameters after a calibration run
     pest.exe: PEST executable
     pest_hp.exe: PEST_HP executable
     pestchek.exe: Executable to check PEST control file before running PEST
     sensan.exe: SENSAN executable
     senschek.exe: Executable used to check the sensan control file before running SENSAN
     targpest.exe: Groundwater Vistas executable to read MODFLOW binary output files for the calculation of target statistics in PEST process
     tempchek.exe: Executable used to check template files before running PEST
     zonbud.exe: Zonebudget executable
     


georef/

Description: 
----------------
This directory contains a polygon shapefile showing the active and inactive 
extent of the model domain. 
     
     Files: 
     -------
     sir20XX_XXXX.dbf: Part of the shapefile (dBASE file) 
     sir20XX_XXXX.prj: Part of the shapefile (projection file)
     sir20XX_XXXX.shp: Part of the shapefile (main file) 
     sir20XX_XXXX.shx: Part of the shapefile (index file) 
     sir20XX_XXXX.sbx: Part of the shapefile 
     sir20XX_XXXX.cpg: Part of the shapefile 
     sir20XX_XXXX.sbn: Part of the shapefile 
     sir20XX_XXXX.shp.xml: Part of the shapefile



model/

Description: 
----------------
This directory contains ten subdirectories with the input files for the 
steady-state model, transient model, and seven scenarios. 

             
     externalfiles/
     
     Description: 
     ----------------
     This directory contains the shared or common files for the steady-state, 
     transient, and scenario simulations. 
                 
          Files:
          -------
          SES_lyr1._kx: Horizontal hydraulic conductivity, layer 1
          SES_lyr2._kx: Horizontal hydraulic conductivity, layer 2
          SES_lyr3._kx: Horizontal hydraulic conductivity, layer 3
          SES_lyr4._kx: Horizontal hydraulic conductivity, layer 4
          SES_lyr5._kx: Horizontal hydraulic conductivity, layer 5
          SES_lyr6._kx: Horizontal hydraulic conductivity, layer 6
          SES_lyr7._kx: Horizontal hydraulic conductivity, layer 7
          SES_lyr8._kx: Horizontal hydraulic conductivity, layer 8
          SES_lyr9._kx: Horizontal hydraulic conductivity, layer 9
          SES_lyr10._kx: Horizontal hydraulic conductivity, layer 10
          SES_lyr11._kx: Horizontal hydraulic conductivity, layer 11
          SES_lyr12._kx: Horizontal hydraulic conductivity, layer 12
          SES_lyr13._kx: Horizontal hydraulic conductivity, layer 13
          SES._kz: Ratio of horizontal and vertical hydraulic conductivity (Kh/Kv), all layers
          SES.nwt: Newton solver file for all simulations except Scenarios 3a-3e
          SES_Scenario3.nwt: Newton solver file for Scenarios 3a-3e
          SES_gage.gage: Gage Package 
                          

     SES_ss/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     the steady-state SES groundwater flow simulation using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_ss.Bat: Command file to run model
          SES_ss.nam: Name file that contains input and output files for simulation
          SES_ss.bas: Basic package
          SES_ss.dis: Discretization package
          SES_ss.drn: Drain package
          SES_ss.ghb: General Head Boundary package
          SES_ss.oc: Output Control file
          SES_ss.rch: Recharge package
          SES_ss.sfr: Streamflow-Routing package
          SES_ss.upw: Upstream Weighting package
          SES_ss.wel: Well package
          SES_ss.zone: Zone file    
          SES_ss_last.hds: Initial heads = final heads from previous simulation
          usgs.model.reference: Model reference file
          
          
     SES_tr/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     the transient SES groundwater flow simulation using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_tr.Bat: Command file to run model
          SES_tr.nam: Name file that contains input and output files for simulation
          SES_tr.bas: Basic package
          SES_tr.dis: Discretization package
          SES_tr.drn: Drain package
          SES_tr.ghb: General Head Boundary package
          SES_tr.oc: Output Control file
          SES_tr.rch: Recharge package
          SES_tr.sfr: Streamflow-Routing package
          SES_tr.upw: Upstream Weighting package
          SES_tr.wel: Well package
          SES_tr.hob: Head-Observation Package 
          SES_tr_last.hds: Initial heads = December 2008 heads from previous simulation, selected because December 2008 recharge is most similar to December 2004 recharge 
          usgs.model.reference: Model reference file
           
          
     SES_Scenario1a/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 1a using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario1a.Bat: Command file to run model
          SES_Scenario1a.nam: Name file that contains input and output files for simulation
          SES_Scenario1a.rch: Recharge package
          usgs.model.reference: Model reference file  
          
               
     SES_Scenario1b/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 1b using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario1b.Bat: Command file to run model
          SES_Scenario1b.nam: Name file that contains input and output files for simulation
          SES_Scenario1b.rch: Recharge package
          usgs.model.reference: Model reference file 
          
               
     SES_Scenario1c/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 1c using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario1c.Bat: Command file to run model
          SES_Scenario1c.nam: Name file that contains input and output files for simulation
          SES_Scenario1c.rch: Recharge package
          usgs.model.reference: Model reference file           
              

     SES_Scenario1d/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 1d using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario1d.Bat: Command file to run model
          SES_Scenario1d.nam: Name file that contains input and output files for simulation
          SES_Scenario1d.ghb: General Head Boundary package
          SES_Scenario1d.rch: Recharge package
          SES_Scenario1d.sfr: Streamflow-Routing package
          SES_Scenario1d.wel: Well package
          usgs.model.reference: Model reference file
          

     SES_Scenario2/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 2 using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario2.Bat: Command file to run model
          SES_Scenario2.nam: Name file that contains input and output files for simulation
          usgs.model.reference: Model reference file
                

     SES_Scenario3a/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 3a using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario3a.Bat: Command file to run model
          SES_Scenario3a.nam: Name file that contains input and output files for simulation
          SES_Scenario3a.dis: Discretization file
          SES_Scenario3a.drn: Drain package
          SES_Scenario3a.ghb: General Head Boundary package
          SES_Scenario3a.oc: Output Control file
          SES_Scenario3a.rch: Recharge package
          SES_Scenario3a.sfr: Streamflow-Routing package
          SES_Scenario3a.wel: Well package
          SES_Scenario3a.hob: Head-Observation package
          SES_Scenario3a_initial.hds: Initial heads file
          usgs.model.reference: Model reference file
                  

     SES_Scenario3b/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 3b using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario3b.Bat: Command file to run model
          SES_Scenario3b.nam: Name file that contains input and output files for simulation
          SES_Scenario3b.wel: Well package
          usgs.model.reference: Model reference file
             

     SES_Scenario3c/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 3c using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario3c.Bat: Command file to run model
          SES_Scenario3c.nam: Name file that contains input and output files for simulation
          SES_Scenario3c.wel: Well package
          usgs.model.reference: Model reference file
          

     SES_Scenario3d/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 3d using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario3d.Bat: Command file to run model
          SES_Scenario3d.nam: Name file that contains input and output files for simulation
          SES_Scenario3d.wel: Well package
          usgs.model.reference: Model reference file
                

     SES_Scenario3e/
     
     Description: 
     ----------------
     This directory contains the name file and all the input files used to run 
     Scenario 3e using MODFLOW-NWT.           
                 
          Files: 
          -------
          Run_SES_Scenario3e.Bat: Command file to run model
          SES_Scenario3e.nam: Name file that contains input and output files for simulation
          SES_Scenario3e.wel: Well package
          usgs.model.reference: Model reference file
          


output/

Description: 
----------------
This directory contains all the output files for the steady-state and transient 
SES groundwater models and seven scenarios.

             
     output.SES_ss/
     
     Description: 
     ----------------
     This directory contains all the output files for the steady-state simulation.
     
          Files: 
          -------
          SES_ss.ddn: Drawdown
          SES_ss.hds: Head
          SES_ss.lst: Listing
          SES_ss.cbb: Cell-by-cell flows
          SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA
          

     output.SES_tr/
     
     Description: 
     ----------------
     This directory contains all the output files for the transient simulation.
     
          Files: 
          -------
          SES_tr.ddn: Drawdown
          SES_tr.hds: Head
          SES_tr.lst: Listing
          SES_tr.cbb: Cell-by-cell flows
          SES_tr.crc: Cell-by-cell for recharge
	        SES_obs_out.hob: Head-observation package output
	        SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA
	        
	        
     output.SES_Scenario1a/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 1a simulation.
     
          Files: 
          -------
          SES_Scenario1a.ddn: Drawdown
          SES_Scenario1a.hds: Head
          SES_Scenario1a.lst: Listing
          SES_Scenario1a.cbb: Cell-by-cell flows
          SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA	    
	        
	        
	   output.SES_Scenario1b/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 1b simulation.
     
          Files: 
          -------
          SES_Scenario1b.ddn: Drawdown
          SES_Scenario1b.hds: Head
          SES_Scenario1b.lst: Listing
          SES_Scenario1b.cbb: Cell-by-cell flows
          SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA	
	        
	        
	   output.SES_Scenario1c/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 1c simulation.
     
          Files: 
          -------
          SES_Scenario1c.ddn: Drawdown
          SES_Scenario1c.hds: Head
          SES_Scenario1c.lst: Listing
          SES_Scenario1c.cbb: Cell-by-cell flows
          SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA	              
          

     output.SES_Scenario1d/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 1d simulation.
     
          Files: 
          -------
          SES_Scenario1d.ddn: Drawdown
          SES_Scenario1d.hds: Head
          SES_Scenario1d.lst: Listing
          SES_Scenario1d.cbb: Cell-by-cell flows
          SES_Scenario1d.crc: Cell-by-cell for recharge
          SES_obs_out.hob: Head-observation package output
          SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
          SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
          SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
          SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
          SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
          SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
          SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
          SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
          SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
          SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
          SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
          SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
          SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
          SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
          SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
          SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
          SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
          SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
          SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
          SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
          SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
          SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
          SES_gage23.gage: Gage package output at Green River near Auburn, WA
          SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
          SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
          SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
          SES_gage27.gage: Gage package output at White River near Auburn, WA
          

     output.SES_Scenario2/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 2 simulation.
     
          Files: 
          -------
          SES_Scenario2.ddn: Drawdown
          SES_Scenario2.hds: Head
          SES_Scenario2.lst: Listing
          SES_Scenario2.cbb: Cell-by-cell flows
          SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA
          

     output.SES_Scenario3a/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 3a simulation.
               
          Files: 
          -------
          SES_Scenario3a.ddn: Drawdown
          SES_Scenario3a.hds: Head
          SES_Scenario3a.lst: Listing
          SES_Scenario3a.cbb: Cell-by-cell flows
          SES_Scenario3a.crc: Cell-by-cell for recharge
          SES_obs_out.hob: Head-observation package output
          SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
          SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
          SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
          SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
          SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
          SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
          SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
          SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
          SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
          SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
          SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
          SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
          SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
          SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
          SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
          SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
          SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
          SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
          SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
          SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
          SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
          SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
          SES_gage23.gage: Gage package output at Green River near Auburn, WA
          SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
          SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
          SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
          SES_gage27.gage: Gage package output at White River near Auburn, WA


     output.SES_Scenario3b/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 3b simulation.
     
          Files: 
          -------
          SES_Scenario3b.ddn: Drawdown
          SES_Scenario3b.hds: Head
          SES_Scenario3b.lst: Listing
          SES_Scenario3b.cbb: Cell-by-cell flows
          SES_Scenario3b.crc: Cell-by-cell for recharge
	        SES_obs_out.hob: Head-observation package output
	        SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA
          

     output.SES_Scenario3c/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 3c simulation.
     
          Files: 
          -------
          SES_Scenario3c.ddn: Drawdown
          SES_Scenario3c.hds: Head
          SES_Scenario3c.lst: Listing
          SES_Scenario3c.cbb: Cell-by-cell flows
          SES_Scenario3c.crc: Cell-by-cell for recharge
	        SES_obs_out.hob: Head-observation package output
	        SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA
          

     output.SES_Scenario3d/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 3d simulation.
     
          Files: 
          -------
          SES_Scenario3d.ddn: Drawdown
          SES_Scenario3d.hds: Head
          SES_Scenario3d.lst: Listing
          SES_Scenario3d.cbb: Cell-by-cell flows
          SES_Scenario3d.crc: Cell-by-cell for recharge
	        SES_obs_out.hob: Head-observation package output
	        SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA  


     output.SES_Scenario3e/
     
     Description: 
     ----------------
     This directory contains all the output files for the Scenario 3e simulation.
     
          Files: 
          -------
          SES_Scenario3e.ddn: Drawdown
          SES_Scenario3e.hds: Head
          SES_Scenario3e.lst: Listing
          SES_Scenario3e.cbb: Cell-by-cell flows
          SES_Scenario3e.crc: Cell-by-cell for recharge
	        SES_obs_out.hob: Head-observation package output
	        SES_gage1.gage: Gage package output at North Fork Clover Creek near Parkland, WA
	        SES_gage2.gage: Gage package output at Spanaway Creek at Spanaway Lake Outlet near Spanaway, WA
	        SES_gage3.gage: Gage package output at Clover Creek near Tillicum, WA
	        SES_gage4.gage: Gage package output at Flett Creek at Tacoma, WA
	        SES_gage5.gage: Gage package output at Leach Creek near Fircrest, WA
	        SES_gage6.gage: Gage package output at Leach Creek near Steilacoom, WA
	        SES_gage7.gage: Gage package output at Chambers Creek below Leach Creek near Steilacoom, WA
	        SES_gage8.gage: Gage package output at Puyallup River near Orting, WA
	        SES_gage9.gage: Gage package output at South Prairie Creek at South Prairie, WA
	        SES_gage10.gage: Gage package output at Puyallup River at Alderton, WA
	        SES_gage11.gage: Gage package output at Puyallup River at East Main Bridge at Puyallup, WA
	        SES_gage12.gage: Gage package output at White River below Clearwater River near Buckley, WA
	        SES_gage13.gage: Gage package output at White River above Boise Creek at Buckley, WA
	        SES_gage14.gage: Gage package output at Boise Creek at Buckley, WA
	        SES_gage15.gage: Gage package output at White River at R Street near Auburn, WA
	        SES_gage16.gage: Gage package output at Puyallup River at 5th Street Bridge at Puyallup, WA
	        SES_gage17.gage: Gage package output at Puyallup River at Puyallup, WA
	        SES_gage18.gage: Gage package output at Clarks Creek at Tacoma Road near Puyallup, WA
	        SES_gage19.gage: Gage package output at Swan Creek at 80th Street East near Tacoma, WA
	        SES_gage20.gage: Gage package output at Green River at Purification Plant near Palmer, WA
	        SES_gage21.gage: Gage package output at Newaukum Creek near Black Diamond, WA
	        SES_gage22.gage: Gage package output at Big Soos Creek above Hatchery near Auburn, WA
	        SES_gage23.gage: Gage package output at Green River near Auburn, WA
	        SES_gage24.gage: Gage package output at Green River at 200th Street at Kent, WA
	        SES_gage25.gage: Gage package output at Mill Creek at Earthworks Park at Kent, WA
	        SES_gage26.gage: Gage package output at Mill Creek near Mouth at Orillia, WA
	        SES_gage27.gage: Gage package output at White River near Auburn, WA
	        
	        
nonpublic/

Description: 
----------------
This directory contains both steady-state and transient model versions with and 
without the mudflow bypass method. These model versions without the mudflow 
bypass method are not included in the report but were created to test the impact 
of the mudflow bypass method implementation on the model results. 

     Files: 
     -------
     SES_ss_RemoveMudflowBypass_mtx.gwv: Groundwater Vistas file for the matrix version of the steady-state model without the mudflow bypass method 
     SES_ss_RemoveMudflowBypass_zone.gwv: Groundwater Vistas file for the zone version of the steady-state model without the mudflow bypass method
     SES_ss_RemoveMudflowBypass.zip: Working directory for the steady-state model without the mudflow bypass method
     SES_ss.gwv: Groundwater Vistas file for the zone version of the steady-state model (with the mudflow bypass method)
     Working_SS.zip: Working directory for zone version of the steady-state model
     SES_tr_RemoveMudflowBypass.gwv: Groundwater Vistas file for the transient model with the mudflow bypass method
     SES_tr_RemoveMudflowBypass.zip: Working directory for the transient model without the mudflow bypass method
     MudflowBypassMethod.pptx: Powerpoint with details on how the mudflow bypass method was removed and how the results compared to the version with the mudflow bypass method
     HK_Lyr2_RemoveMudflowBypass.csv: Hydraulic conductivities for layer 2 of the model with the mudflow bypass method removed
     
       
     LyrBottoms_RemoveMudflowBypass/
     
     Description: 
     ----------------
     This directory contains the layer bottoms in both csv and text files for 
     the model versions without the mudflow bypass method. Version 7.10 was the 
     model version before the mudflow bypass method was implemented, so these 
     layer bottoms are used to remove it.
     
          Files: 
          -------
          lyr2_bot_v7.10.csv: Comma-separated values file containing Layer 2 bottom elevations
          lyr2_bot_v7.10.DAT: Text file containing Layer 2 bottom elevations
          lyr3_bot_v7.10.csv: Comma-separated values file containing Layer 3 bottom elevations
          lyr3_bot_v7.10.DAT: Text file containing Layer 3 bottom elevations
          lyr4_bot_v7.10.csv: Comma-separated values file containing Layer 4 bottom elevations
          lyr4_bot_v7.10.DAT: Text file containing Layer 4 bottom elevations
          lyr5_bot_v7.10.csv: Comma-separated values file containing Layer 5 bottom elevations
          lyr5_bot_v7.10.DAT: Text file containing Layer 5 bottom elevations
          lyr6_bot_v7.10.csv: Comma-separated values file containing Layer 6 bottom elevations
          lyr6_bot_v7.10.DAT: Text file containing Layer 6 bottom elevations
          lyr7_bot_v7.10.csv: Comma-separated values file containing Layer 7 bottom elevations
          lyr7_bot_v7.10.DAT: Text file containing Layer 7 bottom elevations
          lyr8_bot_v7.10.csv: Comma-separated values file containing Layer 8 bottom elevations
          lyr8_bot_v7.10.DAT: Text file containing Layer 8 bottom elevations
          lyr9_bot_v7.10.csv: Comma-separated values file containing Layer 9 bottom elevations
          lyr9_bot_v7.10.DAT: Text file containing Layer 9 bottom elevations
          lyr10_bot_v7.10.csv: Comma-separated values file containing Layer 10 bottom elevations
          lyr10_bot_v7.10.DAT: Text file containing Layer 10 bottom elevations
          lyr11_bot_v7.10.csv: Comma-separated values file containing Layer 11 bottom elevations
          lyr11_bot_v7.10.DAT: Text file containing Layer 11 bottom elevations
          lyr12_bot_v7.10.csv: Comma-separated values file containing Layer 12 bottom elevations
          lyr12_bot_v7.10.DAT: Text file containing Layer 12 bottom elevations      
          
          
source/

Description: 
----------------
This directory contains the source code for the standard code version of 
MODFLOW-NWT used to run the groundwater flow simulations. It also contains the 
source code for PEST and PEST_HP used in the calibration process.


     hp_suite/
     
     Description: 
     ----------------
     PEST_HP source code used to run PEST calibrations in parallel.
     

     MODFLOW-NWT_1.1.4/
     
     Description: 
     ----------------
     MODFLOW-NWT source code used to run the groundwater flow simulations.
     

     pest17/
     
     Description: 
     ----------------
     PEST source code used to run MODFLOW model calibrations.
     


