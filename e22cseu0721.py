class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        self.matches.append({
            "Location": location,
            "Team 01": team1,
            "Team 02": team2,
            "Timing": timing
        })

    def search_by_team(self, team_name):
        return [match for match in self.matches if team_name in (match["Team 01"], match["Team 02"])]

    def search_by_location(self, location):
        return [match for match in self.matches if match["Location"] == location]

    def search_by_timing(self, timing):
        return [match for match in self.matches if match["Timing"] == timing]

def main():
    flight_table = FlightTable()

    flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India", "South Africa", "DAY")
    flight_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    flight_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY")

    while True:
        print("Choose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter the team name: ")
            matches = flight_table.search_by_team(team_name)
        elif choice == 2:
            location = input("Enter the location: ")
            matches = flight_table.search_by_location(location)
        elif choice == 3:
            timing = input("Enter the timing: ")
            matches = flight_table.search_by_timing(timing)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print("\nSearch Results:")
        if matches:
            for match in matches:
                print(f"Location: {match['Location']}, Team 01: {match['Team 01']}, Team 02: {match['Team 02']}, Timing: {match['Timing']}")
        else:
            print("No matches found for the given criteria.\n")

if __name__ == "__main__":
    main()
