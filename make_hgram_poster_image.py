import json_scripts
import numpy as np
import pandas as pd

def main():

  ini_df = load_hgram_matrix()

  gene_classes = load_gene_classes()

  # # make hgram viz with four gene types and no categories
  # make_viz_no_cats(ini_df, gene_classes)

  make_viz_with_cats(ini_df, gene_classes)

def make_viz_with_cats(ini_df, gene_classes):

  keep_rows = get_4_fam_genes(gene_classes)

  inst_df = ini_df.ix[keep_rows]

  inst_rows = inst_df.index.tolist()
  inst_cols = inst_df.columns.tolist()

  print(len(inst_rows))
  print(len(inst_cols))

  new_rows = []
  # add row categories
  for inst_row in inst_rows:
    inst_row =  'Gene: ' + inst_row
    inst_type = 'Type: type'
    inst_tuple = (inst_row, inst_type)

    new_rows.append(inst_tuple)

  # make new dataframe
  mat = inst_df.values
  col_names = inst_df.columns.tolist()

  new_df = pd.DataFrame(data=mat, columns=col_names, index=new_rows)

  make_viz_json(new_df, 'hgram_4_fam_with_cats.json')

def make_viz_no_cats(ini_df, gene_classes):

  keep_rows = get_4_fam_genes(gene_classes)

  inst_df = ini_df.ix[keep_rows]

  make_viz_json(inst_df, 'hgram_4_fam_no_cats.json')

def get_4_fam_genes(gene_classes):
  keep_rows = gene_classes['TF']
  keep_rows.extend(gene_classes['KIN'])
  keep_rows.extend(gene_classes['GPCR'])
  keep_rows.extend(gene_classes['IC'])
  keep_rows = list(set(keep_rows))

  return keep_rows


def make_viz_json(inst_df, name):
  from clustergrammer import Network
  net = Network()

  filename = 'json/'+name
  load_df = {}
  load_df['mat'] = inst_df
  net.df_to_dat(load_df)
  net.swap_nan_for_zero()
  net.make_clust(views=[])
  net.write_json_to_file('viz', filename, 'no-indent')

def load_hgram_matrix():
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