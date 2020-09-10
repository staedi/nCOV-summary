![](https://img.shields.io/github/last-commit/staedi/nCOV-summary/master) ![](https://img.shields.io/github/commit-activity/w/staedi/nCOV-summary)

# nCOV-summary
Novel COVID-19 virus summary dataset which is updated daily at 4PM KST(GMT+9)

## Data Sources
* [Johns Hopkins University CSSE](https://github.com/CSSEGISandData/COVID-19): Prime source for global Novel COVID-19 status
* [KCDC](http://ncov.mohw.go.kr): South Korea CDC for daily snapshot covering provincial detailed data

## Statistics
* *Cumulative* Measures: Cumulative figures from the inception
  * `Confirmed`: Total infections in a state (when applicable), otherwise in the country as a whole
  * `Deaths`: Total casualties in a state (when applicable), otherwise in the country as a whole 
  * `Tot_Confirmed`: Total infections in a country
  * `Tot_Deaths`: Total casualties in a country
* *Incremental* Measures: Daily changes
  * `i_Confirmed`: Daily incremental infections in a state (when applicable), otherwise in the country as a whole
  * `i_Deaths`: Daily incremental casualties in a state (when applicable), otherwise in the country as a whole 
  * `iTot_Confirmed`: Daily incremental infections in a country
  * `iTot_Deaths`: Daily incremental casualties in a country
* *Per-population* Measures: Above measures are recalculated by `100,000` populations
  * `rConfirmed`: Per-100K cumulative infections in a state (when applicable), otherwise in the country as a whole
  * `rDeaths`: Per-100K cumulative casualties in a state (when applicable), otherwise in the country as a whole 
  * `rTot_Confirmed`: Per-100K cumulative infections in a country
  * `rTot_Deaths`: Per-100K cumulative casualties in a country
  
  * `ri_Confirmed`: Per-100K daily infections changes in a state (when applicable), otherwise in the country as a whole
  * `ri_Deaths`: Per-100K daily casualties changes  in a state (when applicable), otherwise in the country as a whole 
  * `riTot_Confirmed`: Per-100K daily infections changes in a country
  * `riTot_Deaths`: Per-100K daily casualties changes in a country

## Generation Schemes
* Only recent *60-days* data are retained to keep the file size reasonable
* Every countries which have *state-level* data from [Johns Hopkins University CSSE](https://github.com/CSSEGISandData/COVID-19) daily dataset contain those data in addition to selected countries in original **summary** dataset (e.g., India, Peru among others are added)
* South Korean dataset are expanded using [KCDC](http://ncov.mohw.go.kr) daily snapshot to include provincial-level status
* US data has been merged into state-level rather than retaining county and much detailed level infos
