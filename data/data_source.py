from model.connect import SQLHelper
from model.sqls import API_INFO, API_FIELF_INFO, API_INFO_PID


class DATAS():

    def get_api_data(self):
        api_info = SQLHelper.select(API_INFO, args=None)
        model_datas = []
        for info in api_info:
            data = {
                "id": info['ID'],
                "url": info['URL'],
                "api_name": info['API_NAME'],
                "api_method": info['API_METHOD'],
                "info": []
            }
            api_field_infos = SQLHelper.select(API_FIELF_INFO, info['ID'])
            data["info"] = self.get_api_info_data(api_field_infos)
            model_datas.append(data)
        return model_datas

    def get_api_info_data(self, api_field_infos):
        info_data = []
        for info in api_field_infos:
            pid_data = SQLHelper.select(API_INFO_PID, info['ID'])
            print(pid_data)
            api_field_child = self.get_api_info_data(pid_data)
            data = {"api_field_name": info['API_FIELD_NAME'],
                    "api_field_type": info['API_FIELD_TYPE'],
                    "api_field_range": info['API_FIELD_RANGE'],
                    "api_field_describe": info['API_FIELD_DESCRIBE'],
                    "api_field_option": info['API_FIELD_OPTION'],
                    "api_field_default": info['API_FIELD_DEFAULT'],
                    "api_field_seat": info['API_FIELD_SEAT'],
                    "api_field_status": info['API_FIELD_STATUS'],
                    "api_field_child": api_field_child}
            info_data.append(data)
        return info_data
