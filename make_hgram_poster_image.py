def main():
  import json_scripts
  import numpy as np

  hgram = json_scripts.load_to_dict('hgram_data_latest/hgram_latest.json')
  hgram['mat'] = np.asarray(hgram['mat'])

  print(hgram.keys())

  print(type(hgram['mat']))
  print(hgram['mat'].shape)

  gene_classes = json_scripts.load_to_dict('gene_classes_harmonogram.json')

  print(gene_classes.keys())

  print(len(hgram['nodes']['row']))

main()