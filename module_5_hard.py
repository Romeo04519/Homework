from time import sleep

class User:
    users_base = {}
    nickname = 'Admin'
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        User.users_base[nickname] = self.password, self.age

class Video:
    videos_base = {}

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.videos_base[title] = self.duration, self.time_now, self.adult_mode

class UrTube:
    current_user = User.nickname

    def __str__(self):
        return f'Urtube'

    def log_in(self, nickname, password):
        if nickname in User.users_base:
            password_base = User.users_base.get(nickname)
            if hash(password) == password_base[0]:
                print(f'Приветствую, {nickname}')
                UrTube.current_user = nickname
            else:
                print('Неверный пароль')
        else:
            print('Пользователь не найден')

    def register(self, nickname, password, age):
        if nickname in User.users_base:
            print(f'Пользователь {nickname} уже существует')
        else:
            User.users_base[nickname] = password, age
            UrTube.current_user = nickname

    def log_out(self):
        UrTube.current_user = None

    def add(self, *args):
        if args[0] in Video.videos_base:
            pass
        else:
            Video(*args)

    def get_videos(self, word_search):
        list = []
        for i in Video.videos_base.keys():
        #     list.append(i)
        # for j in list:
            if word_search.lower() in str(i).lower():
                list.append(i)
            else:
                continue
        return f'{list}'

    def watch_video(self, word_check):
        if word_check in Video.videos_base:
            if UrTube.current_user in User.users_base:
                user_pruf = User.users_base.get(UrTube.current_user)
                video_check = Video.videos_base.get(word_check)
                if video_check[2] == True:
                    if user_pruf[1] >= 18:
                        for i in range(video_check[1], video_check[0]+1):
                            print(i, end =' ')
                        print ('Конец видео')
                    else:
                        print ('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(video_check[1], video_check[0] + 1):
                        sleep(10)
                        print(i, end=' ')
                    print('Конец видео')

            else:
                print('Войдите в аккаунт, чтобы смотреть видео')

        else:
            pass


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


#


