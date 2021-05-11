class VideoGame:
    name = 'Witcher 3'
    developers = 'CD Project'
    main_character = 'Geralt 0f Rivia'

    def info(self):
        print(f'Name: {self.name}\n'
              f'Developers: {self.developers}\n'
              f'Main character: {self.main_character}')

first_copy_game = VideoGame()
first_copy_game.info()
