#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd
import statsmodels.api as sm

# Assign spreadsheet filename to `file`
file = 'Harmon_Foods.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
# print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df
df = xl.parse('HARMON')

X = df[["CP", "CP(t-1)", "DA", "DA(t-2)", "SeasIndx"]] ## X usually means our input variables (or independent variables)
y = df["Sales"] ## Y usually means our output/dependent variable
X = sm.add_constant(X) ## let's add an intercept (beta_0) to our model

# Note the difference in argument order
model = sm.OLS(y, X).fit() ## sm.OLS(output, input)
predictions = model.predict(X)

# Print out the statistics
print(model.summary())
