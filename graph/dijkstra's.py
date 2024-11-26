import heapq
from collections import defaultdict
from heapq import heappush

input_data = "US:UK:UPS:4 US:UK:DHL:5 UK:CA:FedEx:10 AU:JP:DHL:20"
cities = ["US", "UK", "CA", "AU", "JP"]


shipping_cost_list = input_data.split(' ')
shipping_cost_list = [i.split(":") for i in shipping_cost_list]

shipping_cost_map = defaultdict(lambda :defaultdict(dict))
cities = set()

for cost in shipping_cost_list:
    source, target, method, price = cost
    cities.add(source)
    cities.add(target)
    shipping_cost_map[source][target][method] = int(price)

def get_cost_to_ship(shipping_cost_map, source, target, method):
    return shipping_cost_map[source][target][method]

print(get_cost_to_ship(shipping_cost_map, "US","UK", "DHL"))

def get_cost_to_ship_with_intermediate(shipping_cost_map, source, target, method=None):
    # source to target
    source_to_target = min([v for k, v in shipping_cost_map[source][target].items()], default=float('inf'))
    for city in cities:
        # source to city
        source_to_city = min([v for k, v in shipping_cost_map[source][city].items()], default=float('inf'))
        # city to target
        city_to_target = min([v for k, v in shipping_cost_map[city][target].items()], default=float('inf'))

        source_to_target = min( source_to_city + city_to_target, source_to_target)
    return source_to_target


print(get_cost_to_ship_with_intermediate(shipping_cost_map, "US","CA", "DHL"))


def get_cost_to_ship_with_intermediate_dijkstras(shipping_cost_map, source, target, method=None):
    # source to target
    source_to_target = min([v for k, v in shipping_cost_map[source][target].items()], default=float('inf'))

    def dijkstras(graph, start):

        priority_queue = []
        heapq.heappush(priority_queue, (0, start))

        costs = { city: float('inf') for city in cities}

        while priority_queue:
            current_cost, current_city = heapq.heappop(priority_queue)

            if costs[current_city] < current_cost:
                continue

            for city, value in graph[current_city].items():
                cost = min([v for k, v in value.items()], default=float('inf'))
                if cost < costs[city]:
                    costs[city] = cost + current_cost
                    heappush(priority_queue, (costs[city], city))
        return costs
    return dijkstras(shipping_cost_map, source)[target]




print(get_cost_to_ship_with_intermediate_dijkstras(shipping_cost_map, "US","CA", "DHL"))
















