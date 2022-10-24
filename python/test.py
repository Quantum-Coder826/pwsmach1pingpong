import numpy as np

data = [ ["Mando", "Grogu", "Eleven", "Jon", "Ross"],
         ["Mandalorian", "Mandalorian","Stranger Things", "Game of Thrones", "Friends"],
         ["Bounty Hunter", "Jedi Master", "Kid", "King", "Paleontologist"],
         [35, 50, 14, 30, 35] ]

np.savetxt("shows.csv", data, delimiter=", ", fmt="% s")