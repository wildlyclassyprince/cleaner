## Cleaner

A Python module for simplified routine data cleaning.

### Libraries

The following libraries are required by the module:

**External:**
>- pandas
>- numpy

To import the module:

`import cleaner2 as cl`

1. If you want to display the unique value counts for each field:

`cl.unique_value_counts(dataframe=data)`

2. If you want to change the character case for columns containing string data (makes it easier for data to be uniform):

`cl.word_case(dataframe=data, font='Title)`

   Available character cases are:
   >- 'Title' : sentence character case
   >- 'Upper' : upper character case
   >- 'Lower' : lower character case

_NB: The default character case is 'Title'._

3. To remove specific columns from the dataset:

`cl.remove_columns(fields=columns_to_remove, dataframe=data)`

4. To remove redundant columns, i.e., columns with single entries, no entries, or with more than 50% of the data missing:

`cl.remove_columns(dataframe=data)`

**Testing**
>- Testing for `cleaner2.py` has been done in Python 3.X. 
>- Testing scripts for `cleaner2.py` are available, however, they are incomplete.
>- `cleaner.py` has NOT been tested.
