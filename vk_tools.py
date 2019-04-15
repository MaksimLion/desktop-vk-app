import vk_api


def auth_handler():
    key = input("Enter authentication code:")
    remember_device = False
    return key, remember_device


def vk_auth(login, password):
    vk_session = vk_api.VkApi(login=login, password=password, auth_handler=auth_handler)
    vk_session.auth()
    vk = vk_session.get_api()
    response = vk.wall.get(count=1)
    print(response)


if __name__ == '__main__':
    login = input()
    password = input()
    vk_auth(login, password)