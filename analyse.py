#! /usr/bin/env python3
import os
import pandas as pd
import numpy as np
from collections import defaultdict

ids = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']

results = defaultdict(list)
for id_ in ids:
    for year in ['2020', '2021']:
        if year == '2020':
            months = range(9, 13)
        else:
            months = range(1, 13)
        for month in months:
            csv_id = f'{id_}-{month}-{year}'
            df = pd.read_csv(os.path.join(csv_id, f'{csv_id}.csv'), header=None)
            wh = np.sum(df.values[:, 0]) / 60
            print(f'{csv_id} {wh:.4f}')
            results[f'{month}-{year}'].append((id_, wh))

for month, whs in results.items():
    lowest_4 = sorted(whs, key=lambda t: t[1])[:8]
    result_str = ', '.join([f'({e[0]}, {e[1]:.2f})' for e in lowest_4])
    print(f'{month}: {result_str}')

