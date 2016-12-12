people = ['Dr. Imrul Tareq', 'Dr. Shakila Yesmin', 'Engr. Imrul Hasan'];

def split_title_lastname(people):
	titles = people.split()[0]
	lastname = people.split()[-1]
	return '{} {}'.format(titles,lastname)

result = list(map(split_title_lastname, people));
print(result);