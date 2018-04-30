# -*- coding: utf-8 -*-

# The suspects ...
import numpy as np
import pandas as pd

# Information
__author__ = "wildlyclassyprince"
__version__ = "$Revision: 0.1.1 $"
__licence__ = "GNU"

# Display values counts for each column.
class display:
	'''
	Display elements of a dataframe.
	'''

	def __init__(self, dataframe):
		self.dataframe = dataframe
		self.shape = dataframe.shape
		self.head = dataframe.head()
		self.columns = dataframe.columns
		self.fields = list()

	def unique_value_counts(self):
		'''
		Prints the total number of unique values in each column.
		'''
		_cols = (x for x in self.dataframe.columns)
		try:
			while True:
				field = _cols.__next__()
				print('='*75,
					  '\n Column Name: ', field,
					  '\n\n',self.dataframe[field],
					  '\n',
					  '='*75,
					  '\n')
		except StopIteration:
			print('Done!\n')
		except KeyError:
			print('Nothing to do.\n')

	def word_case(self, font='Title'):
		'''
		Change the letter-case for columns containiing strings.
		'''
		self.font = font
		_names = (x for x in self.columns)
		try:
			while True:
				value = _names.__next__()
				if (self.dataframe[value].dtype == 'O'):
					if (font in ['Title', 'title']):
						self.dataframe[value] = self.dataframe[value].str.title()
					elif (font in ['Lower', 'lower']):
						self.dataframe[value] = self.dataframe[value].str.lower()
					elif (font in ['Upper', 'upper']):
						self.dataframe[value] = self.dataframe[value].str.upper()
					else:
						pass
		except StopIteration:
			print('Done!\n')
		except KeyError:
			print('Nothing to do.\n')
		return self.columns

class clean:
	'''
	Removing unwanted or unnecessary columns.
	'''

	def drop_fields(self, field):
		'''
		Return the dataframe after deleting the tagged columns.
		'''

		print('Initial dataframe shape:{0}{1}'.format(self.shape, '\n'))
		_drop = (x for x in self.fields.append(field))
		try:
			while True:
				del self.dataframe[_drop.__next__()]
		except StopIteration:
			print('\nDone!\nNew dataframe shape:', self.shape,
						'\n\nThis is what the dataframe looks like now:\n')
		except KeyError:
			print('Column does not exist.')
			pass
		return self.head

	def remove_fields(self):
		'''
		To remove redundant columns, i.e., columns with single or no
		entries, or with more than 50% of the data missing from a dataset.
		'''

		# First, we identify the columns we want to remove.
		print('Initial shape of the dataset:{0}{1}'.format(self.shape, '\n'))
		_remove_cols = []
		for column in self.columns:

		# Check the number of unique items in each column.
			if len(self.dataframe[column].unique()) == 1:
				_remove_cols.append(column)
				# Check the number of missing values in each column.
				# In this case, if half the column has missing values, we want to drop it.
			elif self.dataframe[column].isnull().sum() > ((self.dataframe.shape[0])/2):
				_remove_cols.append(column)
			if len(_remove_cols) > 0:
				for colum in _remove_cols:
					print('The following will be removed:{0}{1}'.format(column, '\n'))
			else:
				print('Nothing to delete.\n')

			# We then proceed to remove the columns.
			_remove = (x for x in _remove_cols)
			try:
				while True:
					del self.dataframe[_remove.__next__()]
			except StopIteration:
				print('Final shape of the dataset:{0}'.format(self.shape))
			except KeyError:
				print('Nothing to do.\n')

		return self.head
