from sklearn.model_selection import train_test_split

def split_data(df_imputed, target_col='Outcome', test_size=0.2, random_state=42):
    X = df_imputed.drop(columns=[target_col])
    y = df_imputed[target_col]

    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)