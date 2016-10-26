
class DataManage(object):

    @staticmethod
    def manage_node_info(result):
        node_data = dict()
        num = 1
        for line in result:
            tmp_dict = dict()
            tmp_dict["name"] = line[1]
            tmp_dict["node_ip"] = line[2]
            tmp_dict["port"] = line[3]
            tmp_dict["cpus"] = line[4]
            tmp_dict["mem"] = line[5]
            tmp_dict["images"] = line[6]
            tmp_dict["state"] = line[7]
            tmp_dict["node_group"] = line[8]
            tmp_dict["containers"] = line[9]
            tmp_dict["os_version"] = line[10]
            tmp_dict["kernel_version"] = line[11]
            tmp_dict["docker_version"] = line[12]
            node_data[num] = tmp_dict
            num += 1
        return node_data

    @staticmethod
    def group_list(result):
        group_data = []
        num = 1
        for line in result:
            tmp_dic = {}
            if num < 10:
                tmp_dic['id'] = "0" + str(num)
            else:
                tmp_dic['id'] = str(num)
            tmp_dic['name'] = line[0]
            tmp_dic['isParent'] = "true"
            tmp_dic['target'] = "rightFrame"
            tmp_dic['url'] = "group?group_id=" + tmp_dic['id']
            group_data.append(tmp_dic)
            num += 1
        return group_data

    @staticmethod
    def node_list(result, id, name):
        node_data = []
        num = 1
        for line in result:
            tmp_dic = {}
            if num < 10:
                tmp_dic['id'] = id + "0" + str(num)
            else:
                tmp_dic['id'] = id + str(num)
            tmp_dic['name'] = line[0]
            tmp_dic['isParent'] = "false"
            tmp_dic['target'] = "rightFrame"
            tmp_dic['url'] = "node?node_ip=" + tmp_dic['name']
            node_data.append(tmp_dic)
            num += 1
        return node_data

    @staticmethod
    def container_list(result, id, name):
        container_data = []
        num = 1
        for line in result:
            tmp_dic = {}
            if num < 10:
                tmp_dic['id'] = id + "0" + str(num)
            else:
                tmp_dic['id'] = id + str(num)
            tmp_dic['name'] = line[0]
            tmp_dic['isParent'] = "false"
            tmp_dic['target'] = "rightFrame"
            tmp_dic['url'] = "container?con_addr=" + tmp_dic['name']
            container_data.append(tmp_dic)
            num += 1
        return container_data

    @staticmethod
    def manage_container_action_info(result):
        con_data = {}
        num = 1
        for line in result:
            tmp_dict = dict()
            tmp_dict["id_num"]      = line[1]
            tmp_dict["node_ip"]     = line[2]
            tmp_dict["con_ip"]      = line[3]
            tmp_dict["name"]        = line[4]
            tmp_dict["image"]       = line[5]
            tmp_dict["created"]     = line[6]
            tmp_dict["state"]       = line[7]
            tmp_dict["memory"]      = line[11]
            tmp_dict["cpuperiod"]   = line[14]
            tmp_dict["cpuquota"]    = line[17]
            tmp_dict["hostname"]    = line[18]
            tmp_dict["cmd"]         = line[20]
            con_data[num]           = tmp_dict
            num += 1
        return con_data


    @staticmethod
    def manage_con_usage_info(result):
        dict_data = {}
        num = 1
        for line in result:
            tmp_dict = dict()
            tmp_dict["con_id"] = line[0]
            tmp_dict["con_ip"] = line[1]
            tmp_dict["node_ip"] = line[2]
            tmp_dict["user_name"] = line[3]
            tmp_dict["con_app"] = line[4]
            tmp_dict["con_desc"] = line[5]
            dict_data[num] = tmp_dict
            num += 1
        return dict_data


    @staticmethod
    def manage_image_list(result):
        image_data = {}
        num = 1
        for line in result:
            tmp_dict = dict()
            tmp_dict["imageid"] = line[0][0:12]
            tmp_dict["repotags"] = line[1]
            tmp_dict["created"] = line[2]
            tmp_dict["virtualsize"] = line[3]
            tmp_dict["size"] = line[4]
            tmp_dict["labels"] = line[5]
            image_data[num] = tmp_dict
            num += 1
        return image_data

