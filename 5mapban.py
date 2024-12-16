# Map Pool
maps = ["Abyss", "Ascent", "Bind", "Haven", "Sunset", "Pearl", "Split"]

# Function to validate user input
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

# Function to simulate BO5 map veto
def map_veto_bo5(team_a, team_b):
    # Copy the map pool for vetoing
    available_maps = maps[:]
    print("Initial Map Pool:", available_maps)
    print()
    
    try:
        # Step 1: Team A bans 1 map
        ban_a1 = get_valid_input(f"{team_a}, choose a map to BAN: ", available_maps)
        available_maps.remove(ban_a1)
        print(f"{team_a} bans {ban_a1}")
        print("Remaining Maps:", available_maps)
        print()
        
        # Step 2: Team B bans 1 map
        ban_b1 = get_valid_input(f"{team_b}, choose a map to BAN: ", available_maps)
        available_maps.remove(ban_b1)
        print(f"{team_b} bans {ban_b1}")
        print("Remaining Maps:", available_maps)
        print()
        
        # Step 3: Team A picks map 1
        pick_a1 = get_valid_input(f"{team_a}, choose a map for MAP 1: ", available_maps)
        available_maps.remove(pick_a1)
        print(f"{team_a} picks {pick_a1}")
        print("Remaining Maps:", available_maps)
        print()
        
        # Step 4: Team B picks side for map 1
        side_b1 = get_valid_input(f"{team_b}, choose a side (Attack/Defense) for MAP 1: ", ["Attack", "Defense"])
        print(f"{team_b} picks {side_b1} side for MAP 1")
        print()
        
        # Step 5: Team B picks map 2
        pick_b2 = get_valid_input(f"{team_b}, choose a map for MAP 2: ", available_maps)
        available_maps.remove(pick_b2)
        print(f"{team_b} picks {pick_b2}")
        print("Remaining Maps:", available_maps)
        print()
        
        # Step 6: Team A picks side for map 2
        side_a2 = get_valid_input(f"{team_a}, choose a side (Attack/Defense) for MAP 2: ", ["Attack", "Defense"])
        print(f"{team_a} picks {side_a2} side for MAP 2")
        print()
        
        # Step 7: Team A picks map 3
        pick_a3 = get_valid_input(f"{team_a}, choose a map for MAP 3: ", available_maps)
        available_maps.remove(pick_a3)
        print(f"{team_a} picks {pick_a3}")
        print("Remaining Maps:", available_maps)
        print()
        
        # Step 8: Team B picks side for map 3
        side_b3 = get_valid_input(f"{team_b}, choose a side (Attack/Defense) for MAP 3: ", ["Attack", "Defense"])
        print(f"{team_b} picks {side_b3} side for MAP 3")
        print()
        
        # Step 9: Team B picks map 4
        pick_b4 = get_valid_input(f"{team_b}, choose a map for MAP 4: ", available_maps)
        available_maps.remove(pick_b4)
        print(f"{team_b} picks {pick_b4}")
        print("Remaining Maps:", available_maps)
        print()
        
        # Step 10: Team A picks side for map 4
        side_a4 = get_valid_input(f"{team_a}, choose a side (Attack/Defense) for MAP 4: ", ["Attack", "Defense"])
        print(f"{team_a} picks {side_a4} side for MAP 4")
        print()
        
        # Remaining map is Map 5
        map_5 = available_maps[0]
        side_b5 = get_valid_input(f"{team_b}, choose a side (Attack/Defense) for MAP 5: ", ["Attack", "Defense"])
        print(f"MAP 5: {map_5}")
        print(f"{team_b} picks {side_b5} side for MAP 5")
        print()
        
        # Summary
        print("Map Veto Summary:")
        print(f"MAP 1: {pick_a1} - {team_b} starts on {side_b1}")
        print(f"MAP 2: {pick_b2} - {team_a} starts on {side_a2}")
        print(f"MAP 3: {pick_a3} - {team_b} starts on {side_b3}")
        print(f"MAP 4: {pick_b4} - {team_a} starts on {side_a4}")
        print(f"MAP 5: {map_5} - {team_b} starts on {side_b5}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example teams
team_a = "Natus Vincere"
team_b = "G2 Esports"

# Start the Map Veto for BO5
map_veto_bo5(team_a, team_b)
