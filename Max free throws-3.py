# 1. open NBA data file
nba_file = open("player_regular_season.csv", "r")

def create_player_list(nba_file):
    """Create a list of players stats."""
    # Creates a list of added value
    player_list = []
    s=0
    for line in nba_file:
        if (s>21000):
            break
        s=s+1
        line_list = line.split(',')
        
        # create tuple: (minutes, last name, first name, year)
        if(line_list[20]=="minutes"):
            continue
        if(line_list[20]=="NULL"):
            line_list[20]="0"
        player_tuple = (int(line_list[20]), line_list[2], line_list[3])
        mileage_list.append(player_tuple)        # 2bII. append tuple
    return player_list
max_minute_list = []

player_list=create_player_list(nba_file)

print("Maximum free throws played:")
print max(player_list)
