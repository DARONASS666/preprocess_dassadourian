import setuptools

# open the readme as set the description
# for the setup.py file as the description
# in the README file
with open('README.md' , 'r') as file:
	long_description = file.read()

setuptools.setup(
	name = 'preprocess_dassadourian', #this should be unique
	version = '0.0.2',
	author = 'Daron Assadourian',
	author_email = 'daron_1997@hotmail.com',
	description = 'This is a preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)