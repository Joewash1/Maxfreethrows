# 1. open NBA data file
nba_file = open("player_regular_season.csv", "r")

def create_player_list(nba_file):
    """Create a list of players stats."""
    # Creates a list of added value
    player_list = []
    s=0
    for line in nba_file:
        if (s>21900):
            break
        s=s+1
        line_list = line.split(',')
        
        # create tuple: (minutes, last name, first name, year)
        if(line_list[6]=="minutes"):
            continue
        if(line_list[20]=="NULL"):
            line_list[20]="0"
        if(line_list[0] == "ConleMi01 "):
            player_tuple=(line_list[0], (int(line_list[20])
        else:
            player_tuple=(line_list[0], (int(line_list[20])
                i = 0;
        while(i < len(player_list) and int(player_tuple[20]) < int(player_list[i][7]) and i < 50):
                    i = i + 1
        player_tuple = (int(line_list[20]), line_list[2], line_list[3])
        mileage_list.append(player_tuple)        # 2bII. append tuple
    return player_list
max_minute_list = []
player_list=create_player_list(nba_file)

print("Maximum games played:")
print (player_list)
