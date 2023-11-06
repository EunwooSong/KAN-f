import sys
import pandas as pd
from kan_f import convert_text
from sklearn.model_selection import train_test_split

p = sys.argv[1]
n = sys.argv[2]

try:
    p = float(p)
    n = int(n)
except ValueError:
    print('Insufficient arguments')
    sys.exit()

p = float(p)
n = int(n)
train_file_name = f'train/train_p_{p}_n_{n}.tsv'
test_file_name = f'test/test_p_{p}_n_{n}.tsv'
print(f"file name is '{train_file_name}' and '{test_file_name}'.")

# 데이터 읽기
df = pd.read_csv('origin.tsv', delimiter='\t')

# 데이터 분활하기 (랜덤하게 0.125)
train_df, test_df = train_test_split(df, test_size=0.125, random_state=42)
new_train_df = {'ko': [], 'en': []}
new_test_df = {'ko': [], 'en': []}

# 데이터 변환하기
for index, row in train_df.iterrows():
    new_train_df['ko'].append(row['ko'])
    new_train_df['en'].append(row['en'])
    for i in range(n):
        new_train_df['ko'].append(convert_text(row['ko'], p, 1)[0])
        new_train_df['en'].append(row['en'])

for index, row in test_df.iterrows():
    new_test_df['ko'].append(row['ko'])
    new_test_df['en'].append(row['en'])
    for i in range(n):
        new_test_df['ko'].append(convert_text(row['ko'], p, 1)[0])
        new_test_df['en'].append(row['en'])

# 데이터 저장하기
new_train_df = pd.DataFrame(new_train_df)
new_test_df = pd.DataFrame(new_test_df)

new_train_df.to_csv(train_file_name, sep='\t', index=False)
new_test_df.to_csv(test_file_name, sep='\t', index=False)