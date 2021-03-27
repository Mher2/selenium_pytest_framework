class Config:
    def __init__(self, env):

        supported_envs = ['dev', 'qa']

        if env.lower() not in supported_envs:
            raise Exception(f'{env} is not supported environment (supported envs: {supported_envs})')

        self.base_url = {
            # https://www.techbeamers.com/websites-to-practice-selenium-webdriver-online/#2httpthedemositecouk
            'dev': "http://dev-the-internet.herokuapp.com",
            'qa': "http://the-internet.herokuapp.com"
        }[env]

        self.app_port = {
            'dev': 3000,
            'qa': ''
        }[env]
