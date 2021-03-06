




>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib as plt
>>> url = "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
>>> df = pd.read_csv(url,header = None)
>>> df
     0    1            2       3      4     5            6    7      8   \
0     3    ?  alfa-romero     gas    std   two  convertible  rwd  front
1     3    ?  alfa-romero     gas    std   two  convertible  rwd  front
2     1    ?  alfa-romero     gas    std   two    hatchback  rwd  front
3     2  164         audi     gas    std  four        sedan  fwd  front
4     2  164         audi     gas    std  four        sedan  4wd  front
5     2    ?         audi     gas    std   two        sedan  fwd  front
6     1  158         audi     gas    std  four        sedan  fwd  front
7     1    ?         audi     gas    std  four        wagon  fwd  front
8     1  158         audi     gas  turbo  four        sedan  fwd  front
9     0    ?         audi     gas  turbo   two    hatchback  4wd  front
10    2  192          bmw     gas    std   two        sedan  rwd  front
11    0  192          bmw     gas    std  four        sedan  rwd  front
12    0  188          bmw     gas    std   two        sedan  rwd  front..........



>>> df.head(10)
   3    ?  alfa-romero  gas    std   two  convertible  rwd  front  88.60  \
0  3    ?  alfa-romero  gas    std   two  convertible  rwd  front   88.6
1  1    ?  alfa-romero  gas    std   two    hatchback  rwd  front   94.5
2  2  164         audi  gas    std  four        sedan  fwd  front   99.8
3  2  164         audi  gas    std  four        sedan  4wd  front   99.4........


[10 rows x 26 columns]
>>> df.tail(10)
     3    ? alfa-romero     gas    std   two convertible  rwd  front  88.60  \
194 -1   74       volvo     gas    std  four       wagon  rwd  front  104.3
195 -2  103       volvo     gas    std  four       sedan  rwd  front  104.3
196 -1   74       volvo     gas    std  four       wagon  rwd  front  104.3
197 -2  103       volvo     gas  turbo  four       sedan  rwd  front  104.3........



>>> df.dtypes
3                int64
?               object
alfa-romero     object
gas             object
std             object
two             object
convertible     object
rwd             object
front           object
88.60          float64
168.80         float64
64.10          float64
48.80          float64
2548             int64
dohc            object
four            object
130              int64
mpfi            object
3.47            object
2.68            object
9.00           float64
111             object
5000            object
21               int64
27               int64
13495           object
dtype: object


