
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

#START a
oscar_winners.add("Watson Emma")
print(oscar_winners)
#END

#START b
oscar_winners_copy = oscar_winners.copy()
oscar_winners_copy.remove("Meryl Streep")
oscar_winners_copy.clear()
print(oscar_winners_copy)
#END

#START c
print(titanic_actors & dark_knight_actors)
#END

#START d
print(iron_man_actors.intersection(avengers_actors))
#END

#START e
print(actor_list.issubset(oscar_winners))
#END

#START f
print(actor_list >= avengers_actors)
#END

#START g
removed_actor = movie_cast.pop()
print(movie_cast)
#END

#START h
removed_movie_cast = movie_cast.discard("Matt Damon")
print(removed_movie_cast)
#END

#START i
titanic_no_winners = titanic_actors - oscar_winners
print(titanic_no_winners)
#END

#START j
unique_actors = titanic_actors.symmetric_difference(dark_knight_actors)
print(unique_actors)
#END

#START k
oscar_winners.update({"Cate Blanchett", "Daniel Day-Lewis"})
print(oscar_winners)
#END

#START l
print(titanic_actors.union(dark_knight_actors))
#END
