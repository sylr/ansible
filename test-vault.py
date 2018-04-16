from ansible.parsing.yaml.loader import AnsibleLoader

if __name__ == "__main__":
	with open("pwet.yml", 'r') as stream:
		loader = AnsibleLoader(stream, "pwet.yml")
		print(loader.get_data())
