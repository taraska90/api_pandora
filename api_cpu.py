# -*- coding: utf-8 -*-
import requests
import pycurl
import cStringIO
import pprint
import urllib

def netw_comp_create():
        ip = '172.16.100.7'
        pandora_url = '/pandora_console'
        apipass = 'S7e3xd9Wa'
        user = 'admin'
        password = 'pandora'
        op = 'set' #set or get mode
        op2 = 'new_network_component' #choose type
        description = 'network%20component%20created%20by%20API'
        network_component_type='15' #remote snmp numeric
        #network_component_type='16' #remote snmp inc
        #network_component_type='18'     #remote snmp boolean
        #network_component_group='50' #cisco test group
        network_component_group='52' #cisco 3600 group
        snmp_community = 'exit'
        min_critical='80'
	max_critical='0'
	min_warning='70'
	max_warning='0'

        return_type = 'csv'
        #other =  network_component_type + "%7C" + description + "%7C%7C%7C%7C" + snmp_community + "%7C2%7C%7C1%7C%7C%7C%7C%7C%7C%7C%7C%7C" + network_component_group +  "%7C" + snmp_oid
        other_mode = 'url_encode_separator_%7C'

        url = "http://" + ip  + pandora_url + "/include/api.php"

        url += "?"
        url += "&op=" + op
        url += "&op2=" + op2
        with open('3600/cpu', 'r') as file:
                    for cpufile in file:
                        other = '' #обнуляю строку
                        cpufile=cpufile.split('|')# делаю из строки интерф+oid список psu и oid'ов
                        module_name = urllib.quote(cpufile[0], safe='')#переформатирую имя интерфейса в url code
                        #id = 'Oper%20Status%20On%20Interface%20'#наименование снимаемых данных
                        id = module_name
                        snmp_oid = cpufile[1] #формирую snmp_oid
                        other =  network_component_type + "%7C" + description + "%7C%7C%7C%7C" + snmp_community + "%7C3%7C%7C1%7C" + min_warning  + "%7C" + max_warning + "%7C%7C" + min_critical + "%7C" + max_critical + "%7C%7C%7C%7C" + network_component_group +  "%7C" + snmp_oid
                        url += "&id=" + id
                        url += "&other=" + other
                        url += "&other_mode=" + other_mode
                        url += "&apipass=" + apipass
                        url += "&user="  + user
                        url += "&pass=" + password
                        print url
			response=requests.get(url)

netw_comp_create()

