from xgboost import XGBClassifier

def train_xgboost(X_train_scaled, y_train):
    xgb_model = XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42, use_label_encoder=False, eval_metrics='logloss')
    xgb_model.fit(X_train_scaled, y_train)
    return xgb_model

def predict_xgboost(xgb_model, X_test_scaled):
    return xgb_model.predict(X_test_scaled)