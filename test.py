import pandas as pd
from graphviz import Digraph

# Taking NFA input from User

nfa = {}
n = int(input("No. of states : "))  # Enter total no. of states
t = int(input("No. of transitions : "))  # Enter total no. of transitions/paths eg: a,b so input 2 for a,b,c input 3
for i in range(n):
    state = input("state name : ")  # Enter state name eg: A, B, C, q1, q2 ..etc
    nfa[state] = {}  # Creating a nested dictionary
    for j in range(t):
        path = input("path : ")  # Enter path eg : a or b in {a,b} 0 or 1 in {0,1}
        print("Enter end state from state {} travelling through path {} : ".format(state, path))
        reaching_state = [x for x in input().split()]  # Enter all the end states that
        nfa[state][path] = reaching_state  # Assigning the end states to the paths in dictionary

print("\nNFA :- \n")
print(nfa)  # Printing NFA
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = input().strip().split()  # Enter final state/states of NFA
###################################################

new_states_list = []  # holds all the new states created in dfa
dfa = {}  # dfa dictionary/table or the output structure we needed
keys_list = list(nfa.keys())  # conatins all the states in nfa plus the states created in dfa are also appended further
path_list = list(nfa[keys_list[0]].keys())  # list of all the paths eg: [a,b] or [0,1]

###################################################

# Computing first row of DFA transition table

dfa[str(keys_list[0])] = {}  # creating a nested dictionary in dfa
for y in range(t):
    var = "".join(nfa[keys_list[0]][
                      path_list[y]])  # creating a single string from all the elements of the list which is a new state
    dfa[str(keys_list[0])][path_list[y]] = var  # assigning the state in DFA table
    if var not in keys_list:  # if the state is newly created
        new_states_list.append(var)  # then append it to the new_states_list
        keys_list.append(var)  # as well as to the keys_list which contains all the states

###################################################

# Computing the other rows of DFA transition table
if len(new_states_list) == 0:
    dfa[str(keys_list[1])] = {}  # creating a nested dictionary in dfa
    for y in range(t):
        var = "".join(nfa[keys_list[1]][path_list[
            y]])  # creating a single string from all the elements of the list which is a new state
        dfa[str(keys_list[1])][path_list[y]] = var  # assigning the state in DFA table
        if var not in keys_list:  # if the state is newly created
            new_states_list.append(var)  # then append it to the new_states_list
            keys_list.append(var)

while len(new_states_list) != 0:  # condition is true only if the new_states_list is not empty
    dfa[str(new_states_list[0])] = {}  # taking the first element of the new_states_list and examining it
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []  # creating a temporay list
            for j in range(len(new_states_list[0])):
                if new_states_list[0][j] in nfa:
                    temp += nfa[new_states_list[0][j]].get(path_list[i], [])  # taking the union of the states
            s = ""
            # unique_chars = set(temp)
            # result_str = ''.join(unique_chars)
            char_dict = {}
            result_str = ''
            for char in temp:
                if char not in char_dict:
                    result_str += char
                    char_dict[char] = True
            s = s.join(result_str)  # creating a single string(new state) from all the elements of the list

            if s not in keys_list and s != "":
                new_states_list.append(result_str)  # then append it to the new_states_list
                keys_list.append(result_str)  # as well as to the keys_list which contains all the states
            dfa[str(new_states_list[0])][path_list[i]] = s  # assigning the new state in the DFA table

    new_states_list.pop(0)  # Removing the first element in the new_states_list

print("\nDFA :- \n")
print(dfa)  # Printing the DFA created
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)  # Printing Final states of DFA

from graphviz import Digraph


def draw_combined_automaton(combined_dict, file_name):
    dot = Digraph(comment='Combined Automaton')

    for state, transitions in combined_dict.items():
        dot.node(state)
        for symbol, next_states in transitions.items():
            if isinstance(next_states, list):
                for next_state in next_states:
                    dot.edge(state, next_state, label=symbol)
            else:
                dot.edge(state, next_states, label=symbol)

    dot.render(file_name, format='png', cleanup=True)
    dot.view(file_name)


# Given DFA
# dfa = {'A': {'0': 'AB', '1': 'B'}, 'AB': {'0': 'ABC', '1': 'BC'}, 'ABC': {'0': 'ABC', '1': 'BC'}, 'BC': {'0': 'C', '1': 'C'}}

# # Given NFA
# nfa = {'A': {'0': ['A', 'B'], '1': ['B']}, 'B': {'0': ['C'], '1': ['C']}, 'C': {'0': [], '1': ['C']}}

# Merge the NFA and DFA
combined_dict = {**nfa, **dfa}

# Draw the combined automaton

draw_combined_automaton(combined_dict, 'combined_automaton')
draw_combined_automaton(nfa, 'nfa')