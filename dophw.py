import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(str(password))
        self.age = int(age)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                return print(f'Вы успешно вошли в акканут {nickname}')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                return print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            print('Вы успешно зарегистрировались')
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта')

    def add(self, *new_videos):
        for new_video in new_videos:
            have = False
            for video in self.videos:
                if video.title == new_video.title:
                    break
            if not have:
                self.videos.append(new_video)
                print(f'Видео__ {new_video.title} __добавлено')


    def get_videos(self, search_word):
        search_word = str(search_word)
        search_video = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                search_video.append(video.title)
        return print(search_video)

    def watch_video(self, cur_title):
        for video in self.videos:
            if video.title == cur_title:
                if self.current_user == None:
                    print("Войдите в аккаунт чтобы смотреть видео")
                elif self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(0, video.duration):
                        i += 1
                        time.sleep(1)
                        print(i)
                    print("Конец видео")






ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
ur.get_videos('лучший')
ur.get_videos('ПРОГ')

# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')