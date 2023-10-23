import numpy as np


infected_nodes=[1,2,3]
test_accuracy=0.5
tests_used=0
nodes=[1,2,3,4,5,6]


while True:
    target_node = input("target_node")
    accuracy = np.random.binomial(1, test_accuracy)
    print('accuracy',accuracy)
    if accuracy == 0:
        if target_node in infected_nodes:
            print('target node in infected nodes')
            tests_used += 1
            break
        else:
            continue

    else:
        tests_used += 1

        nodes.remove(target_node)

    print('nodes', nodes)