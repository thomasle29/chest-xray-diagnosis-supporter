import yaml


class Reader:
    '''
    Reader class
    '''

    # Identify path config file 
    config_dir = "Config/SERVICE_CONFIG.yaml"

    def get_config(self):
        '''
        This function try to read a config file have identity above;
        Giving the value of the config file
        '''

        # Read config file
        with open(self.config_dir) as file:
            # Load config data
            data = yaml.load(file, Loader=yaml.FullLoader)

            # Close file
            file.close()
        
        return data