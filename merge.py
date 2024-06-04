import pandas as pd

def merge(formatted_data):
    occurence_df = pd.read_csv(formatted_data)
    tracks_df = pd.read_csv('dataset/Music_Info.csv')
    merged_df = pd.merge(occurence_df, tracks_df, on='track_id') # Cocokan di track id
    artist_info = merged_df.groupby(['artist', 'genre']).agg({'occurence': 'sum', 'name': 'first'}).reset_index() # Sum jika ada kesamaan
    artist_info.columns = ['artist', 'genre', 'occurrences', 'track_name']
    artist_info = artist_info.sort_values(by='occurrences', ascending=False)
    artist_info.to_csv('merged/merged_data.csv', index=False)

merge('output/total_listen_id_formatted.csv')