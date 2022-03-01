# pada

![GitHub](https://img.shields.io/github/license/eleveyuan/pada) ![python3](https://img.shields.io/badge/langs-python3-blue)

pada is an onomatopoeia, like the sound we make when building blocks.

a ligthweight feature manage framework

1. load_data: load data
2. feature definition: metadata, input data, transform
3. assemble: construct

## download and install
you can install by pip command
``` python 
pip install pada
```
or download source
``` python
python setup.py install
```



## pada command line generates the project directory

```
project
|---definition
|  |-feats_def.py
|---load_data.py
|---main.py
|---url.py    
```

## base introduce

### load_data.py
define a function named *data()*, return your data which is a pd.DataFrame

### definition
you should define your feature in this directory

### url.py
find your feature definition by *url()* function

### main.py
run your feature engeering by *run()* function

