from common import com
import copy


class MOCKJSON():

    def get_api_info(self, api_info_data):
        api_json = {}
        api_json_temp = {}
        for api_info in api_info_data:
            self.get_json(api_info, api_json, api_json_temp)
        return [api_json, api_json_temp]

    def get_json(self, api_info, api_json, api_json_temp):
        """
        接口字段信息mock数据，拼接
        """
        if api_info['api_field_status'] == "1":
            api_info_name = api_info['api_field_name']
            if api_info['api_field_default'] == '':
                if api_info['api_field_describe']:
                    values = com.mock(api_info['api_field_describe'])
                    api_json.setdefault(api_info_name, values)
                    api_json_temp.setdefault(api_info_name, values)
                else:
                    api_info_type = api_info['api_field_type']
                    rang = com.change_list(api_info['api_field_range'])
                    if api_info_type.upper() == "STRING":
                        values = com.get_random_num(str1='STRING', min_length=int(rang[0]), max_length=int(rang[1]))
                        values_temp = values[2]
                        api_json.setdefault(api_info_name, values)
                        api_json_temp.setdefault(api_info_name, values_temp)
                    elif api_info_type.upper() == "INT":
                        values = com.get_random_num(str1='INT', min_length=int(rang[0]), max_length=int(rang[1]))
                        values_temp = values[2]
                        api_json.setdefault(api_info_name, values)
                        api_json_temp.setdefault(api_info_name, values_temp)
                    elif api_info_type.upper() == "OBJ":
                        api_json.setdefault(api_info_name, self.get_api_info(api_info["api_field_child"]))
                    elif api_info_type.upper() == "ARR":
                        api_json.setdefault(api_info_name, [self.get_api_info(api_info["api_field_child"])])
                    elif api_info_type.upper() == "LIST":
                        rang = com.change_list(api_info['api_field_range'])
                        values = com.get_random_list(int(rang[0]), int(rang[1]))
                        api_json.setdefault(api_info_name, values)
            else:
                values = api_info['api_field_default']
                api_json.setdefault(api_info_name, values)
        else:
            pass

    def get_case_list(self, case_temp, **case):
        case_dict = dict(case_temp)
        case_list = []
        for k, v in case.items():
            if isinstance(v, list):
                for i in v:
                    case_dict[k] = i
                    case_list.append(copy.deepcopy(case_dict))
            else:
                for item in self.get_case_list(case_dict[k], **case[k]):
                    case_dict[k] = item
                    case_list.append(copy.deepcopy(case_dict))
        return case_list
