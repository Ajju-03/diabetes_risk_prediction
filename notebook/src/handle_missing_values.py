from sklearn.impute import SimpleImputer
import pandas as pd

def simple_impute(df):
    imputer = SimpleImputer(strategy='median')
    imputed_data_array = imputer.fit_transform(df)
    df_imputed = pd.DataFrame(imputed_data_array, columns=df.columns)

    return df_imputed 