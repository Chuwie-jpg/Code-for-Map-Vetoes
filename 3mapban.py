# Map Pool
maps = ["Abyss", "Ascent", "Bind", "Haven", "Sunset", "Pearl", "Split"]

# Function to simulate map veto
def map_veto(team_a, team_b):
    # Copy the map pool for vetoing
    available_maps = maps[:]
    print("Initial Map Pool:", available_maps)
    print()
    
    def get_valid_input(prompt, valid_choices):
        """Helper function to ensure input is valid and within choices."""
        while True:
            choice = input(prompt).strip()
            if choice in valid_choices:
                return choice
            print(f"Invalid choice. Please choose from: {valid_choices}")

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

    # Step 7: Team A bans 1 map
    ban_a2 = get_valid_input(f"{team_a}, choose a map to BAN: ", available_maps)
    available_maps.remove(ban_a2)
    print(f"{team_a} bans {ban_a2}")
    print("Remaining Maps:", available_maps)
    print()

    # Step 8: Team B bans 1 map
    ban_b2 = get_valid_input(f"{team_b}, choose a map to BAN: ", available_maps)
    available_maps.remove(ban_b2)
    print(f"{team_b} bans {ban_b2}")
    print("Remaining Map:", available_maps)
    print()

    # Remaining map is Map 3
    map_3 = available_maps[0]
    side_a3 = get_valid_input(f"{team_a}, choose a side (Attack/Defense) for MAP 3: ", ["Attack", "Defense"])
    print(f"MAP 3: {map_3}")
    print(f"{team_a} picks {side_a3} side for MAP 3")
    print()

    # Summary
    print("Map Veto Summary:")
    print(f"MAP 1: {pick_a1} - {team_b} starts on {side_b1}")
    print(f"MAP 2: {pick_b2} - {team_a} starts on {side_a2}")
    print(f"MAP 3: {map_3} - {team_a} starts on {side_a3}")

# Example teams
team_a = "Praxis Esports"
team_b = "7SEPTCREW"

# Start the Map Veto
map_veto(team_a, team_b)
