Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> url ="http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
>>> df = pd.read_csv(url,header = None)
>>> headers=["symboling","normalized-losses","make","fuel-type","aspiration","number-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
>>> df.columns=headers
>>> df.head(5)
   symboling normalized-losses         make fuel-type aspiration  \
0          3                 ?  alfa-romero       gas        std
1          3                 ?  alfa-romero       gas        std
2          1                 ?  alfa-romero       gas        std
3          2               164         audi       gas        std
4          2               164         audi       gas        std

  number-of-doors   body-style drive-wheels engine-location  wheel-base  \
0             two  convertible          rwd           front        88.6
1             two  convertible          rwd           front        88.6
2             two    hatchback          rwd           front        94.5
3            four        sedan          fwd           front        99.8
4            four        sedan          4wd           front        99.4

   ...    engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0  ...            130         mpfi  3.47    2.68               9.0        111
1  ...            130         mpfi  3.47    2.68               9.0        111
2  ...            152         mpfi  2.68    3.47               9.0        154
3  ...            109         mpfi  3.19    3.40              10.0        102
4  ...            136         mpfi  3.19    3.40               8.0        115

   peak-rpm city-mpg highway-mpg  price
0      5000       21          27  13495
1      5000       21          27  16500
2      5000       19          26  16500
3      5500       24          30  13950
4      5500       18          22  17450

[5 rows x 26 columns]
>>> df
     symboling normalized-losses         make fuel-type aspiration  \
0            3                 ?  alfa-romero       gas        std
1            3                 ?  alfa-romero       gas        std
2            1                 ?  alfa-romero       gas        std
3            2               164         audi       gas        std
4            2               164         audi       gas        std
5            2                 ?         audi       gas        std
6            1               158         audi       gas        std
7            1                 ?         audi       gas        std
8            1               158         audi       gas      turbo
9            0                 ?         audi       gas      turbo
10           2               192          bmw       gas        std
11           0               192          bmw       gas        std
12           0               188          bmw       gas        std
13           0               188          bmw       gas        std
14           1                 ?          bmw       gas        std
15           0                 ?          bmw       gas        std
16           0                 ?          bmw       gas        std
17           0                 ?          bmw       gas        std
18           2               121    chevrolet       gas        std
19           1                98    chevrolet       gas        std
20           0                81    chevrolet       gas        std
21           1               118        dodge       gas        std
22           1               118        dodge       gas        std
23           1               118        dodge       gas      turbo
24           1               148        dodge       gas        std
25           1               148        dodge       gas        std
26           1               148        dodge       gas        std
27           1               148        dodge       gas      turbo
28          -1               110        dodge       gas        std
29           3               145        dodge       gas      turbo
..         ...               ...          ...       ...        ...
175         -1                65       toyota       gas        std
176         -1                65       toyota       gas        std
177         -1                65       toyota       gas        std
178          3               197       toyota       gas        std
179          3               197       toyota       gas        std
180         -1                90       toyota       gas        std
181         -1                 ?       toyota       gas        std
182          2               122   volkswagen    diesel        std
183          2               122   volkswagen       gas        std
184          2                94   volkswagen    diesel        std
185          2                94   volkswagen       gas        std
186          2                94   volkswagen       gas        std
187          2                94   volkswagen    diesel      turbo
188          2                94   volkswagen       gas        std
189          3                 ?   volkswagen       gas        std
190          3               256   volkswagen       gas        std
191          0                 ?   volkswagen       gas        std
192          0                 ?   volkswagen    diesel      turbo
193          0                 ?   volkswagen       gas        std
194         -2               103        volvo       gas        std
195         -1                74        volvo       gas        std
196         -2               103        volvo       gas        std
197         -1                74        volvo       gas        std
198         -2               103        volvo       gas      turbo
199         -1                74        volvo       gas      turbo
200         -1                95        volvo       gas        std
201         -1                95        volvo       gas      turbo
202         -1                95        volvo       gas        std
203         -1                95        volvo    diesel      turbo
204         -1                95        volvo       gas      turbo

    number-of-doors   body-style drive-wheels engine-location  wheel-base  \
0               two  convertible          rwd           front        88.6
1               two  convertible          rwd           front        88.6
2               two    hatchback          rwd           front        94.5
3              four        sedan          fwd           front        99.8
4              four        sedan          4wd           front        99.4
5               two        sedan          fwd           front        99.8
6              four        sedan          fwd           front       105.8
7              four        wagon          fwd           front       105.8
8              four        sedan          fwd           front       105.8
9               two    hatchback          4wd           front        99.5
10              two        sedan          rwd           front       101.2
11             four        sedan          rwd           front       101.2
12              two        sedan          rwd           front       101.2
13             four        sedan          rwd           front       101.2
14             four        sedan          rwd           front       103.5
15             four        sedan          rwd           front       103.5
16              two        sedan          rwd           front       103.5
17             four        sedan          rwd           front       110.0
18              two    hatchback          fwd           front        88.4
19              two    hatchback          fwd           front        94.5
20             four        sedan          fwd           front        94.5
21              two    hatchback          fwd           front        93.7
22              two    hatchback          fwd           front        93.7
23              two    hatchback          fwd           front        93.7
24             four    hatchback          fwd           front        93.7
25             four        sedan          fwd           front        93.7
26             four        sedan          fwd           front        93.7
27                ?        sedan          fwd           front        93.7
28             four        wagon          fwd           front       103.3
29              two    hatchback          fwd           front        95.9
..              ...          ...          ...             ...         ...
175            four    hatchback          fwd           front       102.4
176            four        sedan          fwd           front       102.4
177            four    hatchback          fwd           front       102.4
178             two    hatchback          rwd           front       102.9
179             two    hatchback          rwd           front       102.9
180            four        sedan          rwd           front       104.5
181            four        wagon          rwd           front       104.5
182             two        sedan          fwd           front        97.3
183             two        sedan          fwd           front        97.3
184            four        sedan          fwd           front        97.3
185            four        sedan          fwd           front        97.3
186            four        sedan          fwd           front        97.3
187            four        sedan          fwd           front        97.3
188            four        sedan          fwd           front        97.3
189             two  convertible          fwd           front        94.5
190             two    hatchback          fwd           front        94.5
191            four        sedan          fwd           front       100.4
192            four        sedan          fwd           front       100.4
193            four        wagon          fwd           front       100.4
194            four        sedan          rwd           front       104.3
195            four        wagon          rwd           front       104.3
196            four        sedan          rwd           front       104.3
197            four        wagon          rwd           front       104.3
198            four        sedan          rwd           front       104.3
199            four        wagon          rwd           front       104.3
200            four        sedan          rwd           front       109.1
201            four        sedan          rwd           front       109.1
202            four        sedan          rwd           front       109.1
203            four        sedan          rwd           front       109.1
204            four        sedan          rwd           front       109.1

     ...    engine-size  fuel-system  bore  stroke compression-ratio  \
0    ...            130         mpfi  3.47    2.68              9.00
1    ...            130         mpfi  3.47    2.68              9.00
2    ...            152         mpfi  2.68    3.47              9.00
3    ...            109         mpfi  3.19    3.40             10.00
4    ...            136         mpfi  3.19    3.40              8.00
5    ...            136         mpfi  3.19    3.40              8.50
6    ...            136         mpfi  3.19    3.40              8.50
7    ...            136         mpfi  3.19    3.40              8.50
8    ...            131         mpfi  3.13    3.40              8.30
9    ...            131         mpfi  3.13    3.40              7.00
10   ...            108         mpfi  3.50    2.80              8.80
11   ...            108         mpfi  3.50    2.80              8.80
12   ...            164         mpfi  3.31    3.19              9.00
13   ...            164         mpfi  3.31    3.19              9.00
14   ...            164         mpfi  3.31    3.19              9.00
15   ...            209         mpfi  3.62    3.39              8.00
16   ...            209         mpfi  3.62    3.39              8.00
17   ...            209         mpfi  3.62    3.39              8.00
18   ...             61         2bbl  2.91    3.03              9.50
19   ...             90         2bbl  3.03    3.11              9.60
20   ...             90         2bbl  3.03    3.11              9.60
21   ...             90         2bbl  2.97    3.23              9.41
22   ...             90         2bbl  2.97    3.23              9.40
23   ...             98         mpfi  3.03    3.39              7.60
24   ...             90         2bbl  2.97    3.23              9.40
25   ...             90         2bbl  2.97    3.23              9.40
26   ...             90         2bbl  2.97    3.23              9.40
27   ...             98         mpfi  3.03    3.39              7.60
28   ...            122         2bbl  3.34    3.46              8.50
29   ...            156          mfi  3.60    3.90              7.00
..   ...            ...          ...   ...     ...               ...
175  ...            122         mpfi  3.31    3.54              8.70
176  ...            122         mpfi  3.31    3.54              8.70
177  ...            122         mpfi  3.31    3.54              8.70
178  ...            171         mpfi  3.27    3.35              9.30
179  ...            171         mpfi  3.27    3.35              9.30
180  ...            171         mpfi  3.27    3.35              9.20
181  ...            161         mpfi  3.27    3.35              9.20
182  ...             97          idi  3.01    3.40             23.00
183  ...            109         mpfi  3.19    3.40              9.00
184  ...             97          idi  3.01    3.40             23.00
185  ...            109         mpfi  3.19    3.40              9.00
186  ...            109         mpfi  3.19    3.40              9.00
187  ...             97          idi  3.01    3.40             23.00
188  ...            109         mpfi  3.19    3.40             10.00
189  ...            109         mpfi  3.19    3.40              8.50
190  ...            109         mpfi  3.19    3.40              8.50
191  ...            136         mpfi  3.19    3.40              8.50
192  ...             97          idi  3.01    3.40             23.00
193  ...            109         mpfi  3.19    3.40              9.00
194  ...            141         mpfi  3.78    3.15              9.50
195  ...            141         mpfi  3.78    3.15              9.50
196  ...            141         mpfi  3.78    3.15              9.50
197  ...            141         mpfi  3.78    3.15              9.50
198  ...            130         mpfi  3.62    3.15              7.50
199  ...            130         mpfi  3.62    3.15              7.50
200  ...            141         mpfi  3.78    3.15              9.50
201  ...            141         mpfi  3.78    3.15              8.70
202  ...            173         mpfi  3.58    2.87              8.80
203  ...            145          idi  3.01    3.40             23.00
204  ...            141         mpfi  3.78    3.15              9.50

    horsepower  peak-rpm city-mpg highway-mpg  price
0          111      5000       21          27  13495
1          111      5000       21          27  16500
2          154      5000       19          26  16500
3          102      5500       24          30  13950
4          115      5500       18          22  17450
5          110      5500       19          25  15250
6          110      5500       19          25  17710
7          110      5500       19          25  18920
8          140      5500       17          20  23875
9          160      5500       16          22      ?
10         101      5800       23          29  16430
11         101      5800       23          29  16925
12         121      4250       21          28  20970
13         121      4250       21          28  21105
14         121      4250       20          25  24565
15         182      5400       16          22  30760
16         182      5400       16          22  41315
17         182      5400       15          20  36880
18          48      5100       47          53   5151
19          70      5400       38          43   6295
20          70      5400       38          43   6575
21          68      5500       37          41   5572
22          68      5500       31          38   6377
23         102      5500       24          30   7957
24          68      5500       31          38   6229
25          68      5500       31          38   6692
26          68      5500       31          38   7609
27         102      5500       24          30   8558
28          88      5000       24          30   8921
29         145      5000       19          24  12964
..         ...       ...      ...         ...    ...
175         92      4200       27          32   9988
176         92      4200       27          32  10898
177         92      4200       27          32  11248
178        161      5200       20          24  16558
179        161      5200       19          24  15998
180        156      5200       20          24  15690
181        156      5200       19          24  15750
182         52      4800       37          46   7775
183         85      5250       27          34   7975
184         52      4800       37          46   7995
185         85      5250       27          34   8195
186         85      5250       27          34   8495
187         68      4500       37          42   9495
188        100      5500       26          32   9995
189         90      5500       24          29  11595
190         90      5500       24          29   9980
191        110      5500       19          24  13295
192         68      4500       33          38  13845
193         88      5500       25          31  12290
194        114      5400       23          28  12940
195        114      5400       23          28  13415
196        114      5400       24          28  15985
197        114      5400       24          28  16515
198        162      5100       17          22  18420
199        162      5100       17          22  18950
200        114      5400       23          28  16845
201        160      5300       19          25  19045
202        134      5500       18          23  21485
203        106      4800       26          27  22470
204        114      5400       19          25  22625

[205 rows x 26 columns]
>>> df.head(10)
   symboling normalized-losses         make fuel-type aspiration  \
0          3                 ?  alfa-romero       gas        std
1          3                 ?  alfa-romero       gas        std
2          1                 ?  alfa-romero       gas        std
3          2               164         audi       gas        std
4          2               164         audi       gas        std
5          2                 ?         audi       gas        std
6          1               158         audi       gas        std
7          1                 ?         audi       gas        std
8          1               158         audi       gas      turbo
9          0                 ?         audi       gas      turbo

  number-of-doors   body-style drive-wheels engine-location  wheel-base  \
0             two  convertible          rwd           front        88.6
1             two  convertible          rwd           front        88.6
2             two    hatchback          rwd           front        94.5
3            four        sedan          fwd           front        99.8
4            four        sedan          4wd           front        99.4
5             two        sedan          fwd           front        99.8
6            four        sedan          fwd           front       105.8
7            four        wagon          fwd           front       105.8
8            four        sedan          fwd           front       105.8
9             two    hatchback          4wd           front        99.5

   ...    engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0  ...            130         mpfi  3.47    2.68               9.0        111
1  ...            130         mpfi  3.47    2.68               9.0        111
2  ...            152         mpfi  2.68    3.47               9.0        154
3  ...            109         mpfi  3.19    3.40              10.0        102
4  ...            136         mpfi  3.19    3.40               8.0        115
5  ...            136         mpfi  3.19    3.40               8.5        110
6  ...            136         mpfi  3.19    3.40               8.5        110
7  ...            136         mpfi  3.19    3.40               8.5        110
8  ...            131         mpfi  3.13    3.40               8.3        140
9  ...            131         mpfi  3.13    3.40               7.0        160

   peak-rpm city-mpg highway-mpg  price
0      5000       21          27  13495
1      5000       21          27  16500
2      5000       19          26  16500
3      5500       24          30  13950
4      5500       18          22  17450
5      5500       19          25  15250
6      5500       19          25  17710
7      5500       19          25  18920
8      5500       17          20  23875
9      5500       16          22      ?

[10 rows x 26 columns]
>>> df.tail(10)
     symboling normalized-losses   make fuel-type aspiration number-of-doors  \
195         -1                74  volvo       gas        std            four
196         -2               103  volvo       gas        std            four
197         -1                74  volvo       gas        std            four
198         -2               103  volvo       gas      turbo            four
199         -1                74  volvo       gas      turbo            four
200         -1                95  volvo       gas        std            four
201         -1                95  volvo       gas      turbo            four
202         -1                95  volvo       gas        std            four
203         -1                95  volvo    diesel      turbo            four
204         -1                95  volvo       gas      turbo            four

    body-style drive-wheels engine-location  wheel-base  ...    engine-size  \
195      wagon          rwd           front       104.3  ...            141
196      sedan          rwd           front       104.3  ...            141
197      wagon          rwd           front       104.3  ...            141
198      sedan          rwd           front       104.3  ...            130
199      wagon          rwd           front       104.3  ...            130
200      sedan          rwd           front       109.1  ...            141
201      sedan          rwd           front       109.1  ...            141
202      sedan          rwd           front       109.1  ...            173
203      sedan          rwd           front       109.1  ...            145
204      sedan          rwd           front       109.1  ...            141

     fuel-system  bore  stroke compression-ratio horsepower  peak-rpm  \
195         mpfi  3.78    3.15               9.5        114      5400
196         mpfi  3.78    3.15               9.5        114      5400
197         mpfi  3.78    3.15               9.5        114      5400
198         mpfi  3.62    3.15               7.5        162      5100
199         mpfi  3.62    3.15               7.5        162      5100
200         mpfi  3.78    3.15               9.5        114      5400
201         mpfi  3.78    3.15               8.7        160      5300
202         mpfi  3.58    2.87               8.8        134      5500
203          idi  3.01    3.40              23.0        106      4800
204         mpfi  3.78    3.15               9.5        114      5400

    city-mpg highway-mpg  price
195       23          28  13415
196       24          28  15985
197       24          28  16515
198       17          22  18420
199       17          22  18950
200       23          28  16845
201       19          25  19045
202       18          23  21485
203       26          27  22470
204       19          25  22625

[10 rows x 26 columns]
>>> df.dtypes
symboling              int64
normalized-losses     object
make                  object
fuel-type             object
aspiration            object
number-of-doors       object
body-style            object
drive-wheels          object
engine-location       object
wheel-base           float64
length               float64
width                float64
height               float64
curb-weight            int64
engine-type           object
num-of-cylinders      object
engine-size            int64
fuel-system           object
bore                  object
stroke                object
compression-ratio    float64
horsepower            object
peak-rpm              object
city-mpg               int64
highway-mpg            int64
price                 object
dtype: object
>>> df.describe()
        symboling  wheel-base      length       width      height  \
count  205.000000  205.000000  205.000000  205.000000  205.000000
mean     0.834146   98.756585  174.049268   65.907805   53.724878
std      1.245307    6.021776   12.337289    2.145204    2.443522
min     -2.000000   86.600000  141.100000   60.300000   47.800000
25%      0.000000   94.500000  166.300000   64.100000   52.000000
50%      1.000000   97.000000  173.200000   65.500000   54.100000
75%      2.000000  102.400000  183.100000   66.900000   55.500000
max      3.000000  120.900000  208.100000   72.300000   59.800000

       curb-weight  engine-size  compression-ratio    city-mpg  highway-mpg
count   205.000000   205.000000         205.000000  205.000000   205.000000
mean   2555.565854   126.907317          10.142537   25.219512    30.751220
std     520.680204    41.642693           3.972040    6.542142     6.886443
min    1488.000000    61.000000           7.000000   13.000000    16.000000
25%    2145.000000    97.000000           8.600000   19.000000    25.000000
50%    2414.000000   120.000000           9.000000   24.000000    30.000000
75%    2935.000000   141.000000           9.400000   30.000000    34.000000
max    4066.000000   326.000000          23.000000   49.000000    54.000000
>>> df.describe(include="all")
         symboling normalized-losses    make fuel-type aspiration  \
count   205.000000               205     205       205        205
unique         NaN                52      22         2          2
top            NaN                 ?  toyota       gas        std
freq           NaN                41      32       185        168
mean      0.834146               NaN     NaN       NaN        NaN
std       1.245307               NaN     NaN       NaN        NaN
min      -2.000000               NaN     NaN       NaN        NaN
25%       0.000000               NaN     NaN       NaN        NaN
50%       1.000000               NaN     NaN       NaN        NaN
75%       2.000000               NaN     NaN       NaN        NaN
max       3.000000               NaN     NaN       NaN        NaN

       number-of-doors body-style drive-wheels engine-location  wheel-base  \
count              205        205          205             205  205.000000
unique               3          5            3               2         NaN
top               four      sedan          fwd           front         NaN
freq               114         96          120             202         NaN
mean               NaN        NaN          NaN             NaN   98.756585
std                NaN        NaN          NaN             NaN    6.021776
min                NaN        NaN          NaN             NaN   86.600000
25%                NaN        NaN          NaN             NaN   94.500000
50%                NaN        NaN          NaN             NaN   97.000000
75%                NaN        NaN          NaN             NaN  102.400000
max                NaN        NaN          NaN             NaN  120.900000

        ...   engine-size  fuel-system  bore  stroke compression-ratio  \
count   ...    205.000000          205   205     205        205.000000
unique  ...           NaN            8    39      37               NaN
top     ...           NaN         mpfi  3.62    3.40               NaN
freq    ...           NaN           94    23      20               NaN
mean    ...    126.907317          NaN   NaN     NaN         10.142537
std     ...     41.642693          NaN   NaN     NaN          3.972040
min     ...     61.000000          NaN   NaN     NaN          7.000000
25%     ...     97.000000          NaN   NaN     NaN          8.600000
50%     ...    120.000000          NaN   NaN     NaN          9.000000
75%     ...    141.000000          NaN   NaN     NaN          9.400000
max     ...    326.000000          NaN   NaN     NaN         23.000000

       horsepower  peak-rpm    city-mpg highway-mpg price
count         205       205  205.000000  205.000000   205
unique         60        24         NaN         NaN   187
top            68      5500         NaN         NaN     ?
freq           19        37         NaN         NaN     4
mean          NaN       NaN   25.219512   30.751220   NaN
std           NaN       NaN    6.542142    6.886443   NaN
min           NaN       NaN   13.000000   16.000000   NaN
25%           NaN       NaN   19.000000   25.000000   NaN
50%           NaN       NaN   24.000000   30.000000   NaN
75%           NaN       NaN   30.000000   34.000000   NaN
max           NaN       NaN   49.000000   54.000000   NaN
