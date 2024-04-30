# VB2000

## An ab initio Valence Bond Program based on the Generalized Product Function Method and the Algebrant Algorithm Version 3.0

Jiabo Li 1, Brian Duke 2, Roy McWeeny 3, David W. O. de Sousa 4 , and Rodrigo S. Bitzer 4

1 SciNet Technologies, 9943 Fieldthorn St., San Diego CA 92127, USA

2 Monash Institute of Pharmaceutical Sciences, Monash University 381 Royal Pde, Parkville, Victoria, 3052, Australia

3 Department of Chemistry, University of Pisa, 56100 Pisa, ITALY

4 Chemistry Institute, Federal University of Rio de Janeiro, Brazil.

Date code finalized: September 2021

Date of most recent change in manual: August 30th, 2021

Copyright © 2000-2017 by Jiabo Li, Brian Duke and Roy McWeeny All Rights Reserved.

Copyright (C) 2018- Jiabo Li, Brian Duke, and Roy McWeeny

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/

1
---
## Citation of VB2000 and the Theory

Publications with results obtained from using VB2000 should cite the software and the theory in the following way.

Reference for the software:
Jiabo Li, Brian Duke, Roy McWeeny, David W.O. de Sousa, Rodrigo S. Bitzer. VB2000 Version 3.0, SciNet Technologies, San Diego, CA, 2021.

References for the theory:

1. Jiabo Li, and Roy McWeeny, "VB2000: Pushing Valence Bond Theory to New Limits", Int. J. Quantum Chem., 89 (2002) 208-216.

2. Jiabo Li, Brian J. Duke, Thomas M. Klapötke, and Roy McWeeny, “Spin Density of Spin-Free Valence Bond Wavefunction and Its Implementation in VB2000”, J. Theor. Comput. Chem., 7 (2008) 853-867.

3.Peter B. Karadakov, David L. Cooper, Brian J. Duke, and Jiabo Li, “Spin-Coupled Theory for 'N Electrons in M Orbitals' Active Spaces”, J. Phys. Chem. A, 116, 7238 - 7244, 2012.

2
---
## Table of Contents

|Contents|Page Number|
|---|---|
|1 Introduction|8|
|1.1 What is VB2000?|8|
|1.2 What is new in VB2000 version 3.0?|10|
|1.3 What was new in VB2000 version 2.7?|11|
|1.4 What was new in VB2000 version 2.6?|11|
|1.5 What was new in VB2000 version 2.5?|12|
|1.6 What was new in VB2000 version 2.1?|13|
|1.7 What was new in VB2000 version 2.0?|13|
|1.8 What was new in VB2000 version 1.8(R2)?|14|
|1.9 What was new in VB2000 version 1.8?|14|
|2 Installation Guide|17|
|2.1 Download VB2000 packages|17|
|2.2 Stand alone VB2000 on a UNIX-like platform|18|
|2.3 GAMESS / VB2000 Version|18|
|2.3.1 Step by step instructions|18|
|2.3.2 Run GAMESS / VB2000|19|
|2.4 GAMESS Windows Version|20|
|2.5 Gaussian-VB2000 Version|20|
|2.6 Systems supported|20|
|2.6.1 Linux|20|
|2.6.2 Cygwin|21|
|2.6.3 Silicon Graphics IRIX64|21|
|2.6.4 Windows platform|21|
|2.6.5 Mac OS X|21|
|2.6.6 The future|21|
|2.7 Running the stand alone tests cases on UNIX-like platforms|21|
|2.8 Running the GAMESS / VB2000 tests cases|22|
|3 Capabilities of VB2000|23|
|3.1 Hartree-Fock molecular orbital theory|23|
|3.2 Pipek-Mezey localization method|23|
|3.3 Modern ab initio Valence Bond method|23|
|3.4 Group Function Theory and its combination with VB method|24|
|3.5 Energy profile of chemical reactions|24|
|3.6 Structure weights|25|
|3.7 Spin density|26|
|3.8 Visualization|26|
|3.9 Strict localization and enhanced localization of VB orbitals|27|
|3.10 Extended functionality with GAMESS / VB2000|27|
|4 Quick Start Tutorial|28|
|4.1 Simple VB calculation of CH4|28|
|4.2 How does it work?|29|
|4.2.1 Hartree-Fock calculation|29|
|4.2.2 Pipek-Mezey MO localization|29|
|4.2.3 LMO group assignment|29|
|4.2.4 Initial VB orbitals|30|
|4.3 Two-group VB wave function of CH3-CH2OH|30|
|4.4 GVB calculation of ethane|31|
|4.5 CASVB(4,4) calculation of H2O|31|
|4.6 Run VB2000 in GAMESS|32|
|4.7 Tips and tricks|32|
|5 Terminology|34|
|5.1 Electron groups|34|
|5.2 Group function|34|
|5.3 System wave function function|34|
|5.4 Macro iteration|34|
|5.5 Rigid rotation of a system wave function|34|
|5.6 VB, VBSCF, SCGVB (SC, SCVB), BOVB, CASVB and CASSCF|35|
|5.7 Group Function Theory (GFT) vs. ORMAS|36|
|6 Input Description|37|
|6.1 General consideration|37|
|6.2 Basic controls and molecule specification|38|
|6.2.1 Method|38|
|HF|38|
|VB(m)|38|
|SCGVB(m)|38|
|SCGVB(m,n)|39|
|CASVB(m,n)|39|
|ION(m,n) or SEN(m,n)|39|
|GPF(ng)|39|
|Dot notation|40|
|6.2.2 Use of libraries from VBOLIB directory|40|
|6.2.3 Basis set|40|
|6.2.4 Options|43|
|PRINTALL|43|
|RESTART|43|
|CIONLY|43|
|NOROT|43|
|FROZEN|43|
|UNITS=BOHR|44|
|SPDEN|44|
|DIIS|44|
|SPHER|44|
|TEST|44|
|Group Function controls|45|
|6.3.1 \$GENCTL|45|
|6.3.2 \$GRPDIM|45|
|6.3.3 \$VBGA (\$VBGROUPASSIGNMENT)|45|
|6.3.4 \$LMOGRPMODIFY|47|
|6.3.5 \$MACROITER|47|
|6.3.6 \$ECONV|47|
|6.3.7 \$ROTATION|47|
|6.3.8 \$NOTROT|48|
|6.3.9 \$FULLHESS|48|
|6.3.10 \$DAMPROT|48|
|VB orbital optimization controls|49|
|6.4.1 \$VBSCF|49|
|6.4.2 \$##VBSCF|49|
|6.4.3 \$##VBSTR|49|
|6.4.4 \$HESSCONST|50|
|6.4.5 \$BRILMASK|51|
|6.4.6 \$##LENHANCE|52|
|6.4.7 \$DPWEIGHT|53|
|6.4.8 \$CMAXCUT|53|
|6.4.9 \$NOLOCVBO|53|
|Initial VB orbital generation|54|
|6.5.1 \$##VBORB|54|
|6.5.2 General expression|54|
|6.5.3 \$##PIVBO|55|
|6.5.4 \$LMODISTORTION|55|
|6.5.5 \$WRITEGUESS|56|
|6.5.6 \$READGUESS|56|
|6.5.7 \$RESTARTFILE|57|
|6.5.8 \$RESTARTMAPPING|57|
|6.5.9 \$AOGROUP (original \$PIORB)|60|
|Control for chemical reaction|61|
|6.6.1 \$REACTION|61|
|Advanced controls|61|
|6.7.1 \$##ROOT|61|
|6.7.2 \$##STRSYMM|62|
|6.7.3 \$MEMORY|62|
|6.7.4 \$VBOLIBGEN|63|
|6.7.5 Controls for canonicalization of LMOs|64|
|6.7.6 \$PRINTHS|65|
|6.7.7 \$CENTROID (for GAMESS version)|65|
|6.7.8 \$NOVBPROP (for GAMESS version)|65|
|6.7.9 Other directives|66|
|6.8 Visualization of VB orbitals and molecules|67|
|6.8.1 \$MOLPLT|67|
|6.8.2 \$PLTORB|67|
|6.8.3 \$VECONLY, \$VECMOS. \$VECLMOS and \$VECINIT|68|
|6.8.4 \$CUBE|69|
|6.8.5 \$GENGRID or \$GRID|70|
|6.8.6 \$LINE|70|
|6.8.7 \$XYZFILE|71|
|6.8.8 \$MOLEKEL|71|
|6.8.9 \$MOLDEN|71|
|6.8.10 \$DENSCUBE|72|
|6.8.11 Using the visualization directives in TEST runs|73|
|6.8.12 3D pictures of two VB orbitals of a O-H bond|73|
|6.9 Getting quick help on commands|73|
|7 Construction of Initial Wave Functions|75|
|7.1 Notations of localized molecular orbitals|75|
|7.1.1 Lone pair|75|
|7.1.2 Two-center bond LMO|77|
|7.1.3 Multi-center bond LMO|78|
|7.2 Notations of VB orbitals|79|
|7.2.1 σ VB orbital|79|
|7.2.2 π VB orbital|79|
|7.2.3 Multiple VBOs|80|
|7.3 Construction of initial VB orbitals|81|
|7.3.1 Initial VBOs by splitting LMOs|81|
|7.3.2 Initial VBOs by VBO libraries|81|
|7.3.3 Linear combination of standard VBOs|81|
!7.3.4 A method for construction of CASSCF space|82|
|8 Test Cases and Output Descriptions|83|
|8.1 VB(4) calculation of H2O|83|
|8.2 CASVB(4,4) calculation of H2O|94|
|8.3 CASVB(8,6) calculation of H2O|106|
|8.4 VB(6) calculation of C6H6|100|
|8.5 VB(6) calculation of the triple bond of C2H2|102|
|8.6 VB(6) calculation of C2H2 with three equivalent banana bonds|104|
|8.7 VB(10) calculation of C2H2|105|
|8.8 VB(12) electron VB calculation of C2H4|106|
|8.9 VB(14) electron VB calculation of C2H6|107|
|8.10 Triplet state of trimethylmethene (TMM) and spin density|108|
|8.11 Singlet state of TMM|110|
|8.12 VB(8)•VB(8) calculation of ethanol|112|
|8.13 All-valence electron VB calculation of C6H6|116|
|8.14 VB(8)•CASVB(6,6)•VB(8) calculation of Si4H6|121|
|8.15 VB calculation of the transition state of [Cl---CH3---Cl]─|123|
|8.16 Energy profile of a SN2 reaction|125|
|8.17 Visualization of VB orbitals of H2O|127|
|8.18 Calculation with dynamic VB orbitals|128|
|8.19 VB calculation with strictly localized orbitals|130|
|8.20 VB calculation of structure weights with localization enhanced VB orbitals|133|
|8.21 Benzene with ionicity (0,2) / seniority (6,2)|138|
|8.22 SCGVB(6,5) calculation of the cyclopentadienyl anion|141|
|8.23 Multiconfigurational SCGVB calculation of the allyl cation|143|
|8.24 Other included input files|145|
|9 Acknowledgments|146|
|10 Appendix I, Limits on parameters|148\
|10.1 Limitations on molecule size|148|
|10.2 Limitation on number of electrons|149|
|11 References|153|

