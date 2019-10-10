import argparse

import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split

from utils import preprocess_sent

parser = argparse.ArgumentParser()
parser.add_argument('json_file')
parser.add_argument('--test_size', type=float, default=0.2)
parser.add_argument('--random_state', type=int, default=42)
parser.add_argument('--train_set', default='train.tsv')
parser.add_argument('--test_set', default='test.tsv')

if __name__=='__main__':
    args = parser.parse_args()

    df = pd.read_json(args.json_file)
    lines = []
    for idx, item in tqdm(df.iterrows()):
        s1 = preprocess_sent(item.question)
        s2 = preprocess_sent(item.text)
        label = str(int(item.label))
        line = '%s\t%s\t%s\n' % (label, s1, s2)
        lines.append(line)
    
    train, test = train_test_split(lines, test_size=args.test_size, random_state=args.random_state)
    
    with open(args.train_set, 'w') as f:
        f.writelines(train)

    with open(args.test_set, 'w') as f:
        f.writelines(test)
