class RadioGaga:

    def __init__(self):
        self.states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
        self.stations = {
            'kone': {'id', 'nv', 'ut'}, 'ktwo': {'mt', 'id', 'wa'},
            'kthree': {'or', 'nv', 'ca'}, 'kfour': {'nv', 'ut'}, 'kfive': {'az', 'ca'}
        }
        self.stations_price = {
            'kone': 1000, 'ktwo': 2000,
            'kthree': 1000, 'kfour': 2500, 'kfive': 1700
        }
        self.state_importance = {"mt": 1, "wa": 1, "or": 1, "id": 1, "nv": 1, "ut": 1, "ca": 1, "az": 1}
        self.final_stations = set()
        self.states_covered = set()

    def add_station(self, station_name: str = None, states: list = None, price: int = None):
        self.stations[station_name] = states
        self.stations_price[station_name] = price
        print("Station added")

    def add_states(self, *states):
        self.states_needed.update(set(states))
        self.state_importance.update(dict.fromkeys(states, 1))
        print("States added")

    def update_state_importance(self, state, importance):
        if state in self.state_importance:
            self.state_importance[state] = importance
            print(f"{state} importance updated")
        else:
            print("No such state in list")

    def __imp_on_pr(self, station):
        if station is None:
            return float("inf")
        importance = 0
        for state in (self.stations[station] - self.states_covered):
            importance += self.state_importance.get(state, 0)
        return importance/self.stations_price[station]

    def get_solution(self):
        while self.states_needed:
            best_station = None
            states_covered = set()
            for station, states in self.stations.items():
                covered = self.states_needed & states
                if len(covered) > len(states_covered):
                    best_station = station
                    states_covered = covered
                elif len(covered) == len(states_covered):
                    if self.__imp_on_pr(best_station) > self.__imp_on_pr(station):
                        best_station = station
                        states_covered = covered
            self.states_covered |= states_covered
            self.states_needed -= states_covered
            self.final_stations.add(best_station)
        return self.final_stations


r = RadioGaga()
print(r.get_solution())