7
---
# 1 Introduction

## 1.1 What is VB2000?

VB2000 is an ab initio electronic structure package for performing modern Valence Bond calculations based on a highly efficient VB algorithm—the so called Algebrant Algorithm. It has a general implementation of the Group Function (GF) Theory, in which a large molecule is described in terms of its constituent parts of physically identifiable "electron groups". The modern VB method implemented in VB2000 produces CASSCF(N,N) quality wave functions with only a small fraction of CPU cost for a CASSCF calculation for N>10. The combination of efficient VB methods and the general implementation GF theory in VB2000 makes it a very powerful tool with the investigation of the nature of chemical bonds.

The development of VB2000 has been motivated by two main considerations. First, there is a need to obtain high-precision electronic wave functions, capable of giving quantitative substance to the empirical and intuitive ideas distilled from more than two hundred years of experimental chemistry. There exist within molecules "structural units" such as chemical bonds and functional groups, often with highly individual properties, which are transferable from one environment to another with little change; the behavior of such units conforms, in many cases, to empirical "additivity rules" which have never received a convincing theoretical explanation. Second, although valence bond theory, as developed in the 'thirties and forties', was brilliantly successful in rationalizing such ideas, within the conceptual framework of quantum mechanics, it failed completely to provide rigorous quantitative predictions. The reason was simply that for a system of N electrons the computational cost of ab initio VB calculations tended to grow like N factorial.

With use of the Algebrant Algorithm, ab initio VB calculations on systems with up to about 14 electrons are now becoming 'routine' — even though N! is then of the order 9×1010. However, the majority of molecules of real chemical interest possess far more than 14 electrons. It therefore becomes mandatory to make some kind of conceptual 'separation' of a larger molecule into smaller and more tractable components. By using the Group Function (GF) approach for this purpose, VB2000 brings molecules with many groups within the scope of rigorous non-empirical investigation. Even though the current release has a limitation to a maximum of 16 electrons for each VB group, the full VB calculation of up to a 16-electron group is technically feasible with even a home PC. With the VB2000 program, innovative VB calculations on relatively large molecules can be performed.

The following special features of VB2000 should be noted: the program has been carefully engineered and is highly modular. There is in principle no limit to the number of electron groups that can be recognized; the larger the molecule, the larger the number of groups to be selected. The actual form of each group function is entirely at the discretion of the user. VB2000 provides a general platform for GF calculations of any kind (e.g. using a VB function for one group and a CASVB (CASSCF equivalent) function for another). Both CASSCF and GVB methods can be considered as special cases of GF Theory.

8
---

The methodology used ensures that calculated energies are true variational upper bounds and that the results obtained are size consistent. The detailed forms of the group functions are not prescribed at the beginning of a calculation (as they were in early GF calculations [9], where the global basis was partitioned into subsets, each considered adequate for describing a particular group); they are determined variationally as a result of optimization of the wave function for the entire system, subject only to a strong-orthogonality constraint. This permits the study of chemical reactions, for instance, in which the subsystems representing reactants and products may have forms which change quite dramatically during the reaction process.

In most cases, even a simple one-structure VB wave function can recover most of the corresponding CASSCF correlation energy with only a small fraction of the CPU cost for the CAS calculation. The use of wave functions of VB type for the groups of greatest chemical interest ensures correct behavior when bond-breaking processes occur within a group, and also ensures that the wave functions describing separate fragments possess a high degree of localization.

The GF theory approach used in VB2000 leads to wave functions which are highly compact and therefore provide clear links with chemistry and 'chemical intuition'. For example, the electron density for the entire molecule is always the sum of the densities of its constituent parts -- even though the forms of the group densities may change appreciably in some chemical processes. This provides a firm basis for the discussion of the 'additivity rules' which apply to many molecular properties.

Very often only a small part of a large molecule is responsible for certain chemical and physical properties. The great flexibility of VB2000 allows one to study such a limited region, with a high-precision wave function, using more approximate group functions (such as Hartree-Fock) to calculate the mean field provided by the rest of the molecule.

One important feature of the VB method is that the optimized orbitals tend to be highly localized. The GF framework combined with localized VB group functions provides the possibility of developing a linear scaling algorithm for truly large systems by harnessing the exponentially increasing computer power.

9
---
## 1.2 What is new in version 3.0?

The VB2000 3.0 release was initially intended to be the 2.8 version, but due to significant postponements in the release and the inclusion of two new developers into the VB2000 team, we have renamed it as the 3.0 version for the public release in 2021.

This version is primarily due to developments that removes restrictions on the kind of GAMESS calculation that is used to construct initial guess orbitals in GAMESS/VB2000. Now all values of SCFTYP can be used, allowing UHF, GVB and MCSCF orbitals, in addition to RHF and ROHF. All kinds of DFT orbitals can be used. MP2, coupled-cluster and configuration interaction can be calculated but the HF orbitals are used. GVB is restricted to closed shell and uses the actual “bond” GVB orbitals after using localized orbitals to calculate the GVB CI pairs. The GVB orbitals can be a particularly good initial guess to use VB2000 for more advanced VB methods than GVB-PP. RUNTYP = OPTIMIZE and RUNTYP = HESSIAN can now be used to optimize the geometry or calculate frequencies with the GAMESS method before doing a VB2000 calculation, as well as optimizing the geometry or calculate frequencies with the VB method. RUNTYP =IRC and RUNTYP = SURFACE can be used with a range of GAMESS methods, calculating VB function at each point.

$GMSPATH/vb2000/DOC/GMS_VB_test.README explains these methods in more detail and describes a set of test files for them.

Other new features are:

- A *.vec file can be created containing a GAMESS like $VEC file for initial orbitals. MOs, LMOs and final VB orbitals. This is now supported by MacMolPlt which labels the orbitals correctly
- Molden files can now be read directly by the stand-alone version, to use the basis set, geometry and MOs directly from another program.
- VB calculations can be done after a optimisation or Hessian with another method or along an IRC or set of saddle points calculate with another method.
- VB2000 can now use the structures for a set of ionicities (number of double occupied orbitals) or, equivalently, seniority numbers (number of singly occupied orbitals).
- The Generalized Product Function Energy Partitioning code from the Nascimanto Group in Brazil was added to the GAMESS/VB2000 version.
- See the CHANGELOG and Change_VB2.7-3.0.pdf in the DOC directory for more details and for other developments.

10
---
## 1.3 What was new in version 2.7?

The VB2000 2.7 release is primarily due to the development of a new way of using Gaussian with VB2000, but there have been many other improvements, which were applied into the GAMESS 2014 release. The new Gaussian/VB2000 version is in the directory “g09-vb2000” below the VB2000 directory. The Gaussian/VB2000 version can calculate centroids of orbitals, but not extents.

Other new features are:

