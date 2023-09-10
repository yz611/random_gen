# RandomGen

A simple random number generator

## Introduction

A random number generator.

Given Random Numbers are `[-1, 0, 1, 2, 3]` and probabilities are `[0.01, 0.3, 0.58, 0.1, 0.01]` if we call nextNum()
100 times we may get the following results:

```
-1: 1 times
0: 22 times 
1: 57 times 
2: 20 times 
3: 0 times
```

As the results are random, these particular results are unlikely.

## Use case

### In script

```python
from RandomGen import RandomGen

random_number_generator = RandomGen(
    [-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01], observation_size=100
)
for i in random_number_generator:
    print(i)
```

### From CLI

```bash
python -m RandomGen -n 100000 -c --pmf
```

Then input the values, probabilities and output size in order, separated by space. 

Note 100000 is the number of total observations and user should input the number of observations to print. 