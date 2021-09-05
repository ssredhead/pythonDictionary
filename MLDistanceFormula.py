star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]

def distance(movie1, movie2):
  distance = ((movie1[0] - movie2[0]) ** 2 + (movie1[1] - movie2[1]) ** 2) ** 0.5
  return distance


print(distance(star_wars, raiders)) # 10.77
print(distance(star_wars, mean_girls)) # 38.89
#Star Wars is more similar to Raiders of the Lost Arc