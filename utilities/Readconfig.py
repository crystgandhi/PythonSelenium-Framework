import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_admin_email():
        admin_email = config.get('common info', 'admin_email')
        return admin_email

    @staticmethod
    def get_admin_password():
        admin_password = config.get('common info', 'admin_password')
        return admin_password
