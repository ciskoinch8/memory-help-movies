# from PySide2 import QtWidgets, QtCore
# from movies import get_movies
# from movies import Movie 


# class App(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("APP CINE")
#         self.setup_ui()
#         self.populate_movies()
#         self.setup_connections()

#     def setup_ui(self):
#         self.main_layout = QtWidgets.QVBoxLayout(self)

#         self.le_movieTitle = QtWidgets.QLineEdit()
#         self.btn_addMovies = QtWidgets.QPushButton("Ajouter")
#         self.lw_movies = QtWidgets.QListWidget()
#         self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
#         self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s)")

#         self.main_layout.addWidget(self.le_movieTitle)
#         self.main_layout.addWidget(self.btn_addMovies)
#         self.main_layout.addWidget(self.lw_movies)
#         self.main_layout.addWidget(self.btn_removeMovies)

#     def setup_connections(self):
#         self.btn_addMovies.clicked.connect(self.add_movie)
#         self.btn_removeMovies.clicked.connect(self.remove_movie)
#         self.le_movieTitle.returnPressed.connect(self.add_movie) # Ajouter un film en appuyant sur la touche entrée

#     def populate_movies(self):
#         movies = get_movies()

#         for movie in movies:
#             lw_item = QtWidgets.QListWidgetItem(movie.title)
#             lw_item.setData(QtCore.Qt.UserRole, movie)
#             self.lw_movies.addItem(lw_item)


#     def add_movie(self):
#         movie_title = self.le_movieTitle.text()
#         if not movie_title:
#             return False
    
#         movie =  Movie(title=movie_title)
#         resultat = movie.add_to_movies()
#         if resultat:
#             lw_item = QtWidgets.QListWidgetItem(movie.title)
#             lw_item.setData(QtCore.Qt.UserRole, movie)
#             self.lw_movies.addItem(lw_item)

#         self.le_movieTitle.setText("")
  

    
#     def remove_movie(self):
#         for selected_item in self.lw_movies.selectedItems():
#             movie = selected_item.data(QtCore.Qt.UserRole)
#             movie.remove_from_movies()
#             self.lw_movies.takeItem(self.lw_movies.row(selected_item))

# app = QtWidgets.QApplication([])
# win = App()
# win.show()
# app.exec_()



from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QLabel
from movies import Movie, get_movies

class App(QtWidgets.QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("APP CINE")
        self.setStyleSheet("color: #fff;"
                        "background-color: #222;"
                        "selection-color: #fff;"
                        "selection-background-color: purple;"
                        "font-weight: bold;")
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")


        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovie = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovie)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)
        self.btn_removeMovie.clicked.connect(self.remove_movie)

    def populate_movies(self):
        self.lw_movies.clear()
        movies = get_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False

        movie = Movie(title=movie_title)
        result = movie.add_to_movies()
        if result:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)
            self.le_movieTitle.setText("")

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()