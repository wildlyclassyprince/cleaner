## Cleaner

A Python module for simplified routine data cleaning.

### Libraries

The following libraries are required by the module:

**External:**
>- pandas
>- numpy
>- matplotlib
>- seaborn

To import the module:

`import cleaner2 as clr`

1. To display the number of unique values for each field:

`clr.unique_values(dataframe=data)`

2. To display the number of unique value counts for each field:

`clr.unique_value_counts(dataframe=data`

3. To change the character case for columns with string data (imposing uniformity on the data):

`clr.word_case(dataframe=data, font='Title')`

   Available character cases are:
   >- 'Sentence'  : capitalize the first word only
   >- 'Title'     : capitalize each word
   >- 'Upper'     : all letters in upper-case
   >- 'Lower'     : all letters in lower-case

_NB: The default character case is 'Title'._

4. To remove specific columns from the dataset (deliberate clean-up of redundant data):

`clr.remove_columns(fields=columns_to_remove, dataframe=data)`

5. To remove redundant columns, i.e., columns with single entries, no entries, or with more than 50% of the data missing:

`clr.remove_columns(dataframe=data)`

6. To plot frequencies:

`clr.frequency_plot(dataframe=data, x=x_variable, title=title_of_plot, xlabel=x_label, hue=None)`

*To-Do:*

This is a to-do list for both scripts, i.e., `cleaner.py` and `cleaner2.py`.

[ ] Rewrite `cleaner.py` and make it Pythonic
[ ] Rewrite `cleaner2.py` with funcion wrappers
[ ] Build tests
[ ] Verify tests and validate functionality
