
awk -f awkscript.awk < Dataset-historic.csv | sed -n '/USA/p'
awk -f awkscript.awk < Dataset-historic.csv | sed -n '/Brazil/p'