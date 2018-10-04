import requests
import json

"""
Задача №1

Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
Задача №2

Поиск общих друзей должен происходить с помощью оператора &, 
т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2,
в этом списке должны быть экземпляры классов.
Задача №3

Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK

"""

'6edd3c2ac83b7541fe62857cf68e6c4ba6e445a25ea9f7f6dc1c6be117613f60562fcb2e5bfd854b8d542'


class VKUser:
    def __init__(self, user_id, app_token):
        self.user_id = user_id
        self.app_token = app_token

    def get_friends(self):
        url = 'https://api.vk.com/method/friends.get?user_id=' + self.user_id + '&v=5.85&access_token=' + self.app_token
        result = requests.get(url)
        friends_dict = json.loads(result.text)
        friends_list = friends_dict.get('response').get('items')
        return friends_list

    def get_info(self,):
        url = 'https://api.vk.com/method/users.get?user_ids='+self.user_id+'&v=5.85&access_token=' + self.app_token
        result = requests.get(url)
        return result.text


def find_friends():
    mutual_friends_list = []
    friend_list_u1 = []
    friend_list_u2 = []
    app_token = '4d6e344290fa8591d97e0981d356d4ec42bc9d60afca0ff4d4143c7d0ed640473e2747d9c3e5e2d6294d8'
    while True:
        print()
        print('Выберите действие:')
        print('u ввести ID пользователей u1 и u2 ')
        print('m получить список общих друзей u1 и u2')
        print('d очистить списки u1 и u2')
        print('e выход')
        get_act = input('Введите требуемое действие.')
        print()
        if get_act == 'u':
            user_id = input('Введите id u1: ')
            user_1 = VKUser(user_id, app_token)
            friend_list_u1 = user_1.get_friends()
            user_id = input('Введите id u2: ')
            user_2 = VKUser(user_id, app_token)
            friend_list_u2 = user_2.get_friends()
            input('Нажмите ENTER для продолжения.')
        elif get_act == 'm':
            if len(friend_list_u1) == 0:
                print('Не получен список друзей u1')
                continue
            if len(friend_list_u2) == 0:
                print('Не получен список друзей u2')
                continue
            mutual = set(friend_list_u1).intersection(friend_list_u2)
            for i in mutual:
                mutual_friends_list = []
                current_user = VKUser(str(i), app_token).get_info()
                json_current_user = json.loads(current_user)
                user_id = json_current_user.get('response')[0].get('id')
                user_first_name = json_current_user.get('response')[0].get('first_name')
                user_last_name = json_current_user.get('response')[0].get('last_name')
                mutual_friends_list.append(['https://vk.com/id' + str(user_id), user_first_name, user_last_name])
            print()
            print('Список общих друзей:')
            for friend in mutual_friends_list:
                print(friend[1], friend[2], friend[0])
                print()

        elif get_act == 'd':
            friend_list_u2 = []
            friend_list_u1 = []
            print('Done')

        elif get_act == 'e':
            exit()


find_friends()
