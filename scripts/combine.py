output = ""

sources = ['Training_Data/fce/fce.dev.gold.bea19.src',
'Training_Data/fce/fce.train.gold.bea19.src',
'Training_Data/lang8/lang8.train.auto.bea19.src',
'Training_Data/nucle/nucle.train.gold.bea19.src',
'Training_Data/wi+locness/A.train.gold.bea19.src',
'Training_Data/wi+locness/B.train.gold.bea19.src',
'Training_Data/wi+locness/C.train.gold.bea19.src']

targets = ['Training Data_m2/fce/fce.dev.gold.bea19.tgt',
'Training_Data/fce/fce.train.gold.bea19.tgt',
'Training_Data/lang8/lang8.train.auto.bea19.tgt',
'Training_Data/nucle/nucle.train.gold.bea19.tgt',
'Training_Data/wi+locness/A.train.gold.bea19.tgt',
'Training_Data/wi+locness/B.train.gold.bea19.tgt',
'Training_Data/wi+locness/C.train.gold.bea19.tgt']

for file in sources:
    with open(file) as f:
        data = f.read() + "\n"
        output += data

with open ('combined_train.src', 'w') as fp:
    fp.write(output)

output = ""

for file in targets:
    with open(file) as f:
        data = f.read() + "\n"
        output += data

with open ('combined_train.tgt', 'w') as fp:
    fp.write(output)

