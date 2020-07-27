import csv
from io import StringIO
#import matplotlib.pyplot as plt
import pandas as pd
import requests
#import seaborn as sns
import os

def get_data(animal_taxon, directory_path):
    #create directory to save files
    directory = str(animal_taxon) + '_data'
    path = os.path.join(directory_path, directory)
    os.mkdir(path)


    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
    'result': 'read_run',
    'query': 'tax_tree('+ str(animal_taxon)+')',
    'fields': 'scientific_name,tax_id,study_accession,study_alias,study_title,sample_accession,sample_alias,accession,secondary_sample_accession,run_accession,base_count,read_count,description,experiment_title,instrument_platform,instrument_model,library_source,library_selection,library_layout,library_name,library_strategy,sequencing_method,sample_description,sample_title,sex,cell_type,tissue_type,first_public,last_updated,fastq_galaxy,fastq_ftp,sra_ftp,sra_galaxy,submitted_ftp,submitted_galaxy,project_name',
    'format': 'tsv'
    }

    response = requests.post('https://www.ebi.ac.uk/ena/portal/api/search', headers=headers, data=data)

    data = StringIO(response.text)
    df = pd.read_csv(data, sep = '\t')

  #return some information about the libraries
    print(pd.value_counts(df['library_source']))
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



    df.to_csv(os.path.join(path, str(animal_taxon)+'_database.csv'))
    multiple_runs.to_csv(os.path.join(path, str(animal_taxon)+'_multiple_runs.csv'))
    multiple_samples.to_csv(os.path.join(path, str(animal_taxon)+'_multiple_samples.csv'))
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
    """
    animal_and_directory = req
    animal = req.split(",")[0]
    directory = req.split(",")[1]
    return get_data(animal, directory)
