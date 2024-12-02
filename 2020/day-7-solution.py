import networkx as nx
import re
import pprint

def remove_bag_literal(bag):
    if 'bags' in bag:
        bag = bag.replace(' bags', '')
    else:
        bag = bag.replace(' bag', '')
    return bag


colors_count = 0


def count_contained_bags(bags_graph, bag):
    return 1 + sum(bags_graph[contained_bag][bag]['capacity']*count_contained_bags(bags_graph,contained_bag)
                   for contained_bag in bags_graph.predecessors(bag))

with open("day-7-input.txt", "r") as puzzle_input:
    edges_list = []
    for relation in puzzle_input.readlines():

        relation = relation.strip(".\n")
        relation = re.split(' contain |, ', relation)
        relation[0] = remove_bag_literal(relation[0])
        print(relation)
        # bags_graph.add_node(relation[0])
        if not relation[1] == 'no other bags':

            for bag in relation[1:]:
                bag = bag.split(" ", 1)
                bag[1] = remove_bag_literal(bag[1])
                edge = (bag[1],relation[0],  {'capacity': int(bag[0]),'visited':False})
                edges_list.append(edge)
    pp = pprint.PrettyPrinter()
    bags_graph = nx.DiGraph(edges_list)
    pp.pprint(bags_graph.nodes)
    shiny_gold=[]
    for bag in bags_graph.nodes:
        if bags_graph.in_degree(bag) == 0 and nx.has_path(bags_graph, bag, "shiny gold"):
            for eventual_containement in nx.all_simple_edge_paths(bags_graph, bag, "shiny gold"):
                containement=eventual_containement[0]
                containement_size=bags_graph.get_edge_data(*containement)["capacity"]
                print(containement,
                      bags_graph.get_edge_data(*containement)["visited"],
                      containement_size)
                partial_contained_bags_count = containement_size
                for containement in eventual_containement[1:]:
                    containement_size=bags_graph.get_edge_data(*containement)["capacity"]
                    print(containement,
                          bags_graph.get_edge_data(*containement)["visited"],
                          containement_size)
                    partial_contained_bags_count *= containement_size
                    if not bags_graph.get_edge_data(*containement)["visited"]:
                        partial_contained_bags_count += containement_size
                    bags_graph.get_edge_data(*containement)["visited"] = True
                print(partial_contained_bags_count)
                colors_count += partial_contained_bags_count
            shiny_gold.append(eventual_containement)
    print(colors_count)
    print(count_contained_bags(bags_graph, "shiny gold") - 1)




