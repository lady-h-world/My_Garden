## Trend Detection

Trend detection is to find data points where an increasing or decreating trend started. It is provided in Kats but not in Greykite.

Kats mainly uses M-K (Mann Kendall) Test for trend detection. It calculates all the differences between y_t and all the previous y_i within the time window, summing up the signs of these differences. The time point that gets the largest positive value is the trend increasing point, and the one gets the smallest negative value is the trend decreasing point.

Besides, Kats also provides Seasonal M-K Test for seasonal trend detection, which performs M-K test within the same season. For example, for monthly seaons, the summed up signs for January observations is only compared with other January observations, there is no cross season comparisons.
