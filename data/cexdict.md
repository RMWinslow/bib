---
title: Data Dictionary for the BLS CEX
description: "This page has a subset of the documentation for the Bureau of Labor Statistics' Consumer Expenditure Survey, placed into a simple list for ease of access and reference"
grand_parent: Other
parent: BLS CEX
layout:  post
search_exclude: true
toc: true
---

This page has a subset of the variables for the
Bureau of Labor Statistics'
Consumer Expenditure Survey, 
placed into a simple list for ease of access and reference

[The original Data Dictionary for the CEX can be found here](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwww.bls.gov%2Fcex%2Fpumd%2Fce_pumd_interview_diary_dictionary.xlsx&wdOrigin=BROWSELINK)
in Excel format.

The below is a list of variables found in the FMLI and MEMI data files as of 2021.


## Summary Files


### FMLI - Consumer Unit Level (Family Level) Interview


- AGE_REF : Age of reference person (Flag: AGE_REF_)
- AGE2 : Age of spouse (Flag: AGE2_)
- ALCBEVCQ : Alcoholic beverages this quarter
- ALCBEVPQ : Alcoholic beverages last quarter
- ALLFULCQ : Fuel oil and other fuels this quarter
- ALLFULPQ : Fuel oil and other fuels last quarter
- APPARCQ : Apparel and services this quarter
- APPARPQ : Apparel and services last quarter
- APTMENT : Does this unit have an apartment or guest house? (Flag: APTMENT_)
    - 04 : Apartment of Guest House
    - 09 : Apartment missing otherwise
    - 1 : Apartment included in structure
    - 2 : Apartment not included in structure
    - 4 : Apartment or Guest House
    - 9 : Apartment
- AS_COMP1 : Number of males age 16 and over in CU (Flag: AS_C_MP1)
- AS_COMP2 : Number of females age 16 and over in CU (Flag: AS_C_MP2)
- AS_COMP3 : Number of males age 2 through 15 in CU (Flag: AS_C_MP3)
- AS_COMP4 : Number of females age 2 through 15 in CU (Flag: AS_C_MP4)
- AS_COMP5 : Number of members under age 2 in CU (Flag: AS_C_MP5)
- BATHRMQ : Number of complete baths in this unit (Flag: BATHRMQ_)
- BBYDAYCQ : Babysitting and child day care this quarter
- BBYDAYPQ : Babysitting and child day care last quarter
- BEDROOMQ : Number of bedrooms in CU (Flag: BEDR_OMQ)
- BLS_URBN : Is this CU located in an urban or rural area
    - 1 : Urban
    - 2 : Rural
- BOYFIFCQ : Clothing for boys, 2 to 15 this quarter
- BOYFIFPQ : Clothing for boys, 2 to 15 last quarter
- BUILDING : Which of these descriptions from the list best describes this building? (Flag: BUIL_ING)
    - 01 : Single family detached (detached structure with only one primary residence, however, the structure could include a rental unit(s) in the basement, attic, etc.)
