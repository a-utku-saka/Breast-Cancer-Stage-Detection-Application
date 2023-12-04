import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier


def predictor():
    dataset = pd.read_csv('./dataset/last_version_breast_cancer.csv')

    obj_cols_word = list()
    obj_cols_cat = list()
    num_cols_cat = list()
    num_cols_cont = list()

    for col in dataset.columns:
        num_of_distinct_values = len(dataset[col].value_counts())
        if dataset[col].dtype == 'object':
            if num_of_distinct_values < 10:
                obj_cols_cat.append(col)
            else:
                obj_cols_word.append(col)
        else:
            if num_of_distinct_values < 10:
                num_cols_cat.append(col)
            else:
                num_cols_cont.append(col)

    cat_df = pd.get_dummies(dataset[obj_cols_cat], prefix=obj_cols_cat, drop_first=True)
    dataset.drop(obj_cols_cat, axis=1, inplace=True)

    new_df = pd.concat([dataset, cat_df], axis=1)
    X = new_df.drop('tumor_stage', axis=1)
    y = new_df['tumor_stage']

    # X_train, _, y_train, _ = train_test_split(X, y, test_size=.2, random_state=42, stratify=y)

    clf = GradientBoostingClassifier(learning_rate=0.005, n_estimators=300,
                                     n_iter_no_change=9, random_state=85,
                                     subsample=0.3204081632653062)
    clf.fit(X, y)

    return clf, list(new_df.columns)