- Changes to the VBOLIB system for the GAMESS version. The number of VBOLIBs has been reduced in this release, but additional VBOLIBs are now created on the fly for the addition of polarization functions and diffuse functions. For example, there is now only one VBOLIB for the 6-31G basis sets with VBOLIBs for 6-31G*, 6-31G**, 6-31G++G**, 6-31G(2df,p) and many more created on the fly. The new Gaussian/VB2000 version uses a similar approach but also creates VBOLIBs for spherical harmonics from Cartesian VBOLIBs on the fly. A new VBLOLIB for 6-311G has been created but for H and 1st row elements only.
- BRILLMASK has been extended to automatically create the mask conditions for the case of localization of VB orbitals to just atoms.
- A new visualization directive $DENSCUBE creates CUBE file for the total density, the density of specific groups and, for open shell systems, the spin density.
- Since both GAMESS and Gaussian with conventional integral storage have both been extended to use h and i basis functions, VB2000 has been extended in this way. However SPHER can not be used with such basis sets and a bug in Gaussian (fixed for the next release) prevents the use g, h and i with Cartesian basis sets.
- The vb2blas.src file has been renamed to vb2000-so.src and it now contains routines, previously in vb2000.src, that are only used in the stand-alone version.
- Greater control over maximum values for many parameters has been introduced and is explained in Appendix I.

## 1.4 What was new in version 2.6?

The VB2000 2.6 release is primarily due to the fact that from this point VB2000 will be released as part of the official GAMESS(US) release. Everything needed to get the GAMESS(US)/VB2000 program working will be found in the directory “vb2000” below the “gamess” directory.

There are however some new features:

- $MOLDEN added to the visualization directives to produce a Molden format file for use by the Molden program.
- Extension of the $PLTORB visualization directive to read data so that a “ready to go” input file is prepared for the pltorb program. Previously the file produced had to be manually edited.
- Make the visualization routines prepare files for the LMOs, rather than the VB orbitals, if the TEST directive is on the command line.
- Improved memory allocation in GAMESS(US)/VB2000. It now uses the maximum of the remaining memory from the GAMESS code or that specified by $MEMORY

11
---
## 1.5 What was new in version 2.5?

The new functionality and enhancements in VB2000 2.5 release are listed as follows:

- 64 bit Linux system support. This allows access to much larger memory.
- Extension for Spin-Coupled method. A new method SC(m,n) is added, where m is the number of electrons, and n is the number of orbitals. In the new definition, SC(m,n) specifies all spin-coupled states of all electron configurations of m electrons in n orbitals. The configurations are defined as those that have the maximum number of occupied orbitals. When m=n, SC(m,n) becomes the original SC method (7)
- Localized non-orthogonal Hartree-Fock calculations. Better localized orbitals with better transferability can be obtained. Overlap penalty is used for the optimization of non-orthogonal Hartree-Fock molecular orbitals. This is necessary to avoid the collapsing of non-orthogonal MOs.
- Projection to use spherical harmonic basis functions. GAMESS and VB2000 stand-alone use Cartesian basis functions internally. Some basis sets are defined in spherical harmonics, such as cc-pVnZ basis sets.
- Computation of VB orbital centroids and extents. This function is only available in GAMESS / VB2000, and latest stand-alone Gaussian / VB2000.
- Extension for the maximum number of elections in each VB group. Up to 16 electrons per VB group can be handled.

12
---
## 1.6 What was new in version 2.1?

The new functionality and enhancements in VB2000 2.1 release are listed as follows:

● New expression of initial VB orbitals using atomic orbitals, LMOs and peir linear combinations.
● New VBO libraries for more basis sets.
● Grid format of orbital visualization files which can be displayed wip Accelry's Discovery Studio Version 2.5
● Many enhancements, including better memory management for large number of basis functions, increasing pe maximum number of basis functions in pe whole molecule as well as in an individual VB group and several bug fixes.
● Improvement of convergence for VBSCF, especially for enhanced localization of VB orbitals and BOVB calculations.
● VB2000 2.1 is updated for pe comparability wip pe current version of GAMESS (2009).

## 1.7 What was new in version 2.0?

The new functionality and enhancements in VB2000 2.0 release are listed as follows:

● Adjustable control for pe localization enhancement of VB orbital optimization.
● Strict localization of VB orbital optimization.
● Interface to GAMESSPLUS for VB-solvation calculation in GAMESS (not recently tested).
● New user interface (UI) of VB2000 on Windows platform can now handle bop VB2000 and GAMESS inputs. For GAMESS calculation, a user should have WinGAMESS installed. Since WinGAMESS has VB2000 module compiled in, a user can also run VB calculations wip WinGAMESS once a VB2000 license has been obtained. N.B. As of 2018, WinGAMESS does not include VB2000.

13
---
## 1.8 What was new in version 1.8(R2)?

The following functionality and enhancements have been added in version 1.8(R2):

Spin-density of VB wavefunction. A direct summation method for spin-density calculation of VB wavefunctions has been implemented.

DIIS convergence control. The Direct Inversion of Iterative Subspace method has been implemented for the convergence control of VB orbital optimization.

Enhancement for multi-structure VB calculations with dynamic VB orbitals (BOVB type calculations). The VB orbital optimizer allows the user to use a set of VB orbitals which can be linearly dependent.

Extended map files.|The map files for N=1 and 13 are added to the MAP directory. (N is the number of electrons in a VB group). 

Many bug fixing. The new version allows VB(1) calculation. Two crashing bugs have been fixed: the VB calculation on a single atom and triplet state of two electron VB.

## 1.9 What was new in version 1.8?

Since the first formal release of VB2000 (Version 1.4) in 2000, we have made numerous improvements and added new functionalities. The most significant developments that have been made since version 1.7 are:

- VB2000 has been fully integrated into two major quantum chemistry programs, GAMESS(US) and Gaussian so that some of the functionalities of GAMESS(US) and Gaussian can be used for VB wave function. See the Installation Guide.
- Valence Bond Orbital (VBO) Library Files have been introduced for construction of initial VB orbitals. The simple intuitive expression of VBOs provides extreme flexibility for VBO construction.
- The limitation for the number of basis functions for the integral module has been removed so that larger molecules can be treated in the stand-alone version.
- Graphic utilities have been added for VB orbital visualization.
- There have been other technical enhancements:
- Introduced a 'dot' notation for group function calculations.
- Introduced dynamic memory allocation.
- Added many more built-in basis sets.
- General efficiency has been Improved.
- Added many new controls.
- Enhanced the portability on many more platforms/compilers.
- Enhanced Pipek-Mezey localization routine.

14
---
The Pipek-Mezey MO localization algorithm becomes ill conditioned when orbitals are nearly localized on the same atom; this is because the localized molecular orbital (LMO) function value changes very little for the mixing of two orbitals nearly localized on the same atom. For this reason, the final LMO orbital coefficients and the LMO orbital energies becomes very sensitive to the convergence criteria and platforms. Even though in most VB calculations, the small differences of LMO do not affect the final results, it can cause confusion. To reduce the numerical instability of the PM localization, we added some numerical controls; if the change in value of the objective function of an LMO is smaller than a certain threshold, then do not perform orbital rotation. Another condition to improve the stability is to first prevent the orbital mixing of energetically close MOs. Thus the inner atom core orbitals of different energies on the same atoms are not allowed to be mixed at the beginning. In this way, the mixing of orbitals localized on the same atom is reduced significantly.

We have introduced maximum localization of the VBOs in CASVB calculations.

Since the CASVB is a full CI wave function in a subspace, the orbitals that span the orbital space could be totally arbitrary. One method to reduce the arbitrariness is to use a localization scheme. In CASVB calculations, the orbitals are not necessary orthogonal to each other, therefore this gives some extra flexibility for the orbital localization. To take advantage of this, a method to achieve the maximum localization of an VB orbitals has been introduced and implemented in VB2000. In this method, the CASVB calculation starts from a set of good initial VBOs, and the localization is performed at the last macro iteration to maximize the localization object function for each VBO within the CAS orbital subspace. This procedure leads to a set of highly localized AO-like orbitals, and the CASVB wave functions are usually very compact (i.e. only a few VB structures give significant contributions).

15
---
We have added more Map files.

|S/N|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0| |x| |x| |x| |x| |x| |x| |x|
|1|x| |x| |x| |x| |x| |x| |x| |
|2| |x| |x| |x| |x| |x| | | | |
|3| | |x| |x| |x| |x| | | | | |
|4| | | |x| |x| |x| | | | | | |
|5| | | | |x| |x| | | | | | | |
|6| | | | | |x| | | | | | | | |

The first row is the numbers of the electrons (N) in VB groups, and the first column is the numbers of unpaired spins (S). The mark "X" indicates that the map file of the corresponding combination of N and S is included in the package. Map files for larger systems are available on personal request. If you need a map file for a combination of N and S not in the above table, consult the authors and they will be sent to you.

16
---
# 2 Installation Guide

## 2.1 Downloading VB2000 packages

As of version 3.0 VB2000 has two flavors, a stand-alone program, and a plugin version embedded into the GAMESS(US) release. The former VB2000 / Gaussian variation is not supported anymore.

