# Om
Dette en analyse af vejr data i La Fortuna Costa Rica. Analysen har til formål at give estimat på, hvor ofte vulkanen Arenal er synlig. Hvis skydækket er mere end 50% tror jeg ikke at der er de store chancer for at kunne se vulkanen og hvis skydækket er 25% eller mindre tror jeg at der er god mulighed for at kunne se vulkanen. 
Python scriptet er lavet med henblik på at være meget simpelt og let at kunne tilpasse til at lave en rapport om skydække, udfra csvfiler med vejr data hentet fra open-meteo.

## La Fortuna - skydække rapport
```
Gennemsnitligt skydække i 2024: 84.15%
Timer i 2024 med 25-50% skydække: 438   svarende til: 5.98%
Timer i 2024 med  0-25% skydække: 152   svarende til: 2.08%

Gennemsnitligt skydække i 2023: 87.07%
Timer i 2023 med 25-50% skydække: 270   svarende til: 3.08%
Timer i 2023 med  0-25% skydække: 50    svarende til: 0.57%

Gennemsnitligt skydække i 2022: 80.88%
Timer i 2022 med 25-50% skydække: 609   svarende til: 6.95%
Timer i 2022 med  0-25% skydække: 865   svarende til: 9.87%
```
### Rapport data
Til rapporten brugt datasættene:
    *'lafortuna_jan01_okt31_2024.csv'*
    *'lafortuna_jan01_dec31_2023.csv'*
    *'lafortuna_jan01_dec31_2022.csv'*

# Vedr. data
Dataene om skydække er hentet fra

https://open-meteo.com/en/docs/historical-weather-api

Der ligger tre andre dataset der kun er for februar - den måned hvor der er flest besøgende i La Fortuna?


## Til at genskabelse af data
Naviger til ovenstående hjemmeside og:
- 	søg efter "la fortuna" - vælg: "La Fortuna Procincia de Alajuela (10.47N, -85.65E)"
- 	timezone er ikke sat "Not set (GMT+0)
- 	vælg: "Start Date" og "End Date"
-   fjern flueben i 'temperature'
-   tilføj flueben i 'Cloud cover Total'
- 	længere nede på siden kan data downloades som en csvfil. 


## Generer rapport
	For at generere en rapport, som ovenstående, (kræver python 'wheather_analysis.py' er lavet med python version 3.12.3) skal csv filen gemmes sammen med i samme mapper (som de andre "lafortuna_..._'årstal'.csv), kan python scriptet lave en repport ved at:
	indlæs dataen fra csv filen - kopier og tilpas som linje 57-57 i 'weather_analysis.py'. Rapporten printes ved at kopiere og tilpasse som linje 62-64 i 'weather_analysis.py'. Kør scriptet.

