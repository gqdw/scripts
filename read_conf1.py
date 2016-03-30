import ConfigParser
    # def read_settings(self):
    #     config = ConfigParser.SafeConfigParser()
    #     conf_path = './zabbix.ini'
    #     if not os.path.exists(conf_path):
    #             conf_path = os.path.dirname(os.path.realpath(__file__)) + '/zabbix.ini'
    #     if os.path.exists(conf_path):
    #             config.read(conf_path)
    #     # server
    #     if config.has_option('zabbix', 'server'):
    #         self.zabbix_server = config.get('zabbix', 'server')

    #     # login
    #     if config.has_option('zabbix', 'username'):
    #         self.zabbix_username = config.get('zabbix', 'username')
    #     if config.has_option('zabbix', 'password'):
    #         self.zabbix_password = config.get('zabbix', 'password')

config = ConfigParser.ConfigParser()
conf_path = 'test.ini'
config.read(conf_path)

if config.has_option('test', 'a'):
    print type(config.get('test', 'a'))
    print config.get('test', 'a')
    print type(config.getint('test', 'a'))

if config.has_option('test', 'c'):
    print config.get('test', 'c')

raw_config = ConfigParser.RawConfigParser()
raw_config.add_section('section1')
raw_config.set('section1', 'an_int', '15')
raw_config.set('section1', 'a_bool', 'true')
raw_config.set('section1', 'a_float', '3.1415')
raw_config.set('section1', 'baz', 'fun')
raw_config.set('section1', 'bar', 'Python')
raw_config.set('section1', 'foo', '%(bar)s is %(baz)s!')

with open('example.cfg', 'wb') as config_file:
    raw_config.write(config_file)

