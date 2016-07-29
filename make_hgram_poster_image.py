def main():
  import json_scripts
  import numpy as np

  # hgram = json_scripts.load_to_dict('hgram_data_latest/hgram_latest.json')
  # hgram['mat'] = np.asarray(hgram['mat'])
  # print(hgram.keys())
  # print(type(hgram['mat']))
  # print(hgram['mat'].shape)

  gene_classes = json_scripts.load_to_dict('gene_classes_harmonogram.json')

  print(gene_classes.keys())

  keep_types = ['TF', 'GPCR', 'IC', 'KIN']

  keep_genes = []

  for inst_class in gene_classes:
    if inst_class in keep_types:

      inst_genes = gene_classes[inst_class]
      keep_genes.extend(inst_genes)

      print(inst_class)
  print(len(keep_genes))

main()