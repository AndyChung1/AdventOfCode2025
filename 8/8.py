import math
from pathlib import Path
from itertools import combinations

input_file = Path(__file__).parent / "input.txt"
points = []
with open(input_file) as file:
    for line in file:
        point = line.rstrip().split(',')
        points.append((int(point[0]), int(point[1]), int(point[2])))


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def merge_circuits(pair, circuits):
    p1, p2 = pair
    circuits_to_merge = [c for c in circuits if p1 in c or p2 in c]
    merged_circuit = set()

    for circuit in circuits_to_merge:
        merged_circuit = merged_circuit.union(circuit)

    merged_circuit = merged_circuit.union({p1, p2})

    for circuit in circuits_to_merge:
        circuits.remove(circuit)

    circuits.append(merged_circuit)    


def part_1():
    possible_pairs = list(combinations(points, 2))
    pairs_and_distances = [(pair, distance(*pair)) for pair in possible_pairs]
    sorted_pairs = sorted(pairs_and_distances, key=lambda x: x[1])
    circuits = []
    i = 0

    while i < 1000:
        shortest_pair = sorted_pairs[i][0]
        p1, p2 = shortest_pair
        if [c for c in circuits if p1 in c or p2 in c]:
            merge_circuits(shortest_pair, circuits)
        else:
            circuits.append({p1, p2})
        
        i += 1
    
    largest_circuits = sorted([len(circuit) for circuit in circuits], reverse=True)
    return math.prod(largest_circuits[:3])


print(part_1())


def part_2():
    possible_pairs = list(combinations(points, 2))
    pairs_and_distances = [(pair, distance(*pair)) for pair in possible_pairs]
    sorted_pairs = sorted(pairs_and_distances, key=lambda x: x[1])
    circuits = []

    for pair in sorted_pairs:
        shortest_pair = pair[0]
        p1, p2 = shortest_pair
        if [c for c in circuits if p1 in c or p2 in c]:
            merge_circuits(shortest_pair, circuits)
        else:
            circuits.append({p1, p2})

        if all(point in circuits[0] for point in points):
            return p1[0] * p2[0]
        
        
print(part_2())