VB2000 stand-alone version is for all UNIX-like systems. It can be used on Windows, either using Cygwin or using the Windows Subsystem for Linux (WSL) available in Windows 10. The former WinVB2000 variation is not supported anymore.

This section describes the installation on UNIX-like platforms. The following instructions assume that a user has received the compressed file of VB2000 package. It will be helpful if you let us know that you are using VB2000 by emailing us at jiaboli@yahoo.com, david.sousarj@gmail.com or rodrigobitzer@gmail.com.

Use the following commands to unpack the compressed tar file on UNIX-like platforms (Unix, Linux and Cygwin):

tar -zxvf vb2000.tar.gz

If the -z flag is not supported on your particular version of UNIX, type:

gunzip vb2000.tar.gz
tar -xvf vb2000.tar

Once the tar file is unpacked successfully, one should see a new directory VB2000 created in the current directory. This is the main directory of VB2000. Go to this directory and you should see the following sub-directories:

BASET - Basis set files.
DOC - Contains pis manual and oper relevant documentation files.
gamess - Files for pe Gamess version.
MAP - Auxiliary files for pe Algebrant algoripm.
molden - Molden test input files.
SRC - Source code.
TESTINP - Input files of test cases.
TESTOUT - Output files.
TOOLS - Utilities.
VBOLIB - VB orbital library files.

17
---
## 2.2 Stand alone VB2000 on a Unix-like platform

To install VB2000 as a stand alone program, one can use the installation script install in the VB2000 root directory and follow the instructions for various platforms and compilers. For GAMESS / VB2000 installation, please read the corresponding specific instructions.

To compile the source code, one can run the installation by issuing the following command:

./install

When the compilation is completed, an executable file vb2000.exe will be found in the current directory, i.e. the main directory VB2000. Check the log file for possible error messages. If your system is not one of the ones included in the install script, you can probably amend one of the choices to fit your system. Please pass on any successful examples to us.

## 2.3 GAMESS/VB2000 Version

From version 2.6, VB2000 is part of the standard GAMESS release. The vb2000 directory, below the gamess directory defined by $GMSPATH, contains the VB2000 files. Note that this is GAMESS(US), not GAMESS(UK). The following instructions assume that you have installed GAMESS released in 2012 or later. As of VB2000 3.0, the VB2000 code is compiled by default when you compile GAMESS in the normal way. If it is not the case, follow the instructions below as you would after making your own changes to VB2000.

### 2.3.1 Step by step instructions

After running config, carry out the following steps:

Step 1. Typing:

./compall

will compile all GAMESS without VB2000 modules. The four VB2000 modules can be compiled by editing compvb in the vb2000/gamess directory, and then copying it one up to the gamess directory.

You must also define the global variable $VB2000PATH to point to the directory where the stand-alone VB2000 is. See the file gamess.README for more
instructions.

18
---
Step 2. Run:

./compvb

This will compile and link GAMESS with VB2000. You probably need to modify the script lked. You may want to alter the VERNO in compvb to give a different executable from one linked earlier.

Step 3. Test GAMESS with VB2000

Move to the vb2000 directory and type
./runallvb

This will run all the VB2000 tests from the tests directory. You will need to read gamess.README and GMS_VB_test.README. The runallvb script uses the rungms script in the main GAMESS directory. You need to check the runallvb script to ensure it is using the correct version and scratch file. When the jobs have finished, a quick check is to type:

grep TERMINATED exam-vb*.log

This should show that all jobs have terminated normally. Then type:
./checkvbtst

which will carry out a more extensive check of the outputs. This script works in a similar way to checktst for the normal GAMESS tests and exactly like checktst used to work.

### 2.3.2 Run GAMESS/VB2000

The GAMESS / VB2000 executable can be used for both normal GAMESS jobs and VB calculations as well. gamess.README gives a more detailed account. To run VB calculations, you need to ensure that two variables are set in your environment. The rungms script should already include the line:

setenv GMSJOBNAME $JOB

The $VB2000PATH environment variable is already set in rumgms as:

setenv VB2000PATH $GMSPATH/vb2000

below where $GMSJOBNAME is defined. Alternatively you can set VB2000PATH in your .cshrc or .bashrc file, depending on which shell you are using. It must point to $GMSPATH/vb2000, but with $GMSPATH expanded of course to the actual path. You must then delete the line defining it in rungms as that will otherwise take precedence.

19
---
## 2.4 GAMESS Windows Version

The Windows GAMESS executables from the GAMESS site did not include VB2000 due to problems with the compiler. We hope to restore this soon.

## 2.5 Gaussian-VB2000 Version

From version 3.0, the Gaussian integrations with VB2000 are not supported anymore. Please check the VB2000 manual of older versions if you want to use it.

## 2.6 Systems supported

Considerable efforts have been put into the improvement of the portability of the VB2000 code. VB2000 has been tested in the past on several platforms with different compilers. It is expected that the code can be ported on to many other platforms without major changes. The details of machines, operating systems and compilers that VB2000 has been tested on are as follows:

### 2.6.1 Linux

Linux is pretty dominant these days for all codes and most of the development of VB2000 has been under Linux or the related Cygwin. We have used several versions of Linux in the past, including Redhat, Fedora Core, Fedora Enterprise, SUSE, Mint and Ubuntu, but all recent work has been in Ubuntu or Mint. Several compilers have been used:

|Compiler|Details|
|---|---|
|gfortran|Many versions of this compiler have been used with success.|
|g77|In the past, we used most versions of this compiler and had no problems. From version 3.0, it will be not supported anymore, due to inclusion of some Fortran 90 elements.|
|Intel compiler|We have used several versions of this compiler, going back to version 6.0. Both the intel C compiler, icc, and gcc can be used for the C routines. This appears to work fine for the stand-alone version. For GAMESS, some versions used to cause diagonalization problems in the initial guess for SCF.|
|Portland compiler|We have used version 3.2-4, and more recently 10.6 on 64 bit Linux. Both the Portland C compiler and gcc can be used for the C routines. Like ifort, with GAMESS, there are some diagonalization problems in the initial guess for SCF.|
|g95|We have some experience of this compiler using similar flags to g77. 

With the stand-alone version, the appropriate flags are given in the install script. it is difficult to select the best choice of flags for a particular piece of code. It is not clear that our choice is the optimal. Our choice is often based on the choice in the GAMESS(US) comp script.

With GAMESS/VB2000, we made no major changes to the standard flags for all the above compilers.

20
---
### 2.6.2 Cygwin

Cygwin is pretty much like Linux. It provides great convenience to work in both Windows and a Unix-like environment. Both g77 and gfortran compilers are used for our developments. Our very recent tests show that the gfortran compiler has excellent performance, especially for GAMESS.

### 2.6.3 Silicon Graphics IRIX64

The experience with this system is now quite old and we no longer have access, so no further information is worth giving here.

### 2.6.4 Windows platform

The version formerly distributed as WinVB2000 was compiled under cygwin with the “-no-cygwin” flag so it used the MinGW include files and libraries, which gives a stand-alone executable.

### 2.6.5 Mac OS X

VB2000 can be successfully installed on the Mac OS with the gfortran compiler, but we have limited experience.

### 2.6.6 The future

We look to users to provide feedback on the use of VB2000 on other machines and under other environments. Information on other machines and compilers will be available on the VB2000 web site as it becomes available from us or others.

21
---

## 2.7 Running the stand alone test cases on UNIX-like platforms

The script runall can be used to run the test jobs. To do this, first go to the VB2000 main directory, and type the command:

./runall

The test jobs run sequentially, and the output files will be put in a temporary directory TEMPOUT. The test run output files are also included in the package, in the directory TESTOUT. One can compare the output files in TESTOUT and TEMPOUT to verify the correctness of the installation. Use the script vbqa.pl to do a simple comparison of the results. Just type ./TOOLS/vbqa.pl. You must have Perl. You may have to check the first line of the script to make sure it points to the correct location of Perl. You may have to make the file executable.

Running the GAMESS / VB2000 test cases: rhe script runallvb in the vb2000 directory in the GAMESS directotry will run a set of tests. By running ./checkvbtst , it will check these in a similar, but not quite identical fashion as the GAMESS checktst utility works. Each input file has
notes on the test, as does GMS_VB_test.README. You should also read gamess.README.

22
---
# 3 Capabilities of VB2000

## 3.1 Hartree-Fock molecular orbital theory

A Hartree-Fock molecular orbital calculation is the starting point for any other type of calculation. Although VB2000 is not designed for pure Hartree-Fock (HF) method, we have made a number of improvements over the last few years. One major improvement is that the maximum number of basis functions that can be handled by the program has been significantly increased. The HF orbitals are used for electron group assignment, initial guess of VB orbitals and initial one-electron densities of all groups based on Pipek-Mezey localization as described in the next section.

## 3.2 Pipek-Mezey localization

