import yaml


class Reader:
    '''
    Reader class
    '''

    # Identify path config file 
    CONFIG_DIR_SERVER = "Config/SERVICE_CONFIG.yaml"
    CONFIG_DIR_MYSQL = "Config/MYSQL_CONFIG.yaml"
    CONFIG_DIR_AI_SERVER = "Config/AI_SERVER_CONFIG.yaml"

    def __init__(self) -> None:
        pass

    def get_config_sever(self):
        '''
        This function try to read a config file have identity above;
        Giving the value of the config file
        '''

        # Read config file
        with open(self.CONFIG_DIR_SERVER) as file:
            # Load config data
            data = yaml.load(file, Loader=yaml.FullLoader)

            # Close file
            file.close()
        
        return data

    def get_config_MySQL(self):
        with open(self.CONFIG_DIR_MYSQL) as file:
            # Load config data
            data = yaml.load(file, Loader=yaml.FullLoader)

            # Close file
            file.close()
        return data

    def get_config_AI_server(self):
        with open(self.CONFIG_DIR_AI_SERVER) as file:
            # Load config data
            data = yaml.load(file, Loader=yaml.FullLoader)

            # Close file
            file.close()
        return data