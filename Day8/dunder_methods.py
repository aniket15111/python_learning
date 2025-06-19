class Movie:
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
    def __str__(self):
        return f"Movie: {self.title} by {self.director}"
    def __repr__(self):
        return f"Movie('{self.title}', '{self.director}', {self.duration})"
    def __len__(self):
        return self.duration


movie1 = Movie("Inception", "Christopher Nolan", 148)
print(movie1)
print(repr(movie1))
print(len(movie1))
print(len(Movie.__dict__))
print(vars(Movie))
