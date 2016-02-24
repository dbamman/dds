## Data

This directory contains the data for homework 2, part 2.1 (the permutation test).  Included are:

### movie.features.txt: 

8,304 movies featurized by the top 100 most frequent genre and actors who appear in them, extracted from Freebase.

Columns:

|Feature name | Feature value | Movie ID|
|---|---|---|
|Horror|	1	|975900|
|Science_Fiction	|1	|975900|
|Supernatural|	1	|975900|

The movies that contain John Goodman are identified as those for which the feature John_Goodman has a value of 1. If a feature name/value does not show up with a Movie ID (e.g., John_Goodman), assume it is 0.

### movie.box_office.txt

Binary indicators for those same movies denoting whether or not they are "box office hits" (among the 25% highest grossing movies in that set), extracted from Wikipedia.  1 = yes, 0 = no.

Columns:

|Movie ID | box office hit?|
|---|---|
|975900|	0|
|10408933|	0|
|171005|	0|
|77856|	1|