Between April 2013 and July 2015, the code 11 includes single family detached houses, college d
    - 02 : Row or townhouse inner unit (2, 3 or 4 story structure with 2 walls in common with other units and a private ground level entrance; it may have a rental unit as part of structure)
    - 03 : End row or end townhouse (one common wall)
    - 04 : Duplex (detached two unit structure with one common wall between the units)
    - 05 : 3-plex or 4-plex (3 or 4 unit structure with all units occupying the same level or levels)
    - 06 : Garden (a multi-unit structure, usually wider than it is high, having 2, 3, or possibly 4 floors; characteristically the units
not only have common walls but are also stacked on top of one another)
    - 07 : High-rise (a multi-unit structure which has 4 or more floors)
    - 08 : Apartment or flat (a unit not described above; could be located in the basement, attic, second floor or over the garage of
one of the units
    - 09 : Mobile home or trailer
    - 10 : College dormitory
Between April 2013 and July 2015, the code 11 includes single family detached houses, college dormitory, mobile home or trailer, as well as other rather than code 10 college dormitory.
    - 11 : Other - specify
Between April 2013 and July 2015, the code 11 includes also single family detached houses, college dormitory, mobile home or trailer in addition to other.
- BUILT : The year range that the property was built (Flag: BUILT_)
    - 01 : 1979 or later
    - 02 : 1978
    - 03 : 1977
    - 04 : 1976
    - 05 : 1975
    - 06 : 1970-1974
    - 07 : 1965-1969
    - 08 : 1960-1964
    - 09 : 1955-1959
    - 1 : 1990 or later
    - 10 : 1950-1954
    - 11 : 1940-1949
    - 12 : 1930-1939
    - 13 : 1920-1929
    - 14 : Before 1920
    - 15 : Don't Know
    - 16 : Before 1900
    - 2 : 1985-1989
    - 3 : 1980-1984
    - 4 : 1975-1979
    - 5 : 1970-1974
    - 6 : 1965-1969
    - 7 : 1960-1964
    - 8 : 1955-1959
    - 9 : 1950-1954
    - xx : Don't Know
- BUSCREEN : Has household had business expenses that could be reimbursed? (Flag: BUSC_EEN)
    - 1 : Yes
    - 2 : No
- CARTKNCQ : Cars and trucks, new (net outlay) this quarter
- CARTKNPQ : Cars and trucks, new (net outlay) last quarter
- CARTKUCQ : Cars and trucks, used (net outlay) this quarter
- CARTKUPQ : Cars and trucks, used (net outlay) last quarter
- CASHCOCQ : Cash contributions this quarter
- CASHCOPQ : Cash contributions last quarter
- CHILDAGE : Age of children of reference person (Flag: CHIL_AGE)
    - 0 : No children
    - 1 : Oldest child less than 6
    - 2 : Oldest child age 6-11 and at least one child less than 6
    - 3 : All children age 6-11
    - 4 : Oldest child age 12-17 and at least one child less than 12
    - 5 : All children age 12-17
    - 6 : Oldest child age great er than 17 and at least one child less than 17
    - 7 : All children age greater than 17
- CHLDRNCQ : Clothing for children under 2 this quarter
- CHLDRNPQ : Clothing for children under 2 last quarter
- CNTRALAC : Does this unit have a -- (Flag: CNTR_LAC)
    - 05 : Central Air conditioning
    - 12 : Central Air Conditioning
    - 5 : Central Air Conditioning
- CREDFINX : What was the total amount paid in finance, late charges, and interest for all cards in the last month? (Flag: CRED_INX)
- CREDITB : Could you tell me which range that best reflects the total amount owed on all major credit cards including store cards and gas cards? (Flag: CREDITB_)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- CREDITBX : Median of Bracket Range (Flag: CRED_TBX)
- CREDITX : What is the total amount owed on all cards? (Flag: CREDITX_)
- CREDTYRX : What was the total amount owed on all cards one year ago today? (Flag: CRED_YRX)
- CREDYR : Did you have any credit cards including store cards and gas cards one year ago today? (Flag: CREDYR_)
    - 1 : Yes
    - 2 : No
- CREDYRB : Could you tell me which range that best reflects the total amount owed on all major credit cards including store cards and gas cards ONE YEAR AGO TODAY? (Flag: CREDYRB_)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- CREDYRBX : Median of Bracket Range (Flag: CRED_RBX)
- CUID : CU sequence number which uniquely identifies CUs (Digits 1-7 of NEWID)
- CUTENURE : Housing tenure (Flag: CUTE_URE)
    - 1 : Homeowner w/ Mortgage
  TENURECU = '1' or '2' and MORT = '1'
    - 2 : Homeowner w/o Mortgage
  TENURECU = '1' or '2' and MORT = '2'
    - 3 : Owned mortgage NR:
    - 4 : Rented
    - 5 : Occupied w/o payment of cash rent:
    - 6 : Student housing
- DEFBENRP : Do you have a defined retirement plan, such as a pension, from an employer? (Flag: DEFB_NRP)
    - 1 : Yes
    - 2 : No
- DIRACC : Is access to the quarters direct or through another unit? (Flag: DIRACC_)
    - 1 : Direct access to living qtrs.
    - 2 : Access through another unit.
- DIVISION : Census Division
    - 1 : New England
    - 2 : Middle Atlantic
    - 3 : East North Central
    - 4 : West North Central
    - 5 : South Atlantic
    - 6 : East South Central
    - 7 : West South Central
    - 8 : Mountain
    - 9 : Pacific
- DMSXCCCQ : Domestic services excluding child care this quarter
- DMSXCCPQ : Domestic services excluding child care last quarter
- DOMSRVCQ : Domestic services this quarter
- DOMSRVPQ : Domestic services last quarter
- EARNCOMP : Composition of earners (Flag: EARN_OMP)
    - 1 : Reference Person only
    - 2 : Reference Person and Spouse only
    - 3 : Reference Person, Spouse and Others
    - 4 : Reference Person and Others
    - 5 : Spouse only
    - 6 : Spouse and Others
    - 7 : Others
    - 8 : No Earners
- ECARTKNC : Outlays for new vehicle purchases this quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount. 
870101 870102 870103 870104
- ECARTKNP : Outlays for new vehicle purchases last quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount.
870101 870102 870103 870104
- ECARTKUC : Outlays for used vehicle purchases this quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount. 
870201 870202 870203 870204
- ECARTKUP : Outlays for used vehicle purchases last quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount. 
870201 870202 870203 870204
- EDUC_REF : Education of reference person (Flag: EDUC0REF)
    - 0 : Never attended
    - 00 : Never attended
    - 1 : Elementary (1-8 yrs.)
    - 10 : 1st-8th grade
    - 11 : 9th-12th grade (No high school diploma)
    - 12 : High school graduate
    - 13 : Some college, no degree
    - 14 : Associate's degree in college
    - 15 : Bachelors degree
    - 16 : Masters degree
    - 17 : Professional/doctorate degree
    - 2 : High school (1-4 yrs.), less than H.S. grad.
    - 3 : High school graduate (4 yrs.)
    - 4 : College (1-4 yrs.), less than college grad.
    - 5 : College graduate (4 yrs.)
    - 6 : More than 4 yrs. of college
    - 7 : Never attended school
- EDUCA2 : What is the highest level of school the spouse has completed or the highest degree the member has received? (Flag: EDUCA2_)
    - 0 : Don't Know
    - 00 : Never attended
    - 1 : Elementary (1-8 yrs.)
    - 10 : 1st-8th grade
    - 11 : 9th-12th grade (No high school diploma)
    - 12 : High School graduate
    - 13 : Some college, no degree
    - 14 : Associate's degree in college
    - 15 : Bachelors degree
    - 16 : Masters degree
    - 17 : Professional/doctorate degree
    - 2 : High school (1-4 yrs.), less than H.S. grad.
    - 3 : High school graduate (4 yrs.)
    - 4 : College (1-4 yrs.), less than college grad.
    - 5 : College graduate (4 yrs.)
    - 6 : More than 4 yrs. of college
    - 7 : Never attended school
- EDUCACQ : Education current quarter
- EDUCAPQ : Education last quarter
- EENTMSCC : Miscellaneous entertainment outlays this quarter including photographic and sports equipment and boat and RV rentals.
- EENTMSCP : Miscellaneous entertainment outlays last quarter including photographic and sports equipment and boat and RV rentals.
- EENTRMTC : Total entertainment outlays this quarter including sound systems, sports equipment, toys, cameras, and down payments on boats and campers.
- EENTRMTP : Total entertainment outlays last quarter including sound systems, sports equipment, toys, cameras, and down payments on boats and campers.
- EHOUSNGC : Total housing outlays this quarter including maintenance, fuels, public services, household operations, house furnishings, and mortgage (lump sum home equity loan or line of credit home equity loan) principle and interest.
- EHOUSNGP : Total housing outlays last quarter including maintenance, fuels, public services, household operations, house furnishings, and mortgage (lump sum home equity loan or line of credit home equity loan) principle and interest.
- ELCTRCCQ : Electricity this quarter
- ELCTRCPQ : Electricity last quarter
- EMISCELC : Miscellaneous outlays this quarter including reduction of mortgage principal (lump sum home equity loan) on other property.
- EMISCELP : Miscellaneous outlays last quarter including reduction of mortgage principal (lump sum home equity loan) on other property.
- EMISCMTC : Mortgage principal outlays this quarter for other property.
- EMISCMTP : Mortgage principal outlays last quarter for other property.
- EMOTRVHC : Outlays for motored recreational vehicles this quarter.
- EMOTRVHP : Outlays for motored recreational vehicles last quarter.
- EMRTPNOC : Mortgage principal outlays this quarter for owned home.
- EMRTPNOP : Mortgage principal outlays last quarter for owned home.
- EMRTPNVC : Mortgage principal outlays this quarter for owned vacation home.
- EMRTPNVP : Mortgage principal outlays last quarter for owned vacation home.
- ENOMOTRC : Outlays for non-motored recreational vehicles this quarter.
- ENOMOTRP : Outlays for non-motored recreational vehicles last quarter.
- ENTERTCQ : Entertainment this quarter
- ENTERTPQ : Entertainment last quarter
- EOTHENTC : Outlays for other entertainment supplies this quarter, equipment, and services including down payments on boats and campers.
- EOTHENTP : Outlays for other entertainment supplies last quarter, equipment, and services including down payments on boats and campers.
- EOTHLODC : Outlays for other lodging this quarter such as owned vacation home, including mortgage principal and interest, property taxes, maintenance, insurance, and other expenses.
- EOTHLODP : Outlays for other lodging last quarter such as owned vacation home, including mortgage principal and interest, property taxes, maintenance, insurance, and other expenses.
- EOTHVEHC : Outlays for other vehicle purchases this quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount.
- EOTHVEHP : Outlays for other vehicle purchases last quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount.
- EOWNDWLC : Owned home outlays this quarter including mortgage principal and interest, property taxes, maintenance, insurance, and other expenses.
- EOWNDWLP : Owned home outlays last quarter including mortgage principal and interest, property taxes, maintenance, insurance, and other expenses.
- ERANKH : Complete income reporters of the total population are ranked in ascending order according to the level of total expenditures. Total expenditures is based on ERANKMTH. The value is a number between 0 and 1. (Flag: ERANKH_)
- ERANKHM : Weighted cumulative percent expenditure outlay ranking of CU to total population. Expenditure outlay is based on ERNKMTHM. The value is a number between 0 and 1. (Flag: ERANKHM_)
- ESHELTRC : Shelter outlays this quarter including mortgage principle and interest for owned home and/or vacation home, rents, insurance, taxes, and maintenance.
- ESHELTRP : Shelter outlays last quarter including mortgage principle and interest for owned home and/or vacation home, rents, insurance, taxes, and maintenance.
- ETOTACX4 : Adjusted total outlays last quarter, sum of outlays from all major expenditure categories.
- ETOTALC : Total outlays this quarter, sum of outlays from all major expenditure categories.
- ETOTALP : Total outlays last quarter, sum of outlays from all major expenditure categories.
- ETOTAPX4 : Adjusted total outlays last quarter, sum of outlays from all major expenditure categories.
- ETRANPTC : Total outlays for transportation this quarter including down payment, principal and finance charges paid on loans, gasoline and motor oil, maintenance and repairs, insurance, public and other transportation, and vehicle rental licenses and other charges.
- ETRANPTP : Total outlays for transportation last quarter including down payment, principal and finance charges paid on loans, gasoline and motor oil, maintenance and repairs, insurance, public and other transportation, and vehicle rental licenses and other charges.
- EVEHPURC : Outlays for vehicle purchases this quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount.
- EVEHPURP : Outlays for vehicle purchases last quarter including down payment, principal and interest paid on loans, or if not financed, purchase amount.
- FAM_SIZE : Number of Members in CU (Flag: FAM__IZE)
- FAM_TYPE : Family Type is based on the relationship of members to reference person, whom physically occupy the address selected for the survey. "Own" children are sons and daughters children including step children and adopted (Flag: FAM__YPE)
    - 1 : Married couple only
    - 2 : Married couple, own children only, oldest child < 6
    - 3 : Married couple, own children only,  oldest child > 6, < 18
    - 4 : Married couple, own children only, oldest child > 17
    - 5 : All other Married couple families
    - 6 : One parent, male, own children at least one age < 18
    - 7 : One parent, female, own children, at least one age < 18_x000D_
    - 8 : Single consumers
    - 9 : Other families
- FDAWAYCQ : Food away from home this quarter
- FDAWAYPQ : Food away from home last quarter
- FDHOMECQ : Food at home this quarter
- FDHOMEPQ : Food at home this quarter
- FDMAPCQ : Meals as pay this quarter
- FDMAPPQ : Meals as pay last quarter
- FDXMAPCQ : Food away excluding meals as pay this quarter
- FDXMAPPQ : Food away excluding meals as pay last quarter
- FEEADMCQ : Fees and admissions this quarter
- FEEADMPQ : Fees and admissions last quarter
- FFTAXOWE : Weighted estimate for Federal tax liabilities for entire CU (Flag: FFTA_OWE)
- fftaxowe : Weighted estimate for Federal tax liabilities at the Tax Unit Level (Flag: FFTA_OWE)
- FGOVRETM : Total amount of government retirement deducted from last pay annualized (Flag: FGOV_ETM)
- FGOVRETX : Total amount of government retirement deducted from last pay annualized (Flag: FGOV_ETX)
- FINATXE1 : Imputed Income After Tax #1
- FINATXE2 : Imputed Income After Tax #2
- FINATXE3 : Imputed Income After Tax #3
- FINATXE4 : Imputed Income After Tax #4
- FINATXE5 : Imputed Income After Tax #5
- FINATXEM : Total amount of family income after estimated taxes in the last 12 months (Imputed or collected data) (Flag: FINAT_EM)
- FINCBTAX : Total amount of family income before taxes in the last 12 months (Collected data) (Flag: FINCBT_X)
- FINCBTX1 : Imputation Iteration #1 - FINCBTAX
- FINCBTX2 : Imputation Iteration #2 - FINCBTAX
- FINCBTX3 : Imputation Iteration #3 - FINCBTAX
- FINCBTX4 : Imputation Iteration #4 - FINCBTAX
- FINCBTX5 : Imputation Iteration #5 - FINCBTAX
- FINCBTXI : Indicator/descriptor variable for income imputation.
- FINCBTXM : Total amount of family income before taxes (Imputed or collected data) (Flag: FINCB_XM)
- FINDRETX : Amount of money placed in a Self-employed retirement plan in past year for all CU members (Flag: FIND_ETX)
- FINLWT21 : Calibration final weight for the full sample
- FJSSDED1 : Imputation Iteration #1 - FJSSDEDX
- FJSSDED2 : Imputation Iteration #2 - FJSSDEDX
- FJSSDED3 : Imputation Iteration #3 - FJSSDEDX
- FJSSDED4 : Imputation Iteration #4 - FJSSDEDX
- FJSSDED5 : Imputation Iteration #5 - FJSSDEDX
- FJSSDEDM : Portion of family income paid to Social Security during the past 12 months, mean of imputation iterations. (Flag: FJSS_EDM)
- FJSSDEDX : Portion of family income paid to Social Security during the past 12 months (Flag: FJSS_EDX)
- FLRCVRCQ : Floor coverings this quarter
- FLRCVRPQ : Floor coverings last quarter
- FMLPYYRX : Annual value of free meals received as part of pay (Flag: FMLP_YRX)
- FOODCQ : Total food this quarter
- FOODPQ : Total food last quarter
- FOOTWRCQ : Footwear this quarter
- FOOTWRPQ : Footwear last quarter
- FPRIPENM : Total amount of private pensions (Flag: FPRI_ENM)
- FPRIPENX : Total amount of private pensions (Flag: FPRI_ENX)
- FRRDEDM : Total amount of Railroad Retirement deducted from last pay annualized (Flag: FRRDEDM_)
- FRRDEDX : Total amount of Railroad Retirement deducted from last pay annualized (Flag: FRRDEDX_)
- FRRETIR1 : Imputation Iteration #1 - FRRETIRX
- FRRETIR2 : Imputation Iteration #2 - FRRETIRX
- FRRETIR3 : Imputation Iteration #3 - FRRETIRX
- FRRETIR4 : Imputation Iteration #4 - FRRETIRX
- FRRETIR5 : Imputation Iteration #5 - FRRETIRX
- FRRETIRI : Indicator/descriptor variable for income imputation.
- FRRETIRM : Total amount of received from Social Security benefits and Railroad benefit checks prior to deductions for medical insurance and Medicare, mean of imputation iterations (Flag: FRRE_IRM)
- FRRETIRX : Total amount received from Social Security benefits and Railroad Benefit checks prior to deductions for medical insurance and Medicare (Flag: FRRE_IRX)
- FS_AMTX1 : Imputation Iteration #1 - FS_AMTX
- FS_AMTX2 : Imputation Iteration #2 - FS_AMTX
- FS_AMTX3 : Imputation Iteration #3 - FS_AMTX
- FS_AMTX4 : Imputation Iteration #4 - FS_AMTX
- FS_AMTX5 : Imputation Iteration #5 - FS_AMTX
- FS_AMTXI : Indicator/descriptor variable for income imputation.
- FS_AMTXM : What was the dollar value of the last food stamps or EBT received (based on mean of imputation iterations)?
- FS_MTHI : In how many of the past 12 months were food stamps or EBTs received? (Flag: FS_MTHI_)
- FSALARY1 : Imputation Iteration #1 - FSALARYX
- FSALARY2 : Imputation Iteration #2 - FSALARYX
- FSALARY3 : Imputation Iteration #3 - FSALARYX
- FSALARY4 : Imputation Iteration #4 - FSALARYX
- FSALARY5 : Imputation Iteration #5 - FSALARYX
- FSALARYI : Indicator/descriptor variable for income imputation.
- FSALARYM : Total amount of income received from salary or wages before deduction by family grouping, mean of imputation iterations (Flag: FSAL_RYM)
- FSALARYX : Total amount of income received from salary or wages before deduction by family grouping (Flag: FSAL_RYX)
- FSMPFRMX : Total income received from self-employment income before deduction by family grouping (Flag: FSMP_RMX)
- FSMPFRX1 : Imputation Iteration #1 - FSMPFRMX
- FSMPFRX2 : Imputation Iteration #2 - FSMPFRMX
- FSMPFRX3 : Imputation Iteration #3 - FSMPFRMX
- FSMPFRX4 : Imputation Iteration #4 - FSMPFRMX
- FSMPFRX5 : Imputation Iteration #5 - FSMPFRMX
- FSMPFRXI : Indicator/descriptor variable for income imputation.
- FSMPFRXM : Total amount of income received from self-employment income by family grouping, mean of imputation iterations (Flag: FSMP_RXM)
- FSSIX : Amount of Supplemental Security Income from all sources received by all CU members in past 12 months (sum SSIX + SSIBX from MEMB file for all CU members) (Flag: FSSIX_)
- FSSIX1 : Imputation Iteration #1 - FSSIX
- FSSIX2 : Imputation Iteration #2 - FSSIX
- FSSIX3 : Imputation Iteration #3 - FSSIX
- FSSIX4 : Imputation Iteration #4 - FSSIX
- FSSIX5 : Imputation Iteration #5 - FSSIX
- FSSIXI : Indicator/descriptor variable for income imputation.
- FSSIXM : Total amount received in supplemental security income checks combined, mean of imputation iterations (Flag: FSSIXM_)
- FSTAXOWE : Weighted estimate for State tax liabilities for entire CU (Flag: FSTA_OWE)
- fstaxowe : Weighted estimate for State tax liabilities for entire CU (Flag: FSTA_OWE)
- FULOILCQ : Fuel oil this quarter
- FULOILPQ : Fuel oil last quarter
- FURNTRCQ : Furniture this quarter
- FURNTRPQ : Furniture last quarter
- GASMOCQ : Gasoline and motor oil this quarter
- GASMOPQ : Gasoline and motor oil last quarter
- GRLFIFCQ : Clothing for girls, 2 to 15 this quarter
- GRLFIFPQ : Clothing for girls, 2 to 15 this quarter
- HEALTHCQ : Health care this quarter
- HEALTHPQ : Health care last quarter
- HH_CU_Q : Count of Consumer Units in this household (Flag: HH_CU_Q_)
- HHID : Identifier for household with more than one CU. Household with only one CU will be set to missing. (Flag: HHID_)
- HIGH_EDU : Highest level of education within the CU.
    - 0 : Never attended
    - 00 : Never attended
    - 10 : 1st-8th grade
    - 11 : 9th-12th grade (No high school diploma)
    - 12 : HS graduate
    - 13 : Some college, no degree
    - 14 : AA degree
    - 15 : Bachelors degree
    - 16 : Masters degree
    - 17 : Professional/doctorate degree
- HISP_REF : Hispanic origin of reference person
    - 1 : Hispanic
    - 2 : Non-Hispanic
- HISP2 : Hispanic origin of spouse
    - 1 : Hispanic
    - 2 : Non-Hispanic
- HLFBATHQ : Number of half baths in this unit (Flag: HLFB_THQ)
- HLTHINCQ : Health insurance this quarter
- HLTHINPQ : Health insurance last quarter
- HORREF1 : Hispanic Origin of the Reference Person (Flag: HORREF1_)
    - 1 : Mexican
    - 2 : Mexican-American
    - 3 : Chicano
    - 4 : Puerto Rican
    - 5 : Cuban
    - 6 : Other groups not listed
- HORREF2 : Hispanic Origin of the spouse (Flag: HORREF2_)
    - 1 : Mexican
    - 2 : Mexican-American
    - 3 : Chicano
    - 4 : Puerto Rican
    - 5 : Cuban
    - 6 : Other groups not listed
- HOUSCQ : Housing this quarter
- HOUSEQCQ : House furnishings and equipment this quarter
- HOUSEQPQ : House furnishings and equipment last quarter
- HOUSOPCQ : Household operations this quarter
- HOUSOPPQ : Household operations last quarter
- HOUSPQ : Housing last quarter
- INC_HRS2 : Number of hours usually worked per week by spouse (Flag: INC__RS2)
- INC_RANK : Weighted cumulative percent ranking based on total current income before taxes (Flag: INC__ANK)
- INC_RNK1 : Imputation Iteration #1 - INC_RANK
- INC_RNK2 : Imputation Iteration #2 - INC_RANK
- INC_RNK3 : Imputation Iteration #3 - INC_RANK
- INC_RNK4 : Imputation Iteration #4 - INC_RANK
- INC_RNK5 : Imputation Iteration #5 - INC_RANK
- INC_RNKM : Weighted cumulative percent ranking based on total current income, based on mean of imputation iterations (Flag: INC__NKM)
- INCLASS2 : Income classification based on INC_RANK (Flag: INCL_SS2)
    - 1 : Less than .1667
    - 2 : .1667 - .3333
    - 3 : .3334 - .4999
    - 4 : .5000 - .6666
    - 5 : .6667 - .8333
    - 6 : .8334 - 1.0000
    - 7 : Incomplete reporting
- INCNONW1 : Reason reference person did not work during the past 12 months (Flag: INCN_NW1)
    - 1 : Retired
    - 2 : Taking care of home/CU
    - 3 : Going to school
    - 4 : Ill, disabled, unable to work
    - 5 : Unable to find work
    - 6 : Doing something else
- INCNONW2 : Reason spouse did not work during the past 12 months (Flag: INCN_NW2)
    - 1 : Retired
    - 2 : Taking care of home/CU
    - 3 : Going to school
    - 4 : Ill, disabled, unable to work
    - 5 : Unable to find work
    - 6 : Doing something else
- INCOMEY1 : Employer from which reference person received the most earnings in past 12 months (Flag: INCO_EY1)
    - 1 : Private company, business or individual
    - 2 : Federal government
    - 3 : State government
    - 4 : Local government
    - 5 : Self-employed in own business, professional practice or farm
    - 6 : Family business or farm, working without pay
- INCOMEY2 : Employer from which spouse received most earnings during the past 12 months (Flag: INCO_EY2)
    - 1 : Private company, business or individual
    - 2 : Federal government
    - 3 : State government
    - 4 : Local government
    - 5 : Self-employed in own business, professional practice or farm
    - 6 : Family business or farm, working without pay
- INCWEEK1 : Number of weeks worked by reference person full or part time in last 12 months, including paid vacation and paid sick leave (Flag: INCW_EK1)
- INCWEEK2 : Number of weeks worked by spouse full or part time in last 12 months, including paid vacation and paid sick leave (Flag: INCW_EK2)
- INTERI : Interview number
- INTRDVB : Range that best reflects the amount you received in interest or dividends during the past 12 months (Flag: INTRDVB_)
    - 01 : $0-$999
    - 02 : $1,000-$1,999
    - 03 : $2,000-$2,999
    - 04 : $3,000-$3,999
    - 05 : $4,000-$4,999
    - 06 : $5,000-$9,999
    - 07 : $10,000-$14,999
    - 08 : $15,000-$19,999
    - 09 : $20,000-$29,999
    - 10 : $30,000-$39,999
    - 11 : $40,000-$49,999
    - 12 : $50,000 and over
- INTRDVBX : Median of Bracket Range (Flag: INTR_VBX)
- INTRDVX : Amount of income received from interest and dividends (Flag: INTRDVX_)
- INTRDVX1 : Imputation Iteration #1 - INTRDIVX
- INTRDVX2 : Imputation Iteration #2 - INTRDIVX
- INTRDVX3 : Imputation Iteration #3 - INTRDIVX
- INTRDVX4 : Imputation Iteration #4 - INTRDIVX
- INTRDVX5 : Imputation Iteration #5 - INTRDIVX
- INTRDVXI : Indicator/descriptor variable for income imputation.
- INTRDVXM : Amount of income received from interest and dividends, mean of the iterations (Flag: INTR_VXM)
- IRA : Do you have any retirement accounts such as 401(k0s, IRAS, Thrift Saving Plans? (Flag: IRA_)
    - 1 : Yes
    - 2 : No
- IRAB : Could you tell me which range that best reflects the total value of all retirement accounts such as 401(k)s, IRAs, and Thrift Savings Plans? (Flag: IRAB_)
    - 1 : $0 - $1999
    - 2 : $2,000 - $9,999
    - 3 : $10,000 - $49,999
    - 4 : $50,000 - $199,999
    - 5 : $200,000 - $449,999
    - 6 : $450,000 and over
- IRABX : Median of Bracket Range (Flag: IRABX_)
- IRAX : As of today, what is the total value of all retirement accounts, such as 401(k)s, IRAs, and Thrift Savings Plans that you own? (Flag: IRAX_)
- IRAYR : Did you have any retirement accounts such as 401(k)s, IRAs, Thrift Savings Plans ONE YEAR AGO TODAY? (Flag: IRAYR_)
    - 1 : Yes
    - 2 : No
- IRAYRB : Range which best reflects the total value of all retirement accounts one year ago today (Flag: IRAYRB_)
    - 1 : $0 - $1999
    - 2 : $2,000 - $9,999
    - 3 : $10,000 - $49,999
    - 4 : $50,000 - $199,999
    - 5 : $200,000 - $449,999
    - 6 : $450,000 and over
- IRAYRBX : Median of Bracket Range (Flag: IRAYRBX_)
- IRAYRX : What was the total value of all retirement accounts one year ago today? (Flag: IRAYRX_)
- JFS_AMT : Annual value of food stamps (Flag: JFS_AMT_)
- JFS_AMT1 : Imputation Iteration #1 - JFS_AMT
- JFS_AMT2 : Imputation Iteration #2 - JFS_AMT
- JFS_AMT3 : Imputation Iteration #3 - JFS_AMT
- JFS_AMT4 : Imputation Iteration #4 - JFS_AMT
- JFS_AMT5 : Imputation Iteration #5 - JFS_AMT
- JFS_AMTM : Annual value of food stamps, mean of imputation iterations.
- LIFINSCQ : Life and other personal insurance this quarter
- LIFINSPQ : Life and other personal insurance last quarter
- LIQDYRBX : Median of Bracket Range (Flag: LIQD_RBX)
- LIQUDYR : Did you have any checking savings money market accounts, or certificates of deposit or CDs one year ago? (Flag: LIQUDYR_)
    - 1 : Yes
    - 2 : No
- LIQUDYRB : Could you tell me which range that best reflects the total value of all checking, savings, money market accounts, and certificates of deposit or CDs ONE YEAR AGO TODAY? (Flag: LIQU_YRB)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- LIQUDYRX : What was the total value of all checking, savings, money market accounts, and certificated of deposit or CDs one year ago today? (Flag: LIQU_YRX)
- LIQUID : Do you have any checking, saving, money market accounts, or certificates of deposit or CDs? (Flag: LIQUID_)
    - 1 : Yes
    - 2 : No
- LIQUIDB : Could you tell me which range best reflects the total value of checking, savings, money market accounts, certificates of deposit or cds? (Flag: LIQUIDB_)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- LIQUIDBX : Median of Bracket Range (Flag: LIQU_DBX)
- LIQUIDX : As of today, what is the total value of all checking, savings, money market accounts, and certificated of deposit or CDs you have? (Flag: LIQUIDX_)
- LMPSUMBX : Median of bracket range (Flag: LMPS_MBX)
- LUMPSUMB : Range that best reflects the total lump sum payments from insurance, estates, trusts, royalties, alimony, prizes or games of chance, or from persons outside your CU received during the last twelve months (Flag: LUMP_UMB)
    - 01 : $0-$999
    - 02 : $1,000 - $1,999
    - 03 : $2,000 - $2,999
    - 04 : $3,000 - $3,999
    - 05 : $4,000 - $4,999
    - 06 : $5,000 - $9,999
    - 07 : $10,000 - $14,999
    - 08 : $15,000 - $19,999
    - 09 : $20,000 - $29,999
    - 10 : $30,000 - $39,999
    - 11 : $40,000 - $49,999
    - 12 : $50,000 and over
- LUMPSUMX : Amount of lump sum payments from estates, trusts, royalties, alimony, prizes, or games of chance or from persons outside CU (Flag: LUMP_UMX)
- MAINRPCQ : Maintenance and repairs this quarter
- MAINRPPQ : Maintenance and repairs last quarter
- MAJAPPCQ : Major appliances this quarter
- MAJAPPPQ : Major appliances last quarter
- MARITAL1 : Marital status of reference person (Flag: MARI_AL1)
    - 1 : Married
    - 2 : Widowed
    - 3 : Divorced
    - 4 : Separated
    - 5 : Never married
- MEALSPAY : Have you received any free meals at work as part of your pay? (Flag: MEAL_PAY)
    - 1 : Yes
    - 2 : No
- MEDSRVCQ : Medical services this quarter
- MEDSRVPQ : Medical services last quarter
- MEDSUPCQ : Medical supplies this quarter
- MEDSUPPQ : Medical supplies last quarter
- MENBOYCQ : Clothing for men and boys this quarter
- MENBOYPQ : Clothing for men and boys last quarter
- MENSIXCQ : Clothing for men, 16 and over this quarter
- MENSIXPQ : Clothing for men, 16 and over last quarter
- MISC1CQ : Miscellaneous expenditures this quarter
- MISC1PQ : Miscellaneous expenditures last quarter
- MISC2CQ : Miscellaneous expenditures this quarter
- MISC2PQ : Miscellaneous expenditures last quarter
- MISCCQ : Miscellaneous expenditures this quarter
- MISCEQCQ : Miscellaneous household equipment this quarter
- MISCEQPQ : Miscellaneous household equipment last quarter
- MISCPQ : Miscellaneous expenditures last quarter
- MISCTAXX : Amount of other taxes paid which were not reported elsewhere during past 12 months (Flag: MISC_AXX)
- MISCX4CQ : Adjusted miscellaneous expenditures this quarter (To be used for population estimates - see information under Summary Expenditure Data heading.) 
MISC1CQ + (4*MISC2CQ)
- MISCX4PQ : Adjusted miscellaneous expenditures last quarter (To be used for population estimates
- MLPAYWKX : About what was the weekly dollar value of these meals? (Flag: MLPA_WKX)
- MLPYQWKS : For how many weeks did members of your household receive these meals during the past 12 months? (Flag: MLPY_WKS)
- MRPINSCQ : Maintenance, repairs, insurance, and other expenses this quarter
- MRPINSPQ : Maintenance, repairs, insurance, and other expenses last quarter
- MRTINTCQ : Mortgage interest this quarter
- MRTINTPQ : Mortgage interest last quarter
- MRTPRNOC : Outlays on owned vacation home mortgage principle this quarter
- MRTPRNOP : Outlays on owned vacation home mortgage principle last quarter
- NETRENT1 : Imputation Iteration #1 - NETRENTX
- NETRENT2 : Imputation Iteration #2 - NETRENTX
- NETRENT3 : Imputation Iteration #3 - NETRENTX
- NETRENT4 : Imputation Iteration #4 - NETRENTX
- NETRENT5 : Imputation Iteration #5 - NETRENTX
- NETRENTB : Range that best reflects the total net rental income or loss during the past 12 months (Flag: NETR_NTB)
    - 00 : Loss
    - 01 : $0-$999
    - 02 : $1,000-$1,999
    - 03 : $2,000-$2,999
    - 04 : $3,000-$3,999
    - 05 : $4,000-$4,999
    - 06 : $5,000-$9,999
    - 07 : $10,000-$14,999
    - 08 : $15,000-$19,999
    - 09 : $20,000-$29,999
    - 10 : $30,000-$39,999
    - 11 : $40,000-$49,999
    - 12 : $50,000 and over
- NETRENTI : Indicator/descriptor variable for income imputation.
- NETRENTM : Amount of income received from net rental income or loss, mean of the iterations (Flag: NETR_NTM)
- NETRENTX : What was the amount of net rental income or loss? (Flag: NETR_NTX)
- NETRNTBX : Median of Bracket Range (Flag: NETR_TBX)
- NEWID : Public use microdata identifier
- NO_EARNR : Number of CU members reported as income earners (Flag: NO_E_RNR)
- NONINCMX : Total amount of family income other than money receipts before taxes (Flag: NONI_CMX)
- NTLGASCQ : Natural gas this quarter
- NTLGASPQ : Natural gas last quarter
- NUM_AUTO : Total number of owned cars (Flag: NUM__UTO)
- NUM_TVAN : Total number of owned trucks and vans (Flag: NUM__VAN)
- OCCUCOD1 : The job in which reference person received the most earnings during the past 12 months (Flag: OCCU_OD1)
    - 01 : Manager, Professional Administrator
    - 02 : Teacher
    - 03 : Professional
    - 04 : Administrative support, including clerical
    - 05 : Sales, retail
    - 06 : Sales, business goods, and services
    - 07 : Technician Service
    - 08 : Protective Service
    - 09 : Private household service
    - 10 : Other Service
    - 11 : Machine Operator, assembler, inspector
    - 12 : Transportation operator
    - 13 : Handler, helper, laborer
    - 14 : Mechanic, repairer, precision production
    - 15 : Construction, mining
    - 16 : Farming
    - 17 : Forestry, fishing, groundskeeping
    - 18 : Armed Forces
- OCCUCOD2 : The job in which reference person received the most earnings during the past 12 months (Flag: OCCU_OD2)
    - 01 : Manager, Professional Administrator
    - 02 : Teacher
    - 03 : Professional
    - 04 : Administrative support, including clerical
    - 05 : Sales, retail
    - 06 : Sales, business goods, and services
    - 07 : Technician Service
    - 08 : Protective Service
    - 09 : Private household service
    - 10 : Other Service
    - 11 : Machine Operator, assembler, inspector
    - 12 : Transportation operator
    - 13 : Handler, helper, laborer
    - 14 : Mechanic, repairer, precision production
    - 15 : Construction, mining
    - 16 : Farming
    - 17 : Forestry, fishing, groundskeeping
    - 18 : Armed Forces
- OFSTPARK : See SWIMPOOL for question and source. (Flag: OFST_ARK)
    - 02 : Off Street Parking
    - 10 : Off Street Parking
- OTHAPLCQ : OTHAPLCQ Other apparel products and services this quarter
- OTHAPLPQ : OTHAPLPQ Other apparel products and services last quarter
- OTHASTB : Range which best reflects the total value of these other financial assets (Flag: OTHASTB_)
    - 1 : $0 - $1999
    - 2 : $2,000 - $9,999
    - 3 : $10,000 - $49,999
    - 4 : $50,000 - $199,999
    - 5 : $200,000 - $449,999
    - 6 : $450,000 and over
- OTHASTBX : Median of Bracket Edit (Flag: OTHA_TBX)
- OTHASTX : As of today, what is the total value of these other financial assets? (Flag: OTHASTX_)
- OTHENTCQ : Other entertainment this quarter
- OTHENTPQ : Other entertainment last quarter
- OTHEQPCQ : Other equipment and services this quarter
- OTHEQPPQ : Other equipment and services last quarter
- OTHFINX : What was the total amount paid in finance, late charges, and interest for all other loans in the last month? (Flag: OTHFINX_)
- OTHFLSCQ : Other fuels this quarter
- OTHFLSPQ : Other fuels last quarter
- OTHHEXCQ : Other household expenses this quarter
- OTHHEXPQ : Other household expenses last quarter
- OTHLNYR : Did you have any other debt such as medical loans or personal loans one year ago today? (Flag: OTHLNYR_)
    - 1 : Yes
    - 2 : No
- OTHLNYRB : Range which best reflects the total amount owed on all other loans one year ago today (Flag: OTHL_YRB)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- OTHLNYRX : What was the total amount owed on all other loans one year ago today? (Flag: OTHL_YRX)
- OTHLOAN : As of today, do you have any other debt such as medical loans or personal loans? (Flag: OTHLOAN_)
    - 1 : Yes
    - 2 : No
- OTHLODCQ : Other lodging this quarter
- OTHLODPQ : Other lodging last quarter
- OTHLONB : Range which best reflects the total amount owed on all other loans (Flag: OTHLONB_)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- OTHLONBX : Median of Bracket Range (Flag: OTHL_NBX)
- OTHLONX : What is the total amount owed on all other loans? (Flag: OTHLONX_)
- OTHLYRBX : Median of Bracket Range (Flag: OTHL_RBX)
- OTHREGB : Range which best reflects the total amount received in Veteran's Administration (VA) payments, unemployment compensation, child support, or alimony during the past 12 months (Flag: OTHREGB_)
    - 01 : $0-$999
    - 02 : $1,000-$1,999
    - 03 : $2,000-$2,999
    - 04 : $3,000-$3,999
    - 05 : $4,000-$4,999
    - 06 : $5,000-$9,999
    - 07 : $10,000-$14,999
    - 08 : $15,000-$19,999
    - 09 : $20,000-$29,999
    - 10 : $30,000-$39,999
    - 11 : $40,000-$49,999
    - 12 : $50,000 and over
- OTHREGBX : Median of Bracket Range (Flag: OTHR_GBX)
- OTHREGX : Amount of income received from any other source such as Veteran’s Administration (VA) payments, unemployment compensation, child support, or alimony (Flag: OTHREGX_)
- OTHREGX1 : Imputation Iteration #1 - OTHREGX
- OTHREGX2 : Imputation Iteration #2 - OTHREGX
- OTHREGX3 : Imputation Iteration #3 - OTHREGX
- OTHREGX4 : Imputation Iteration #4 - OTHREGX
- OTHREGX5 : Imputation Iteration #5 - OTHREGX
- OTHREGXI : Indicator/descriptor variable for income imputation.
- OTHREGXM : Amount of income received from any other source such as Veteran’s Administration (VA) payments, unemployment compensation, child support, or alimony, mean of the iterations (Flag: OTHR_GXM)
- OTHRINC1 : Imputation Iteration #1 - OTHRINCX
- OTHRINC2 : Imputation Iteration #2 - OTHRINCX
- OTHRINC3 : Imputation Iteration #3 - OTHRINCX
- OTHRINC4 : Imputation Iteration #4 - OTHRINCX
- OTHRINC5 : Imputation Iteration #5 - OTHRINCX
- OTHRINCB : Range that best reflects the total amount of other money income received during the last twelve months (Flag: OTHR_NCB)
    - 01 : $0-$999
    - 02 : $1,000 - $1,999
    - 03 : $2,000 - $2,999
    - 04 : $3,000 - $3,999
    - 05 : $4,000 - $4,999
    - 06 : $5,000 - $9,999
    - 07 : $10,000 - $14,999
    - 08 : $15,000 - $19,999
    - 09 : $20,000 - $29,999
    - 10 : $30,000 - $39,999
    - 11 : $40,000 - $49,999
    - 12 : $50,000 and over
- OTHRINCI : Indicator/descriptor variable for income imputation.
- OTHRINCM : Amount received in other money income including money received from care of foster children, mean of imputation iterations. (Flag: OTHR_NCM)
- OTHRINCX : Amount received in other money income including money received from care of foster children, cash scholarships and fellowships, or stipends not based on working (Flag: OTHR_NCX)
- OTHSTYR : Did you have any other financial assets, such as annuities, trusts, and royalties on year ago today? (Flag: OTHSTYR_)
    - 1 : Yes
    - 2 : No
- OTHSTYRB : Range which best reflects the total value of these other financial assets one year ago today. (Flag: OTHS_YRB)
    - 1 : $0 - $1999
    - 2 : $2,000 - $9,999
    - 3 : $10,000 - $49,999
    - 4 : $50,000 - $199,999
    - 5 : $200,000 - $449,999
    - 6 : $450,000 and over
- OTHSTYRX : What was the value of these other financial assets one year ago today? (Flag: OTHS_YRX)
- OTHSYRBX : Median of Bracket Range (Flag: OTHS_RBX)
- OTHVEHCQ : Other vehicles this quarter
- OTHVEHPQ : Other vehicles last quarter
- OTRINCBX : Median of bracket range (Flag: OTRI_CBX)
- OWNDWECQ : Owned dwellings this quarter
- OWNDWEPQ : Owned dwellings last quarter
- OWNVACC : Expenditures on owned vacation homes this quarter including mortgage interest, insurance, taxes, maintenance, and
miscellaneous household equipment
 VOTHRLOP+VMISCHEP

This variable includes expenditures related to vacation homes. Because these types of e
- OWNVACP : Expenditures on owned vacation homes last quarter including mortgage interest, insurance, taxes, maintenance, and
miscellaneous household equipment
 VOTHRLOP+VMISCHEP

This variable includes expenditures related to vacation homes. Because these types of e
- PERINSCQ : heading prior to this list of variables. Personal insurance and pensions this quarter
- PERINSPQ : heading prior to this list of variables. Personal insurance and pensions last quarter
- PERSCACQ : Personal care this quarter
- PERSCAPQ : Personal care last quarter
- PERSLT18 : # of CU Members less than 18 AGE < 18 (Flag: PERS_T18)
- PERSOT64 : Number of persons over 64 SUM OF MEMBERS WHERE AGE > 64 BY CU (Flag: PERS_T64)
- PETTOYCQ : Pets, toys, and playground equipment this quarter
- PETTOYPQ : Pets, toys, and playground equipment last quarter
- POPSIZE : Population size of the PSU
    - 1 : More than 4 million
    - 2 : 1.20-4 million
    - 3 : 0.33-1.19 million
    - 4 : 125 - 329.9 thousand
    - 5 : Less than 125 thousand
    - 6 : Suppressed
- PORCH : Does this unit have a porch (Flag: PORCH_)
    - 03 : Porch, terrace, patio, or balcony
- PREDRGCQ : Prescription drugs this quarter
- PREDRGPQ : Prescription drugs last quarter
- PRINEARN : Principal Earner (Flag: PRIN_ARN)
- PRINERN1 : Imputation Iteration #1 - PRINEARN
- PRINERN2 : Imputation Iteration #2 - PRINEARN
- PRINERN3 : Imputation Iteration #3 - PRINEARN
- PRINERN4 : Imputation Iteration #4 - PRINEARN
- PRINERN5 : Imputation Iteration #5 - PRINEARN
- PRINERNM : Principal Earner based on mean imputed income. (Flag: PRIN_RNM)
- PROPTXCQ : Property taxes this quarter
- PROPTXPQ : Property taxes last quarter
- PSU : Primary Sampling Unit
    - 1102 : Philadelphia – Wilmington – Atlantic City, PA – NJ – DE - MD
    - 1103 : Boston – Brockton – Nashua, MA – NH – ME CT
    - 1109 : New York, NY
    - 1110 : New York, Connecticut suburbs
    - 1111 : New Jersey suburbs
    - 1207 : Chicago – Gary – Kenosha, IL – IN - WI
    - 1208 : Detroit – Ann Arbor – Flint, MI
    - 1210 : Cleveland – Akron, OH
    - 1211 : Minneapolis – St. Paul, MN – WI
    - 1312 : Washington, DC – MD – VA – WV
    - 1313 : Baltimore, MD
    - 1316 : Dallas – Ft. Worth, TX
    - 1318 : Houston – Galveston – Brazoria, TX
    - 1319 : Atlanta, GA
    - 1320 : Miami – Ft. Lauderdale, FL
    - 1419 : Los Angeles – Orange, CA
    - 1420 : Los Angeles suburbs, CA
    - 1422 : San Francisco – Oakland – San Jose, CA
    - 1423 : Seattle – Tacoma – Bremerton, WA
    - 1424 : San Diego, CA
    - 1429 : Phoenix – Mesa, AZ
    - S11A : Boston-Cambridge-Newton, MA-NH
    - S12A : New York-Newark-Jersey City, NY-NJ-PA
    - S12B : Philadelphia-Camden-Wilmington, PA-NJ-DE-MD
    - S23A : Chicago-Naperville-Elgin, IL-IN-WI
    - S23B : Detroit-Warren-Dearborn, MI
    - S24A : Minneapolis-St. Paul-Bloomington, MN-WI
    - S24B : St. Louis, MO-IL
    - S35A : Washington-Arlington-Alexandria, DC-VA-MD-WV
    - S35B : Miami-Fort Lauderdale-West Palm Beach, FL
    - S35C : Atlanta-Sandy Springs-Roswell, GA
    - S35D : Tampa-St. Petersburg-Clearwater, FL
    - S35E : Baltimore-Columbia-Towson, MD
    - S37A : Dallas-Fort Worth-Arlington, TX
    - S37B : Houston-The Woodlands-Sugar Land, TX
    - S48A : Phoenix-Mesa-Scottsdale, AZ
    - S48B : Denver-Aurora-Lakewood, CO
    - S49A : Los Angeles-Long Beach-Anaheim, CA
    - S49B : San Francisco-Oakland-Hayward, CA
    - S49C : Riverside-San Bernardino-Ontario, CA
    - S49D : Seattle-Tacoma-Bellevue, WA
    - S49E : San Diego-Carlsbad, CA
    - S49F : Honolulu, HI
    - S49G : Anchorage, AK
- PUBTRACQ : Public and other transportation this quarter
- PUBTRAPQ : Public and other transportation last quarter
- QINTRVMO : Interview month
    - 1 : January
    - 2 : Feburary
    - 3 : March
    - 4 : April
    - 5 : May
    - 6 : June
    - 7 : July
    - 8 : August
    - 9 : September
    - 10 : October
    - 11 : November
    - 12 : December
- QINTRVYR : Interview year
- RACE2 : Race of spouse (Flag: RACE2_)
    - 1 : White
    - 2 : African American or Black
    - 3 : American Indian, Aleut, or Eskimo
    - 4 : Asian or Pacific Islander
    - 5 : Other
    - 6 : Multi-race
- READCQ : Reading this quarter
- READPQ : Reading last quarter
- REF_RACE : Race of reference person (Flag: REF__ACE)
    - 1 : White
    - 2 : Black
    - 3 : Native American
    - 4 : Asian
    - 5 : Other
    - 6 : Multirace
- REFGEN : Generation of the reference person: 

Create five values for generation based on the birth year of the reference person
    - 1 : Birth year of 1928 or earlier - Greatest generation (G.I. Generation)
    - 2 : Birth year from 1929 to 1945 - Silent generation.
    - 3 : Birth year from 1946 to 1964 - Baby boomers.
    - 4 : Birth year from 1965 to 1980 - also known as Generation X.
    - 5 : Birth year of 1981 or later.  Sometimes referred to as the Millennials.
- REGION : Region
    - 1 : Northeast
    - 2 : Midwest
    - 3 : South
    - 4 : West
- RELECTRC : Expenditures on electricity for rented vacation homes this quarter
- RELECTRP : Expenditures on electricity for rented vacation homes last quarter 260114
- RENDWECQ : Rented dwelling this quarter
- RENDWEPQ : Rented dwelling last quarter
- RENTEQVX : If someone were to rent your home today, how much do you think it would rent for monthly, unfurnished and without utilities? (Flag: RENT_QVX)
- RETPENCQ : Retirement, pensions, Social Security this quarter
- RETPENPQ : Retirement, pensions, Social Security last quarter
- RETSRVBX : Median of Bracket Range (Flag: RETS_VBX)
- RETSURV : Amount of income received from retirement, survivor, or disability pensions (Flag: RETSURV_)
    - 1 : Yes
    - 2 : No
- RETSURV1 : Imputation Iteration #1 - RETSURVX
- RETSURV2 : Imputation Iteration #2 - RETSURVX
- RETSURV3 : Imputation Iteration #3 - RETSURVX
- RETSURV4 : Imputation Iteration #4 - RETSURVX
- RETSURV5 : Imputation Iteration #5 - RETSURVX
- RETSURVB : Range that best reflects the total amount received in retirement, survivor, or disability pensions during the past 12 months (Flag: RETS_RVB)
    - 01 : $0-$999
    - 02 : $1,000-$1,999
    - 03 : $2,000-$2,999
    - 04 : $3,000-$3,999
    - 05 : $4,000-$4,999
    - 06 : $5,000-$9,999
    - 07 : $10,000-$14,999
    - 08 : $15,000-$19,999
    - 09 : $20,000-$29,999
    - 10 : $30,000-$39,999
    - 11 : $40,000-$49,999
    - 12 : $50,000 and over
- RETSURVI : Indicator/descriptor variable for income imputation.
- RETSURVM : Amount of income received from retirement, survivor, or disability pensions, mean of the iterations (Flag: RETS_RVM)
- RETSURVX : What was the amount received in retirement, survivor, or disability pensions during the past 12 months. 

NOTE: Because this information is only collected from respondents in the 5th interview, the reported values have been multiplied by four to produce s (Flag: RETS_RVX)
- RFUELOIC : Expenditures on fuel oil for rented vacation homes this quarter
- RFUELOIP : Expenditures on fuel oil for rented vacation homes last quarter
- RNATLGAC : Expenditures on natural gas for rented vacation homes this quarter
- RNATLGAP : Expenditures on natural gas for rented vacation homes last quarter
- RNTAPYCQ : Rent as pay this quarter
- RNTAPYPQ : Rent as pay last quarter
- RNTXRPCQ : Rent excluding rent as pay this quarter
- RNTXRPPQ : Rent excluding rent as pay last quarter
- ROOMSQ : Number of rooms in CU living quarters, including finished living areas, excluding all baths (Flag: ROOMSQ_)
- ROTHRFLC : Expenditures on other fuels for rented vacation homes this quarter
- ROTHRFLP : Expenditures on other fuels for rented vacation homes last quarter
- ROYESTB : Range that best reflects the total amount received in royalty income or income from estates and trusts during the past 12 months (Flag: ROYESTB_)
    - 01 : $0-$999
    - 02 : $1,000-$1,999
    - 03 : $2,000-$2,999
    - 04 : $3,000-$3,999
    - 05 : $4,000-$4,999
    - 06 : $5,000-$9,999
    - 07 : $10,000-$14,999
    - 08 : $15,000-$19,999
    - 09 : $20,000-$29,999
    - 10 : $30,000-$39,999
    - 11 : $40,000-$49,999
    - 12 : $50,000 and over
- ROYESTBX : Median of Bracket Range (Flag: ROYE_TBX)
- ROYESTX : Amount of income received from royalty income or income from estates and trusts (Flag: ROYESTX_)
- ROYESTX1 : Imputation Iteration #1 - ROYESTX
- ROYESTX2 : Imputation Iteration #2 - ROYESTX
- ROYESTX3 : Imputation Iteration #3 - ROYESTX
- ROYESTX4 : Imputation Iteration #4 - ROYESTX
- ROYESTX5 : Imputation Iteration #5 - ROYESTX
- ROYESTXI : Indicator/descriptor variable for income imputation.
- ROYESTXM : Amount of income received from royalty income or income from estates and trusts, mean of the iterations (Flag: ROYE_TXM)
- RWATERPC : Expenditures on water and public services for rented vacation homes this quarter
- RWATERPP : Expenditures on water and public services for rented vacation homes
- SEX_REF : Sex of reference person (Flag: SEX_REF_)
    - 1 : Reference person is male
    - 2 : Reference person is female
- SEX2 : Sex of spouse person (Flag: SEX2_)
    - 1 : Male
    - 2 : Female
- SHELTCQ : Shelter this quarter
- SHELTPQ : Shelter last quarter
- SMLAPPCQ : Small appliances, miscellaneous housewares this quarter
- SMLAPPPQ : Small appliances, miscellaneous housewares last quarter
- SMSASTAT : Does CU reside inside a Metropolitan Statistical Area (MSA)?
    - 1 : Yes
    - 2 : No
- SOLARPNL : Solar panels (Flag: SOLA_PNL)
    - 08 : Solar panels
- ST_HOUS : Are these living quarters presently used as student housing by a college or university? (Flag: ST_HOUS_)
    - 1 : Student housing
    - 2 : Not student housing
- STATE : The 2010 Federal information processing standard state code
    - 01 : Alabama
    - 02 : Alaska
    - 04 : Arizona
    - 05 : Arkansas
    - 06 : California
    - 08 : Colorado
    - 09 : Connecticut
    - 10 : Delaware
    - 11 : District of Columbia
    - 12 : Florida
    - 13 : Georgia
    - 14 : Massachusetts
    - 15 : Hawaii
    - 16 : Idaho
    - 17 : Illinois
    - 18 : Indiana
    - 19 : Iowa
    - 20 : Kansas
    - 21 : Kentucky
    - 22 : Louisiana
    - 23 : Maine
    - 24 : Maryland
    - 25 : Massachuse
    - 26 : Michigan
    - 27 : Minnesota
    - 28 : Mississippi
    - 29 : Missouri
    - 30 : Montana
    - 31 : Nebraska
    - 32 : Nevada
    - 33 : New Hampshire
    - 34 : New Jersey
    - 35 : Wisconsin
    - 36 : New York
    - 37 : North Carolina
    - 39 : Ohio
    - 40 : Oklahoma
    - 41 : Oregon
    - 42 : Pennsylvania
    - 43 : Missouri
    - 44 : Rhode Island
    - 45 : South Carolina
    - 46 : South Dakota
    - 47 : Tennessee
    - 48 : Texas
    - 49 : Utah
    - 51 : Virginia
    - 52 : Maryland
    - 53 : Washington
    - 54 : Virginia
    - 55 : Wisconsin
    - 56 : North Carolina
    - 58 : Georgia
    - 59 : Florida
    - 61 : Kentucky
    - 62 : Tennesssee
    - 63 : Alabama
    - 72 : Louisiana
    - 74 : Texas
    - 84 : Colorado
    - 86 : Arizona
    - 91 : Washington
    - 92 : Oregon
    - 93 : California
    - 94 : Alaska
    - 95 : Hawaii
- STCKYRBX : Median of Bracket Range (Flag: STCK_RBX)
- STDNTYR : Did you have student loans one years ago today? (Flag: STDNTYR_)
    - 1 : Yes
    - 2 : No
- STDNTYRB : Range which best reflects the total amount owed on all student loans one year ago today (Flag: STDN_YRB)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- STDNTYRX : What was the total amount owed on all student loans one year ago today? (Flag: STDN_YRX)
- STDTYRBX : Median of Bracket Range (Flag: STDT_RBX)
- STOCKB : Range which best reflects the total value of all directly-held stocks, bonds, and mutual funds (Flag: STOCKB_)
    - 1 : $0 - $1999
    - 2 : $2,000 - $9,999
    - 3 : $10,000 - $49,999
    - 4 : $50,000 - $199,999
    - 5 : $200,000 - $449,999
    - 6 : $450,000 and over
- STOCKBX : Median of Bracket Range (Flag: STOCKBX_)
- STOCKX : As of today, what is the total value of all directly-held stocks, bonds, and mutual funds? (Flag: STOCKX_)
- STOCKYR : Did you have any directly-held stocks, bonds, or mutual funds one year ago? (Flag: STOCKYR_)
    - 1 : Yes
    - 2 : No
- STOCKYRB : Range which best reflects the total value of all directly-held stocks, bonds, and mutual funds one year ago today (Flag: STOC_YRB)
    - 1 : $0 - $1999
    - 2 : $2,000 - $9,999
    - 3 : $10,000 - $49,999
    - 4 : $50,000 - $199,999
    - 5 : $200,000 - $449,999
    - 6 : $450,000 and over
- STOCKYRX : What was the total value of all directly-held stocks, bonds, and mutual funds one year ago today? (Flag: STOC_YRX)
- STUDFINX : What was the total amount paid in finance, late charges, and interest for all student loans in the last month? (Flag: STUD_INX)
- STUDNTB : Range which best reflects the total amount owed on all student loans (Flag: STUDNTB_)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- STUDNTBX : Median of Bracket Range (Flag: STUD_TBX)
- STUDNTX : What is the total amount owed on all student loans? (Flag: STUDNTX_)
- SWIMPOOL : Does this unit have a swimming pool (Flag: SWIM_OOL)
    - 01 : Swimming pool
    - 1 : Swimming pool
- TAIRFARC : Trip expenditures on airfare this quarter
- TAIRFARP : Trip expenditures on airfare last quarter
- TALCBEVC : Total trip expenditures this quarter on alcoholic beverages at restaurants, cafes, and bars
- TALCBEVP : Total trip expenditures last quarter on alcoholic beverages at restaurants, cafes, and bars 200900
- TCARTRKC : Trip expenditures on car or truck rental this quarter
- TCARTRKP : Trip expenditures on car or truck rental last quarter
- TELEPHCQ : Telephone services this quarter
- TELEPHPQ : Telephone services last quarter
- TENTRMNC : Total trip expenditures on entertainment this quarter including sporting events, movies, and recreational vehicle rentals 
TFEESADC+TOTHENTC
- TENTRMNP : Total trip expenditures on entertainment last quarter including sporting events, movies, and recreational vehicle rentals TFEESADP+TOTHENTP
- TEXTILCQ : Household textiles this quarter
- TEXTILPQ : Household textiles last quarter
- TFAREC : Trip expenditures this quarter on transportation fares including airfare, intercity bus, train, and ship fare 
TAIRFARC+TOTHFARC
- TFAREP : Trip expenditures last quarter on transportation fares including airfare, intercity bus, train, and ship fare (TAIRFARP+TOTHFARP)
- TFEESADC : Trip expenditures on miscellaneous entertainment this quarter including recreation expenses, participation sport fees, and admission fees to sporting events and movies
- TFEESADP : Trip expenditures on miscellaneous entertainment last quarter including recreation expenses, participation sport fees, and admission fees to sporting events and movies
- TFOODAWC : Food and non-alcoholic beverages this quarter at restaurants, cafes, and fast food places during out-of-town trips
- TFOODAWP : Food and non-alcoholic beverages last quarter at restaurants, cafes, and fast food places during out-of-town trips
- TFOODHOC : Food and beverages purchased and prepared by CU this quarter during out-of-town trips
- TFOODHOP : Food and beverages purchased and prepared by CU last quarter during out-of-town trips
- TFOODTOC : Total trip expenditures on food this quarter including both restaurant food and food prepared by CU
- TFOODTOP : Total trip expenditures on food last quarter including both restaurant food and food prepared by CU
- TGASMOTC : Trip expenditures on gas and oil this quarter
- TGASMOTP : Trip expenditures on gas and oil last quarter
- TLOCALTC : Trip expenditures this quarter on local transportation including taxis, buses etc.
- TLOCALTP : Trip expenditures last quarter on local transportation including taxis, buses etc.
- TOBACCCQ : Tobacco and smoking supplies this quarter
- TOBACCPQ : Tobacco and smoking supplies last quarter
- TOTEX4CQ : Adjusted total expenditures this quarter collected in Interview Survey
- TOTEX4PQ : Adjusted total expenditures last quarter
- TOTEXPCQ : Total expenditures this quarter
- TOTEXPPQ : Total expenditures last quarter
- TOTHENTC : Trip expenditures on recreational vehicle rentals this quarter including campers, boats, and other vehicles
- TOTHENTP : Trip expenditures on recreational vehicle rentals last quarter including campers, boats, and other vehicles
- TOTHFARC : Tip expenditures this quarter on other transportation fares including intercity bus and train fare, and ship fare
- TOTHFARP : Tip expenditures last quarter on other transportation fares including intercity bus and train fare, and ship fare
- TOTHRLOC : Total trip expenditures on lodging this quarter including rent for vacation home, and motels
- TOTHRLOP : Total trip expenditures on lodging last quarter including rent for vacation home, and motels
- TOTHTREC : Trip expenditures this quarter for other transportation expenses including parking fees, and tolls
- TOTHTREP : Trip expenditures last quarter for other transportation expenses including parking fees, and tolls
- TOTHVHRC : Trip expenditures on other vehicle rentals this quarter
- TOTHVHRP : Trip expenditures on other vehicle rentals last quarter 520905 520906
- TOTXEST : Estimated total taxes paid
- TRANSCQ : Transportation this quarter
- TRANSPQ : Transportation last quarter
- TRNOTHCQ : Local public transportation, excluding on trips this quarter
- TRNOTHPQ : Local public transportation, excluding on trips last quarter
- TRNTRPCQ : Public and other transportation on trips this quarter
- TRNTRPPQ : Public and other transportation on trips last quarter
- TTOTALC : Total of all trip expenditures last quarter
- TTOTALP : Total of all trip expenditures last quarter
- TTRANPRC : Total trip expenditures on transportation this quarter including airfare, local transportation, tolls and parking fees, and car rentals
TGASMOTP+TVRENTLP+TTRNTRIP
- TTRANPRP : Total trip expenditures on transportation last quarter including airfare, local transportation, tolls and parking fees, and car rentals
TGASMOTP+TVRENTLP+TTRNTRIP
- TTRNTRIC : Trip expenditures this quarter for public transportation, including airfares 
TFAREC+TLOCALTC
- TTRNTRIP : Trip expenditures last quarter for public transportation, including airfares
TFAREP+TLOCALTP
- TVRDIOCQ : Televisions, radios, and sound equipment this quarter
- TVRDIOPQ : Televisions, radios, and sound equipment last quarter
- TVRENTLC : Trip expenditures on vehicle rentals and other fees this quarter 
TCARTRKC+TOTHVHRC+TOTHTREC
- TVRENTLP : Trip expenditures on vehicle rentals and other fees last quarter
TCARTRKP+TOTHVHRP+TOTHTREP
- UNISTRQ : How many housing units, both occupied and vacant, are there in this structure? (Flag: UNISTRQ_)
    - 01 : Only OTHER units
    - 02 : Mobile home or trailer
    - 03 : One, detached
    - 04 : One, attached
    - 05 : 2 housing units
    - 06 : 3-4 housing units
    - 07 : 5-9 housing units
    - 08 : 10-19 housing units
    - 09 : 20-49 housing units
    - 10 : 50 or more housing units
- UTILCQ : Utilities, fuels and public services this quarter 
NTLGASCQ + ELCTRCCQ + ALLFULCQ + TELEPHCQ + WATRPSCQ
- UTILOWNC : Expenditures on owned vacation home utilities this quarter including water, trash, electricity, and fuels
VFUELOIC+VOTHRFLC+VELECTRC+VNATLGAC
 +VWATERPC
- UTILOWNP : Expenditures on owned vacation home utilities last quarter including water, trash, electricity, and fuels
VFUELOIP+VOTHRFLP+VELECTRP+VNATLGAP
 +VWATERPP
- UTILPQ : Utilities, fuels and public services last quarter
NTLGASPQ + ELCTRCPQ + ALLFULPQ + TELEPHPQ + WATRPSPQ
- UTILRNTC : Expenditures on rented vacation home utilities this quarter including water, trash, electricity, and fuels
RFUELOIC+ROTHRFLC+RELECTRC+RNATLGAC+RWATERPC
- UTILRNTP : Expenditures on rented vacation home utilities last quarter including water, trash, electricity, and fuels
RFUELOIP+ROTHRFLP+RELECTRP+RNATLGAP+RWATERPP
- VEHFINCQ : Vehicle finance charges this quarter
- VEHFINPQ : Vehicle finance charges last quarter
- VEHICTAX : Personal property taxes for vehicles
- VEHINSCQ : Vehicle insurance this quarter
- VEHINSPQ : Vehicle insurance last quarter
- VEHQ : Total number of owned vehicles (Flag: VEHQ_)
- VEHQL : Total number of leased autos, trucks, and vans (Flag: VEHQL_)
- VELECTRC : Expenditures on electricity for owned vacation homes this quarter
- VELECTRP : Expenditures on electricity for owned vacation homes last quarter
- VFUELOIC : Expenditures on fuel oil for owned vacation homes this quarter
- VFUELOIP : Expenditures on fuel oil for owned vacation homes last quarter
- VMISCHEC : Expenditures on miscellaneous household equipment for owned vacation homes this quarter
- VMISCHEP : Expenditures on miscellaneous household equipment for owned vacation homes last quarter
- VNATLGAC : Expenditures on natural gas for owned vacation homes this quarter
- VNATLGAP : Expenditures on natural gas for owned vacation homes last quarter
- VOTHRFLC : Expenditures on other fuels for owned vacation homes this quarter
- VOTHRFLP : Expenditures on other fuels for owned vacation homes last quarter
- VOTHRLOC : Expenditures on owned vacation homes this quarter including mortgage interest, insurance, taxes, and maintenance
- VOTHRLOP : Expenditures on owned vacation homes last quarter including mortgage interest, insurance, taxes, and maintenance
- VRNTLOCQ : Vehicle rental, leases, licenses, and other charges this quarter
- VRNTLOPQ : Vehicle rental, leases, licenses, and other charges last quarter
- VWATERPC : Expenditures on water and public services for owned vacation homes this quarter
- VWATERPP : Expenditures on water and public services for owned vacation homes last quarter
- WATRPSCQ : Water and other public services this quarter
- WATRPSPQ : Water and other public services last quarter
- WELFARE1 : Imputation Iteration #1 - WELFAREX
- WELFARE2 : Imputation Iteration #2 - WELFAREX
- WELFARE3 : Imputation Iteration #3 - WELFAREX
- WELFARE4 : Imputation Iteration #4 - WELFAREX
- WELFARE5 : Imputation Iteration #5 - WELFAREX
- WELFAREI : Indicator/descriptor variable for income imputation.
- WELFAREM : Amount received from public assistance or welfare including money received from job training grants such as Job Corps, mean of imputation iterations. (Flag: WELF_REM)
- WELFAREX : Amount received from public assistance or welfare including money received from job training grants such as Job Corps (Flag: WELF_REX)
- WELFREBX : Median of bracket range (Flag: WELF_EBX)
- WHLFYR : Did you own any whole life insurance or other life insurance policies that can be surrendered for cash or borrowed against prior to the death of the person insured one year ago today? (Flag: WHLFYR_)
    - 1 : Yes
    - 2 : No
- WHLFYRB : Range which best reflects the total surrender value of these policies one year ago today. (Flag: WHLFYRB_)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- WHLFYRBX : Median of Bracket Range (Flag: WHLF_RBX)
- WHLFYRX : What was the total surrender value of these policies one year ago today? (Flag: WHLFYRX_)
- WHOLIFB : Range which best reflects the total surrender value of these policies. (Flag: WHOLIFB_)
    - 1 : $0 - $499
    - 2 : $500 - $999
    - 3 : $1,000 - $2,499
    - 4 : $2,500 - $9,999
    - 5 : $10,000 - $34,999
    - 6 : $35,000 and over
- WHOLIFBX : Median of Bracket Range (Flag: WHOL_FBX)
- WHOLIFX : As of today, what is the total surrender value of these policies? (Flag: WHOLIFX_)
- WINDOWAC : Does this unit have a window AC unit? (Flag: WIND_WAC)
    - 06 : Window Air Conditioner
    - 11 : Window Air Conditioner
- WOMGRLCQ : Clothing for women and girls this quarter WOMSIXCQ + GRLFIFCQ
- WOMGRLPQ : Clothing for women and girls last quarter WOMSIXPQ + GRLFIFPQ
- WOMSIXCQ : Clothing for women, 16 and over this quarter
- WOMSIXPQ : Clothing for women, 16 and over last quarter
- WTREP01 : CU replicate weight # 01. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP02 : CU replicate weight # 02. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP03 : CU replicate weight # 03. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP04 : CU replicate weight # 04. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP05 : CU replicate weight # 05. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP06 : CU replicate weight # 06. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP07 : CU replicate weight # 07. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP08 : CU replicate weight # 08. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP09 : CU replicate weight # 09. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP10 : CU replicate weight # 10. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP11 : CU replicate weight # 11. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP12 : CU replicate weight # 12. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP13 : CU replicate weight # 13. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP14 : CU replicate weight # 14. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP15 : CU replicate weight # 15. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP16 : CU replicate weight # 16. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP17 : CU replicate weight # 17. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP18 : CU replicate weight # 18. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP19 : CU replicate weight # 19. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP20 : CU replicate weight # 20. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP21 : CU replicate weight # 21. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP22 : CU replicate weight # 22. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP23 : CU replicate weight # 23. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP24 : CU replicate weight # 24. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP25 : CU replicate weight # 25. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP26 : CU replicate weight # 26. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP27 : CU replicate weight # 27. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP28 : CU replicate weight # 28. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP29 : CU replicate weight # 29. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP30 : CU replicate weight # 30. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP31 : CU replicate weight # 31. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP32 : CU replicate weight # 32. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP33 : CU replicate weight # 33. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP34 : CU replicate weight # 34. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP35 : CU replicate weight # 35. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP36 : CU replicate weight # 36. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP37 : CU replicate weight # 37. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP38 : CU replicate weight # 38. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP39 : CU replicate weight # 39. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP40 : CU replicate weight # 40. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP41 : CU replicate weight # 41. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP42 : CU replicate weight # 42. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP43 : CU replicate weight # 43. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.
- WTREP44 : CU replicate weight # 44. This variable is one of the 44 half sample replicate weights (WTREP01 - WTREP44), which are used for variance computations.


























































































### MEMI - Member Level Interview


- AGE : What is the member's age? (Flag: AGE_)
- ANGOVRTM : Annual amount of government retirement deducted from pay, based on SALARYM. (Flag: ANGO_RTM)
- ANGOVRTX : Annual amount of government retirement deducted from pay (Flag: ANGO_RTX)
- ANPRVPNM : Annual amount of private pensions deducted from pay, based on SALARYM. (Flag: ANPR_PNM)
- ANPRVPNX : Annual amount of private pensions deducted from pay (Flag: ANPR_PNX)
- ANRRDEDM : Annual amount of railroad retirement deducted from pay, based on SALARYM. (Flag: ANRR_EDM)
- ANRRDEDX : Annual amount of Railroad retirement deducted from pay (Flag: ANRR_EDX)
- ARM_FORC : Is member now in the Armed Forces? (Flag: ARM__ORC)
    - 1 : Yes
    - 2 : No
- ASIAN : Country of Asian origin (Flag: ASIAN_)
    - 1 : Chinese
    - 2 : Filipino
    - 3 : Japanese
    - 4 : Korean
    - 5 : Vietnamese
    - 6 : Asian Indian
    - 7 : Other - specify
- CU_CODE : What is this person's relation to reference person?
    - 0 : Blank or illegible entry
    - 1 : Reference person
    - 2 : Spouse
    - 3 : Child or adopted child
    - 4 : Grandchild
    - 5 : In-law
    - 6 : Brother or sister
    - 7 : Mother or father
    - 8 : Other related persons
    - 9 : Unrelated persons
- EARNER : Indicates whether the member earned income or not (Flag: EARNER_)
    - 1 : Member Earns Income AGE >= 14 and INCWEEKQ > 0 and INCOMEY=1, 2, 3, 4, or 5
    - 2 : Member earns no income AGE < 14 or AGE >= 14 and INCWEEKQ > 0 and INCOMEY=6 or AGE >= 14 and INCWEEKQ=0
- EARNTYPE : Type of earner (Flag: EARN_YPE)
    - 1 : Member worked full time for a full year
    - 2 : Member worked part time for a full year
    - 3 : Member worked full time for part of year
    - 4 : Member worked part time for part of year
- EDUCA : What is the highest level of school the member has completed or the highest degree the member has received? (Flag: EDUCA_)
    - 00 : Never attended
    - 01 : 1st grade
    - 02 : 2nd grade
    - 03 : 3rd grade
    - 04 : 4th grade
    - 05 : 5th grade
    - 06 : 6th grade
    - 07 : 7th grade
    - 08 : 8th grade
    - 09 : 9th grade
    - 1 : No schooling completed, or less than 1 year
    - 10 : 10th grade
    - 11 : 11th grade
    - 12 : 12th grade
    - 13 : First year of college or equivalent
    - 14 : Second year of college or equivalent
    - 15 : Third year of college or equivalent
    - 16 : Fourth year of college or equivalent
    - 17 : One year of graduate school
    - 18 : Two or more years of graduate school
    - 2 : Nursery, kindergarten, and elementary (grades 1-8)
    - 21 : First year of college or equivalent
    - 22 : Second year of college or equivalent
    - 23 : Third year of college or equivalent
    - 24 : Fourth year of college or equivalent
    - 25 : One year of graduate school
    - 26 : Two or more years of graduate school
    - 3 : High school (grades 9-12), no degree
    - 31 : One year of graduate school
    - 32 : Two or more years of graduate school
    - 38 : 12th grade, no diploma
    - 39 : High school graduate
    - 4 : High school graduate - high school diploma or equivalent (GED)
    - 40 : Some college, no degree
    - 41 : Associate degree, occupational/vocational
    - 42 : Associate degree, academic
    - 43 : Bachelor's degree
    - 44 : Master's degree
    - 45 : Professional school degree
    - 46 : Doctorate degree
    - 5 : Some college, but no degree
    - 6 : Associate's degree in college
    - 7 : Bachelor's degree (BA, AB, BS, etc.)
    - 8 : Master's, professional, or doctorate degree (MA, MS, MBA, MD, JD, PhD, etc.)
- EMPLCONT : Other than Social Security, did any employer or union that the member worked for during the last 12 months contribute to a pension or retirement plan that the member was enrolled in? (Flag: EMPL_ONT)
    - 1 : Yes, employer contributed to pension
    - 2 : No, employer did not contribute to pension
- GOVRETX : Amount of government retirement deducted from last pay (Flag: GOVRETX_)
- GROSPAYX : Amount of last gross pay (Flag: GROS_AYX)
- HISPANIC : Country of Hispanic Origin (Flag: HISP_NIC)
    - 1 : Mexican
    - 2 : Mexican-American
    - 3 : Chicano
    - 4 : Puerto Rican
    - 5 : Cuban
    - 6 : Cuban-American
    - 7 : Central or South American
    - 8 : Other Hispanic group not listed
- HORIGIN : Are you Spanish, Hispanic, or Latino?
    - 1 : Yes
    - 2 : No
- IN_COLL : Is the member currently enrolled in a college or university either . . .? (Flag: IN_COLL_)
    - 1 : Full time
    - 2 : Part time
    - 3 : Not at all
- INC_HRSQ : Number of hours worked per week (Flag: INC__RSQ)
- INCMEDCR : Is the amount of the last Social Security or Railroad Retirement payment received AFTER the deduction for a Medicare premium? (Flag: INCM_DCR)
    - 1 : Yes, includes Medicare deduction
    - 2 : No, does not include Medicare deduction
- INCNONWK : What was the main reason the member did not work during the past 12 months? Was the member . . .? (Flag: INCN_NWK)
    - 1 : Retired
    - 2 : Taking care of home/family
    - 3 : Going to school
    - 4 : Ill, disabled, unable to work
    - 5 : Unable to find work
    - 6 : Doing something else
- INCOMEY : Was the member . . . ? (Type of employee) Refers to job where member received the most earnings in the past 12 months. (Flag: INCOMEY_)
    - 1 : An employee of a private company, business or individual working for wages or salary
    - 2 : A federal government employee
    - 3 : A state government employee
    - 4 : A local government employee
    - 5 : Self-employed in own business, professional practice or farm
    - 6 : Working w/o pay in family business or farm
- INCWEEKQ : Number of weeks worked full time or part time (last 12 months) (Flag: INCW_EKQ)
- INDRETX : Amount of money placed in a retirement plan in the past year (Flag: INDRETX_)
- JSSDEDX : Estimated amount of income contributed to Social Security by member in past 12 months (Flag: JSSDEDX_)
- JSSDEDX1 : Imputation Iteration #1 - JSSDEDX
- JSSDEDX2 : Imputation Iteration #2 - JSSDEDX
- JSSDEDX3 : Imputation Iteration #3 - JSSDEDX
- JSSDEDX4 : Imputation Iteration #4 - JSSDEDX
- JSSDEDX5 : Imputation Iteration #5 - JSSDEDX
- JSSDEDXM : Social Security payment during the past 12 months, mean of imputation iterations. (Flag: JSSD_DXM)
- MARITAL : Marital status of member
    - 1 : Married
    - 2 : Widowed
    - 3 : Divorced
    - 4 : Separated
    - 5 : Never married
- MEDICOV : Does the money deducted for Social Security cover only the Medicare portion of Social Security? (Flag: MEDICOV_)
    - 1 : Yes, the money deducted for Social Security covers only the Medicare portion.
    - 2 : No, the money deducted for Social Security does not cover only the Medicare portion.
- MEMBNO : Member Number
- MEMBRACE : Race of member
    - 1 : White
    - 2 : Black
    - 3 : Native American
    - 4 : Asian
    - 5 : Pacific Islander
    - 6 : Multi-race
    - 7 : Other
- NEWID : Public use microdata identifier
- OCCUCODE : The job in which the member received the most earnings during the past 12 months fits best in the following category. (Flag: OCCU_ODE)
    - 01 : Manager, Professional Administrator
    - 02 : Teacher
    - 03 : Professional
    - 04 : Administrative support, including clerical
    - 05 : Sales, retail
    - 06 : Sales, business goods, and services
    - 07 : Technician Service
    - 08 : Protective Service
    - 09 : Private household service
    - 10 : Other Service
    - 11 : Machine Operator, assembler, inspector
    - 12 : Transportation operator
    - 13 : Handler, helper, laborer
    - 14 : Mechanic, repairer, precision production
    - 15 : Construction, mining
    - 16 : Farming
    - 17 : Forestry, fishing, groundskeeping
    - 18 : Armed Forces
- PAYPERD : What period of time did this last gross pay cover? (Flag: PAYPERD_)
    - 1 : One week
    - 2 : Two weeks
    - 3 : Month
    - 4 : Quarter
    - 5 : Year
    - 6 : Other
    - 7 : Other
- PAYSTUB : Does the respondent have a paper or electronic pay check record for the last paycheck? (Flag: PAYSTUB_)
    - 1 : Yes
    - 2 : No
- PRIVPENX : Amount of private pension deducted from last pay (Flag: PRIV_ENX)
- RC_ASIAN : Race as reported by respondent. (Flag: RC_A_IAN)
    - 4 : Asian
- RC_BLACK : Race as reported by respondent. (Flag: RC_B_ACK)
    - 2 : Black
- RC_DK : Race as reported by respondent. (Flag: RC_DK_)
    - 7 : Don’t Know
- RC_NATAM : Race as reported by respondent. (Flag: RC_N_TAM)
    - 3 : Native American
- RC_OTHER : Race as reported by respondent. (Flag: RC_O_HER)
    - 6 : Other
- RC_PACIL : Race as reported by respondent. (Flag: RC_P_CIL)
    - 5 : Pacific Islander
- RC_WHITE : Race as reported by respondent. (Flag: RC_W_ITE)
    - 1 : White
- RRRDEDX : Amount of Railroad Retirement deducted from last pay (Flag: RRRDEDX_)
- RRRETIR1 : Imputation Iteration #1 - RRRETIRX
- RRRETIR2 : Imputation Iteration #2 - RRRETIRX
- RRRETIR3 : Imputation Iteration #3 - RRRETIRX
- RRRETIR4 : Imputation Iteration #4 - RRRETIRX
- RRRETIR5 : Imputation Iteration #5 - RRRETIRX
- RRRETIRB : Range that best reflects the amount of your last Social Security or Railroad Retirement payment during the last 12 months (Flag: RRRE_IRB)
    - 1 : Less than $300
    - 10 : $1500 and over
    - 2 : $300-$399
    - 3 : $400-$499
    - 4 : $500-$599
    - 5 : $600-$699
    - 6 : $700-$799
    - 7 : $800-$899
    - 8 : $900-$999
    - 9 : $1000-$1499
- RRRETIRI : Indicator/descriptor variable for income imputation.
- RRRETIRM : Amount of last Social Security or Railroad Retirement check, mean of imputation iterations. (Flag: RRRE_IRM)
- RRRETIRX : Amount of last Social Security or Railroad Retirement check (Flag: RRRE_IRX)
- RRRETRBX : Median of bracket range (Flag: RRRE_RBX)
- SALARYB : Range that best reflects the total wages and salaries for all jobs during the last 12 months (Flag: SALARYB_)
    - 01 : $0-$4,999
    - 02 : $5,000-$9,999
    - 03 : $10,000-$14,999
    - 04 : $15,000-$19,999
    - 05 : $20,000-$29,999
    - 06 : $30,000-$39,999
    - 07 : $40,000-$49,999
    - 08 : $50,000-$69,999
    - 09 : $70,000-$89,999
    - 10 : $90,000-$119,999
    - 11 : $120,000 and over
- SALARYBX : Median of bracket range (Flag: SALA_YBX)
- SALARYX : During the past 12 months, what was the amount of wages or salary income received, before any deductions? (Flag: SALARYX_)
- SALARYX1 : Imputation Iteration #1 - SALARYX
- SALARYX2 : Imputation Iteration #2 - SALARYX
- SALARYX3 : Imputation Iteration #3 - SALARYX
- SALARYX4 : Imputation Iteration #4 - SALARYX
- SALARYX5 : Imputation Iteration #5 - SALARYX
- SALARYXI : Indicator/descriptor variable for income imputation.
- SALARYXM : Amount of income received before from wages or salary deductions, mean of imputation iterations. (Flag: SALA_YXM)
- SCHLMLPD : Time period of expense (Flag: SCHL_LPD)
    - 1 : Day
    - 2 : Week
    - 3 : Two weeks
    - 4 : Month
    - 5 : Other, specify
- SCHLMLRX : How much was paid since the first of the reference month, not including this month? (Flag: SCHL_LRX)
- SCHLMLX : Since the beginning of the reference period, not including the current month, what has been the usual expense for the meals purchased at school? (Flag: SCHLMLX_)
- SCHMLWKQ : Number of weeks (Flag: SCHM_WKQ)
- SEMPFRM1 : Imputation Iteration #1 - SEMPFRMX
- SEMPFRM2 : Imputation Iteration #2 - SEMPFRMX
- SEMPFRM3 : Imputation Iteration #3 - SEMPFRMX
- SEMPFRM4 : Imputation Iteration #4 - SEMPFRMX
- SEMPFRM5 : Imputation Iteration #5 - SEMPFRMX
- SEMPFRMI : Indicator/descriptor variable for income imputation.
- SEMPFRMM : Amount of income received from self-employment, mean of the iterations (Flag: SEMP_RMM)
- SEMPFRMX : What was the amount of self-employment income or loss? (Flag: SEMP_RMX)
- SEX : Sex of Member
    - 1 : Male
    - 2 : Female
- SLFEMPS1 : Imputation Iteration #1 - SLFEMPSS
- SLFEMPS2 : Imputation Iteration #2 - SLFEMPSS
- SLFEMPS3 : Imputation Iteration #3 - SLFEMPSS
- SLFEMPS4 : Imputation Iteration #4 - SLFEMPSS
- SLFEMPS5 : Imputation Iteration #5 - SLFEMPSS
- SLFEMPSM : Self-employment social security contribution, mean of imputation iterations. (Flag: SLFE_PSM)
- SLFEMPSS : Self-employment social security contribution (Flag: SLFE_PSS)
- SMPFRMB : Range that best reflects the income or loss from self-employment during the past 12 months (Flag: SMPFRMB_)
    - 00 : LOSS
    - 01 : $0-$4,999
    - 02 : $5,000-$9,999
    - 03 : $10,000-$14,999
    - 04 : $15,000-$19,999
    - 05 : $20,000-$29,999
    - 06 : $30,000-$39,999
    - 07 : $40,000-$49,999
    - 08 : $50,000-$69,999
    - 09 : $70,000-$89,999
    - 10 : $90,000-$119,999
    - 11 : $120,000 and over
- SMPFRMBX : Median of Bracket Range (Flag: SMPF_MBX)
- SOCRRX : Amount of Social Security and Railroad Retirement income received by member in past 12 months (Flag: SOCRRX_)
- SOCRRX1 : Imputation Iteration #1 - SOCRRX
- SOCRRX2 : Imputation Iteration #2 - SOCRRX
- SOCRRX3 : Imputation Iteration #3 - SOCRRX
- SOCRRX4 : Imputation Iteration #4 - SOCRRX
- SOCRRX5 : Imputation Iteration #5 - SOCRRX
- SOCRRXM : Annual amount received from Social Security benefits and Railroad payments, mean of imputation iterations. (Flag: SOCRRXM_)
- SOCSRRET : During the past 12 months, did you receive any Social Security or Railroad Retirement benefits? (Flag: SOCS_RET)
    - 1 : Yes
    - 2 : No
- SS_RRQ : During the past 12 months, how many Social Security or Railroad Retirement payments did the member receive? (Flag: SS_RRQ_)
- SSIB : Range that best reflects the amount you received in Supplemental Security income from all government sources during the last 12 months (Flag: SSIB_)
    - 01 : $0-$999
    - 02 : $1,000 - $1,999
    - 03 : $2,000 - $2,999
    - 04 : $3,000 - $3,999
    - 05 : $4,000 - $4,999
    - 06 : $5,000 - $9,999
    - 07 : $10,000 - $14,999
    - 08 : $15,000 - $19,999
    - 09 : $20,000 - $29,999
    - 10 : $30,000 - $39,999
    - 11 : $40,000 - $49,999
    - 12 : $50,000 and over
- SSIBX : Median of bracket range (Flag: SSIBX_)
- SSIX : Amount received in supplemental security income checks combined (Flag: SSIX_)
- SSIX1 : Imputation Iteration #1 - SSIX
- SSIX2 : Imputation Iteration #2 - SSIX
- SSIX3 : Imputation Iteration #3 - SSIX
- SSIX4 : Imputation Iteration #4 - SSIX
- SSIX5 : Imputation Iteration #5 - SSIX
- SSIXI : Indicator/descriptor variable for income imputation.
- SSIXM : Amount received in supplemental security income checks combined, mean of imputation iterations. (Flag: SSIXM_)
- SSNORM : Are Social Security payments normally deducted from your paycheck? (Flag: SSNORM_)
    - 1 : Yes, Social Security including medicare payments normally deducted from paychecks
    - 2 : No, Social Security including medicare payments normally not deducted from paycheck
- TAX_UNIT : Identifies which tax unit the member was placed in (Flag: TAX__NIT)
- TRANAMTX : What is the usual out-of-pocket cost? (Flag: TRAN_MTX)
- TRANDAYX : How many days per week usually? (Flag: TRAN_AYX)
- TRANPD : What is the time period? (Flag: TRANPD_)
    - 1 : Day
    - 2 : Week
    - 3 : Month
- TU_CODE : Identifies the code of the taxpayer (Taxpayer, Spouse, dependent) (Flag: TU_CODE_)
    - 1 : Taxpayer
    - 2 : Spouse
    - 3 : Dependent
- TU_DPNDT : For dependent tax payers, this identifies the TAX_UNIT that the member is a dependent of (Flag: TU_D_NDT)
- VETERAN : Did you ever serve on Active Duty in the U.S. Armed Forces? (Flag: VETERAN_)
    - 1 : Yes, served on active duty
    - 2 : Did not serve on active duty
- WKSTATUS : Work Status of Member (Past Year)
    - 1 : Employed INCOMEY=1, 2, 3, or 4
    - 2 : Self-Employed INCOMEY=5
    - 3 : Working without pay INCOMEY=6









## Flag Values

Some variables have secondary "Flag" variables associated with them.
Here are the meanings of each flag value.

- A : Valid blank; a blank field where a response is not anticipated
- B : Invalid blank due to invalid nonresponse; nonresponse that is not consistent with other data reported by the CU
- C : Blank due to "Don't know," refusal, or other nonresponse
- D : Valid value; unadjusted
- E : Valid value; allocated
- F : Valid value; imputed or adjusted in some other way
- G : Valid value; allocated and imputed
- H : Valid blank for an expenditure that is a "parent record" where the expenditure was allocated to other records and the original expenditure was overwritten with a blank
- T : Valid value; topcoded or suppressed
- U : Valid value; allocated then topcoded or suppressed
- V : Valid value; imputed or adjusted in some other way then topcoded or suppressed
- W : Valid value; allocated and imputed or adjusted in some other way then topcoded or suppressed















## Detailed Income and Expenditures

### MTBI - Monthly Expenditures

- ALCNO : Allocation Number
- COST : Total cost of item, including sales tax (Flag: COST_)
- EXPNAME : Name of expense variable from which UCC mapped
- GIFT : Was this item bought for someone outside the CU?
    - 1 : Yes
    - 2 : No
- NEWID : Public use microdata identifier
- PUBFLAG : Is amount included in published reports?
    - 1 : Not published
    - 2 : Published in Integrated Bulletin
- REF_MO : Reference Month of this expenditure
- REF_YR : Reference Year of this expenditure
- RTYPE : RECORD TYPE of the corresponding EXPN record
    - APA : Section 6, Part A
    - APB : Section 6, Part B
    - APL : Section 1, Part C
    - CLA : Section 9, Part A
    - CLB : Section 9, Part B
    - CLC : Section 9, Part C
    - CLD : Section 9, Part B
    - CNT : Section 19, Part B
    - CRA : Section 5, Part A
    - CRB : Section 5, Part B
    - EDA : Section 16, Part A
    - ENT : Section 17, Part B
    - EQB : Section 7, Part B
    - EQD : Section 7, Part D
    - FN2 : Section 21
    - FNA : Section 21, Part A.2
    - FNB : Section 21, Part B
    - FRA : Section 8, Part A
    - FRB : Section 8, Part B
    - HHM : Section 13
    - HHP : Section 13
    - HIM : Section 13
    - IHB : Section 14, Part B
    - IHC : Section 14, Part C
    - IHD : Section 14, Part D
    - INB : Section 13, Part B
    - LSD : Section 10, Part B
    - MDB : Section 15, Part B
    - MDC : Section 15, Part D
    - MIS : Section 19, Part A
    - OPB : Section 3, Part B
    - OPC : Section 3, Part C
    - OPD : Section 3, Part D
    - OPF : Section 3, Parts F and G
    - OPH : Section 3, Part H
    - OPI : Section 3, Part I
    - OVB : Section 11, Part B
    - OVC : Section 11, Part C
    - RLV : Section 10, Parts A.1 and A.2
    - RNT : Section 2, Parts A and B
    - SUB : Section 17, Part A
    - TR1 : Section 18, Part A
    - TR2 : Section 18, Part A
    - TRB : Section 18, Parts B and C
    - TRD : Section 18, Part D
    - TRE : Section 18, Part E
    - TRF : Section 18, Part F
    - UTA : Section 4, Part A
    - UTB : Section 4, Part B
    - UTC : Section 4, Part C
    - UTI : Section 4, Part C
    - UTP : Section 4, Part B
    - VEQ : Section 12, Parts A and B
    - VLR : Section 12, Part C
    - VOT : Section 12, Part D
    - XPA : Section 20, Part A
    - XPB : Section 20, Part B
- SEQNO : Sequence Number
- UCC : Universal Classification Code
    - 002120 : Other non-health insurance
    - 006001 : Total amount owed to creditors, 2nd interview
    - 006002 : Total amount owed to creditors, 5th interview
    - 006003 : Total amount owed to creditors, 2nd interview
    - 006004 : Total amount owed to creditors, 5th interview
    - 006005 : Total amount owed to creditors, 2nd interview CY + 1
    - 006006 : Total amount owed to creditors, 5th interview CY + 1
    - 006009 : TOTAL AMT OWED CY Q2
    - 006010 : TOTAL AMT OWED CY+1,Q2
    - 190901 : Food or board at school
    - 190902 : Catered affairs
    - 190903 : Food on out-of-town trips
    - 190904 : Food prepared by consumer unit on out-of-town trips
    - 200900 : Alcoholic beverages purchased on trips
    - 210110 : Rent
    - 210210 : Lodging on out-of-town trips
    - 210310 : Housing while attending school
    - 210901 : Ground rent
    - 210902 : Ground rent
    - 220111 : Fire and extended coverage
    - 220112 : Fire and extended coverage
    - 220121 : Homeowners insurance
    - 220122 : Homeowners insurance
    - 220211 : Property taxes
    - 220212 : Property taxes
    - 220311 : Mortgage interest
    - 220312 : Mortgage interest
    - 220313 : Interest paid, home equity loan
    - 220314 : Interest paid, home equity loan
    - 220321 : Prepayment penalty charges
    - 220511 : Wall-to-wall carpet not installed, capital improvement (owned home)
    - 220512 : Materials and supplies purchased for insulation, dwellings under constr, additions, finishing, remodeling, landscaping, etc.
    - 220513 : Supplies purchased for additions, maintenance and repairs, and new construction
    - 220611 : Capital improvement labor and materials (owned home)
    - 220612 : Dishwasher, disposal, or range hood
    - 220613 : DISHWASHER, DISPOSAL, OR RANGE HOOD CAPITAL IMPROVEMENTS, OWNED VACATION
    - 220614 : Installed wall-to-wall carpeting
    - 220615 : Capital improvement labor and materials (owned vacation)
    - 220616 : Wall-to-wall carpeting
    - 220901 : Parking
    - 220902 : Parking
    - 230111 : REP/MAINT LABOR/MAT RNTR
    - 230112 : Painting and papering
    - 230113 : Plumbing and water heating
    - 230114 : Heat, a/c, electrical work
    - 230115 : Roofing and gutters
    - 230116 : OTH REP/MAINT LABOR/MAT OWND
    - 230117 : REPLACEMENT, REPAIR AND MAINTENANCE OF DISHWASHER, DISPOSAL, OR RANGE
HOOD RENTER
    - 230118 : Dishwashers (built-in), garbage disposals, range hoods, (owned home)
    - 230119 : REPAIR AND MAINTENANCE SERVICES OWNED VACATION
    - 230121 : REPAIR OR REPLACEMENT OF HARD SURFACED FLOORING RENTER
    - 230122 : Repair and replacement of hard surface flooring
    - 230123 : Repair and replacement of hard surface flooring
    - 230131 : Wall-to-wall carpet, installed (renter)
    - 230132 : Wall-to-wall carpet, installed (replacement)(owned home)
    - 230133 : Wall-to-wall carpet (replacement) (owned home)
    - 230134 : Wall-to-wall carpet (renter)
    - 230141 : Repair of built-in appliances
    - 230142 : Repair of built-in appliances
    - 230150 : Repair or maintenance services
    - 230151 : Other repair and maintenance services
    - 230152 : Repair and remodeling services
    - 230901 : Property management
    - 230902 : PROPERTY MANAGEMENT OWNED VACATION
    - 240111 : Paint, wallpaper, and supplies
    - 240112 : Paints, wallpaper and supplies
    - 240113 : Paints, wallpaper, supplies
    - 240121 : Tools and equipment for painting and wallpapering
    - 240122 : Tools and equipment for painting and wallpapering
    - 240123 : Tools and equipment for painting and wallpapering
    - 240211 : Materials for plastering, panels, roofing, gutters, etc.
    - 240212 : Materials for plaster., panel., siding, windows, doors, screens, awnings
    - 240213 : Materials and equipment for roof and gutters
    - 240214 : Materials for plastering, paneling, roofing, gutters, downspouts, siding, windows, doors, screens, and awnings
    - 240221 : Materials for patio, walk, fence, driveway, masonry, brick and stucco work
    - 240222 : Materials for patio, walk, fence, driveway, masonry, brick and stucco work
    - 240223 : MATERIALS AND SUPPLIES FOR REPAIRING OUTDOOR PATIOS, WALKS, FENCES,
DRIVEWAYS, OR PERMANENT SWIMMING POOLS AND MASONRY, BRICK OR
STUCCO WORK, OWNED VACATION
    - 240311 : Plumbing supplies and equipment
    - 240312 : Plumbing supplies and equipment
    - 240313 : MATERIALS AND SUPPLIES FOR PLUMBING OR WATER HEATING INSTALLATIONS
AND REPAIRS, OWNED VACATION
    - 240321 : Electrical supplies, heating and cooling equipment
    - 240322 : Electrical supplies, heating and cooling equipment
    - 240323 : MATERIALS AND SUPPLIES FOR ELECTRICAL WORK, HEATING OR AIR CONDITIONING
JOBS, FOR OWNED VACATION
    - 250111 : Fuel oil (renter)
    - 250112 : Fuel oil (owned home)
    - 250113 : Fuel oil (owned vacation)
    - 250114 : Fuel oil (rented vacation)
    - 250211 : Gas, btld/tank (renter)
    - 250212 : Gas, btld/tank (owned home)
    - 250213 : Gas, btld/tank (owned vacation)
    - 250214 : Gas, btld/tank (rented vacation)
    - 250221 : Coal (renter)
    - 250222 : Coal (owned home)
    - 250223 : Coal (owned vacation)
    - 250901 : oil, duraflame log, and sterno
    - 250902 : Wood/other fuels (owned home)
    - 250903 : Wood/other fuels (owned vacation)
    - 250904 : Wood/other fuels (rented vacation)
    - 250911 : Coal, wood, other fuels (renter)
    - 250912 : Coal, wood, other fuels (owned home)
    - 250913 : Coal, wood, other fuels (owned vacation)
    - 250914 : Coal, wood, other fuels (rented vacation)
    - 260111 : Electricity (renter)
    - 260112 : Electricity (owned home)
    - 260113 : Electricity (owned vacation)
    - 260114 : Electricity (rented vacation)
    - 260211 : Utility--natural gas (renter)
    - 260212 : Utility--natural gas (owned home)
    - 260213 : Utility--natural gas (owned vacation)
    - 260214 : Utility--natural gas (rented vacation)
    - 270000 : Telephone service, including public pay phones
    - 270101 : Residential telephone/pay phones
    - 270102 : Cellular phone service
    - 270103 : Pager service
    - 270104 : A card, document, or electronic media that consumers may purchase at retail outlets, vending machines, or electronically, which allows the purchaser to make prepaid toll or long distance calls.
    - 270105 : Voice over IP service
    - 270106 : Residential landline telephone service where there are specific charges per call or per group of calls. Local, Interstate toll, Intrastate toll, and International toll phone calling are included. Residential landline bundle of services that includes landline telephone service, and one or both of the following: television service and/or Internet service. Services priced are primarily specific plans offered by the selected company. All applicable per-plan charges, or individual charges for telephone, television, and/or Internet segments of the plan are eligible for pricing. 
    - 270211 : Water/sewer maint. (renter)
    - 270212 : Water/sewer maint. (owned home)
    - 270213 : Water/sewer maint. (owned vacation)
    - 270214 : Water/sewer maint. (rented vacation)
    - 270310 : Cable and satellite television services
    - 270311 : All prerecorded audio media (other than audio books) on satellite radio.
    - 270411 : Trash/garb. coll. (renter)
    - 270412 : Trash/garb. coll. (owned home)
    - 270413 : Trash/garb. coll. (owned vacation)
    - 270414 : Trash/garb. coll. (rented vacation)
    - 270901 : Septic tank clean. (renter)
    - 270902 : Septic tank clean. (owned home)
    - 270903 : Septic tank cleaning owned vacations
    - 270904 : Septic tank clean. (rented vacation)
    - 280110 : Bathroom linens
    - 280120 : Bedroom linens
    - 280130 : Kitchen and dining room linens
    - 280140 : Kitchen , dining room, other linens
    - 280210 : Curtains and draperies
    - 280220 : Slipcovers, decorative pillows
    - 280230 : Sewing materials for slipcovers, curtains, other sewing materials for the home
    - 280900 : Other linens
    - 290110 : Mattress and springs
    - 290120 : Other bedroom furniture
    - 290210 : Sofas
    - 290310 : Living room chairs
    - 290320 : Living room tables
    - 290410 : Kitchen, dining room furniture
    - 290420 : Infants'' furniture
    - 290430 : Outdoor furniture
    - 290440 : Wall units, cabinets and other occasional furniture
    - 300111 : Refrigerators, freezers (renter)
    - 300112 : Refrigerators, freezers (owned home)
    - 300211 : Washing machines (renter)
    - 300212 : Washing machines (owned home)
    - 300216 : Clothes washer or dryer (renter)
    - 300217 : Clothes washer or dryer (owned home)
    - 300221 : Clothes dryers (renter)
    - 300222 : Clothes dryers (owned home)
    - 300311 : Cooking stoves, ovens (renter)
    - 300312 : Cooking stoves, ovens (owned home)
    - 300321 : Microwave ovens (renter)
    - 300322 : Microwave ovens (owned home)
    - 300331 : Portable dishwasher (renter)
    - 300332 : Portable dishwasher (owned home)
    - 300411 : Window air conditioners (renter)
    - 300412 : Window air conditioners (owned home)
    - 310110 : Black and white tv
    - 310120 : Color tv - console
    - 310130 : Color tv - portable, table model
    - 310140 : Televisions
    - 310210 : VCR''s and video disc players
    - 310220 : Video cassettes, tapes, and discs
    - 310230 : Video game hardware and software
    - 310231 : Video game software
    - 310232 : Video game players and video game accessories. Eligible game consoles are those that play games loaded from a separate media, typically an optical disk.
    - 310240 : Streaming, downloading video
    - 310243 : Rental, streaming, downloading video
    - 310311 : Radios
    - 310312 : Phonographs
    - 310313 : Tape recorders and players
    - 310314 : Personal digital audio players
    - 310316 : Stereos, radios, speakers, and sound components including those in vehicles
    - 310320 : Sound components and component systems
    - 310330 : ACCESSORIES AND OTH SOUND EQUIP
    - 310333 : Accessories and other sound equipment
    - 310334 : Satellite dishes
    - 310340 : All prerecorded audio media (other than audio books). Some audio formats, such as DVD-audio may have a relatively small portion of graphical content and still be eligible.
    - 310341 : Compact disc, tape, record and video mail order clubs
    - 310342 : Records, CDs, audio tapes, needles
    - 310350 : Streaming, downloading audio
    - 310400 : All types of applications, games, and ringtones for handheld devices. This includes "Apps" purchased directly from cell phones or online "app" stores.
    - 320110 : Room size rugs and other floor covering, nonpermanent
    - 320111 : Floor coverings, nonpermanent
    - 320120 : Window coverings
    - 320130 : Infants'' equipment
    - 320150 : Outdoor equipment
    - 320161 : Wall-to-wall carpet, not installed carpet squares (renter)
    - 320162 : Wall-to-wall carpet, not installed (replacement)
    - 320163 : Wall-to-wall carpet (replacement)(renter)
    - 320210 : Clocks
    - 320220 : Lamps and lighting fixtures
    - 320221 : Lamps, lighting fixtures, ceiling fans
    - 320230 : OTH HOUSEHOLD DECORATIVE ITEMS
    - 320231 : Other household decorative items
    - 320232 : Telephones and accessories
    - 320233 : Clocks and other household decorative items
    - 320310 : Plastic dinnerware
    - 320320 : China and other dinnerware
    - 320330 : Flatware
    - 320340 : Glassware
    - 320345 : Dinnerware, glassware, serving pieces
    - 320350 : Silver serving pieces
    - 320360 : Other serving pieces
    - 320370 : Nonelectric cookware
    - 320410 : Lawn and garden equipment
    - 320420 : Power tools
    - 320511 : Electric floor cleaning equipment
    - 320512 : Sewing machines
    - 320521 : Small electric kitchen appliances
    - 320522 : Portable heating and cooling equipment
    - 320611 : Material for insulation, other maintenance and repair
    - 320612 : Material for insulation, other maintenance and repair
    - 320613 : CONSTRUCTION MATERIALS OWNED VACATION
    - 320621 : Material for hard surface flooring
    - 320622 : Materials for hard surface flooring, repair and replacement
    - 320623 : Materials for hard surface flooring
    - 320624 : Flooring installation, repair, replacement
    - 320625 : Flooring installation, repair, replacement
    - 320626 : Flooring installation, repair, replacement
    - 320631 : Material for landscape maintenance
    - 320632 : Materials for landscaping maintenance
    - 320633 : Materials for landscaping maintenance
    - 320901 : Office furniture for home use
    - 320902 : Hand tools
    - 320903 : Indoor plants, fresh flowers
    - 320904 : Closet and storage items
    - 330511 : Termite/pest control products
    - 340210 : Babysitting and child care
    - 340211 : Babysitting and child care in your own home
    - 340212 : Babysitting and child care in someone else''s home
    - 340310 : Housekeeping services
    - 340410 : Gardening, lawn care service
    - 340420 : Water softening service
    - 340510 : Moving, storage, freight
    - 340520 : Household laundry and dry cleaning, sent out (nonclothing) not coin-operated
    - 340530 : Coin-operated household laundry and dry cleaning (nonclothing)
    - 340610 : Repair of tv, radio, and sound equipment
    - 340620 : Appliance repair, including service center
    - 340630 : Reupholstering, furniture repair
    - 340901 : Repairs/rentals of lawn and garden equipment, hand or power tools, other household equipment
    - 340902 : Rental of televisions
    - 340903 : Other home services
    - 340904 : Rental of furniture
    - 340905 : Rental of VCR, radio, and sound equipment
    - 340906 : Care for elderly, invalids, handicapped, etc.
    - 340907 : Appliance rental
    - 340908 : Rental of equipment for non business use
    - 340910 : Adult day care centers
    - 340911 : Management and upkeep services for security
    - 340912 : MANAGEMENT AND UPKEEP SERVICES FOR SECURITY OWNED VACATION
    - 340914 : Services for termite/pest control
    - 340915 : Home security system service fee
    - 350110 : Tenant''s insurance
    - 360110 : Men''s suits
    - 360120 : Men''s sportcoats, tailored jackets
    - 360210 : Men''s coats and jackets
    - 360311 : Men''s underwear
    - 360312 : Men''s hosiery
    - 360320 : Men''s nightwear
    - 360330 : Men''s accessories
    - 360340 : Men''s sweaters and vests
    - 360350 : Men''s active sportswear
    - 360410 : Men''s shirts
    - 360420 : Men's shirts, sweaters, and vests
    - 360511 : Men''s pants
    - 360512 : Men''s shorts, shorts sets
    - 360513 : Men's pants and shorts
    - 360901 : Men''s uniforms
    - 360902 : Men''s costumes
    - 370110 : Boys'' coats and jackets
    - 370120 : Boys'' sweaters
    - 370125 : Boy's shirts and sweaters
    - 370130 : Boys'' shirts
    - 370211 : Boys'' underwear
    - 370212 : Boys'' nightwear
    - 370213 : Boys'' hosiery
    - 370220 : Boys'' accessories
    - 370311 : Boys'' suits, sportcoats, vests
    - 370312 : Boys'' pants
    - 370313 : Boys'' shorts, shorts sets
    - 370314 : Boys' pants and shorts
    - 370901 : Boys'' uniforms and active sportswear
    - 370902 : Boys'' costumes
    - 370903 : Boys' uniforms
    - 370904 : Boys' active sportswear
    - 380110 : Women''s coats and jackets
    - 380210 : Women''s dresses
    - 380311 : Women''s sportcoats, tailored jackets
    - 380312 : Women''s vests and sweaters
    - 380313 : Women''s shirts, tops, blouses
    - 380315 : Women's sweaters, shirts, tops, vests
    - 380320 : Women''s skirts
    - 380331 : Women''s pants
    - 380332 : Women''s shorts, shorts sets
    - 380333 : Women's pants and shorts
    - 380340 : Women''s active sportswear
    - 380410 : Women''s sleepwear
    - 380420 : Women''s undergarments
    - 380430 : Women''s hosiery
    - 380510 : Women''s suits
    - 380901 : Women''s accessories
    - 380902 : Women''s uniforms
    - 380903 : Women''s costumes
    - 390110 : Girls'' coats and jackets
    - 390120 : Girls'' dresses and suits
    - 390210 : Girls'' shirts, blouses, sweaters
    - 390221 : Girls'' skirts and pants
    - 390222 : Girls'' shorts, shorts sets
    - 390223 : Girls' skirts, pants, and shorts
    - 390230 : Girls'' active sportswear
    - 390310 : Girls'' underwear and sleepwear
    - 390321 : Girls'' hosiery
    - 390322 : Girls'' accessories
    - 390901 : Girls'' uniforms
    - 390902 : Girls'' costumes
    - 400110 : Men''s footwear
    - 400210 : Boys'' footwear
    - 400220 : Girls'' footwear
    - 400310 : Women''s footwear
    - 410110 : Infant coat, jacket, snowsuit
    - 410111 : INFANT COAT/JACKET/SNOWSUIT 9B
    - 410112 : INFANT COAT/JACKET/SNOWSUIT 9A
    - 410120 : Infant dresses, outerwear
    - 410121 : INFANT DRESSES/OUTERWEAR 9B
    - 410122 : INFANT DRESSES/OUTERWEAR 9A
    - 410130 : Infant underwear
    - 410131 : INFANT UNDERGARMENTS 9B
    - 410132 : INFANT UNDERGARMENTS 9A
    - 410140 : Infant nightwear, loungewear
    - 410141 : INFANT NIGHTWEAR/LOUNGEWEAR 9B
    - 410142 : INFANT NIGHTWEAR/LOUNGEWEAR 9A
    - 410901 : Infant accessories
    - 410902 : INFANTS   OTHER CLOTHING
    - 410903 : INFANT ACCESSORIES 9A
    - 410904 : INFANT HOSIERY 9A
    - 420110 : Material for making clothes
    - 420115 : Material and supplies for sewing, needlework, quilting (includes household items)
    - 420120 : Sewing patterns and notions
    - 430110 : Watches
    - 430120 : Jewelry
    - 430130 : Luggage
    - 440110 : Shoe repair and other shoe service
    - 440120 : Coin-operated apparel laundry and dry cleaning
    - 440130 : Alteration, repair and tailoring of apparel and accessories
    - 440140 : Clothing rental
    - 440150 : Watch and jewelry repair
    - 440210 : Apparel laundry and dry cleaning not coin-operated
    - 440900 : Clothing storage
    - 450110 : New cars
    - 450116 : Trade-in allowance for new cars
    - 450210 : New trucks
    - 450216 : Trade-in allowance for new trucks or vans
    - 450220 : New motorcycles
    - 450226 : Trade-in allowance for new motorcycles, motor scooters, or mopeds
    - 450310 : Car lease payments
    - 450311 : Charges other than basic lease, such as insurance or maintenance (car lease)
    - 450312 : Trade-in allowance (car lease)
    - 450313 : Cash downpayment (car lease)
    - 450314 : Termination fee (car lease)
    - 450350 : Car/truck lease payments
    - 450351 : Extra fees for car/truck lease
    - 450352 : Trade in allowance for car/truck lease
    - 450353 : CASH DWNPYMNT FOR CAR/TRUCK LEASE
    - 450354 : Termination fee for car/truck lease
    - 450410 : Truck lease payments
    - 450411 : Charges other than basic lease, such as insurance or maintenance (truck/van lease)
    - 450412 : Trade-in allowance (truck/van lease)
    - 450413 : Cash downpayment (truck lease)
    - 450414 : Termination fee (truck lease)
    - 460110 : Used cars
    - 460116 : Trade-in allowance for used cars
    - 460901 : Used trucks
    - 460902 : Used motorcycles
    - 460907 : Trade-in allowance for used trucks or vans
    - 460908 : Trade-in allowance for used motorcycles, motor scooters, or mopeds
    - 470111 : Gasoline
    - 470112 : Diesel fuel
    - 470113 : Gasoline on out-of-town trips
    - 470211 : Motor oil
    - 470212 : Motor oil on out-of-town trips
    - 470220 : Coolant, brake fluid, transmission fluid, and other additives
    - 470311 : Electric vehicle charging
    - 480110 : Tires - purchased, replaced, installed
    - 480211 : PARTS/EQUIP/ACCESSORIES
    - 480212 : Vehicle products and cleaning services
    - 480213 : Parts, equipment, and accessories
    - 480214 : Vehicle audio equipment
    - 480215 : Vehicle video equipment
    - 480216 : VEHICLE CLEAN SRVCS INCL CARWASH
    - 490110 : Body work and painting
    - 490211 : Clutch, transmission repair
    - 490212 : Drive shaft and rear-end repair
    - 490220 : Brake work (old)
    - 490221 : Brake work, including adjustments
    - 490231 : Repair to steering or front-end
    - 490232 : Repair to engine cooling system
    - 490300 : Vehicle or engine repairs
    - 490311 : Motor tune-up
    - 490312 : Lube, oil change, and oil filters
    - 490313 : Front-end alignment, wheel balance
    - 490314 : Shock absorber replacement
    - 490315 : Brake adjustment (old)
    - 490317 : Minor repairs and services out of town trips
    - 490318 : Repair tires and other repair work
    - 490319 : Vehicle air conditioning repair
    - 490411 : Exhaust system repair
    - 490412 : Electrical system repair
    - 490413 : Motor repair, replacement
    - 490500 : VEHICLE ACCESSORIES INCL. LABOR
    - 490501 : Vehicle accessories including labor
    - 490502 : Vehicle audio equipment including labor
    - 490900 : Auto repair service policy
    - 500110 : Vehicle insurance
    - 510110 : Automobile finance charges
    - 510901 : Truck finance charges
    - 510902 : Motorcycle and plane finance charges
    - 520110 : Vehicle registration
    - 520310 : Drivers'' license
    - 520410 : Vehicle inspection
    - 520511 : Auto rental
    - 520512 : Auto rental, out-of-town trips
    - 520516 : Auto/truck rental
    - 520517 : Auto/truck rental, out-of-town trips
    - 520521 : Truck rental
    - 520522 : Truck rental, out-of-town trips
    - 520530 : PARKING FEES
    - 520531 : Parking fees in home city, excluding residence
    - 520532 : Parking fees, out-of-town trips
    - 520541 : Tolls or electronic toll passes
    - 520542 : Tolls on out-of-town trips
    - 520550 : Towing charges
    - 520560 : Global positioning services
    - 520901 : Docking and landing fees
    - 520902 : Motorcycle rental
    - 520903 : AIRCRAFT RENTAL
    - 520904 : Rental non-camper trailer
    - 520905 : Motorcycle rental, out-of-town trips
    - 520906 : AIRCRAFT RENTAL/OUT-OF-TOWN TR
    - 520907 : Boat and trailer rental out-of-town trips
    - 530110 : Airline fares
    - 530210 : Intercity bus fares
    - 530311 : Intracity mass transit fares
    - 530312 : Local trans. on out-of-town trips
    - 530411 : Taxi fares and limousine services on trips
    - 530412 : Taxi fares and limousine services
    - 530510 : Intercity train fares
    - 530901 : Ship fares
    - 530902 : School bus
    - 540000 : Prescription drugs
    - 550110 : Eyeglasses and contact lenses
    - 550320 : Medical equipment for general use
    - 550330 : Supportive and convalescent medical equipment
    - 550340 : Hearing aids
    - 560110 : Physician''s services
    - 560210 : Dental services
    - 560310 : Eyecare services
    - 560320 : SERV BY PRCTIONER OTH THAN PHYS
    - 560330 : Lab tests, x-rays
    - 560400 : Service by professionals other than physician
    - 560410 : Non physician services inside home
    - 560420 : Non physician services outside home
    - 560900 : NURSE/THERAPY/MISC. MEDIC SERV
    - 570110 : Hospital room
    - 570111 : Hospital room and services
    - 570210 : Hospital service other than room
    - 570220 : Care in convalescent or nursing home
    - 570230 : Other medical care service
    - 570240 : Medical care in retirement community
    - 570901 : Rental of medical equipment
    - 570903 : Rental of supportive, convalescent medical equipment
    - 580110 : COMMERCIAL HEALTH INSURANCE
    - 580111 : Traditional fee for service health plan (not BCBS)
    - 580112 : Traditional fee for service health plan (BCBS)
    - 580113 : Preferred provider health plan (not BCBS)
    - 580114 : Preferred provider health plan (BCBS)
    - 580115 : Fee for service health plan (not BCBS)
    - 580116 : Fee for service health plan (BCBS)
    - 580210 : BLUECROSS/BLUE SHIELD
    - 580310 : Health maintenance plans
    - 580311 : Health maintenance organization (not BCBS)
    - 580312 : Health maintenance organization (BCBS)
    - 580400 : Long term care insurance
    - 580401 : Long term care insurance (not BCBS)
    - 580402 : Long term care insurance (BCBS)
    - 580411 : Dental care insurance (not BCBS)
    - 580412 : Dental care insurance (BCBS)
    - 580421 : Prescription drug insurance (not BCBS)
    - 580422 : Prescription drug insurance (BCBS)
    - 580431 : Vision care insurance (not BCBS)
    - 580432 : Vision care insurance (BCBS)
    - 580441 : Vision care insurance (not BCBS)
    - 580442 : Vision care insurance (BCBS)
    - 580901 : Medicare payments
    - 580902 : COML MEDICAR SUPLMNT/OTH HLTH INS
    - 580903 : Commercial medicare supplement (not BCBS)
    - 580904 : Commercial medicare supplement (BCBS)
    - 580905 : Other health insurance (not BCBS)
    - 580906 : Other health insurance (BCBS)
    - 580907 : Medicare prescription drug premium
    - 580908 : Medicaid premiums
    - 580909 : Tricare/military premiums
    - 580910 : Tricare/military premiums
    - 590110 : Newspapers
    - 590111 : Newspaper subscriptions
    - 590112 : Newspapers, non-subscriptions
    - 590210 : Magazines
    - 590211 : Magazine subscriptions
    - 590212 : Magazines, non-subscriptions
    - 590220 : Books thru book clubs
    - 590230 : Books not thru book clubs
    - 590310 : Newspaper, magazine by subscription
    - 590410 : Newspaper, magazine non-subscription
    - 600110 : Outboard motor
    - 600121 : Boat without motor and boat trailers
    - 600122 : Trailer and other attachable campers
    - 600127 : Trade in allowance for boat without motor or non camper-type trailer, such as for boat or cycle
    - 600128 : Trade-in allowance for trailer-type or other attachable-type camper
    - 600131 : MOTORIZED CAMPER COACH/OTH VEH
    - 600132 : Purchase of boat with motor
    - 600137 : TRADE ALLOW/MOTOR CAMPER, OTH VEH
    - 600138 : Trade-in allowance for boat with motor
    - 600141 : Purchase of motorized camper
    - 600142 : Purchase of other vehicle
    - 600143 : Trade in allowance, motorized camper
    - 600144 : Trade in allowance, other vehicle
    - 600210 : Athletic gear, game tables, and exercise equipment
    - 600310 : Bicycles
    - 600410 : Camping equipment
    - 600420 : Hunting and fishing equipment
    - 600430 : Winter sports equipment
    - 600900 : Water sports and miscellaneous sports equipment
    - 600901 : Water sports equipment
    - 600902 : Other sports equipment
    - 610110 : Toys, games, arts and crafts, and tricycles
    - 610120 : Playground equipment
    - 610130 : Musical instruments and accessories
    - 610140 : Stamp and coin collecting
    - 610210 : Film
    - 610230 : Photographic equipment
    - 610320 : Pet purchase, supplies, medicine
    - 610900 : Recreation expenses, out-of-town trips
    - 620110 : CLUB MEMBERSHIP DUES AND FEES
    - 620111 : Social, recreation, health club membership
    - 620112 : Credit card memberships
    - 620113 : Automobile service clubs
    - 620114 : Automobile service clubs and GPS services
    - 620115 : Shopping club membership fees
    - 620121 : Fees for participant sports
    - 620122 : Participant sports, out-of-town trips
    - 620211 : Movie, theater, amusement parks, and other
    - 620212 : Movie, other admissions, out-of-town trips
    - 620213 : Play, theater, opera, concert
    - 620214 : Movies, parks, museums
    - 620215 : Tickets to movies
    - 620216 : Tickets to parks or museums
    - 620221 : Admission to sporting events
    - 620222 : Admission to sports events, out-of-town trips
    - 620310 : Fees for recreational lessons
    - 620320 : Photographer fees
    - 620330 : Photo processing
    - 620410 : Pet services
    - 620420 : Vet services
    - 620902 : RENTAL CAMPER/OTH VEHS ON TRIPS
    - 620903 : Other entertainment services, out-of-town trips
    - 620904 : Rental and repair of musical instruments
    - 620905 : Repair and rental of photographic equipment
    - 620906 : Rental of boat
    - 620907 : RENTAL OF CAMPERS OTHER R.V.S
    - 620908 : Rental and repair of miscellaneous sports equipment
    - 620909 : Rental of campers on out-of-town trips
    - 620912 : Rental of video cassettes, tapes, films, and discs
    - 620916 : Rental of computer and video game hardware and software
    - 620917 : Rental of video hardware/accessories
    - 620918 : Rental of video software
    - 620919 : Rental of other vehicles on out-of-town trips
    - 620921 : Rental of motorized camper
    - 620922 : Rental of other RV"s
    - 620926 : Lotteries and pari-mutuel losses
    - 620930 : Online gaming services
    - 630110 : Cigarettes
    - 630210 : Other tobacco products
    - 640130 : Wigs and hairpieces
    - 640420 : Electric personal care appliances
    - 640430 : Adult diapers
    - 650110 : Personal care service for females (old)
    - 650210 : Personal care service for males (old)
    - 650310 : Personal care services
    - 650900 : Repair of personal care appliances
    - 660110 : School books, supplies, equipment for college
    - 660210 : School books, supplies, equipment for elementary, high school
    - 660310 : Encyclopedia and other sets of reference books
    - 660410 : School books, supplies, equipment for vocational and technical schools
    - 660900 : School books, supplies, equipment for day care, nursery, preschool, other
    - 660901 : School books, supplies, equipment for day care, nursery
    - 660902 : School books, supplies, equipment for other schools
    - 670110 : College tuition
    - 670210 : Elementary and high school tuition
    - 670310 : Day care centers, nursery, and preschools
    - 670410 : Vocational and technical school tuition
    - 670901 : Other schools tuition
    - 670902 : Other school expenses including rentals
    - 670903 : Test preparation, tutoring services
    - 680110 : Legal fees
    - 680140 : Funeral expenses
    - 680210 : Safe deposit box rental
    - 680220 : Checking accounts, other bank service charges
    - 680310 : Live entertainment for catered affairs
    - 680320 : Rental of party supplies for catered affairs
    - 680901 : Cemetery lots, valuts, maintenace fees
    - 680902 : Accounting fees
    - 680904 : Dating services
    - 680905 : Vacation clubs
    - 690110 : Computers for non-business
    - 690111 : Computers and computer hardware for nonbusiness use
    - 690112 : Computer software and accessories for nonbusiness use
    - 690113 : Repair of computer systems for nonbusiness use
    - 690114 : Computer information services
    - 690115 : Personal digital assistants
    - 690116 : Internet services away from home
    - 690117 : Portable memory
    - 690118 : Digital book readers
    - 690119 : Computer software
    - 690120 : Computer accessories
    - 690210 : Telephone answering device
    - 690220 : Calculators
    - 690230 : Business equipment for home use
    - 690241 : Smoke alarms (renter)
    - 690242 : Smoke alarms (owned home)
    - 690244 : Other household appliances (renter)
    - 690245 : Other household appliances (owned home)
    - 690310 : Installation of computer
    - 690320 : Installation of televisions
    - 690330 : Installation of satellite television equipment
    - 690340 : Installation of sound systems
    - 690350 : Installation of other video equipment or sound systems
    - 700110 : Life, endowment, annuity, other personal insurance
    - 710110 : Finance charges excluding mortgage and vehicle
    - 790210 : Total purchases at grocery stores
    - 790220 : Food and nonalcoholic beverage purchases at grocery stores
    - 790230 : Food and nonalcoholic beverage purchases at convenience or specialty stores
    - 790240 : AVG FOOD/NONALC BEV EXPENSES
    - 790310 : Beer and wine for home use
    - 790320 : Other alcoholic beverages for home use
    - 790330 : BEER/WINE/OTH ALC FOR HOME USE
    - 790410 : Dining out at restaurants, cafeterias, drive-ins, etc. (excluding alcoholic beverages)
    - 790420 : Alcoholic beverages at restaurants, cafeterias, drive-ins, etc.
    - 790430 : School lunches
    - 790600 : Expenses for other properties
    - 790610 : Contractors labor and materials, supplies CU obtained, apppliances provided by contractor, other property
    - 790611 : Dishwasher, disposal, range hood capital improvement (other property)
    - 790620 : Management services and improvements of other properties
    - 790630 : Special assessments (other property)
    - 790640 : Property management, security, parking (other property)
    - 790690 : Construction materials for jobs not started
    - 790710 : Purchase price of property (other property)
    - 790720 : PURCHASE COMMONS OTH PROP
    - 790730 : Closing costs purchase of property (other property)
    - 790810 : Sale price of property or trade-in amount (other property)
    - 790820 : Mortgage held after sale of real estate (other property)
    - 790830 : Total expenses in sale of property (other property)
    - 790840 : OTHER CHARGES IN SALE OF OTHER PROPERTIES
    - 790910 : Special lump sum mortgage payments (other property)
    - 790920 : Reduction of mortgage principal (other property)
    - 790930 : Original loan amount (mortgage obtained during interview quarter) (other property)
    - 790940 : Reduction mortgage principal, home equity loan (other property)
    - 790950 : Original loan amount, home equity loan (loan obtained during interview quarter) (other property)
    - 800111 : Alimony expenditures
    - 800121 : Child support expenditures
    - 800700 : Meals as pay
    - 800710 : Rent as pay
    - 800721 : Market value of owned home
    - 800800 : CASH GIFTS/CONTRIBUTIONS
    - 800803 : Money given to non-CU members, charities, and other organizations
    - 800804 : Support for college students
    - 800811 : Gift to non-CU members of stocks, bonds, and mutual funds
    - 800821 : Cash contributions to charities and other organizations
    - 800831 : Cash contributions to church, religious organizations
    - 800841 : Cash contribution to educational institutions
    - 800851 : Cash contribution to political organizations
    - 800861 : Other cash gifts
    - 810101 : Purchase price of property (owned home)
    - 810102 : Purchase price of property (owned vacation)
    - 810201 : COMMON AREAS OWND
    - 810202 : Amount of purchase price that was for common areas owned vacation
    - 810301 : Closing costs purchase of property (owned home)
    - 810302 : Closing costs owned vacation
    - 810400 : Gifts of out of town trip expenses
    - 820101 : Sale price of property or trade-in amount (owned home)
    - 820102 : Sale price of property or trade-in amount (owned vacation)
    - 820201 : Principle amount trust held own home
    - 820202 : Principle amont of truct holding for new purchaser owned vacation
    - 820301 : Total expenses in sale of property (owned home)
    - 820302 : Total expenses in sale of property (owned vacation)
    - 820401 : OTHER SELLING CHARGES OWND
    - 830101 : Special lump sum mortgage payment (owned home)
    - 830102 : Special lump sum mortgage payment (owned vacation)
    - 830201 : Reduction of mortgage principal (owned home)
    - 830202 : Reduction of mortgage principal (owned vacation)
    - 830203 : Reduction mortgage principal, home equity loan (owned home)
    - 830204 : Reduction mortgage principal, home equity loan (owned vacation)
    - 830301 : Original loan amount (mortgage obtained during interview quarter) (owned home)
    - 830302 : Original loan amount (mortgage obtained during interview quarter) (owned vacation)
    - 830303 : Original loan amount, home equity loan (loan obtained during interview quarter) (owned home)
    - 830304 : Original loan amount, home equity loan (loan obtained during interview quarter) (owned vacation)
    - 840101 : Special assessments (owned home)
    - 840102 : Special assessments (owned vacation)
    - 850100 : Reduction of vehicle loan principal
    - 850200 : Vehicle principal balance (loan obtained during interview quarter)
    - 850300 : Other vehicle finance charges
    - 860100 : Sale of automobiles
    - 860200 : Sale of trucks, including vans
    - 860300 : AMT MOTOR CAMPER SOLD/REIM
    - 860301 : Sale of motor camper
    - 860302 : Sale of other vehicles
    - 860400 : Sale of trailer type and other attachable campers
    - 860500 : Sale of motorcycles
    - 860600 : Sale of boats, with motors
    - 860700 : Sale of boats, without motors and boat trailers
    - 860800 : Sale of aircraft
    - 870101 : New cars, trucks, or vans (net outlay), purchase not financed
    - 870102 : Cash downpayment for new cars, trucks, or vans, purchase financed
    - 870103 : Finance charges on loans for new cars, trucks, or vans
    - 870104 : Principal paid on loans for new cars,trucks, or vans
    - 870201 : Used cars, trucks, or vans (net outlay), purchase not financed
    - 870202 : Cash downpayment for used cars, trucks, or vans, purchase financed
    - 870203 : Finance charges on loans for used cars, trucks, or vans
    - 870204 : Principal paid on loans for used cars, trucks, or vans
    - 870301 : Motorcycles, motor scooters, or mopeds (net outlay), purchase not financed
    - 870302 : Cash downpayment for motorcycles, motor scooters, or mopeds, purchase financed
    - 870303 : Finance charges on loans for motorcycles, motor scooters, or mopeds
    - 870304 : Principal paid on loans for motorcycles, motor scooters, or mopeds
    - 870401 : Boat without motor or non camper-type trailer, such as for boat or cycle (net outlay), purchase not financed
    - 870402 : Cash downpayment for boat without motor, or non camper-type trailer, such as for boat or cycle, purchase financed
    - 870403 : Finance charges on loans for boat without motor or non camper- type trailer, such as for boat or cycle
    - 870404 : Principal paid on loans for boat without motor, or non camper-trailer, such as for boat or cycle
    - 870501 : Trailer-type or other attachable-type camper (net outlay), purchase not financed
    - 870502 : Cash downpayment for trailer-type or other attachable-type camper, purchase financed
    - 870503 : Finance charges on loans for trailer-type or other attachable-type camper
    - 870504 : Principal paid on loans for trailer-type or other attachable-type camper
    - 870601 : MTR CAMPER/OTHER VEH., NOT FIN.
    - 870602 : DOWNPAY, MTR CAMP/OTHER, FIN.
    - 870603 : INTEREST, MTR CAMP/OTHER, FIN.
    - 870604 : PRINCIPAL, MTR CAMP/OTHER, FIN.
    - 870605 : Purchase of motorized camper, not financed
    - 870606 : Principal, motorized camper, financed
    - 870607 : Interest, motorized camper, financed
    - 870608 : Downpayment, motorized camper, financed
    - 870701 : Boat with motor (net outlay), purchase not financed
    - 870702 : Cash downpayment for boat with motor, purchase financed
    - 870703 : Finance charges on loans for boat with motor
    - 870704 : Principal paid on loans for boat with motor
    - 870801 : Purchase of other vehicle, not financed
    - 870802 : Principal, other vehicle, financed
    - 870803 : Interest, other vehicle, financed
    - 870804 : Downpayment, other vehicle, financed
    - 880110 : Interest paid, home equity line of credit
    - 880120 : Principal paid, home equity line of credit (owned home)
    - 880210 : Interest paid, home equity line of credit (other property)
    - 880220 : Principal paid, home equity line of credit (other property)
    - 880310 : Interest paid, home equity line of credit
    - 880320 : Principal paid, home equity line of credit (owned vacation)
    - 900002 : Occupational expenses
    - 910042 : Monthly transit subsidy
    - 910050 : Estimated monthly rental value of owned home
    - 910060 : Estimated monthly rental value of time share
    - 910070 : Estimated monthly rental value of owned vacation home (excluding time share)
    - 910080 : Rent received from time share
    - 910090 : Rent received from owned vacation home
    - 910100 : Rental equivalence of vacation home
    - 910101 : Estimated monthly rental value of vacation home not available for rent
    - 910102 : Estimated monthly rental value of vacation home available for rent
    - 910103 : Estimated annual rental value of timeshare
    - 910104 : 910104 CPI ADJ RENT EQUIV OF OWNED HOME
    - 910105 : 910105 CPI ADJ RE VAC HOME NOT AVAIL RNT
    - 910106 : CPI vacation home available for rent
    - 910107 : 910107 CPI ADJ RENT EQUIV FOR TIMESHARES
    - 950024 : VEHICLE PERSONAL PROPERTY TAXES
    - 950030 : 2008 Tax stimulus
    - 990900 : Rental and installation of dishwashers, range hoods, and garbage disposals
    - 990920 : Materials for additions, finishing basements, remodeling rooms
    - 990930 : Materials to finish basement, remodel rooms or build patios, walks, etc. (maint., repair and repl. - owned properties)
    - 990940 : Materials for finishing, remolding, building patios, walks or other enclosures owned vacation
    - 990950 : Materials for dwellings under construction and additions Renter/under contruction/second home
- UCCSEQ : Sequence number of UCC in a given mapping















































### ITBI - Deatailed Monthly Income


- NEWID : Public use microdata identifier
- PUBFLAG : Is amount included in published reports?
    - 1 : Not published
    - 2 : Published in Integrated Bulletin
- REFMO : Reference Month of this expenditure
- REFYR : Reference Year of this expenditure
- UCC : Universal Classification Code
    - 001000 : Purchase price of stocks, bonds or mutual funds including broker fees
    - 001010 : Sale price stocks/bonds/mutual funds, net
    - 001210 : Invests to farm/business
    - 001220 : Assets taken from farm/business
    - 002010 : Change in savings account
    - 002020 : Change in checking account
    - 002030 : Change in amount us saving bonds
    - 003000 : Change in money owed to cu
    - 003100 : Surrender of ins policies
    - 005100 : Value of savings, checking, money market, and CDs
    - 005110 : Value of savings, checking, money market, and CDs
    - 005200 : VAL RETIREMENT PLANS
    - 005210 : VAL RETIREMENT PLANS YR AGO
    - 005300 : SURRNDR VAL WHOLE LIF POL
    - 005310 : SURRNDR VAL WHOLE LIF POL YR AGO
    - 005400 : Amount owed on credit cards
    - 005410 : Amount owed on credit cards one year ago
    - 005420 : Finance, late, interest charges for credit cards
    - 005500 : Amount owed on student loans
    - 005510 : Amount owed on student loans one year ago
    - 005520 : Finance, late, interest charges for student loans
    - 005600 : Amount owed on other loans
    - 005610 : Amount owed on other loans one year ago
    - 005620 : Finance, late, interest charges for other loans
    - 005700 : Value of other financial assets
    - 005710 : Value of other financial assets one year ago
    - 005800 : Value of stocks, bonds, mutual funds
    - 005810 : Value of stocks, bonds, mutual funds one year ago
    - 800112 : Alimony annual
    - 800122 : Child support annual
    - 800720 : MARKET VALUE OF OWNED HOME
    - 800801 : Cash contributions to non-CU members, including students, alimony, and child support (old)
    - 800802 : Cash support for college students (Sec. 22)
    - 800810 : Gifts of cash, stocks and bonds to non-CU members (old)
    - 800820 : Contributions to charity
    - 800830 : Contributions to church
    - 800840 : Contributions to educational organizations
    - 800850 : Contributions to political organizations
    - 800860 : Other contributions
    - 800910 : Deductions for government retirement
    - 800920 : Deductions for railroad retirement
    - 800931 : Deductions for private pensions
    - 800932 : Non-payroll deposit to retirement plans
    - 800940 : Deductions for Social Security
    - 900000 : Wages and salaries
    - 900001 : Occupational expenses
    - 900010 : Net business income
    - 900020 : Net farm income
    - 900030 : Social Security and railroad retirement income
    - 900040 : Pensions and annuities
    - 900050 : Dividends, royalties, estates, trusts
    - 900060 : Roomer and boarder income
    - 900070 : Other rental income
    - 900080 : Interest
    - 900090 : Supplemental security income
    - 900100 : Unemployment compensation
    - 900110 : Workers'' compensation and veterans'' benefits
    - 900120 : Public assistance
    - 900130 : REGULAR CONTRIBUTIONS FOR SUPPORT
    - 900131 : Child support payments
    - 900132 : Other regular contributions including alimony
    - 900140 : Other income
    - 900150 : Food stamps
    - 900160 : Self-employment income
    - 900170 : Retirement, survivors, disability income
    - 900180 : Interest and dividends
    - 900190 : Net room/rental income
    - 900200 : Royalty, estate, trust income
    - 900210 : Other regular income
    - 900220 : Lump sum payment received
    - 910000 : Lump sum receipts
    - 910010 : Money from sale of household furnishings, etc.
    - 910020 : Refund from overpayment on Social Security
    - 910030 : Refunds from insurance policies
    - 910040 : Refunds from property taxes
    - 910041 : Lump sum child support payment
    - 910050 : Rental equivalence of owned home
    - 920010 : Market value of all savings accounts
    - 920020 : Market value of all checking accounts
    - 920030 : Market value of all U.S. savings bonds
    - 920040 : Market value of all securities
    - 950000 : Federal income tax
    - 950001 : Federal income tax refunds
    - 950002 : Federal income tax deducted
    - 950003 : Additional federal income tax paid
    - 950004 : Federal income tax (imputed)
    - 950010 : State and local income tax
    - 950011 : State and local income tax refunds
    - 950012 : State and local income tax deducted
    - 950013 : Additional state and local income tax paid
    - 950014 : State and local income tax (imputed)
    - 950021 : Other taxes
    - 950022 : Personal property taxes
    - 950023 : Other tax refunds
    - 980000 : Income before taxes
    - 980010 : People
    - 980020 : Age of reference person
    - 980030 : Earners
    - 980040 : Vehicles (owned)
    - 980050 : Children under 18
    - 980060 : People 65 and older
    - 980070 : Income after taxes
    - 980071 : Income after taxes
    - 980090 : Percent homeowner
    - 980210 : Men
    - 980220 : Women
    - 980230 : With mortgage
    - 980240 : Without mortgage
    - 980260 : Renter
    - 980270 : Black or African-American
    - 980280 : White and other
    - 980281 : White
    - 980282 : Asian
    - 980283 : All other races
    - 980285 : Hispanic or Latino
    - 980286 : Not Hispanic or Latino
    - 980290 : Elementary (1-8)
    - 980300 : High school (9-12)
    - 980310 : College
    - 980320 : Never attended and other
    - 980330 : At least one vehicle owned
    - 980340 : At least one vehicle leased
    - 980350 : At least one vehicle owned or leased
    - 980360 : Vehicles (leased)
- VALUE : Value of UCC (Flag: VALUE_)

















































### Imputed Monthly Income

- IMPNUM : Income Imputation Iteration
    - 1 : First
    - 2 : Second
    - 3 : Third
    - 4 : Fourth
    - 5 : Fifth
- NEWID : Public use microdata identifier
- PUBFLAG : Is amount included in published reports?
    - 1 : Not published
    - 2 : Published in Integrated Bulletin
- REFMO : Reference Month of this expenditure
- REFYR : Reference Year of this expenditure
- UCC : Universal Classification Code
    - 001000 : Purchase price of stocks, bonds, mutual funds
    - 001010 : Sale price stocks/bonds/mutual funds, net
    - 001210 : Invests to farm/business
    - 001220 : Assets taken from farm/business
    - 002010 : Change in savings account
    - 002020 : Change in checking account
    - 002030 : Change in amount us saving bonds
    - 003000 : Change in money owed to cu
    - 003100 : Surrender of ins policies
    - 800112 : Alimony annual
    - 800122 : Child support annual
    - 800801 : Cash contributions to non-CU members, including students, alimony, and child support (old)
    - 800802 : Cash support for college students (Sec. 22)
    - 800810 : Gifts of cash, stocks and bonds to non-CU members (old)
    - 800820 : Contributions to charity
    - 800830 : Contributions to church
    - 800840 : Contributions to educational organizations
    - 800850 : Contributions to political organizations
    - 800860 : Other contributions
    - 800940 : Deductions for Social Security
    - 900000 : Wages and salaries
    - 900001 : Occupational expenses
    - 900010 : Net business income
    - 900020 : Net farm income
    - 900030 : Social Security and railroad retirement income
    - 900040 : Pensions and annuities
    - 900050 : Dividends, royalties, estates, trusts
    - 900060 : Roomer and boarder income
    - 900070 : Other rental income
    - 900080 : Interest
    - 900090 : Supplemental security income
    - 900100 : Unemployment compensation
    - 900110 : Workers'' compensation and veterans'' benefits
    - 900120 : Public assistance
    - 900131 : Child support payments
    - 900132 : Other regular contributions including alimony
    - 900140 : Other income
    - 900150 : Food stamps
    - 900160 : Self-employment income
    - 900170 : Retirement, survivors, disability income
    - 900180 : Interest and dividends
    - 900190 : Net room/rental income
    - 900200 : Royalty, estate, trust income
    - 900210 : Other regular income
    - 910000 : Lump sum receipts
    - 910010 : Money from sale of household furnishings, etc.
    - 910020 : Refund from overpayment on Social Security
    - 910030 : Refunds from insurance policies
    - 910040 : Refunds from property taxes
    - 910041 : Lump sum child support payment
    - 920010 : Market value of all savings accounts
    - 920020 : Market value of all checking accounts
    - 920030 : Market value of all U.S. savings bonds
    - 920040 : Market value of all securities
    - 950000 : Federal income tax
    - 950001 : Federal income tax refunds
    - 950002 : Federal income tax deducted
    - 950003 : Additional federal income tax paid
    - 950010 : State and local income tax
    - 950011 : State and local income tax refunds
    - 950012 : State and local income tax deducted
    - 950013 : Additional state and local income tax paid
    - 950022 : Personal property taxes
    - 950023 : Other tax refunds
    - 980000 : Income before taxes
    - 980070 : Income after taxes
    - 980071 : Income after taxes
    - 980280 : White and other
- VALUE : Value of UCC (Flag: VALUE_)
















### NTAXI - Estimated State and Federal Income Taxes

- ADDTX_CY : Additional Child Tax Credit, current year
- ADDTX_PY : Additional Child Tax Credit, prior year
- AGE_SP : Age of spouse (or zero). Variable 6 in TaxSim model.
- AGE_TP : Age of tax payer (or zero). Variable 6 in TaxSim model.
- AMTDEDCT : Itemized deductions with Alternative Minimum Tax (AMT) preference (Flag: AMTD_DCT)
- AMTIN_CY : Income for the Alternative Minimum Tax, current year
- AMTIN_PY : Income for the Alternative Minimum Tax, prior year
- AMTOW_CY : Alternative Minimum Tax (AMT) Liability, current year
- AMTOW_PY : Alternative Minimum Tax (AMT) Liability, prior year
- CHDTX_CY : Child Tax Credit, current year
- CHDTX_PY : Child Tax Credit, prior year
- CHLDCARE : Child care expenses (Flag: CHLD_ARE)
- DEPCNT : Count of dependents in tax unit
- DEPUND13 : Count of dependents in the tax unit whose ages are less than 13
- DEPUND17 : Count of dependents in the tax unit whose ages are less than 17 (Flag: DEPU_D17)
- DEPUND18 : Count of dependents in the tax unit whose ages are less than 18
- DIVINC : Dividend income
- DPCAR_CY : Dependent Care Credit, current year
- DPCAR_PY : Dependent Care Credit, prior year
- EITCR_CY : Earned income tax credit, current year
- EITCR_PY : Earned income tax credit, prior year
- FDAGI_CY : Federal AGI, current year
- FDAGI_PY : Federal AGI, prior year
- FICA_CY : Federal Insurance Contributions Act (FICA) - US payroll tax, * current year
- FICA_PY : Federal Insurance Contributions Act (FICA) - US payroll tax, * prior year
- FICAR_CY : FICA rate current year
- FICAR_PY : FICA rate previous year
- FILESTAT : Filing Status
- FRATE_CY : Federal marginal rate current year
- FRATE_PY : Federal marginal rate previous year
- FRGTX_CY : Amount of tax owed based on AGI, current year (before any credits and excluding AMT)
- FRGTX_PY : Amount of tax owed based on AGI, prior year (before any credits and excluding AMT)
- FTAXO_CY : Federal income tax liability after all credits, current year
- FTAXO_PY : Federal income tax liability after all credits, prior year
- FTAXOWE : Weighted estimate for Federal tax liabilities at the Tax Unit Level
- FTXBC_CY : Federal Income tax before credits, current year (before credits and including AMT)
- FTXBC_PY : Federal Income tax before credits, prior year (before credits and including AMT)
- NEWID : Public use microdata identifier
- NONTXINC : Other non-taxable transfer income (Flag: NONT_INC)
- OTHDEDCT : Non AMT itemized deductions (Flag: OTHD_DCT)
- OTHTXINC : Other taxable income (Flag: OTHT_INC)
- PROPTXPD : Property taxes paid (Flag: PROP_XPD)
- RNTPAID : Rent paid (used for calculating state property tax rebates) (Flag: RNTPAID_)
- SDCAR_CY : State dependent care credit, current year
- SDCAR_PY : State dependent care credit, prior year
- SEITC_CY : State earned income credit, current year
- SEITC_PY : State earned income credit, prior year
- SITDD_CY : State itemized deduction amount, current year
- SITDD_PY : State itemized deduction amount, prior year
- SOI_ST : Statistics of income state code (Flag: SOI_ST_)
- SOSSECB : Social security benefits (Flag: SOSSECB_)
- SPRCR_CY : State property tax credit, current year
- SPRCR_PY : State property tax credit, prior year
- SRATE_CY : State marginal rate current year
- SRATE_PY : State marginal rate previous year
- SSTDD_CY : State standard deduction amount, current year
- SSTDD_PY : State standard deduction amount, prior year
- STAGI_CY : State AGI, current year
- STAGI_PY : State AGI, prior year
- STAXO_CY : State income tax liability after all credits, current year
- STAXO_PY : State income tax liability after all credits, prior year
- STAXOWE : Weighted estimate for State tax liabilities at the Tax Unit Level
- TAX_UNIT : Identifies which tax unit the member was placed in (Flag: TAX__NIT)
- TAXPENS : Taxable pensions (Flag: TAXPENS_)
- TAXYR_CY : The year that tax will be calculated for, current year
- TAXYR_PY : The year that tax will be calculated for, previous year
- WAGE_HD : Wage and salary income of taxpayer (Flag: WAGE_HD_)
- WAGE_SP : Wage and salary income of taxpayer's spouse (Flag: WAGE_SP_)
- WAGE_SP : Wage and salary income of taxpayer's spouse (Flag: WAGE_SP_)
- WAGE_SP : Wage and salary income of taxpayer's spouse (Flag: WAGE_SP_)