The Pipek-Mezey (PM) method for localization of molecular orbitals (MOs) has been implemented. This utility plays a critical role in VB2000. First, the LMOs provide a solid base for dividing electrons into spatially separable groups. The LMOs of each electron groups are the starting points for generating the initial group functions and the corresponding one-electron densities. One of the initial guess methods for VB orbitals is to split each bonding LMO into two overlapping AO-like orbitals. See more details in Chapter 7. The PM method is based on a simple criterion: the localized MOs should maximize the sum of the squares of Mulliken charges of all atoms from each individual MO. The PM algorithm is also very simple, being based on successive rotations of orbital pairs. This method usually leads to results which are remarkably similar to those obtained from more sophisticated methods, and the cost in CPU time is quite negligible.

## 3.3 Modern ab initio VB method

A major feature of VB2000 is the implementation of modern valence bond theory at ab initio level using the algebrant algorithm. The VB engine in VB2000 has been implemented in the most general form. It can be used to perform very general VB calculations such as:

- Multiple-Structure VB (VB)
- Spin-Coupled Theory, recently renamed Spin-Coupled Generalized Valence Bond (SCGVB)
- Complete Active Space VB (CASVB)
- VB with Localized Electron Pairs (GVB)
- VB Configuration Interaction (VBCI)
- Breathing Orbital VB (BOVB)

VBCI implements a multi-structure VB calculation without orbital optimization. Usually one starts with the optimized VB orbitals obtained from a single structure VB calculation.


This option can be useful when the further optimization of VB orbitals with multi-structures becomes expensive. Our experiences show that further optimization with multi-structures has little gain as compared with the corresponding VBCI calculation with optimized orbitals of a single structure calculation. The output from VB, SCGVB and VBCI calculations normally includes the weights of all resonance structures.

23
---
## 3.4 Group Function Theory and its combination with VB method

As indicated in the Introduction, an essential feature of VB2000 is the implementation of the Group Function Theory, in which a molecular wave function is expressed as an antisymmetrized product of individual group functions [6-8]. The spin-orbitals (one electron 'groups') of a Slater determinant are thus replaced by many-electron group functions - each of which may allow a considerable degree of intra group electron correlation. In VB2000, the electron-correlated group functions are obtained by the VB method. Even though the general mathematical formulation of this approach was completed more than four decades ago and it provides a unifying frame work for many varieties of electron correlation calculations, the general implementation of GF Theory, especially its combination with VB method, was introduced for the first time in VB2000. The general implementation of GF Theory in VB2000 provides tremendous flexibility for this type of computation: a molecular system can be divided into any number of electron groups and each group can be treated at any level of electron correlation of the user's choice. A common scenario is that a higher level of theory (such as CASVB) is used for the most critical regions in a molecule, for instance the bond breaking and forming region, while for the remaining parts some less accurate methods (such as simple VB, even Hartree-Fock) are used. Even though the general idea of using different levels of theory for different part of a molecule is somewhat similar to QM/MM or ONIOM, the approach in VB2000 is fundamentally different from QM/MM and ONIOM. In QM/MM, the system is not described in full quantum mechanics, and the QM/MM boundary is usually a source of trouble due to the lack of consistency for treating a molecule system. ONIOM is basically a highly sophisticated interpolation method based on the computation of different sizes of model systems and different levels of theory. In contrast, the GFT method is a fully quantum mechanical method with a consistent Hamiltonian. Moreover, the approach as a whole is variational.

## 3.5 Energy profile of chemical reactions

VB2000 provides a functionality for the automatic calculation of the energy profile of a chemical reaction along the reaction path guided by a few intermediate structures (such as reactant, transition state, and product etc.). Only for the simplest cases, the Linear Synchronous Transition (LST) method is a good approximation for the reaction path between reactant and product geometries. However, if a few good representative intermediate structures along the reaction path are available, one can use the linear
interpolation between each two consecutive structures for constructing a reasonably good path for the whole reaction. Assume Gi and Gi+1 are two consecutive structures, and Gx is the linear interpolation point between them, then the Cartesian coordinates of Gx can be obtained from the following equation:

Gx = xGi + (1 - x)Gi+1

To make the geometry change as smooth and possible, the structures Gi (i = 1,... NGeoms) should be aligned for the best overlap between each two consecutive structures. This is done automatically by the program using the Kabsch algorithm. The geometries of the representative structures along the reaction path can be obtained from an independent source (for instance, an IRC calculation at a lower level of theory, or even created manually according to some basic knowledge of a chemical reaction). VB2000 also provides controls for how fine the resolution is for the geometry changes along the reaction path. Details of the controls in the input are given in the INPUT section of this manual.

Structure weights

Important information from a multi-structure VB calculation is provided by the weights of the various VB structures. In VB2000, we have implemented four types of structure weight analysis, i.e. The Mulliken Type (also called Chirgwin-Coulson type[22]), Löwdin type[23], Gallup and Norbeck[24] and Hiberty type[25]. The structure weights of the types are calculated according to the following formulas. Let's assume that the multi-structure VB wave function is expressed as follows:

Ψ = ∑i CiΨi

where Ψi is a normalized VB wave function of structure i. The Chirgwin-Coulson structure weights can be calculated as following:

Wi = ∑j Ci Cj Sij

where Sij is the overlap of structure i and j.

A drawback of above formalism is that negative values of weights can be obtained, which is not physical. A remedy for this the negative value problem is to use a Löwdin formalism. This involves the Löwdin orthogonalization of the structure wave functions, i.e.

where \( \phi_i \) (i=1, ... M) are the orthogonalized structure wave functions obtained by using the Löwdin procedure), and \( C_i \) is the new coefficient of the corresponding structure i.

The Löwdin weight can be calculated as the square of the corresponding coefficient:

\( W_i = (C_i)^2 \)

Another remedy for the negative value problem was first used by Hiberty, in which the squares of the original coefficients are used as the structure weights, i.e.

\( W_i = \frac{(C_i)^2}{\sum_{j} (C_j)^2} \)

In ideal cases where all the structure wave functions are orthogonal, all the above three formulas give the same results. All problems come from the case when structure wave functions are not orthogonal, and in this case, none of them are perfect. When the structure functions are not orthogonal discrepancies among the results are sometimes found; but these are usually small. If large discrepancies occur, the numbers obtained should be used with caution.

24
---
## 3.7 Spin density

The spin density for open shell VB wave functions can be calculated. Please note that by defaults, the open-shell VB group must be the last one.

## 3.8 Visualization

In both the stand-alone and GAMESS / VB2000 versions, functionality has been added for plotting 2D VB orbitals, displaying 3D orbitals and molecular geometries. The 3D orbital files in Gaussian Cube format can be generated. The files can be visualized by a variety of visualization programs, such as VMD, MacMolPlt, Molekel, Ghemical, Pltorb, Molplt, gOpenMol, Pymol etc. To extend the graphic visualization with the industrial leading tool for molecular modeling and simulation, Accelry's Discovery Studio (DS) and its free version DS Visualizer, the 3D orbitals in grid format can be generated and displayed in DS Visualizer.

These are described in more detail in section 6.8

26
---
## 3.9 Strict localization and enhanced localization of VB orbitals

In most cases, VB orbitals are highly localized. The localized AO-like VB orbitals provide a clear picture that each VB structure corresponds to a Lewis structure unambiguously. However, it is not uncommon that the VB orbitals have considerable delocalization over to the neighbor atoms. Such a situation happens more often in special bonding patterns. Sometimes, it is not clear whether the delocalization has a strong physical driving force or just an outcome of variational optimization. To study this, one can force the VB orbitals to be localized and to see whether this has a significant impact on the energy of VB wavefunction or not. If the energy increases significantly due to the localization constraints, then one may add more ionic VB structures in the wave function, and thus we know the system has considerable contribution of ionic structures.

There are different ways to force VB orbital localization. One straight approach is to divide basis functions into groups, and only allow each VB orbital to be optimized within a particular predefined group of basis functions. This is the strict localization constraints as used in BOVB approach. A control for strict localization ($BRILLMASK) has been implemented in VB2000 version 2.0. Check out sections 6.4.5 and 8.19 for usage.

The strict localization of VB orbitals is a too harsh constraint and may lead to too high energy. It is not only cumbersome to use but also is limited to some very simple systems. Therefore, we have introduced a more flexible control for localization enhancement of VB orbitals. In this control, an adjustable parameter, which can be considered as a parameter for the strength of localization, is used. If this parameter is set to zero, then the VB orbitals are optimized under no constraints. If this parameter is set to infinity, then the VB orbitals are strictly localized. A particular useful application of such a control is for the cases that the structure weight analysis is needed while the VB orbitals are significantly delocalized so that the structure weights become somewhat ambiguous. Another application is for the case that the localization patterns of the final optimized VB orbitals are different from the initial guess.

## 3.10 Extended functionalities in GAMESS / VB2000

A very significant technical improvement in VB2000 is its ability to be fully integrated with third-party programs: GAMESS and, formerly, Gaussian. In addition to all functionalities of the stand-alone version, some additional features have been added for VB calculations.

- Dipole moments and higher moments calculations, and other properties
- Geometry optimization
- Vibrational frequency calculations
- Effective core potential (pseudo-potential calculation)
- More built-in basis sets

27
---
# 4 Quick Start Tutorial

