import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("C:\\Users\\Keerti\\Downloads\\sleep_health_data.csv")
_main_dataframe_ = pd.DataFrame(dataset)
while True:
    print("Welcome to the Sleep Health data analysis.")
    print("Choose how would you like to proceed:")
    print("1. Display the dataset.")
    print("2. Display the dataset without index.")
    print("3. Display the dataset without header.")
    print("4. Display the dataset with specific rows.")
    print("5. Display the dataset with specific columns.")
    break
_dataset_display_ = int(input("Enter your choice:"))
if _dataset_display_ == 1:
    print("Choice: Display the dataset.")
    print(_main_dataframe_)
elif _dataset_display_ == 2:
    print("Choice: Display the dataset without index.")
    _df_no_index_ = pd.read_csv("C:\\Users\\Keerti\\Downloads\\sleep_health_data.csv",index_col = 0)
    print(_df_no_index_)
elif _dataset_display_ == 3:
    print("Choice: Display the dataset without header.")
    _df_no_header_ = pd.read_csv("C:\\Users\\Keerti\\Downloads\\sleep_health_data.csv",header = None)
    print(_df_no_header_)
elif _dataset_display_ == 4:
    print("Choice: Display the dataset with specific rows.")
    print(_main_dataframe_)
    n = int(input("Enter the number of rows you want:"))
    _df_specific_rows_ = pd.read_csv("C:\\Users\\Keerti\\Downloads\\sleep_health_data.csv",nrows = n)
    print(_df_specific_rows_)
elif _dataset_display_ == 5:
    print("Choice: Display the dataset with specific columns.")
    print(_main_dataframe_)
    i = int(input("Enter the number of columns you want"))
    colmns = [ ]
    for i in range(0,i):
        _col_name_ = input("Enter column name:")
        colmns.append(_col_name_)
    _df_specific_columns_ = pd.read_csv("C:\\Users\\Keerti\\Downloads\\sleep_health_data.csv",usecols = colmns)
    print(_df_specific_columns_)
else:
    print("Invalid Request")
#print(_main_dataframe_)
while True:
    print("Choose whichever function you want to use by entering the number associating to it.")
    print("1. Displaying the rows from the top.")
    print("2. Displaying the rows from the bottom.")
    print("3. Fetching index's names from the data. ")
    print("4. Fetching column's names from the data.")
    print("5. Fetching size of the dataset.")
    print("6. Fetching Shape of the dataset.")
    print("7. Fetching the datatype of the dataset.")
    print("8. Perform a Transpose on the dataset.")
    print("9. Accessing condition based values from the dataset.")
    print("10. Visualisation of the dataset.")
    break
_choice_ = int(input("Enter choice:"))
if _choice_ == 1:
    print("Choice: Displaying the rows from the top.")
    print("Please enter the number of rows you wish to see:")
    _head_choice_ = int(input("Enter your choice:"))
    if _dataset_display_ == 1:
        df = _main_dataframe_.head(_head_choice_)
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.head(_head_choice_)
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.head(_head_choice_)
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.head(_head_choice_)
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.head(_head_choice_)
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 2:
    print("Choice: Displaying the number of rows from the bottom.")
    print("Please enter the number of rows you wish to see:")
    _tail_choice_ = int(input("Enter your choice:"))
    if _dataset_display_ == 1:
        df = _main_dataframe_.tail(_tail_choice_)
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.tail(_tail_choice_)
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.tail(_tail_choice_)
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.tail(_tail_choice_)
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.tail(_tail_choice_)
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 3:
    print("Choice: Fetching index's names from the data.")
    if _dataset_display_ == 1:
        df = _main_dataframe_.index
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.index
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.index
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.index
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.index
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 4:
    print("Choice: Fetching the column's name of the dataset.")
    print(_main_dataframe_.columns)
    if _dataset_display_ == 1:
        df = _main_dataframe_.columns
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.columns
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.columns
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.columns
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.columns
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 5:
    print("Choice: Fetching the size of the dataset.")
    if _dataset_display_ == 1:
        df = _main_dataframe_.size
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.size
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.size
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.size
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.size
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 6:
    print("Choice: Fetching the shape of the dataset.")
    if _dataset_display_ == 1:
        df = _main_dataframe_.shape
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.shape
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.shape 
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.shape
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.shape
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 7:
    print("Choice: Fetching the datatype of the dataset.")
    if _dataset_display_ == 1:
        df = _main_dataframe_.dtypes
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.dtypes
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.dtypes
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.dtypes
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.dtypes
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 8:
    print("Choice: Perform the Transpose on the dataset.")
    if _dataset_display_ == 1:
        df = _main_dataframe_.T
        print(df)
    elif _dataset_display_ == 2:
        df = _df_no_index_.T
        print(df)
    elif _dataset_display_ == 3:
        df = _df_no_header_.T
        print(df)
    elif _dataset_display_ == 4:
        df = _df_specific_rows_.T
        print(df)
    elif _dataset_display_ == 5:
        df = _df_specific_columns_.T
        print(df)
    else:
        print("Invalid Request")
