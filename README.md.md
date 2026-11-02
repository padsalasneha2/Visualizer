# 📊 Data Analysis & Visualization Program

> A menu-driven Python application to load, explore, clean, analyze, and visualize data from CSV files.

---

## 📌 Table of Contents

- [📖 About the Project](#-about-the-project)
- [🎯 Project Objectives](#-project-objectives)
- [✨ Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [⚙️ Requirements](#️-requirements)
- [📥 Installation](#-installation)
- [🚀 How to Run](#-how-to-run)
- [🧭 Main Menu](#-main-menu)
- [📂 Load Dataset](#-load-dataset)
- [🔍 Explore Data](#-explore-data)
- [🧮 DataFrame Operations](#-dataframe-operations)
- [🧹 Missing Data Handling](#-missing-data-handling)
- [📈 Statistical Analysis](#-statistical-analysis)
- [🎨 Data Visualization](#-data-visualization)
- [💾 Save a Visualization](#-save-a-visualization)
- [🖥️ Sample Outputs](#️-sample-outputs)
- [📁 Project Structure](#-project-structure)
- [⚠️ Important Notes and Limitations](#️-important-notes-and-limitations)
- [🔮 Possible Future Improvements](#-possible-future-improvements)
- [👨‍💻 Author](#-author)
- [📜 License](#-license)

---

## 📖 About the Project

The **Data Analysis & Visualization Program** is a Python-based, menu-driven application designed to perform common data analysis tasks on CSV datasets.

The application uses the Pandas library to load and manipulate tabular data, NumPy for numerical array operations, Matplotlib to create charts, and Seaborn for statistical visualizations.

Users interact with the application through a command-line menu. They can load a CSV file, inspect its structure, search and filter records, handle missing values, calculate descriptive statistics, and create different types of charts.

This project is useful for learning the basics of Python programming, data analysis, data cleaning, and data visualization.

## 🎯 Project Objectives

- 📂 Read and work with data stored in CSV files.
- 🔍 Understand a dataset's rows, columns, and data types.
- 🧮 Perform common DataFrame and NumPy operations.
- 🧹 Identify and handle missing values.
- 📊 Calculate descriptive statistical measures.
- 🎨 Present data visually using different chart types.
- 💾 Save a generated visualization to an image file.

## ✨ Features

| Feature | Description |
|---|---|
| 📂 CSV loading | Load a dataset from a CSV file path |
| 🔍 Data exploration | View sample rows, column names, data types, and DataFrame information |
| 🔎 Data search | Find records containing a text value in a selected column |
| ↕️ Data sorting | Sort records using a selected column |
| 🎯 Data filtering | Select records matching an exact column value |
| 🔗 DataFrame combining | Concatenate the current DataFrame with another CSV DataFrame |
| ✂️ Data splitting | Divide a DataFrame into two row or column sections |
| 🔢 NumPy operations | Convert numeric data to an array and perform basic calculations |
| 🧹 Missing-value handling | Display, fill, drop, or replace missing values |
| 📈 Statistical analysis | Calculate summary statistics for numeric columns |
| 🎨 Visualization | Generate eight types of plots |
| 💾 Plot saving | Save the current Matplotlib figure |

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| 🐼 **Pandas** | CSV reading, DataFrame manipulation, filtering, and statistics |
| 🔢 **NumPy** | Numerical arrays, splitting, and mathematical operations |
| 📊 **Matplotlib** | Creating and saving charts |
| 🌈 **Seaborn** | Correlation heatmap and box plot |

## ⚙️ Requirements

Before running the project, make sure you have:

- Python 3.8 or a newer version.
- A terminal or command prompt.
- A CSV dataset to analyze.
- Internet access for the initial package installation, if the libraries are not already installed.

### 📦 Required Python Libraries

```text
pandas
numpy
matplotlib
seaborn
```

## 📥 Installation

### Step 1: Check Python

Open your terminal or command prompt and run:

```bash
python --version
```

If your system uses the `python3` command, run:

```bash
python3 --version
```

### Step 2: Install the libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 3: Create a project folder

For example:

```text
data-analysis-visualization
```

### Step 4: Save the Python source code

Save the supplied program in a Python file named:

```text
sales_data_analyzer.py
```

## 🚀 How to Run

1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Run the following command:

```bash
python sales_data_analyzer.py
```

If required, use:

```bash
python3 sales_data_analyzer.py
```

The main menu will appear in the terminal. Enter the number for the operation you want to perform.

## 🧭 Main Menu

When the application starts, it displays the following menu:

```text
========== Data Analysis & Visualization Program ==========
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
=======================================================
Enter your choice:
```

### Main Menu Options

| Option | Menu item | Explanation |
|---:|---|---|
| 1 | 📂 Load Dataset | Reads a CSV file into the program |
| 2 | 🔍 Explore Data | Opens the data exploration menu |
| 3 | 🧮 Perform DataFrame Operations | Opens the DataFrame operations menu |
| 4 | 🧹 Handle Missing Data | Opens the missing-value handling menu |
| 5 | 📈 Generate Descriptive Statistics | Displays statistics for numeric columns |
| 6 | 🎨 Data Visualization | Opens the chart selection menu |
| 7 | 💾 Save Visualization | Saves the current Matplotlib plot |
| 8 | 🚪 Exit | Closes the program |

> **Important:** Load a dataset before selecting options 2, 3, 4, 5, or 6. Those operations require data to be present.

## 📂 Load Dataset

Select option **1 — Load Dataset**.

The program asks for the CSV file path:

```text
Enter your choice: 1
Enter the path of the dataset (CSV file): sales.csv
Dataset loaded successfully!
```

You can enter a relative path, such as `data/sales.csv`, or a full path to a file on your computer.

The program uses Pandas `read_csv()` to read the file.

## 🔍 Explore Data

Select option **2 — Explore Data**.

The exploration menu provides five options:

```text
1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic info
```

| Option | Operation | Explanation |
|---:|---|---|
| 1 | First five rows | Displays the first five records using `head()` |
| 2 | Last five rows | Displays the last five records using `tail()` |
| 3 | Column names | Displays the DataFrame column names |
| 4 | Data types | Displays each column's data type |
| 5 | Basic information | Displays information using `info()` |

### Example: First Five Rows

For illustration, suppose a CSV has `Product`, `Sales`, and `Profit` columns:

```text
  Product  Sales  Profit
0       A    100      20
1       B    200      40
2       C    300      60
3       D    400      80
4       E    500     100
```

The actual output depends on the dataset loaded.

## 🧮 DataFrame Operations

Select option **3 — Perform DataFrame Operations**.

The program displays:

```text
1. Display data
2. Search data
3. Sort data
4. Filter data
5. Combine DataFrames
6. Split DataFrame
7. NumPy array operations
8. Aggregate functions
9. Create pivot table
```

### 1. 📋 Display Data

Prints the complete DataFrame in the terminal.

### 2. 🔎 Search Data

- Enter a column name.
- Enter the text or value to search for.
- The program searches that column using partial text matching.
- The search is case-insensitive and ignores missing values during the match.

### 3. ↕️ Sort Data

Enter the column name to sort by. The program displays the DataFrame sorted by that column using Pandas `sort_values()`.

### 4. 🎯 Filter Data

Enter a column name and a value. The program displays rows where the selected column, converted to text, exactly matches the entered value.

### 5. 🔗 Combine DataFrames

Enter the path to another CSV file. The program reads the second file and combines the rows using `pd.concat()`.

The operation uses `ignore_index=True` to create a new sequential index in the displayed combined DataFrame. The original DataFrame is not replaced by this result.

### 6. ✂️ Split DataFrame

The program offers two choices:

- **Split by rows:** divides the rows into two approximately equal parts using NumPy `array_split()`.
- **Split by columns:** displays the first and second halves of the columns separately.

### 7. 🔢 NumPy Array Operations

The program selects numeric columns and converts them into a NumPy array.

It displays:

- The numeric array.
- The array shape.
- Array values after adding 10.
- Array values after multiplying by 2.
- The mean of each numeric column.

### 8. ➕ Aggregate Functions

Displays the following calculations for numeric columns:

- Sum using `sum()`.
- Mean using `mean()`.
- Non-missing count using `count()`.

### 9. 🧾 Create Pivot Table

Enter:

- An index column.
- A numeric value column.

The program creates a Pandas pivot table using `sum` as the aggregation function.

## 🧹 Missing Data Handling

Select option **4 — Handle Missing Data**.

The menu provides four choices:

```text
1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with a specific value
```

### 1. 🔍 Display Missing Rows

Displays all rows containing at least one missing value.

### 2. 📊 Fill Missing Values with Mean

Selects numeric columns and fills their missing values with the mean of their respective columns.

### 3. 🗑️ Drop Rows with Missing Values

Removes every row containing at least one missing value from the current DataFrame.

### 4. ✏️ Replace Missing Values

Asks for a replacement value and fills missing cells in the DataFrame with that value.

> ⚠️ **Data note:** Cleaning operations modify the DataFrame currently held in memory. Review your dataset before choosing an operation. The mean option applies to numeric columns only.

## 📈 Statistical Analysis

Select option **5 — Generate Descriptive Statistics**.

The program selects numeric columns and displays descriptive statistics.

### Statistical Measures

| Measure | Meaning |
|---|---|
| 🔢 Count | Number of non-missing numeric values |
| 📈 Mean | Arithmetic average |
| 🎯 Median | Middle value |
| 📉 Standard deviation | Measure of spread around the mean |
| 📐 Variance | Measure of squared spread |
| 📊 Percentiles | Values at the 25th, 50th, and 75th percentiles |
| ➕ Sum | Total of numeric values |

The program uses:

- `describe()`
- `sum()`
- `mean()`
- `median()`
- `std()`
- `var()`
- `quantile()`

### Example Statistical Output

The following values are illustrative only:

```text
Descriptive Statistics:

             Sales      Profit
count          5.0         5.0
mean         300.0        60.0
std          158.1        31.6
min          100.0        20.0
25%          200.0        40.0
50%          300.0        60.0
75%          400.0        80.0
max          500.0       100.0

Sum:
Sales     1500
Profit     300

Mean:
Sales     300.0
Profit     60.0
```

Actual values are calculated from the loaded CSV.

## 🎨 Data Visualization

Select option **6 — Data Visualization**.

The program supports eight visualization options.

```text
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Seaborn Heatmap
8. Seaborn Box Plot
```

### 1. 📊 Bar Plot

Displays the frequency of values in a selected column.

**Suitable for:** Comparing categories or counting repeated values.

### 2. 📈 Line Plot

Creates a line plot from a selected numeric column.

**Suitable for:** Viewing the sequence or trend of numeric values.

### 3. 🔵 Scatter Plot

Asks for two numeric columns:

- X-axis column.
- Y-axis column.

Displays the relationship between the two selected variables.

**Suitable for:** Exploring possible relationships between numeric variables.

### 4. 🥧 Pie Chart

Displays the frequency distribution of values in a selected column as proportions.

**Suitable for:** Showing category shares.

### 5. 📶 Histogram

Creates a histogram for a selected numeric column, using 10 bins.

**Suitable for:** Understanding the distribution of numeric data.

### 6. 🧱 Stack Plot

Asks for numeric column names separated by commas and displays their stacked values.

**Suitable for:** Comparing cumulative values across multiple numeric series.

### 7. 🌡️ Seaborn Heatmap

Creates a correlation matrix from numeric columns and displays it as a heatmap.

**Suitable for:** Exploring correlations between numeric columns.

### 8. 📦 Seaborn Box Plot

Creates a box plot for a selected numeric column.

**Suitable for:** Viewing the distribution and spread of numeric values.

> **Note:** The program displays the selected chart in a Matplotlib window. The available columns and their data types determine which chart selections are suitable.

## 💾 Save a Visualization

Select option **7 — Save Visualization** after creating a chart.

The program asks for a filename:

```text
Enter file name to save the plot (e.g., plot.png): sales_chart.png
Visualization saved as sales_chart.png successfully!
```

The plot is saved using Matplotlib's `savefig()` function.

You can use image extensions supported by your Matplotlib environment, such as `.png` or `.jpg`.

## 🖥️ Sample Outputs

The examples below illustrate the program's prompts and output format. They are not screenshots of an actual execution.

### 📂 Dataset Loading

```text
Enter your choice: 1
Enter the path of the dataset (CSV file): sales.csv
Dataset loaded successfully!
```

### 🔍 Data Exploration

```text
1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic info

Enter your choice: 1

  Product  Sales  Profit
0       A    100      20
1       B    200      40
2       C    300      60
3       D    400      80
4       E    500     100
```

### 🧹 Missing Data Menu

```text
=======hendal mising data=======
1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with a specific value

Enter your choice:
```

### 🎨 Visualization Menu

```text
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Seaborn Heatmap
8. Seaborn Box Plot

Enter your choice:
```

### 🚪 Exit

```text
Enter your choice: 8
Exiting the program. Goodbye!
```

## 📁 Project Structure

A suggested folder structure is:

```text
data-analysis-visualization/
│
├── sales_data_analyzer.py
├── README.md
├── requirements.txt
│
└── data/
    └── sales.csv
```

### 📄 requirements.txt

Create a file named `requirements.txt` containing:

```text
pandas
numpy
matplotlib
seaborn
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## ⚠️ Important Notes and Limitations

- The application is a command-line program, not a graphical user interface.
- The program reads CSV files; it does not currently load Excel files.
- Load a dataset before using the data exploration, DataFrame, cleaning, statistics, or visualization menus.
- Column names must match the names in the loaded dataset.
- Some visualization choices require numeric columns.
- Search uses partial, case-insensitive text matching.
- Filter uses exact matching after converting the selected column to text.
- The DataFrame combine option displays a concatenated result but does not replace the current DataFrame.
- The split options display separate sections; they do not save separate files.
- The pivot table uses sum aggregation.
- The program does not currently export a cleaned or modified DataFrame to a new CSV file.
- The save-visualization option saves the current Matplotlib figure.
- The sample outputs in this README are illustrative; your actual results depend on your CSV data.

## 🔮 Possible Future Improvements

The following are possible extensions and are not currently included in the supplied source code:

- ✅ Add an option to export cleaned data to CSV.
- ✅ Add stronger validation for user input and column names.
- ✅ Add support for Excel files.
- ✅ Add more chart customization options.
- ✅ Add a graphical user interface.
- ✅ Add automated tests.
- ✅ Add logging for errors and program activity.

## 👨‍💻 Author

**Project Name:** Data Analysis & Visualization Program  
**Programming Language:** Python  
**Project Type:** CSV Data Analysis and Visualization  
**Interface:** Command Line
**author name:** sneha padsala

_Add your name, institution, course, or contact details here if required._

## 📜 License

No license information was included in the supplied source code. If you plan to publish or distribute this project, choose an appropriate license and add its terms to the repository.

---

⭐ **Thank you for checking out the Data Analysis & Visualization Program!**