The simplest way to start a calculation on a UNIX-like platform is to submit a job in the installation directory. You can also run a job in a different directory by setting the environment variable:

- setenv VB2000PATH &lt;Your VB2000 Directory&gt;
- or
- export VB2000PATH=&lt;Your VB2000 Directory&gt;

where &lt;Your VB2000 Directory&gt; is the full path of your VB2000 installation directory. You can add VB2000PATH setting in your .cshrc or .bashrc file, depending on which shell you are using.

Before doing a VB calculation, the very first decision that a user should make is how many and which electrons (or which chemical bonds and lone pairs) should be treated by VB method. In this chapter, a few examples are provided.

## 4.1 Simple VB calculation of CH4

The first example is a VB calculation of 8 electrons on the 4 C-H bonds of methane. To do the calculation, just copy or write the following lines into a new input file (it is already available at TESTINP/extra/extra01_ch4vb8.inp):

<pre>
#! VB(8)/D95

TEST CH4 5 GROUPS (1 CORE + 4 BONDS)

0 1
6  .000000   .000000  .000000
1 -.880321   .417906 -.470561
1  .259946   .591217  .868290
1 -.202850 -1.018388  .304590
1  .823225   .009265 -.702319

</pre>

Please note that you should always keep at least one blank line at the end of the input file. Save the file as example01.inp (for example) and run the job:

./vb2000.exe example01 &gt;example01.out

This calculation produces one core orbital corresponding to the 1s core of carbon atom and 8 VB orbitals corresponding to the 4 C-H bonds.

28
---
## 4.2 How does it work?

Here are the basic steps for a typical VB calculation in VB2000.

### 4.2.1 Hartree-Fock calculation

The first step of a VB calculation is usually a Hartree-Fock molecular orbital calculation. The RHF method is used for a closed shell system and a quasi-ROHF method is used for an open shell system. In the quasi-ROHF method, the Fock matrix is constructed from the total density in the same as in the RHF method.

### 4.2.2 Pipek-Mezey MO localization

The canonical molecular orbitals from a Hartree-Fock calculation are transformed into a set of localized molecular orbitals (LMOs) by Pipek-Mezey method. The generated LMOs are used for the following two purposes:

- Group assignment for electrons on LMOs
- Initial guess of VB orbitals by splitting bonding LMOs

The LMOs are grouped in the following types and order: inner core orbitals, lone pairs, and bonding LMOs. For each type of LMOs, the orbitals are ordered in an ascendant order of their orbital energies. Each LMO has a label to indicate its type. The Mulliken population of each LMO is calculated and used to determine its LMO type. If a LMO has approximately equal electron distribution on two directly connected atoms, then this LMO is a bonding LMO between the two. If the population is localized on one atom, then it is either an inner core or a lone pair. If a LMO is localized on more than two atoms, and it is marked as a multi-center (MC) bonding orbital.

### 4.2.3 LMO group assignment

The program does the LMO group assignment automatically according to the input. For simple VB calculations, the default assignment is usually what a user needs. For the above example, the input specifies VB(8), an eight-electron VB calculation. Since the molecule has 10 electrons in total, there is a Hartree-Fock core group with two electrons and a VB group with eight electrons. By default, VB2000 starts with the Hartree-Fock group and then the VB group(s) specified in the input. In the CH4 case, the first LMO is assigned to the Hartree-Fock group, and the remaining 4 LMOs, which are bonding orbitals corresponding to the 4 C-H bonds, are assigned to the VB group.

In some cases, the default LMO assignment may not be what you need. One should explicitly assign LMOs to the appropriate groups by using $LMOGRPMODIFY input. A more advanced control for the same purpose is $VBGA. See Chapter 6 for more details.

One can always do a TEST run (keyword: TEST) run and check the order of LMOs.

29
---
### 4.2.4 Initial VB orbitals

By default, the initial VB orbitals for a VB group are generated by splitting the bonding LMOs assigned to this group, and the lone pair orbitals of the VB group are used directly as part of the VB orbitals. Each LMO is split into two VB orbitals. For example, if a VB group has L lone pairs and M bonding LMOs, then L + 2M VB orbitals will be generated for the 2(L+M) electrons. Of course, one can always change the number of VB orbitals and the way for generating the initial VB orbitals by using addition controls in the input. See Chapter 6 for $##VBORB and $AOGROUP controls.

If all above methods fail, there is a last resort: $READGUESS. This option read the initial guess from a text file. The initial guess can be generated from any method. In some cases, you only need to modify a few VB orbitals. In the case, you can first generate such a file by using $WRITEGUESS, and then modify it using any text file editor.

## 4.3 Two-group VB wave function of CH3-CH2OH

Input file (TESTINP/example12_etOH.inp):

<pre></pre>
#! VB(8).VB(8)/D95 PRINTALL

TEST C2H5OH (TWO VB GROUPS)

0 1
6  -0.4413   1.9095    -0.1486
1   0.1529   2.7834    -0.4194
1  -1.2624   1.8366    -0.8622
1  -0.8754   2.0884     0.8352
1  -0.2076  -0.2379     0.0887
6   0.4029   0.6280    -0.1666
1   0.8338   0.4543    -1.1531
1   2.0387   1.4420     0.5056
8   1.4477   0.7230     0.7814

$VBGA
1-2 => 2
1-3 => 2
1-4 => 2
1-6 => 2
6-7 => 3
5-6 => 3
6-9 => 3
8-9 => 3

</pre>

In this case, the molecule is divided into two groups: CH3- and -CH2OH, each contains 4 covalent bonds and is described by a VB(8) group function. The system wave function is thus the generalized product of two VB(8) functions and the Hartree-Fock function of the remaining electrons. The $VBGA flag specifies the VB group assignments. The first group is the Hartree-Fock, the second group is the first VB group, and the third the second VB group. The lines following $VBGA flag can be read as: the covalent bond between atom 1 and atom 2 is assigned to group 2, etc. See Chapter 7 for more details.

30
---
## 4.4 GVB calculation of ethane

Input file (TESTINP/extra/extra02_c2h6gvb.inp):

<pre>
#! VB(2).VB(2).VB(2).VB(2).VB(2).VB(2).VB(2)/D95
    
TEST C2H6 (7 SIGMA BONDS)
    
0 1
6   .000000   .000000   .000000
6   .000000   .000000  1.540011
1  1.027669   .000000  -.363311
1  -.513834  -.889987  -.363311
1  -.513834   .889987  -.363311
1 -1.027669   .000000  1.903322
1   .513834   .889987  1.903322
1   .513834  -.889987  1.903322

</pre>

As a special case of GF theory approach, the 7 GVB pairs can be described by 7 VB group functions each with two electrons in two orbitals. There is a shortcut for GVB specification in the keyword. By getting familiar with these terms, it will be easier to understand the inputs and outputs of VB2000. For the above case, the key word can be simplified as

#! GPF(8)/D95

By default, if there are no additional flags, the GPF(n) key word will be interpreted as n-1 GVB pairs.

## 4.5 CASVB(4,4) calculation of H2O

<pre>
Input file (TESTINP/example02_h2ocas.inp):
    
#! CASVB(4,4)/D95 PRINTALL
    
TEST H2O
    
0 1
8   .000000   .000000   .000000
1   .801842   .000000   .555582
1  -.801842   .000000   .555582

</pre>

In this case, the four electrons of the O-H bonds are included in the CASVB calculation.

31
---
## 4.6 Run VB2000 in GAMESS

To run a VB calculation in GAMESS, you need:

1. Add VBTYP=VB2000 in $CONTRL block.
2. Include a normal VB2000 input in a $VB2000 block.

Here is an example of VB run in GAMESS:

<pre>
 $CONTRL SCFTYP=RHF COORD=UNIQUE VBTYP=VB2000 $END
 $SYSTEM TIMLIM=20 MEMORY=2000000 $END
 $BASIS GBASIS=STO NGAUSS=3 $END
 $GUESS GUESS=HUCKEL $END
 $DATA
Water STO-3G
C1
OXYGEN 8.0 0.0000000000 0.0000000000 0.0000000000
HYDROGEN 1.0 0.0000000000 -0.7572153434 0.5865355237
HYDROGEN 1.0 0.0000000000 0.7572153434 0.5865355237
 $END
 $VB2000
#! VB(4)/STO-3G PRINTALL
    
Water
    
0 1
8 0.0000000000  0.0000000000 0.0000000000
1 0.0000000000 -0.7572153434 0.5865355237
1 0.0000000000  0.7572153434 0.5865355237
    
 $END

</pre>

One major advantage of running VB2000 in GAMESS is that the properties of VB wave function can be computed. In the log file of GAMESS / VB2000 run, the VB properties, including the dipole moment, are printed after the following line:

<pre>
----------------------------------
PROPERTIES FOR THE VB WAVEFUNCTION
----------------------------------
</pre>

The dipole moment is printed under the ELECTROSTATIC MOMENTS.

32
---
## 4.7 Tips and tricks

The following advices may help you to run VB2000 more effectively for your systems:

1. If you want to run a multi-group VB calculation, specify the VB groups explicitly using the “dot” notation, such as VB(8).CASVB(6,6).VB(8). You can specify the same kind of calculation by using GPF(ng) and other controls, but the “dot” notation is much easier to use and intuitive.
2. You can do a VB calculation of a molecule at one geometry and do another VB calculation on the same molecule at a different geometry by reading the VB orbitals of a previous calculation. This is not only a good way to speed up convergence of a new calculation, but also a necessary step for generating initial VB orbitals for a bond breaking calculation in some cases.

If a VB group has many resonance structures and you have difficulty to determine which ones make major contributions, you can try a CASVB calculation first and then check the biggest contributors.

Try to avoid running CASVB or SCGVB for groups with large number of electrons (N>8 for CASVB and N>10 for SCGVB). If you want to run SCGVB(12), you can run a VB(12) for orbital optimization with one or a few structures, and then do a SCGVB(12) as a restart calculation without further
optimization of VB orbitals (using key word CIONLY). SCGVB(11) and SCGVB(12) have 132 structures, which is just about feasible but not advised.
SCGVB(13) and SCGVB(14) have 429 structures which is not possible.

The spin-density calculation can be very time consuming for group with more than 12 electrons.

If VBSCF for VB orbital optimization becomes unstable, you can add a constant to Hessian diagonal elements by using $HESSCONST, starting from 0.1. A larger value can make the iteration more stable, but it can slow down the convergence. Use PRINTALL option to watch closely the iterations and adjust the parameter so that you can get the converged results without slowing down the iteration too much.

Using the DIIS option can reduce the chance of symmetry broken solutions if you wish to keep certain symmetry. See Chapter 6 for more details about key word DIIS. However, the DIIS option sometimes can lead to false convergence.

If the macro iteration is unstable (total energy becomes oscillating, you can set a damping factor for rigid rotation. See Chapter 6 for control $DAMPROT.

We will post more tips for VB calculations on the VB2000 website. Comments and suggestions from users are highly appreciated.

33
---
# 5 Terminology

The following definitions and related concepts are frequently used in describing the technical details of VB2000. By getting familiar with these terms, it will be easier to understand the inputs and outputs of VB2000.

## 5.1 Electron group

A group of electrons moving in a particular region of a molecule. For instance, the electrons of the benzene molecule fall into three groups: the pi-electrons, the sigma-bond electrons and the core electrons. Even though electrons are indistinguishable, it is convenient to regard a number of electrons, described using a particular subspaces of basis functions, as an "electron group".

## 5.2 Group function

An antisymmetrized wave function describing a group of electrons in the mean field of all other groups.

## 5.3 System wave function

A generalized production function (GPF) describing the entire molecular system. Such a wave function can be constructed as an antisymmetrized product of group functions of all electron groups in the molecule.

## 5.4 Macro iteration

A round of group-by-group optimizations of group functions, followed by a 'rigid rotation' of the system wave function. Usually such a procedure is repeated until the system wave function converges. The group wave functions are optimized within their own subspace, and the the rigid rotation is performed for the global optimization of the system wave function. In VB2000, the global optimization algorithm is very general and applies no matter how each group function is constructed.

## 5.5 Rigid rotation of a system wave function

Let us assume that the system wave function of a molecule is expressed in terms of M orthogonal orbitals (e.g. a set of Löwdin-orthogonalized orbitals). A 'rigid rotation' of the system wave function is one which all the parameters in the wave function, expressed in the orthogonal basis, are held constant (thus, the orbital coefficients, the VB structure coefficients, the one- and two-electron density matrices defined in the orthogonal basis are left unchanged) while the orthogonal basis are rotated in the M-dimensional space.

34
---
## 5.6 VB, VBSCF, SCGVB (SC or SCVB), BOVB, CASVB and CASSCF

There is much confusion in the literature concerning VB terminology. In this section we try to clarify the one used in our present work. Most of the differences among VB computations are purely technical. The term 'VB calculation' generally means the wave function is constructed in VB form by defining VB orbitals and their spin-pairing patterns. In modern VB calculations the VB orbitals are usually optimized in some self-consistent way and this gives rise to the term 'VBSCF method'.

In simple cases (e.g. for a saturated molecule) a single VB structure can often provide a fairly good description of the electronic structure; but cases where the chemical bonds cannot be plausibly assigned in any unique way (as in reactions, where bonds may be continually formed or broken) a single structure is inadequate. No single pairing scheme serves to give a good description of the whole structure or process and a multi-structure VB function becomes necessary. One such a choice is the so-called Spin-Coupled or, more recently renamed, Spin-Coupled Generalised Valence Bond wavefunction in VB form (SCGVB), which uses one set of VB orbitals but all linearly independent spin-pairing patterns–without any change of orbital occupation numbers (i.e. without 'excitations'). SCGVB has been proposed as a compromise between the use of “full-GVB” mainly in the USA and SC or SCVB elsewhere. We support this change.

Another approach used in describing bond-breaking/forming processes also employs a multi-structure VB function, but allows different sets of orbitals for different structures: this is the Breathing Orbital VB (or BOVB) method[26], in which the orbitals are allowed to expand or contract (i.e. 'breathe') on changing from one structure to another. The BOVB method can efficiently incorporate dynamic correlation in a VB wave function while keeping the compact form of the function.

A CASVB calculation is mathematically equivalent to CASSCF: it involves a set of VB orbitals which define the Complete Active Space and includes all linearly independent spin-coupled functions that can be constructed from them. CASVB is not designed as an efficient alternative to CASSCF, but it has some advantages that CASSCF does not provide. In particular, the orbitals have no orthogonality constraints and so can be highly localized like atomic orbitals. Since the CAS wave function is invariant under orbital transformations in the active space, we can require maximum localization of the VBOs, without constraints, in any function of CASVB type – even with a limited number of structures. The CASVB wave function is then also highly compact, a few structures providing almost all significant contributions. One should note the CASVB method implemented in VB2000 is different from Cooper's CASVB approach, in which the CASSCF wave function is transformed into VB form of a subset of CASSCF space. VB2000 provides a very general implementation of VB theory and is capable of performing all the above types of calculation. The SCGVB and CASVB keywords in VB2000 allow one to perform the specified computation without knowing any of the details involved in constructing all the VB structures.

35
---
## 5.7 Group Function Theory (GFT) vs. ORMAS

To the best of our knowledge, no other electronic structure program has a general implementation of group function theory which can perform full optimization of a wave function which is expressed as a generalized product of group function. GVB and MCSCF can be considered as two special cases of GFT. The Occupation Restricted Multiple Active Space Configuration Interaction (ORMAS) method has been introduced in GAMESS(US)[27,28]. The general philosophy of ORMAS has a certain similarity to GFT in terms of multiple groups. But the two methods are actually totally different both technically and theoretically. It would be interesting to compare the two methods. The ORMAS method involves two steps: first the active space (a set of active orbitals) is partitioned into an unrestricted number of orbitals, and secondly occupation restrictions are specified in the form of the minimal and maximal number of electrons allowed for each group. ORMAS can be considered the most general implementation of restricted active space SCF method, thus all other variations such CASSCF and the 3-group RASSCF can be recovered by appropriate specifications of the restriction parameters. ORMAS efficiently eliminates ineffective configurations in CI computation while keeping the flexibility to account the electron correlations among groups. One should be aware that the flexibility for group-group electron correlation comes at the price the number of exponentially increasing of configurations - even though such an increase is considerably reduced by the restrictions.

The group function method approaches the electron correlation of large systems in a different way. It also involves two steps. The first step is similar to that of ORMAS, i.e. a molecule system can be partitioned into an unrestricted number of electron groups. The second step is quite different from ORMAS: 1) the number of electrons in each group is fixed, i.e. electrons are not hopping between different groups; 2) the wave function is expressed as the antisymmetrized product of group functions; 3) each group function is optimized in the mean field of the other groups thus the small inter-group correlation is neglected. A major advantage of this approach is that the computational cost increases only linearly with the number of groups instead of exponentially as in ORMAS. In principle, any correlation method can be used for the group function of a GF group. For instance, a GF group can be further divided into multiple subgroups and the ORMAS method can be applied to these subgroups.

36
---
# 6 Input Descriptions

VB2000 is designed to balance the flexibility of controls and the convenience of usability. Most of the controls and options needed are automated as defaults, which in most cases work well. This automation reduces the input to a minimum. On the other hand, many controls can be customized and will overwrite the defaults with explicit input, thus providing the maximum flexibility. One should also understand that VB2000 is not designed as a black box. Input backed by chemical knowledge is essential to obtain insights into interesting chemical systems. VB2000 is designed to provide convenient controls to convert sophisticated theory into practice so as to test, verify and refine theoretical ideas about the nature of chemical bonds. This chapter illustrates how to specify different kinds of calculations in the input files.

## 6.1 General considerations

The controls in the program are divided into three Levels, as follows.

