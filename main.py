from planet import Planet

planet_1 = Planet("Proxima Centauri b","Earth-sized, terrestrial","Red Dwarf") 
planet_2 = Planet("TRAPPIST-1e", "Earth-sized,in habit-zone", "Ultra-cool Dwarf (M8V)")
planet_3 = Planet("Kepler-452b", "Super-Earth, near-Earth-sized", "Sun-like (G-type)")


print(planet_1) 
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