elif _choice_ == 9:
    while True:
        print("Choice: Accessing condition based values from the dataset.")
        print("Please select which type of condition you want to apply on the dataset:")
        print("1. Row filtering conditions")
        print("2. Column filtering conditions")
        print("3. Rows and Columns to find a single value")
        break
    _slic_choice_ = int(input("Enter your choice:"))
    if _slic_choice_ == 1:
        print("Choice: Row filtering conditions")
        while True:
            print("Select the type of slicing:")
            print("1. Integer Based Slicing")
            print("2. Label Based Slicing")
            break
        _s_choice_ = int(input("Enter slicing type:"))
        if _s_choice_ == 1:            
            print("Slicing Type: Integer Based Slicing")
            if _dataset_display_ == 1:
                print(_main_dataframe_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _main_dataframe_.iloc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 2:
                print(_df_no_index_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_no_index_.iloc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 3:
                print(_df_no_header_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_no_header_.iloc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 4:
                print(_df_specific_rows_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_specific_rows_.iloc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 5:
                print(_df_specific_columns_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_specific_columns_.iloc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            else:
                print("Invalid Request")        
        elif _s_choice_ == 2:
            print("Slicing Type: Label Based Slicing")
            if _dataset_display_ == 1:
                print(_main_dataframe_)
                _st_variable_ = input("Enter starting index:")
                _end_variable_ = input("Enter ending index:")
                _slic_dataframe_ = _main_dataframe_.loc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 2:
                print(_df_no_index_)
                _st_variable_ = input("Enter starting index:")
                _end_variable_ = input("Enter ending index:")
                _slic_dataframe_ = _df_no_index_.loc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 3:
                print(_df_no_header_)
                _st_variable_ = input("Enter starting index:")
                _end_variable_ = input("Enter ending index:")
                _slic_dataframe_ = _df_no_header_.loc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 4:
                print(_df_specific_rows_)
                _st_variable_ = input("Enter starting index:")
                _end_variable_ = input("Enter ending index:")
                _slic_dataframe_ = _df_specific_rows_.loc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            elif _dataset_display_ == 5:
                print(_df_specific_columns_)
                _st_variable_ = input("Enter starting index:")
                _end_variable_ = input("Enter ending index:")
                _slic_dataframe_ = _df_specific_columns_.loc[_st_variable_ : _end_variable_, : ]
                print(_slic_dataframe_)
            else:
                print("Invalid Request")
        else:
            print("Invalid Request")
    elif _slic_choice_ == 2:
        print("Choice: Column filtering conditions")
        while True:
            print("Select the type of slicing:")
            print("1. Integer Based Slicing")
            print("2. Label Based Slicing")
            break
        _s_choice_ = int(input("Enter slicing type:"))
        if _s_choice_ == 1:
            print("Slicing Type: Integer Based Slicing")
            if _dataset_display_ == 1:
                print(_main_dataframe_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _main_dataframe_.iloc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 2:
                print(_df_no_index_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_no_index_.iloc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 3:
                print(_df_no_header_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_no_header_.iloc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 4:
                print(_df_specific_rows_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_specific_rows_.iloc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 5:
                print(_df_specific_columns_)
                _st_variable_ = int(input("Enter starting integer:"))
                _end_variable_ = int(input("Enter ending integer:"))
                _st_variable_ = _st_variable_ -1
                _end_variable_ = _end_variable_ +1
                _slic_dataframe_ = _df_specific_columns_.iloc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            else:
                print("Invalid Request")
        elif _s_choice_ == 2:
            print("Slicing Type: Label Based Slicing")
            if _dataset_display_ == 1:
                print(_main_dataframe_)
                _st_variable_ = input("Enter starting column:")
                _end_variable_ = input("Enter ending column:")
                _slic_dataframe_ = _main_dataframe_.loc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 2:
                print(_df_no_index_)
                _st_variable_ = input("Enter starting column:")
                _end_variable_ = input("Enter ending column:")
                _slic_dataframe_ = _df_no_index_.loc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 3:
                print(_df_no_header_)
                _st_variable_ = input("Enter starting column:")
                _end_variable_ = input("Enter ending column:")
                _slic_dataframe_ = _df_no_header_.loc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 4:
                print(_df_specific_rows_)
                _st_variable_ = input("Enter starting column:")
                _end_variable_ = input("Enter ending column:")
                _slic_dataframe_ = _df_specific_rows_.loc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 5:
                print(_df_specific_columns_)
                _st_variable_ = input("Enter starting column:")
                _end_variable_ = input("Enter ending column:")
                _slic_dataframe_ = _df_specific_columns_.loc[ : ,_st_variable_ : _end_variable_]
                print(_slic_dataframe_)
            else:
                print("Invalid Request")
        else:
            print("Invalid Request")
    elif _slic_choice_ == 3:
        print("Choice: Rows and Columns to find a single value")
        while True:
            print("Select the type of slicing:")
            print("1. Integer Based Slicing")
            print("2. Label Based Slicing")
            break
        _s_choice_ = int(input("Enter slicing type:"))
        if _s_choice_ == 1:
            print("Slicing Type: Integer Based Slicing")
            if _dataset_display_ == 1:
                print(_main_dataframe_)
                _st_row_variable_ = int(input("Enter starting integer for rows:"))
                _end_row_variable_ = int(input("Enter ending integer for rows:"))
                _st_column_variable_ = int(input("Enter starting integer for columns:"))
                _end_column_variable_ = int(input("Enter ending integer for columns:"))
                _st_row_variable_ = _st_row_variable_ -1
                _end_row_variable_ = _end_row_variable_ +1
                _st_column_variable_ = _st_column_variable_ -1
                _end_column_variable_ = _end_column_variable_ +1
                _slic_dataframe_ = _main_dataframe_.iloc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 2:
                print(_df_no_index_)
                _st_row_variable_ = int(input("Enter starting integer for rows:"))
                _end_row_variable_ = int(input("Enter ending integer for rows:"))
                _st_column_variable_ = int(input("Enter starting integer for columns:"))
                _end_column_variable_ = int(input("Enter ending integer for columns:"))
                _st_row_variable_ = _st_row_variable_ -1
                _end_row_variable_ = _end_row_variable_ +1
                _st_column_variable_ = _st_column_variable_ -1
                _end_column_variable_ = _end_column_variable_ +1
                _slic_dataframe_ = _df_no_index_.iloc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 3:
                print(_df_no_header_)
                _st_row_variable_ = int(input("Enter starting integer for rows:"))
                _end_row_variable_ = int(input("Enter ending integer for rows:"))
                _st_column_variable_ = int(input("Enter starting integer for columns:"))
                _end_column_variable_ = int(input("Enter ending integer for columns:"))
                _st_row_variable_ = _st_row_variable_ -1
                _end_row_variable_ = _end_row_variable_ +1
                _st_column_variable_ = _st_column_variable_ -1
                _end_column_variable_ = _end_column_variable_ +1
                _slic_dataframe_ = _df_no_header_.iloc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 4:
                print(_df_specific_rows_)
                _st_row_variable_ = int(input("Enter starting integer for rows:"))
                _end_row_variable_ = int(input("Enter ending integer for rows:"))
                _st_column_variable_ = int(input("Enter starting integer for columns:"))
                _end_column_variable_ = int(input("Enter ending integer for columns:"))
                _st_row_variable_ = _st_row_variable_ -1
                _end_row_variable_ = _end_row_variable_ +1
                _st_column_variable_ = _st_column_variable_ -1
                _end_column_variable_ = _end_column_variable_ +1
                _slic_dataframe_ = _df_specific_rows_.iloc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 5:
                print(_df_specific_columns_)
                _st_row_variable_ = int(input("Enter starting integer for rows:"))
                _end_row_variable_ = int(input("Enter ending integer for rows:"))
                _st_column_variable_ = int(input("Enter starting integer for columns:"))
                _end_column_variable_ = int(input("Enter ending integer for columns:"))
                _st_row_variable_ = _st_row_variable_ -1
                _end_row_variable_ = _end_row_variable_ +1
                _st_column_variable_ = _st_column_variable_ -1
                _end_column_variable_ = _end_column_variable_ +1
                _slic_dataframe_ = _df_specific_columns_.iloc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            else:
                print("Invalid Request")
        elif _s_choice_ == 2:
            print("Slicing Type: Label Based Slicing")
            if _dataset_display_ == 1:
                print(_main_dataframe_)
                _st_row_variable_ = input("Enter starting index for rows:")
                _end_row_variable_ = input("Enter ending index for rows:")
                _st_column_variable_ = input("Enter starting column for columns:")
                _end_column_variable_ = input("Enter ending column for columns:")                
                _slic_dataframe_ = _main_dataframe_.loc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 2:
                print(_df_no_index_)
                _st_row_variable_ = input("Enter starting index for rows:")
                _end_row_variable_ = input("Enter ending index for rows:")
                _st_column_variable_ = input("Enter starting column for columns:")
                _end_column_variable_ = input("Enter ending column for columns:")                
                _slic_dataframe_ = _df_no_index_.loc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 3:
                print(_df_no_header_)
                _st_row_variable_ = input("Enter starting index for rows:")
                _end_row_variable_ = input("Enter ending index for rows:")
                _st_column_variable_ = input("Enter starting column for columns:")
                _end_column_variable_ = input("Enter ending column for columns:")                
                _slic_dataframe_ = _df_no_header_.loc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 4:
                print(_df_specific_rows_)
                _st_row_variable_ = input("Enter starting index for rows:")
                _end_row_variable_ = input("Enter ending index for rows:")
                _st_column_variable_ = input("Enter starting column for columns:")
                _end_column_variable_ = input("Enter ending column for columns:")                
                _slic_dataframe_ = _df_specific_rows_.loc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            elif _dataset_display_ == 5:
                print(_df_specific_columns_)
                _st_row_variable_ = input("Enter starting index for rows:")
                _end_row_variable_ = input("Enter ending index for rows:")
                _st_column_variable_ = input("Enter starting column for columns:")
                _end_column_variable_ = input("Enter ending column for columns:")                
                _slic_dataframe_ = _df_specific_columns_.loc[_st_row_variable_ : _end_row_variable_,_st_column_variable_ : _end_column_variable_]
                print(_slic_dataframe_)
            else:
                print("Invalid Request")
        else:
            print("Invalid Request")
    else:
        print("Invalid Request")
elif _choice_ == 10:
    while True:
        print("Choice: Visualisation of the dataset.")
        print("Please select type of visualisation to perform on the dataset:")
        print("1. Bar Chart Visualisation")
        print("2. Line plot Visualisation")
        print("3. Histogram Visualisation")
        break
    _viz_choice_ = int(input("Enter your choice:"))
    if _viz_choice_ == 1:
        print("Choice: Bar Chart")
        while True:
            print("Choose Bar Chart to use:")
            print("1. Vertical Bar chart")
            print("2. Horizontal Bar chart")
            break
        _bar_choice_ = int(input("Enter your choice:"))
        if _bar_choice_ == 1:
            print("Choice: Vertical Bar chart")
            if _dataset_display_ == 1:
                print(_main_dataframe_)
                _main_dataframe_.plot(kind = "bar")
                plt.show()
            elif _dataset_display_ == 2:
                print(_df_no_index_)
                _df_no_index_.plot(kind = "bar")
                plt.show()
            elif _dataset_display_ == 3:
                print(_df_no_header_)
                _df_no_header_.plot(kind = "bar")
                plt.show()
            elif _dataset_display_ == 4:
                print(_df_specific_rows_)
                _df_specific_rows_.plot(kind = "bar")
                plt.show()
            elif _dataset_display_ == 5:
                print(_df_specific_columns_)
                _df_specific_columns_.plot(kind = "bar")
                plt.show()
            else:
                print("Invalid Request")
        elif _bar_choice_ == 2:
            print("Choice: Horizontal Bar chart")
        else:
            print("Invalid Request")
        if _dataset_display_ == 1:
            print(_main_dataframe_)
            _main_dataframe_.plot(kind = "barh")
            plt.show()
        elif _dataset_display_ == 2:
            print(_df_no_index_)
            _df_no_index_.plot(kind = "barh")
            plt.show()
        elif _dataset_display_ == 3:
            print(_df_no_header_)
            _df_no_header_.plot(kind = "barh")
            plt.show()
        elif _dataset_display_ == 4:
            print(_df_specific_rows_)
            _df_specific_rows_.plot(kind = "barh")
            plt.show()            
        elif _dataset_display_ == 5:
            print(_df_specific_columns_)
            _df_specific_columns_.plot(kind = "barh")
            plt.show()
        else:
            print("Invalid Request")
    elif _viz_choice_ == 2:
        print("Choice: Line Plot")
        if _dataset_display_ == 1:
            print(_main_dataframe_)
            _main_dataframe_.plot(kind = "line")
            plt.show()
        elif _dataset_display_ == 2:
            print(_df_no_index_)
            _df_no_index_.plot(kind = "line")
            plt.show()
        elif _dataset_display_ == 3:
            print(_df_no_header_)
            _df_no_header_.plot(kind = "line")
            plt.show()
        elif _dataset_display_ == 4:
            print(_df_specific_rows_)
            _df_specific_rows_.plot(kind = "line")
            plt.show()
        elif _dataset_display_ == 5:
            print(_df_specific_columns_)
            _df_specific_columns_.plot(kind = "line")
            plt.show()
        else:
            print("Invalid Request")
    elif _viz_choice_ == 3:
        print("Choice: Histogram")
        if _dataset_display_ == 1:
            print(_main_dataframe_)
            _main_dataframe_.plot(kind = "hist")
            plt.show()
        elif _dataset_display_ == 2:
            print(_df_no_index_)
            _df_no_index_.plot(kind = "hist")
            plt.show()
        elif _dataset_display_ == 3:
            print(_df_no_header_)
            _df_no_header_.plot(kind = "hist")
            plt.show()
        elif _dataset_display_ == 4:
            print(_df_specific_rows_)
            _df_specific_rows_.plot(kind = "hist")
            plt.show()
        elif _dataset_display_ == 5:
            print(_df_specific_columns_)
            _df_specific_columns_.plot(kind = "hist")
            plt.show()
        else:
            print("Invalid Request")
    else:        
        print("Invalid Request")
else:
    print("Invalid Request")
print("")

