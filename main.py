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


class VkFriends:
    def __init__(self, app_token):
        self.app_token = app_token

    def get_friends(self, user_id):
        url = 'https://api.vk.com/method/friends.get?user_id=' + user_id + '&v=5.52&access_token=' + self.app_token
        result = requests.get(url)
        friends_dict = json.loads(result.text)
        friends_list = friends_dict.get('response').get('items')
        return friends_list

    def get_user_info(self, user_id):
        url = 'https://api.vk.com/method/users.get?user_ids='+user_id+'&v=5.85&access_token=' + self.app_token
        result = requests.get(url)
        return result.text

    def get_mutual(self,friends_list1, friends_list2):
        locallist = []
        set_for_find = set(friends_list1)
        mutual = set_for_find.intersection(friends_list2)
        for i in mutual:
            curuser = self.get_user_info(str(i))
            json_curuser = json.loads(curuser)
            u_id = json_curuser.get('response')[0].get('id')
            u_fn = json_curuser.get('response')[0].get('first_name')
            u_ln = json_curuser.get('response')[0].get('last_name')
            locallist.append(['https://vk.com/id'+str(u_id), u_fn, u_ln])
        return locallist

def find_friends():
    app_token = '6edd3c2ac83b7541fe62857cf68e6c4ba6e445a25ea9f7f6dc1c6be117613f60562fcb2e5bfd854b8d542'
    vk_api = VkFriends(app_token)
    friend_list_u1 = []
    friend_list_u2 = []

    while True:
        print('Выберите действие:')
        print('u1 Получить друзей пользователя 1')
        print('u2 получить друзей пользователя 2')
        print('m получить список общих друзей u1 и u2')
        print('d очистить списки u1 и u2')
        print('e выход')
        get_act = input('Введите требуемое действие.')

        if get_act == 'u1':

            user_id = input('Введите id u1: ')
            friend_list_u1 = vk_api.get_friends(user_id)
            print('Done')

        elif get_act == 'u2':
            user_id = input('Введите id u2: ')
            friend_list_u2 = vk_api.get_friends(user_id)
            print('Done')

        elif get_act == 'm':
            if len(friend_list_u1) == 0:
                print('Не получен список друзей u1')
                continue
            if len(friend_list_u2) == 0:
                print('Не получен список друзей u2')
                continue
            mutual_list = vk_api.get_mutual(friend_list_u1, friend_list_u2)
            print()
            print('Список общих друзей:')
            for friend in mutual_list:
                print(friend[1], friend[2], friend[0])
                print()

        elif get_act == 'd':
            friend_list_u2 = []
            friend_list_u1 = []
            print('Done')

        elif get_act == 'e':
            exit()


find_friends()
