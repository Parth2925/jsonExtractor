import json
from tabulate import tabulate


def load_json():
	try:
		with open("sample.json", 'r') as f:
			data = json.load(f)
			return data
	except Exception as e:
		print(f'Json file not found: {e}')
		exit()

def get_list(data, criteria, value):
	user_info = []
	for id in data:
		profile = id['profile']
		try:
			if value in id[criteria]:
				user = [profile['firstName'], profile['lastName'], profile['email'], profile['Role']]
				user_info.append(user)
		except Exception as e:
			print(f'Criteria or Value not found in the JSON: {e}')
			exit()		
	return user_info
	
def format_data(user_list):
	return tabulate(user_list, headers=["firstName", "lastName", "email", "Role"])

def get_criteria():
	criteria = input("Enter Criteria Name: ")
	return criteria

def get_value():
	value = input("Enter Value: ")
	return value

def main():
	data = load_json()
	criteria = get_criteria()
	value = get_value()
	output = format_data(get_list(data, criteria, value))
	with open('output.txt', 'w') as f:
		f.write(output)
	print(output)


if __name__ == '__main__':
	main()
