import pickle as pkl
import pandas as pd
import shutil
import os

def clean():
    print('cleaning htmlLibrary and librarianTools...')
    shutil.rmtree('./htmlLibrary')
    shutil.rmtree('./librarianTools')

def make_df():
    currentDir = os.getcwd()
    os.chdir('htmlLibrary')
    df = pd.DataFrame()
    print('building df...')
    for f in os.listdir():
        row = {}
        dlList = pkl.load(open(f, 'rb'))
        for dl in dlList:
            row['Link'] = dl.link
            row['epochTimeScraped'] = dl.epochTimeScraped
            row['utcTimeScraped'] = dl.utcTimeScraped
            row['Html'] = dl.html
            df = df.append(row, ignore_index=True)
    os.chdir(currentDir)
    return df

def make_csv(filename):
    if filename.split('.')[-1] != 'csv':
        filename += '.csv'
    print('building', filename)
    df = make_df()
    df.to_csv(filename, index=False)
