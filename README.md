# Iterated Prisoner's Dilemma Simulated via Genetic Algorithm

## Description
THIS IS A WORK IN PROGRESS <br />
At the time of writing, this simulation isn't perfect and details may change

This project is genetic algorithm simulation of the stochastic iterated prisoners dilemma. Simulation parameters are easily changeable within the main.py script. The simulation consists of a population of "players" who are instances of the player class. These players assign weights to the actions of their opponents and themselves, calculating a probability 
that they will defect or cooperate in a given circumstance. The player instances will compete against each other in an round-robin iterated prisoners dilemma, the details of which are set in the main script. After a round of this, the selection algorithm will pick the fittest sqrt(population_size) players based on their total score for the round (unless
record is set to true, in which case it will pick based on Win-Loss-Draw record). The attributes of these fittest players will then be randomly crossed with each other via the crossover algorithm, giving us a new population the same size as the original. This simulation uses a uniform crossover algorithm. Finally, a mutation algorithm introduces 
a bit of random variance in the attributes of the new players. This process of competition, selection, crossover, and mutation completes a generation. The simulation can be run for a set number of generations, with the results of each being tracked. These results are saved in a csv, and can be graphed using graph.py. 

## Installation and usage
Simply clone the repository and install the necessary requirements (I will improve this process when the simulation is more complete). Then run main.py to run the simulation (make sure to set values at the top of main.py if you want specific characteristics). After running, you can run graph.py to see a couple graphs of simulation trends over
the generations. 
 
## Future plans
I'm still troubleshooting some of the math in this simulation, once I get a result I'm happy with, my plan is the rewrite the simulation in JavaScript and implement a UI which would allow the user to set simulation characteristics, add their own player, simulate a game between two players, and more fun stuff. 

## Inspirations and References
https://www.youtube.com/watch?v=nr8biZfSZ3Y <br />
https://www.youtube.com/watch?v=mScpHTIi-kM <br />
https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/npd.html <br />
https://www.datacamp.com/tutorial/genetic-algorithm-python 
