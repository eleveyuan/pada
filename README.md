# pada

pada is an onomatopoeia, like the sound we make when building blocks.

a ligthweight feature manage framework

1. load_data: load data
2. feature definition: metadata, input data, transform
3. assemble: construct


## pada command line generates the project directory

```
project
|---definition
|  |-feats_def.py
|---load_data.py
|---main.py
|---url.py    
```

## tutorial

### load_data.py
define a function named *data()*, return your data which is a pd.DataFrame

### url.py
find your feature definition by *url()* function

### main.py
run your feature engeering by *run()* function

