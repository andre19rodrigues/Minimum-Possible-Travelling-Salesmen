# Minimum-Possible-Travelling-Salesmen

This is an academic project that solves with genetic algorithms the NP-hard problem of the travelling salesman.

Two approaches have been made:

 - The **first** is the normal approach, it calculates the shortest path for a travelling salesman, starting and ending at the same point (warehouse), going through all points once and only once. The distance between point A and point B may be different from the distance between point B and point A, as in real life, due to several factors, such as one-way streets, etc.
 - The **second** approach simulates the operation of a delivery company where there is a warehouse from which the employees depart to deliver the products. Each employee has a daily limit of work (we considered a distance limit). A goal of a company would be to deliver all the products using the shortest distance and the smallest number of employees possible, with each employee limited to a maximum daily working distance. The rules are the same, each employee can go once and only once to each location. The distance between the same delivery points may be different depending on the direction. An employee can not go to a point where another employee has already been.
The final result is shown in a graph, using networkx.

[André Rodrigues](https://github.com/andre19rodrigues) & [Fábio Pereira](https://github.com/FabioAndrePereira)
