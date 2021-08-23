available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

#add stamina grains to health points, if key doesn't exist, add zero
health_points += available_items.get("stamina grains", 0)
#pop stamina grains from list
available_items.pop("stamina grains", 0)

#add power strw to health_points
health_points += available_items.pop("power stew", 0)

#add mystic bread in the same way
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
