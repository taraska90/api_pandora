import pycurl
import cStringIO
import pprint

def main():
	ip = '172.16.100.7'
	pandora_url = '/pandora_console'
	apipass = 'S7e3xd9Wa'
	user = 'admin'
	password = 'pandora'
	op = 'get'
	op2 = 'all_agents'
	return_type = 'csv'
	other = ''
	other_mode = ''
	
	url = "http://" + ip  + pandora_url + "/include/api.php"
	
	url += "?"
        url += "&op=" + op
        url += "&op2=" + op2
	url += "&return_type=" + return_type
	url += "&apipass=" + apipass
	url += "&user="  + user
	url += "&pass=" + password
	
	buf = cStringIO.StringIO()
	
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	
	output = buf.getvalue()
	buf.close()
	
	lines = output.split("\n")
	agents = []
	for line in lines:
		if not line:
			continue
		
		fields = line.split(";")
		agent = {}
		agent['id_agent'] = fields[0]
		agent['name'] = fields[1]
		agent['ip'] = fields[2]
		agent['description'] = fields[3]
		agent['os_name'] = fields[4]
		agent['url_address'] = fields[5]
		
		agents.append(agent)
	
	for agent in agents:
		print("---- Agent #" + agent['id_agent'] + " ----")
		print("Name: " + agent['name'])
		print("IP: " + agent['ip'])
		print("Description: " + agent['description'])
		print("OS: " + agent['os_name'])
		print("URL: " + agent['url_address'])
		print("")


main()
#if __name__ == "__main__":
#    main()
