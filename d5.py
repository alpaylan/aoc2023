
def map_to_dest(map, source):
    for i in range(len(map)):
        if source >= map[i][1] and source <= map[i][1] + map[i][2]:
            return map[i][0] + (source - map[i][1])
    return source

def map_partial_app(mapname, map1, source, range_):
    result_map = []
    print("mapname", mapname)
    print("source", source, "range", range_, "map", map1)
    for mapi in sorted(map1, key=lambda x: x[1]):
        if source >= mapi[1] and source <= mapi[1] + mapi[2]:
            if source + range_ <= mapi[1] + mapi[2]:
                print("finishing range: source", source, "range", range_, "mapi", mapi)
                result_map.append((mapi[0] + (source - mapi[1]), range_))
                print("result_map", result_map)
                return result_map
            else:
                print("unfinished range: source", source, "range", range_, "mapi", mapi)
                result_map.append((mapi[0] + (source - mapi[1]), (mapi[1] + mapi[2]) - source))
                range_ -= (mapi[1] + mapi[2]) - source
                source += (mapi[1] + mapi[2]) - source
    if range_ > 0:
        result_map.append((source, range_))
    print("result_map", result_map)
    return result_map


def p1():
    with open("d5.input") as f:
        lines = f.read().splitlines()
        score = 0

    seeds = list(map(int, lines[0][7:].split(" ")))
    seeds_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    current_map = None
    for line in lines:
        if line == "":
            continue
        if line.startswith("seed-to-soil"):
            current_map = seeds_to_soil
        elif line.startswith("soil-to-fertilizer"):
            current_map = soil_to_fertilizer
        elif line.startswith("fertilizer-to-water"):
            current_map = fertilizer_to_water
        elif line.startswith("water-to-light"):
            current_map = water_to_light
        elif line.startswith("light-to-temperature"):
            current_map = light_to_temperature
        elif line.startswith("temperature-to-humidity"):
            current_map = temperature_to_humidity
        elif line.startswith("humidity-to-location"):
            current_map = humidity_to_location
        else:
            if current_map is None:
                continue
            else:
                current_map.append(list(map(int, line.split(" "))))

    min_loc = float('inf')
    for seed in seeds:
        p1 = map_to_dest(seeds_to_soil, seed)
        p2 = map_to_dest(soil_to_fertilizer, p1)
        p3 = map_to_dest(fertilizer_to_water, p2)
        p4 = map_to_dest(water_to_light, p3)
        p5 = map_to_dest(light_to_temperature, p4)
        p6 = map_to_dest(temperature_to_humidity, p5)
        p7 = map_to_dest(humidity_to_location, p6)
        print(seed, p7)
        if p7 < min_loc:
            min_loc = p7

    print(min_loc)

def p2():
    with open("d5.input") as f:
        lines = f.read().splitlines()
        score = 0

    seeds = list(map(int, lines[0][7:].split(" ")))
    seed_pairs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds) - 1, 2)]
    print(seed_pairs)
    seeds_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    current_map = None
    for line in lines:
        if line == "":
            continue
        if line.startswith("seed-to-soil"):
            current_map = seeds_to_soil
        elif line.startswith("soil-to-fertilizer"):
            current_map = soil_to_fertilizer
        elif line.startswith("fertilizer-to-water"):
            current_map = fertilizer_to_water
        elif line.startswith("water-to-light"):
            current_map = water_to_light
        elif line.startswith("light-to-temperature"):
            current_map = light_to_temperature
        elif line.startswith("temperature-to-humidity"):
            current_map = temperature_to_humidity
        elif line.startswith("humidity-to-location"):
            current_map = humidity_to_location
        else:
            if current_map is None:
                continue
            else:
                current_map.append(list(map(int, line.split(" "))))

    min_loc = float('inf')
    for (start, range_) in seed_pairs:
            p1 = map_partial_app("seeds_to_soil", seeds_to_soil, start, range_)
            for (start, range_) in p1:
                p2 = map_partial_app("soil_to_fertilizer", soil_to_fertilizer, start, range_)
                for (start, range_) in p2:
                    p3 = map_partial_app("fertilizer_to_water", fertilizer_to_water, start, range_)
                    for (start, range_) in p3:
                        p4 = map_partial_app("water_to_light", water_to_light, start, range_)
                        for (start, range_) in p4:
                            p5 = map_partial_app("light_to_temperature", light_to_temperature, start, range_)
                            for (start, range_) in p5:
                                p6 = map_partial_app("temperature_to_humidity", temperature_to_humidity, start, range_)
                                for (start, range_) in p6:
                                    p7 = map_partial_app("humidity_to_location", humidity_to_location, start, range_)
                                    for (start, range_) in p7:
                                        if start < min_loc:
                                            min_loc = start

    print(min_loc)

if __name__ == "__main__":
    p2()