|Level 1: Defaults.|When controls are not set explicitly, the defaults take effects automatically, being preset according to the type of calculation.|
|---|---|
|Level 2: Global controls.|Most of the default settings can be overwritten by providing explicit inputs. There are two kinds of the global controls: (1) controls that concern the optimization of the total wave functions (including the number of subgroups, number of macro iterations, etc.); (2) controls that relate to a specific method. All groups treated by the same method can be dealt with using the same method-specific global controls. A global control can be either a key word or a dollar '

The control consists of two parts, i.e. the control flag and the control-content. The control flag always starts with a dollar ('$') sign, followed by a two-digit number and the name of the control (no space in between). We use upper-case letters for all control names. The two-digit number (here represented by ##) is the number of the group that the control is applied to. The number starts from 01 up to 99. In most common cases, the first group is
flag string.|
|Level 3: Controls for individual groups.|The optimization of the group wave function of any specific group can be controlled directly by a level 3 control. The general expression of a level 3 control is as follows:|

The control consists of two parts, i.e. the control flag and the control-content. The control flag always starts with a dollar ('$') sign, followed by a two-digit number and the name of the control (no space in between). We use upper-case letters for all control names. The two-digit number (here represented by ##) is the number of the group that the control is applied to. The number starts from 01 up to 99. In most common cases, the first group is a Hartree-Fock group, and the second one a VB group. The control content can be either empty or a multiple line input.

37
---
## 6.2 Basic controls and the input of a molecule

The input for a calculation starts with ‘#!’ (historically it was so to distinguish it from ‘#’ used in the Gaussian package) and followed by basic controls and molecule specification as shown below:

<pre>
#! METHOD/BASIS_SET [OPTIONS]
[Blank]
Title or comments (can be multiple lines)
[Blank]
Charge, Multiplicity
Atomic#1, X1, Y1, Z1
Atomic#2, X2, Y2, Z2
…
[Blank]
[Oper controls]

</pre>

The first input can be continued and terminated by a blank line. Multiple lines of comments can be inserted before providing the numbers of charge and multiplicity. The comments are also terminated with a blank line. For each atom, the atomic number and its Cartesian coordinates should be provided. All these numbers can be given in free format. The atom input is also terminated by a blank line. After the atomic input, additional controls can be provided in the input. All these controls are described in the following sections.

### 6.2.1 Method

In the above, METHOD can be any of the key words explained below.

HF: If the METHOD is set to HF, then Hartree-Fock method will be used for the whole molecule. This is essentially a regular molecular orbital calculation.

VB(m): VB method will be used for a group of m electrons. By default, only one VB structure will be included in the calculation. One can explicitly specify multiple VB structures by using an additional control flag $##VBSTR (see section 6.4.3)

SCGVB(m): Spin-Coupled method (recently renamed SCGVB to remove the confusion of different names – SC, SCVB and full-GVB) is used for a set of m electrons in m orbitals. All linear independent spin-configuration of m electrons in m orbitals are included in an automatic way. Therefore, there is no essential difference between SCGVB(m) and VB(m) with multiple VB structures. SCGVB(m) provides a convenient shortcut for a special multiple-VB structure calculation that a user don't have to write all linear independent spin configurations explicitly. The keywords SC(m) and SCVB(m) can also be used. SCGVB is limited to 12 electrons. It seems that the changing of array bounds to have more structures is a long way short of what is needed. SCGVB(13) and SCGVB(14) have the same number of structures but the time and resources to complete that calculation makes it totally unattainable at present. 

SCGVB(m,n): We can ask ourselves: what would be the most natural way to extend Spin-Coupled method to systems where the number of electrons is not equal to the number of orbitals? In VB2000, we define it as the all spin-coupled states from all possible electron-orbital configurations which have the maximum number of occupied orbitals. For instance, in the case of SC(m,m), there only one such a configuration, that is all orbitals are occupied with one electron on each, and all spin-coupled states are from the spin-coupling schemes from this configuration. Thus SCGVB(m,m) = SCGVB(m). An essential advantage of SCGVB method is that the wave function and optimized orbitals are independent of the way to choose the Lewis structures of the SCGVB space, therefore, the results is not biased to any personal preference. As with SCGVB(m), the largest value of m is 12 but SCGVB(12,11) takes longer to run that SCGVB(12,12), One can make special use of SCGVB(m,n) when m = 2n, i.e. all orbitals are double-occupied. In this case, SCGVB option turns into non-orthogonal Hartree-Fock method. In VB2000, we use this trick to do non-orthogonal localized Hartree-Fock molecular orbital calculations. Even though for regular VB calculation the maximum number of electrons in each VB group is currently limited to 16, the non-orthogonal Hartree-Fock MO calculations does not have such a limitation. The limitation for the number of non-orthogonal molecular orbitals comes from the limit of total number of basis functions which can be handled by the program and the computational time. It should be noted that the non orthogonal Hartree-Fock MO computation is much more expensive than the regular Hartree-Fock method. CASVB(m,n)

Complete Active Space VB (CASVB) is used for a set of m electrons in n orbitals. It is mathematically equal to a CASSCF(m,n) method, i.e. the wave functions produced by the two methods have the same energy and properties. The CASVB method has some unique advantages that the orbitals in CASVB wave functions are nonorthogonal and can be maximally localized. ION(m,n) or SEN(m,n)

This provides a level of calculation between SC and CASVB based on the seniority number (SEN) or the equivalent ionicity (ION). SC has structures of maximum possible seniority number and the lowest possible ionicity. CASVB has structures of all possible seniority number or ionicity. It requires $xxIONICITY or $xxSENIORITY to define the range of either included, See GAMESS / VB2000 test examvb-40 or stand alone test example21.


39
---
GPF(ng): This an old way to specify a multi-group VB calculation, where ng is the number of electron groups including the Hartree-Fock core. Additional controls are required for this method. This notation will become obsolete in the future release. The most convenient way to specify a multiple-group VB calculation is by the dot notation which is described in the next section.

Dot (•) notation: The dot notation has been introduced since version 1.8 for specifying a multi-group VB calculation. This notation is a more convenient and intuitive than the GPF notation. For example, VB(8)·CASVB(6,6)·VB(8) specify a 3 VB group calculation. One should note that if the molecule is a open-shell system, then the last VB group must include the open-shell electrons. Only one VB group can have unpaired spins.

### 6.2.2 Use of libraries from VBOLIB directory.

A set of libraries, known as VBOLIBs are included in the VBOLIB directory. This are used to select the initial guess. See section 6.5. These VBOLIBs are basis set specific.

### 6.2.3 Basis set

a) The stand-alone VB2000.
BASIS_SET is the name of the basis set, which can be any one of the following:
STO-3G
STO-4G
STO-6G
D95             (Dunning/Huzinaga full double-zeta)
MIDIX           (Minnesota MIDI! basis set)
3-21G
3-21G*
6-31G
6-31G*
6-31+G*
6-31G**
6-31++G**
cc-pVDZ
AUG-cc-pVDZ
TZVP
GEN             (general basis set provided by user with a basis set file)
GENNG           (general minimal basis set provided by user with a basis set file)

The first 15 are built-in basis sets and VBOLIBs are available for all of them. GEN is a
flag for a user defined basis set: when specified, the program will expect additional input
(after the atomic input) as follows:

&basis_set_file

where basis_set_file is the file name of the user-defined basis set, which should be put in the directory BASET. You can also provide the basis set file with the full path if the file is not in the BASET directory, for instance,

    /usr/people/jli/VB20000/GEN/basis_set_file
    
This file should be prepared in the appropriate format (see the format used for the standard basis set files in BASET). GENNG is identical to GEN in all respects except that it is restricted to minimum basis sets, and it uses the STO-nG VBOLIB, while GEN does not use any VBOLIB. A
program, TOOLS/get_gen_sto6g.f, is available to create STO-6G basis sets with general STO exponents. Details of the input is given in comments at the top of the file.

40
---
b) GAMESS/VB2000 version.
This version can use any basis set defined in GAMESS, using the $BASIS group, the $DATA group  or an external file. However, only basis set defined in the $BASIS group can use a VBOLIB, with one exception:

          VBOLIBD95

which can be defined in the $DATA group but D95 must be correctly given in the !# command line. The number of VBOLIBs is less than the number in the stand-alone version, but they are more useful as extra VBOLIBs can be created from them on the fly to add polarisation and diffuse functions, as indicated below.

          VBOLIBSTO-nG

is used for any STO-nG basis set defined in GAMESS plus the STO-nG* basis sets that add a single d polarisation function to atoms heavier than Ne. This VBOLIB can also handle the MINI basis set in GAMESS up to Ne. d and f polarisation functions using NDFUNC and NFFUNC are allowed.

          VBOLIB3-21G

is similar but can also be used for the rarely used 6-21G basis set. 3-21G* and 6-21G* which has a single d polarisation function on atoms heavier than Ne.
          VBOLIB6-31G
          
can be used for 4-31G, 5-31G and 6-31G and can accommodate up to three d and one f polarisation functions and a single diffuse sp set of diffuse functions on heavy elements and a single s diffuse functions on H using the “++” nomenclature. Thus it can handle at least to 6-31++G(3d2fg,3f2dp).

41
---
