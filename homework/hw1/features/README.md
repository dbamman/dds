# features

This directory contains sample features that can be used to train a Oscar predictor; each of these feature files also represents the format your own feature files must adhere to.  Specifically, each feature file contains exactly three (tab-separated) columns:

* The first column is the feature name
* The second column is the feature value
* The third column is the Wikipedia canonical id identifying the data point it applies to.  This canonical id is the nominee identifier in the labeled datsets in the `labels/` directory.


|Feature Name | Feature value | Wikipedia canonical id|
|:-:|:-:|:-:|
won_gg_drama_movie|	1	|/wiki/On_Golden_Pond_(1981_film)
won_gg_drama_movie|	1	|/wiki/E.T._the_Extra-Terrestrial
...|...|...
won_gg_drama_movie|	1|	/wiki/Boyhood_(film)
won_gg_drama_movie|	1|	/wiki/The_Revenant_(2015_film)

For this homework, you will submit 6 different feature files like these, one for each Academy Award category (in `labels/`); each feature file should contains *all* of your feature representations for all of the movies from 1960-2015.

You only need to include feature values for nominees where that value is nonzero.  If we see a nominee isn't listed with a provided feature name in your feature set, we'll assume that value is 0.

