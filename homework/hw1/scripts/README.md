# scripts

This contains the single script `oscars.py` which we'll use to generate predictions from the feature files you submit.

This file implements binary logistic regression, predicting the classification of {winner vs. not winner} for each of the data points, along with L2 regularization (the value of the regularization parameter is optimized using cross-validation to minimize overfitting).  To use this model to predict the Academy Award winner, we will independent predict the probability of each nominee winning; the nominee with the highest probability among the competitors is selected as the winner.  This model only considers training data from 1960-2014.

Feel free to use this model to assess the potential of your features.

Run with (e.g.) `python oscars.py ../features/golden_globe_winners.txt ../labels/film.txt`