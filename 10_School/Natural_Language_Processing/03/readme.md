# About
To check this week's exercise, execute from this folder following command (linux based terminal):

```
./run.sh
```

Below, I leave some comments to the given exercises.

# Lecture 5
## Implementing POS tagger
I implemented the tagger as a classifier. Therefore, fitting means computing
`emission` and `transition` matrices. And `predict` class then implements
`viterbi` algorithm to actually decode the given input and predict
corresponding labels.

# Lecture 6
## Implementing FFNN
All the important info can be inspected by running the `run.sh` script from the
command line.
