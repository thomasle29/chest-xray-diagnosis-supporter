from csv import reader
import yaml


class Reader:
    '''
    Reader class
    '''
    
    # Identify path config file 
    config_dir_server = "API_service\\Config\\SERVICE_CONFIG.yaml"
    config_dir_MySQL = "API_service\\Config\\MYSQL_CONFIG.yaml"
    def get_config_sever(self):
        '''
        This function try to read a config file have identity above;
        Giving the value of the config file
        '''

        # Read config file
        with open(self.config_dir_server) as file:
            # Load config data
            data = yaml.load(file, Loader=yaml.FullLoader)

            # Close file
            file.close()
        
        return data

    def get_config_MySQL(self):
        with open(self.config_dir_MySQL) as file:
            # Load config data
            data = yaml.load(file, Loader=yaml.FullLoader)

            # Close file
            file.close()
        return data
