import mechanize
 
PE_LOGIN = 'http://projecteuler.net/login'
PE_PROGRESS = 'http://projecteuler.net/progress='
CRAWL_LIST = ['kazel']

#load user info
f = open('.security', 'r')
USERNAME = f.readline()
PASSWORD = f.readline()
f.close()

USERNAME=USERNAME[:len(USERNAME)-1]
PASSWORD=PASSWORD[:len(PASSWORD)-1]

def foo(inp):
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

		try:
			idx = data.index('</a></td>')
		except ValueError:
			return out
		data = data[idx+9:]
		num += 1
 
def main():
	browser = mechanize.Browser()
	browser.open(PE_LOGIN)

	browser.select_form(name="login_form")
	browser['username'] = USERNAME
	browser['password'] = PASSWORD

	res = browser.submit()

	for u in CRAWL_LIST:
		f = open('result/'+u, 'w+b')
		res = browser.open(PE_PROGRESS+u)
		rstr = foo(res.get_data())
		f.write(rstr)
		f.close()

if __name__ == "__main__":
	main()
