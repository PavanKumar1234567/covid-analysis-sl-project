top3.png top3states.png pie_brazil.png pie_india.png pie_usa.png pie_karnataka.png pie_Maharastra.png pie_kerala.png deaths_male_vs_female.png: covid_analysis.py WHO-COVID-19-global-data.csv top3data.csv top3male_female.csv covid_19_india.csv Dataset-historic.csv
	python3 covid_analysis.py

top3male_female.csv: awkscript.awk preprocess.sh Dataset-historic.py
	./preprocess.sh < Dataset-historic.csv >top3male_female.csv
