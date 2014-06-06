import mechanize
 
PE_LOGIN = 'http://projecteuler.net/login'
PE_FRIENDS = 'http://projecteuler.net/friends'
PE_PROGRESS = 'http://projecteuler.net/progress='

#load user info
f = open('.security', 'r')
USERNAME = f.readline()
PASSWORD = f.readline()
f.close()

USERNAME=USERNAME[:-1]
PASSWORD=PASSWORD[:-1]

def get_crawl_list(inp):
	out = []
	idx = 0
	data = inp
	while True:
		try:
			idx = data.index('progress=') + 9
		except ValueError:
			break
		data = data[idx:]
		idx = data.find('\"')
		str = data[:idx]
		if str == USERNAME:
			break
		out.append(str)
	return out

def get_solved(inp):
	idx = inp.find('<div id=\"problems_solved_section\">')
	i2 = inp.find('<div id=\"problems_solving_awards_section\">')
	data = inp[idx:i2]
	idx = data.find('<tr>')
	i2 = data.rfind('</tr>')
	data = data[idx:i2+10]
	num = 1
	out = ""
	while True:
		try:
			idx = data.index('<td class=')
		except ValueError:
			return out

		if data.startswith('<td class=\"problem_solved\">',idx):
			out += str(num) + ' '

		idx = data.find('</a></td>')
		data = data[idx+9:]
		num += 1
 
def main():
	browser = mechanize.Browser()
	browser.open(PE_LOGIN)

	browser.select_form(name="login_form")
	browser['username'] = USERNAME
	browser['password'] = PASSWORD

	browser.submit()
	
	res = browser.open(PE_FRIENDS)

	crawl_list = get_crawl_list(res.get_data())
	
	for u in crawl_list:
		f = open('result/'+u, 'w+b')
		res = browser.open(PE_PROGRESS+u)
		rstr = get_solved(res.get_data())
		f.write(rstr)
		f.close()

if __name__ == "__main__":
	main()
