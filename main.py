import pandas as pd
from pybaseball import playerid_reverse_lookup

# Load the master dataframe
df_master = pd.read_csv("Appearances.csv")
print("Master dataframe loaded")

while True:
    team1 = input("Enter Team 1 ID: ")
    team2 = input("Enter Team 2 ID: ")

    # Filter data for Team 1 and Team 2
    df_t1 = df_master[df_master['teamID'] == team1]
    df_t2 = df_master[df_master['teamID'] == team2]

    # Merge the dataframes to find players who played for both teams
    df_both = pd.merge(df_t1, df_t2, on='playerID')

    if not df_both.empty:
        player_id = df_both["playerID"].iloc[-1]

        # Use pybaseball to look up the player's name
        player_info = playerid_reverse_lookup(player_id, key_type='bbref')

        if not player_info.empty:
            player_first_name = player_info["name_first"].iloc[0]
            player_last_name = player_info["name_last"].iloc[0]
            print(f"Player who played for both {team1} and {team2}: {player_first_name} {player_last_name}")
        else:
            print("Player information not found.")
    else:
        print(f"No players found who played for both {team1} and {team2}.")
