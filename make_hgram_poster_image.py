import json_scripts

def main():

  ini_df = load_hgram_matrix()

  gene_classes = load_gene_classes()

  make_viz(ini_df, gene_classes)

def make_viz(ini_df, gene_classes):
  print('make visualization')

def load_hgram_matrix():
  import numpy as np
  import pandas as pd

  hgram = json_scripts.load_to_dict('hgram_data_latest/hgram_latest.json')
  hgram['mat'] = np.asarray(hgram['mat'])

  mat = hgram['mat']
  row_names = hgram['nodes']['row']
  col_names = hgram['nodes']['col']

  # nodes, and mat
  ini_df = pd.DataFrame(data=mat, columns=col_names, index=row_names)

  return ini_df

def load_gene_classes():
  gene_classes = json_scripts.load_to_dict('gene_classes_harmonogram.json')

  keep_types = ['TF', 'GPCR', 'IC', 'KIN']

  keep_genes = []

  for inst_class in gene_classes:
    if inst_class in keep_types:

      inst_genes = gene_classes[inst_class]
      keep_genes.extend(inst_genes)

  return gene_classes


main()