import csv
from io import StringIO
#import matplotlib.pyplot as plt
import pandas as pd
#import requests
#import seaborn as sns
#import os

def get_data(db_url):
    df = pd.read_csv(db_url, sep = ',')

  #return some information about the libraries
    print("Source database information:\n")
    print(df.info())
    print("Library source: \n")
    print(pd.value_counts(df['library_source']))
    print("\nLibrary strategy:\n")
    print(pd.value_counts(df['library_strategy']))




    multiple_runs = df['run_accession'].value_counts()
    multiple_runs = multiple_runs[multiple_runs.gt(1)]

    multiple_samples = df['sample_accession'].value_counts()
    multiple_samples = df[df['sample_accession'].isin(multiple_samples.index[multiple_samples.gt(1)])][['study_accession','sample_accession']]
    multiple_samples['count'] = multiple_samples.groupby(['sample_accession'])['study_accession'].transform('count')
    multiple_samples = multiple_samples.drop_duplicates().sort_values(by= 'count', ascending=False).reset_index(drop=True)

  #sample_plot = sns.barplot(data = multiple_samples, x = 'sample_accession', y = 'count', palette = 'muted') 
  #plt.xticks(rotation=90)

  #plt.show()


    print("\nMultiple run accessions:\n") 
    print(multiple_runs)
    print("\nMultiple sample accessions per study:\n")
    print(multiple_samples)
    
    return()
  #plot the library information
'''
  sns.countplot(x = df['library_strategy'], palette= 'muted')
  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.savefig(os.path.join(path, str(animal_taxon)+'_library_strategy.png'))
  sns.countplot(x = df['library_source'], palette= 'muted')
  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.savefig(os.path.join(path, str(animal_taxon)+'_library_source.png'))
  return()'''

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    
    animal_and_directory = req
    animal = req.split(",")[0]
    directory = req.split(",")[1]"""
    return get_data(req)
