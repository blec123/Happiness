# Happiness

## Motivation

In this repository for the Udacity Data Scientist degree first I was wondering about what data to take a look at. After some thoughts I ended up with happiness. Because what's more important than happiness, right?

Next I thought what might be relevant for that. So I ended up with a rather economical and job related view and also a context to politics. I know there is a lot more, but I had to start somewhere.

## Project Overview

Next I started to look at data, and the most sufficient I found was the Eouropean Social Studies, which every two years from 2002 to 2018 questioned several 100k europeans from different countries about their life, happiness and so on... all freely available as csv :) I supported that with the world bank data for a GDP per Capita and got started.

ESS from https://www.europeansocialsurvey.org/downloadwizard/

GDP per Capita: https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD?end=2020&start=2003&view=map

I asked three main questions:

1. What is the relation betwteen happiness and income?
2. What is the relation between happiness and other professional factors, like education, working hours, etc.
3. What is the relation between happiness, economics and the trust of people in politics, and official institutions.

For each of those three questions I made a notebook:

Happiness_and income.ipynb
Happiness_and_other_job_related_matters.ipynb
Happiness_and_politics.ipynb

The main import and a first data sorting is done in the import_prep.py .

Other files are:

  ESS1-9e01_1.zip:      ESS-dataset zipped, becuse too big as csv. Has to be unzipped to work
  
  GDPPerCapita.csv:     csv with the gdp per capita data from the world bank
  
  Gini_coefficient.csv: csv with gini coefficient from world bank (unfortunetly did not have the time to use it anymore)
  
  Inflation.csv:        csv with inflation data (unfortunetly same here, did not have enough time to take it into account)
  
  U.S._Crude_Oil_First_Purchase_Price.csv: csv of crude oil prices world market
  
  income.png:           income range for first three rounds of ESS data
  
  codebook.html:        explanation of ESS variables
  
  

  ## Results
  
  Answer 1:
  
  I could find out, that there is a relation between happiness and income. In general a higher income goes along with higher happiness in average. For the variance of the     happiness the opposite is true. The increase of happiness over income however slows down the higher the income groups are (looks a bit like logarithm). This so far is based on the country depend data, and the income groups are decils within a country.
  Looking cross countries though above certain threshold of $ 30k -40k GDP per capita, there cannot be seen an increase in happiness anymore. So it seems
  comparing the results, that above the mentioned threshold it is a lot more important what you have in comparison to people you relate to within your own country, than what you totally got.
  
  Answer 2:
  
  There is a realtion between education and happiness. In average the higher the educational level the happier people are. But higher education also in average relates to a higher income. The same is true for the level of self organization at work. So its hard to tell, which of those causes the higher happiness and which is rather a side effect.
  To me surprisingly the weekly working hours have only a very slim affect on happiness. People who work 40 or more hours seem a bit less happy than those who work under 40h per week, but the effect is rathe marginal compared to the other factors.
  
  Generally I could observe, that the lower the average happiness, the higher is its variance. So generally speaking considering all those factors, there seems to be a significatn number of people who are happy independently of there financial status, education or other matters, whereas another part seem to have strong dependency on them.
  
  Answer 3:
  
  In general it can be stated, that the trust in institutions is not very high. Police and legal system have the highest level of trust, parliament and EU in the middle, but politicians and parties most people do not trust very much.
  Compared to happiness, people who are happier have a higher trust in public affairs than those who are less happy. This states true for all six. Looking at the icome the same is true besides parties and politicians. There the average income drops significantly at very high trust levels.
  Also, people see themselves as rather moderate seem to have a higher income than those on the extreme left or right wing.
  There also is a relationship between trust in public affairs and the change of GDP per capita. As soon as there is a crisis and the gdp per capita drops or stays the same, the trust goes down rapidly, but takes a lot longer to pick up again. Nevertheless these situations surprisingly do not really seem to have an influence on the general happiness of people.
