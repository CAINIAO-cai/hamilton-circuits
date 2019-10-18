import timeit
import functools
import utilities


def NN(distances, initial_vertex, vertices):
    N = len(vertices)

    circuit = [initial_vertex]
    current_vertex = initial_vertex

    unvisited_vertices = list(vertices)
    unvisited_vertices.remove(initial_vertex)

    cost = 0
    for i in range(N - 1):
        next_vertex = unvisited_vertices[0]
        min_distance = distances[current_vertex][next_vertex]
        for vertex in unvisited_vertices:
            if distances[current_vertex][vertex] < min_distance:
                next_vertex = vertex
                min_distance = distances[current_vertex][vertex]
        circuit.append(next_vertex)
        unvisited_vertices.remove(next_vertex)
        current_vertex = next_vertex
        cost = cost + min_distance

    circuit.append(initial_vertex)
    cost = cost + distances[current_vertex][initial_vertex]
    return circuit, cost


if __name__ == "__main__":
    # build our moons array(our entry point is also considered a moon)
    moons = utilities.read_input('input.txt')

    # build our 2-D matrix with the distances
    distances = utilities.calc_distances(moons)

    # run the nearest neighbour algorithm
    circuit, cost = NN(distances, moons[0], moons)

    # calculate average running speed of NN for our problem
    t = timeit.Timer(functools.partial(NN, distances, moons[0], moons))
    timeit_results = t.autorange()

    # print the results from NN
    utilities.print_alg_results("nearest neighbour", distances, circuit, cost, timeit_results)
