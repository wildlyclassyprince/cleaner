# -*- coding: utf-8 -*-

# The suspects ...
import numpy as np
import pandas as pd

# Information
__author__ = "wildlyclassyprince"
__version__ = "$Revision: 0.1.1 $"
__licence__ = "GNU"

# Value counts
def unique_value_counts(dataframe):
	'''
	Prints the unique value counts for each column.
	'''
	_cols = (x for x in dataframe.columns)
	try:
		while True:
			field = _cols.__next__()
			print('='*75,
				  '\n Column Name: ', field,
				  '\n\n', dataframe[field].unique(),
				  '\n',
				  '='*75,
				  '\n')
	except StopIteration:
		print('Done.')
	except KeyError:
		print('Nothing to do.\n')

# Letter-case
def word_case(dataframe, font='Title'):
	'''
	Change the letter-case for columns containing string.
	'''
	_names = (i for i in dataframe.columns)
	try:
		while True:
			column = _names.__next__()
			if (dataframe[column].dtype == 'O'):
				if (font in ['Title', 'title']):
					dataframe[column] = dataframe[column].str.title()
				elif (font in ['Lower', 'lower']):
					dataframe[column] = dataframe[column].str.lower()
				elif (font in ['Upper', 'upper']):
					dataframe[column] = dataframe[column].str.upper()
				else:
					pass
	except StopIteration:
		print('Done.\n')
	except KeyError:
		print('Nothing to do.\n')
	return dataframe.head()

# Removing specific columns
def drop_fields(fields, dataframe):
	'''
	Returns the dataframe after deleting the tagged columns.
	'''
	print('Initial dataframe shape: {}\n'.format(dataframe.shape))
	_drop = (x for x in fields)
	try:
		while True:
			del dataframe[_drop.__next__()]
	except StopIteration:
		print('\nDone!\nNew dataframe shape: {}\n\nThe new dataframe:\n'.format(dataframe.shape))
	except KeyError:
		print('Column does not exist.')
		pass
	return dataframe.head()


# Removing redundant columns
def remove_columns(dataframe):
	'''
	To remove redundant columns, i.e., columns with single or no entries,
	or with more than 50% of the data missing.
	'''
	# First, we identify the columns we want to remove:
	print('Initial shape of the dataset:{}\n'.format(dataframe.shape))
	_removeColumn = []
	for column in dataframe.columns:
		# 1. Number of unique items the columns contains:
		if (len(dataframe[column].unique()) == 1):
			_removeColumn.append(column)
		# 2. Number of missing values:
		elif (dataframe[column].isnull().sum() > ((dataframe.shape[0])/2)):
			_removeColumn.append(column)

	if (len(_removeColumn) > 0):
		for column in _removeColumn:
			print('The following will be removed: {}\n'.format(column))
	else:
		print('Nothing to delete.\n')

	# Removing the columns
	deleteColumn = (x for x in _removeColumn)
	try:
		while True:
			del dataframe[deleteColumn.__next__()]
	except StopIteration:
		print('Final shape of the dataset:{}'.format(dataframe.shape))

	return dataframe.head()
