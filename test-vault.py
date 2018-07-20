from ansible.parsing.yaml.loader import AnsibleLoader
from pprint import pprint
from inspect import getmembers

if __name__ == "__main__":
	with open("pwet.yml", 'r') as stream:
		loader = AnsibleLoader(stream, "pwet.yml", vault_secrets="azeaze")
		pprint(getmembers(loader))
		#print(loader.get_data())
