import math
import random
import sys
from decimal import Decimal


class Moon:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.theta = math.radians(random.randrange(360))
        self.x = self.radius * math.cos(self.theta)
        self.y = self.radius * math.sin(self.theta)

    def cartesian_distance(self, moon):
        delta_x = self.x - moon.x
        delta_y = self.y - moon.y
        distance = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))
        return distance

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)


def read_input(file):
    #set seed for randomising the theta of vertices
    random.seed(1)

    vertices = []
    with open(file, 'r') as f:
        next(f)  # skip first line
        for line in f:
            name = line.split(",")[0]
            radius = float(line.split(",")[1])
            vertex = Moon(name, radius)
            vertices.append(vertex)
    return vertices


def calc_distances(vertices):
    distances = {}
    for starting_vertex in vertices:
        distances_aux = {}
        for ending_vertex in vertices:
            distances_aux[ending_vertex] = starting_vertex.cartesian_distance(ending_vertex)
        distances[starting_vertex] = distances_aux
    return distances


def print_alg_results(alg_name, distances, circuit, cost, timeit_results):
    titlecased_name = alg_name.title()
    initials_of_name = "".join(word[0].upper() for word in alg_name.split())

    # redirect all prints to our file
    sys.stdout = open(initials_of_name + "_output.txt", "w")

    print(titlecased_name + " Results")
    print("-" * len(titlecased_name + " Results"))
    print("N = " + str(len(circuit) - 1))
    print()
    print("Distances Matrix(10^3 km):")
    # print headers
    print('{:>9s}'.format(""), end="|", flush=True)
    for moon in distances:
        print('{:>9s}'.format(moon.name), end="|", flush=True)
    print()
    # print distances
    for starting_moon in distances:
        print('{:>9s}'.format(starting_moon.name), end="|", flush=True)
        for ending_moon in distances:
            print('{:9.2f}'.format(distances[starting_moon][ending_moon]), end="|", flush=True)
        print()
    print()

    print(titlecased_name + " Circuit:")
    for i in range(len(circuit) - 1):
        print(circuit[i], end=" -> ", flush=True)
    print(circuit[-1])
    print("Total Distance: " + '{:.2f}'.format(cost) + "*10^3km")
    print()
    print("Performance Results")
    print("-" * len("Performance Results"))
    print("Repetitions: " + str(timeit_results[0]))
    print("Total time required (s): " + "{:.2E}".format(Decimal(timeit_results[1])))
    print("Average time of one execution (s): " + "{:.2E}".format(Decimal(timeit_results[1]/timeit_results[0])))