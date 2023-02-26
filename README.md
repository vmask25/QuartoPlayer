# Quarto

## Task
Create an agent trained to play **Quarto! Game**.

## General Idea
We decided to implement an agent that exploits **minMax strategy**. Given the high number of possible reachable states, a certain number of optimizations were required.

In particular, looking through academic papers, we found out that in the board there are a certain number of exploitable **symmetries**, which allow us to greatly reduce the amount of explorable states.

## Development

In order to implement minMax algorithm and to reduce the already not low computational weight, we introduce a **dictionary** to store already visited states.
To achieve this, we used the actual state of the board as _key_ and the possible moves with a goodness metric as _values_.

To maximize **collisions** in the dictionary, we check all the symmetries of the state.
In this way even if the state seems unseen, we already know the best next move.
Obviously we need to transpose the move's information accordingly to corresponding symmetry. To do that we confronted on paper a "base" board and several "symmetric boards" to evaluate differences. We then implemented a _deSymmetrize_ function to perform the task.

Even checking the symmetries, the number of possible states is some order of magnitude too high to be fully explored in reasonable time. So we introduce **alpha-beta pruning** in order to cut irrelevant branches.

We decided to implement a **stopping condition** in the exploration, based on the number of keys in the dictionary. After reaching this limit (tweaked by hand), the agent will stop the exploration and will perform some moves without further exploring from that state. After few moves, the stopping condition is reset and we start again exploring from the new state. In the beginning those moves were randomly generated. This strategy led to poor performances during some test games. So we chose to implement a more heuristic strategy, in which we rapidly **test** all the possible moves we can perform in that state and we ignore those that could lead to an immediate opponent's victory.

To further reduce the exploration space, we decide to **randomly** make the first move (piece selection), in this way at the beginning of the exploration we can cut 15/16th of the original search tree.

## Performances
As we found out, the maximum number of keys in the dictionary heavily impact performance. Se we had to tune this parameter in order to obtain good results with acceptable computational time.

Specifically we tested these values:

- 1000: barely winning against random. Initial exploration time of few seconds.
- 10k: almost always winning against random, but ineffective against human-like players. Initial exploration time of tens of seconds.
- 100k: winning against random, can compete against basic opponents. Initial exploration time of 1-2 minutes.
- 200k: can easily win against basic opponents and compete with intermediate players. Initial exploration time of roughly 5 minutes.
- 400k: can win against intermediate players and compete with experienced players. Initial exploration time of roughly 9 minutes.

Despite the pretty high initial exploration time, **400k** in our opinion is the best value. Using that the agent is capable of high performance and, after the first exploration, the subsequent moves are made without any delay w.r.t the opponent's move.
Is worth mentioning also **100k**, because it leads to acceptable results with a much shorter initial exploration time.
Smaller values are useful only against random or for code-testing purposes.

(Measures were taken using python _time_ library on a AMD Ryzen 5 3600x)

## Sources
Besides the code provided by the professors, we used the following sources:
- Theoretical:
    - https://www.slideshare.net/MatthewKerner2/quarto-55043713

    - https://web.archive.org/web/20041012023358/http://ssel.vub.ac.be/Members/LucGoossens/quarto/quartotext.htm

    - https://www.mathpages.com/home/kmath352.htm

    - http://web.archive.org/web/20120306212129/http://www.cs.rhul.ac.uk/~wouter/Talks/quarto.pdf
- Practical:
    - https://github.com/PetrosTepoyan/QuartoGame-GameSearchAlgorithms/blob/7d8ea4b50a788ab8c9e1563252151e6dac2072a4/Code/board.py#L133

## Contributors

- [Marco Sacchet](https://github.com/saccuz)
- [Fabrizio Sulpizio](https://github.com/Xiusss)
