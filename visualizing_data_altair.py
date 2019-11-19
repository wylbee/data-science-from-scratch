# %% codecell
# altair
import altair as alt
import numpy as np
import pandas as pd

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

source = pd.DataFrame({
	'Year': years,
	'Amount': gdp
	})

alt.Chart(source).mark_line().encode(
	x='Year',
	y='Amount'
)
