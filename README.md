# Python Based A* Pathfinding implementation
For more details on the [A* algorithm](https://wikipedia.org/wiki/A*_search_algorithm)

## definition(start_node, goal_node, cost_method, heuristic_method, neighbor_method, depth_limit=None)

### Expected Objects
 - start_node
    - The node in your map that you are starting at. This can be any value/object you want
 - goal_node
    - The node in your map that you are targeting to reach. This can also be any value/object you want
 - depth_limit
    - The number of passes you want a* to do before stopping. By default this is set to None and therefore will run until its little heart gives out. Use this if you are looking to do IDA ([Iterative Deepening A*](https://wikipedia.org/wiki/Iterative_deepening_A*))

### Expected Methods
 - cost_method
    - definition(current_node, neighbor_node)
    - #### Expected Return: a numerical representation of the cost of moving from our current node to the presented neighbor_node.
 
 - heuristic_method
    - definition(node1, node2)
    - #### Expected Return: a numerical representation of the "benefit" of moving from node1 to node2. This will be where most "logic" happens
        in a*. The general usage of this will be as follows
        - heuristic_method(neighbor_node, goal_node)
 
 - neighbor_method
    - definition(node)
    - #### Expected Return: a list of neighboring nodes to the presented node. As before, the list can contain any object type you want.
  
### Returns
 - A list of nodes (provided at some point by the neighbor_method) that is the most efficient path to follow from start to finish

### Usage
  ```python
  import astar

  def cost_method(current_node, neighbor_node):
      # You can do whatever logic you want here. Traditionally this would return the distance between the 2 nodes
      # EG
      # return distance(current_node, neighbor_node)
      # However as long as you return a number of some kind, a* will accept it. 
      return 0

  def heuristic_method(node1, node2):
      # Here is where a bulk of your logic should go. This is how you will determine which node is the preferred one to
      # traverse to. See https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode for more details
      return 0

  def neighbor_method(node):
      # You should look at the current node being presented and return a list of its "neighbor" nodes. Neighbors in this sense are
      # any node that you could sensibly jump to from the presented node
      return []

  path = astar(your_map.start, your_map.desired_end, cost_method, heuristic_method, neighbor_method)
  # once a* is done, it will return a path in order from start to end that you can traverse through
  ```
