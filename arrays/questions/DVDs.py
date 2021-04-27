# DVD Box Maximum number of dvds the inventory can hold = 100

# DVD:
    # Movie name
    # year
    # director
    # description

dvd_collection = [None] * 15   # serves as the dvd box that holds a maximum of 100 dvds

class DVD:

    def __init__(self, name, release_year, director, description=None):
        self.name = name
        self.release_year = release_year
        self.director = director
        self.description = description


    def __str__(self):
        return f"{self.name}, directed by {self.director}, released in {self.release_year}"


if __name__ == "__main__":
    avenger_dvd = DVD("Avengers", 2012, "Abuchi Obiegbu")
    incredible_dvd = DVD("The Incredibles", 2004, "Dika Eneh")
    lion_king_dvd = DVD("The Lion King", 2019, "Jon Favreau")

    dvd_collection[0] = avenger_dvd
    dvd_collection[1] = incredible_dvd
    dvd_collection[2] = lion_king_dvd

    for i in range(3):
        print(dvd_collection[i])