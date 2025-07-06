import pandas as pd


# Preprocess function
def preprocess(df, region_df):
    # Filter for Summer Olympics
    df = df[df['Season'] == 'Summer']

    # Merge with region_df to add region info
    df = df.merge(region_df, on='NOC', how='left')

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # One-hot encode the 'Medal' column (Gold, Silver, Bronze)
    df = pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)

    return df
