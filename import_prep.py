# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:16:47 2022

@author: BLECHNE
"""
import pandas as pd

def file_importer(list_of_countries):

    # Read in datasets
    ess_base = pd.read_csv('Ess1-9e01_1.csv')
    infl = pd.read_csv('Inflation.csv')
    gdp = pd.read_csv('GDPPerCapita.csv')
    gini_base = pd.read_csv('Gini_coefficient.csv').set_index('Country Name')
    # list of relevant years for GDP data

    list_of_years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    
    gdp_data = gdp.loc[gdp['Country Name'].isin(list_of_countries),  ['Country Name'] + list_of_years].set_index('Country Name').transpose()
    
    gdp_growth_data = pd.DataFrame(index=list_of_years)

    # Get growth rates for all countries
    
    for column in gdp_data.columns:
        gdp_growth_data[column + '_growth'] = gdp_data[column].pct_change()
        
    # Prepare ESS survey data
    
    replace_country_dict = {'BE': 'Belgium', 'CH': 'Switzerland', 'DE': 'Germany', 'ES': 'Spain', 'FI': 'Finland', 'FR': 'France',
                        'GB': 'United Kingdom', 'HU': 'Hungary', 'IE': 'Ireland', 'NL': 'Netherlands', 'NO': 'Norway',
                        'PL': 'Poland', 'PT': 'Portugal', 'SI': 'Slovenia', 'SE': 'Sweden'}

    replace_year_dict = {'ESS1e06_6': '2002', 'ESS2e03_6': '2004', 'ESS3e03_7': '2006', 'ESS4e04_5': '2008', 'ESS5e03_4': '2010',
                     'ESS6e02_4': '2012', 'ESS7e02_2': '2014', 'ESS8e02_2': '2016', 'ESS9e03': '2018'}

    rename_columns_dict = {'cntry': 'country', 'name': 'year', 'idno': 'RespondentID',
        'ppltrst': 'Trust people', 'pplfair': 'People fair', 'pplhlp': 'People helpful', 'trstprl': 'Trust parliament',
        'trstlgl': 'Trust Legal', 'trstplc': 'Trust police', 'trstplt': 'Trust politicians',
        'trstprt': 'Trust parties', 'trstep': 'Trust EU', 'trstun': 'Trust UN',
        'lrscale': 'Left Right', 'stflife': 'Satisfied with life', 'stfeco': 'Satisfied with economy', 'stfgov': 'Satisfied with gov',
        'stfdem': 'Satisfied with democracy', 'stfedu': 'Satisfied with eductation', 'gincdif': 'More equality',
        'euftf': 'EU unification', 'happy': 'Happiness', 'atchctr': 'Attached to country', 'atcherp': 'Attached to EU',
        'hhmmb': 'Num ppl household', 'gndr': 'Gender', 'agea': 'Age', 'emplrel': 'Employment Relation',
        'eisced': 'Highest education Norm', 'wkdcorg': 'Self organize work 1',
        'wkdcorga': 'Self organize work 2-9', 'wkhtot': 'Time at work', 'hinctnt': 'Net income 1-3',
        'hinctnta': 'Net income 4-9', 'hincfel': 'Happy with income'}

    ess_pp1 = ess_base.replace(replace_country_dict).replace(replace_year_dict).rename(columns=rename_columns_dict)
    
    # Setting up replacment dicts

    replace_edu_dict = {1 : 'ES-ISCED I', 2 : 'ES-ISCED II', 3 : 'ES-ISCED IIIb', 4 : 'ES-ISCED IIIa',
                        5 : 'ES-ISCED IV', 6 : 'ES-ISCED V1', 7 : 'ES-ISCED V2' }
    replace_employment_dict = {1 : 'Employee', 2 : 'Self-employed', 3 : 'Working for own family business' }
    reaplace_gender_dict = {1 : 'Male', 2 : 'Female'}
    replace_happy_income_dict = {1 : 'Living comfortly', 2 : 'Doing ok', 3 : 'Having some trouble', 4 : 'Having big difficulties'}
    
    
    # Replacing values
    
    ess_pp1['Highest education Norm'] = ess_pp1['Highest education Norm'].map(replace_edu_dict)
    ess_pp1['Employment Relation'] = ess_pp1['Employment Relation'].map(replace_employment_dict)
    ess_pp1['Gender'] = ess_pp1['Gender'].map(reaplace_gender_dict)
    ess_pp1['Happy with income'] = ess_pp1['Happy with income'].map(replace_happy_income_dict)
    
    # Prepare gini coefficient data 
    
    gini_rel = gini_base[gini_base.index.isin(list_of_countries)]
    gini_rel = gini_rel[ess_pp1['year'].unique()]
    
    
    return ess_pp1, gdp_data, gdp_growth_data, infl, gini_rel