import vk_api

class VkTools:

    def vk_auth(self, login, password, auth_handler):
        vk_session = vk_api.VkApi(login=login, password=password, auth_handler=auth_handler)
        vk_session.auth()
        vk = vk_session.get_api()

    def auth_handler(self):
        key = self.get_key()
        remember_device = False
        return key, remember_device