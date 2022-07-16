from ast import arg
from unittest import result
from Infrastructure import util
import Config.reader as reader
import main
import json
import requests


class App:
    '''
    App class
    Manufacturing application function of this service
    '''
    reader = reader.Reader()
    config_MySQL = reader.get_config_MySQL()
    # config database
    def __init__(self) -> None:
        self.util   = util.Util(host = self.config_MySQL['MYSQL']['HOST'], 
                                user = self.config_MySQL['MYSQL']['USER'], 
                                password = self.config_MySQL['MYSQL']['PASSWORD'], 
                                database = self.config_MySQL['MYSQL']['DATABASE'])

    def pro_login(self, args):
        args = self.pre_json(args)
        sql = self.util
        return sql.pro_login(args)
    

    def pro_new_medical_record(self,args):
        args = self.pre_json(args)
        sql = self.util
        new_medical = sql.pro_new_medical_record(args)
        chest_result 
        if new_medical == "0":
            chest_result = self.chestDiagnosis(args["xray_image"])
            chest_result_dict = json.reads(chest_result)
            for rs in chest_result_dict:
                self.pro_diagnosis_report(  [args["medical_record_id"],
                                            sql.pro_disease_id(rs),
                                            rs["base64_image_diagnosis"],
                                            [chec_re]])


            for dis in chest_result:
                for dis_infor in dis:
                    self.pro_diagnosis_report([args["medical_record_id"],sql.pro_disease_id(chest_result_dict[])])
            return chest_result
        else:
            return new_medical
    
    def pro_diagnosis_report(self,args):
        args = self.pre_json(args)
        sql = self.util
        return sql.pro_diagnosis_report(args)

    def chestDiagnosis(self,medical_args):
        response = requests.get("http://127.0.0.1:8000/chest/diagnosis",params=medical_args)
        result = response.text
        if result == "0":
            return "0"
        return response.text


    def pre_json(self,j_str):
        j_arr = []
        for str in j_str:
            j_arr.append(j_str[str])
        return j_arr