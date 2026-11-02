
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = pd.DataFrame()

    def __del__(self):
        pass

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print("Error loading dataset:", e)

    def explore_data(self):
        if self.data.empty:
            print("Please load dataset first!")
            return

        print("\n1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(self.data.head())
        elif choice == "2":
            print(self.data.tail())
        elif choice == "3":
            print(self.data.columns.tolist())
        elif choice == "4":
            print(self.data.dtypes)
        elif choice == "5":
            self.data.info()

    def dataframe_operations(self):
        if self.data.empty:
            print("Please load dataset first!")
            return

        print("\n1. Display data")
        print("2. Search data")
        print("3. Sort data")
        print("4. Filter data")
        print("5. Combine DataFrames")
        print("6. Split DataFrame")
        print("7. NumPy array operations")
        print("8. Aggregate functions")
        print("9. Create pivot table")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(self.data)

        elif choice == "2":
            column = input("Enter column name: ")
            value = input("Enter search value: ")
            if column in self.data.columns:
                print(self.data[
                    self.data[column].astype(str).str.contains(
                        value, case=False, na=False
                    )
                ])
            else:
                print("Column not found!")

        elif choice == "3":
            column = input("Enter column name to sort: ")
            if column in self.data.columns:
                print(self.data.sort_values(column))
            else:
                print("Column not found!")

        elif choice == "4":
            column = input("Enter column name: ")
            value = input("Enter value to filter: ")
            if column in self.data.columns:
                print(self.data[
                    self.data[column].astype(str) == value
                ])
            else:
                print("Column not found!")

        elif choice == "5":
            path = input("Enter another CSV file path: ")
            try:
                df2 = pd.read_csv(path)
                print(pd.concat([self.data, df2], ignore_index=True))
            except Exception as e:
                print("Error:", e)

        elif choice == "6":
            print("1. Split by rows")
            print("2. Split by column")
            option = input("Enter your choice: ")

            if option == "1":
                parts = np.array_split(self.data, 2)
                print("First part:\n", parts[0])
                print("Second part:\n", parts[1])
            elif option == "2":
                print("First half of columns:")
                print(self.data.iloc[:, :len(self.data.columns)//2])
                print("Second half of columns:")
                print(self.data.iloc[:, len(self.data.columns)//2:])

        elif choice == "7":
            numeric = self.data.select_dtypes(include="number")
            arr = numeric.to_numpy()

            print("NumPy Array:\n", arr)
            print("Array Shape:", arr.shape)

            if arr.size > 0:
                print("Addition:\n", arr + 10)
                print("Multiplication:\n", arr * 2)
                print("Column Mean:\n", np.mean(arr, axis=0))

        elif choice == "8":
            numeric = self.data.select_dtypes(include="number")
            print("Sum:\n", numeric.sum())
            print("Mean:\n", numeric.mean())
            print("Count:\n", numeric.count())

        elif choice == "9":
            print("Available columns:", self.data.columns.tolist())
            index_col = input("Enter index column: ")
            value_col = input("Enter numeric value column: ")

            if index_col in self.data.columns and value_col in self.data.columns:
                try:
                    print(pd.pivot_table(
                        self.data,
                        index=index_col,
                        values=value_col,
                        aggfunc="sum"
                    ))
                except Exception as e:
                    print("Error:", e)
            else:
                print("Column not found!")

    def clean_data(self):
        if self.data.empty:
            print("Please load dataset first!")
            return
        print("=======hendal mising data=======")
        print("\n1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(self.data[self.data.isnull().any(axis=1)])

        elif choice == "2":
            numeric = self.data.select_dtypes(include="number")
            self.data[numeric.columns] = numeric.fillna(numeric.mean())
            print("Missing values filled with mean!")

        elif choice == "3":
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped!")

        elif choice == "4":
            value = input("Enter replacement value: ")
            self.data = self.data.fillna(value)
            print("Missing values replaced!")

    def statistical_analysis(self):
        if self.data.empty:
            print("Please load dataset first!")
            return

        numeric = self.data.select_dtypes(include="number")

        print("\nDescriptive Statistics:")
        print(numeric.describe())

        print("\nSum:\n", numeric.sum())
        print("\nMean:\n", numeric.mean())
        print("\nMedian:\n", numeric.median())
        print("\nStandard Deviation:\n", numeric.std())
        print("\nVariance:\n", numeric.var())
        print("\nPercentiles:\n", numeric.quantile([0.25, 0.50, 0.75]))

    def visualize_data(self):
        if self.data.empty:
            print("Please load dataset first!")
            return

        print("\n1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Seaborn Heatmap")
        print("8. Seaborn Box Plot")

        choice = input("Enter your choice: ")
        numeric = self.data.select_dtypes(include="number")

        if choice == "1":
            column = input("Enter column name: ")
            if column in self.data.columns:
                self.data[column].value_counts().plot(kind="bar")
                plt.title("Bar Plot")

        elif choice == "2":
            column = input("Enter column name: ")
            if column in numeric.columns:
                numeric[column].plot(kind="line")
                plt.title("Line Plot")

        elif choice == "3":
            x = input("Enter x-axis column name: ")
            y = input("Enter y-axis column name: ")
            if x in numeric.columns and y in numeric.columns:
                plt.scatter(self.data[x], self.data[y])
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Scatter Plot")

        elif choice == "4":
            column = input("Enter column name: ")
            if column in self.data.columns:
                self.data[column].value_counts().plot(
                    kind="pie", autopct="%1.1f%%"
                )
                plt.title("Pie Chart")

        elif choice == "5":
            column = input("Enter numeric column name: ")
            if column in numeric.columns:
                plt.hist(self.data[column].dropna(), bins=10)
                plt.title("Histogram")

        elif choice == "6":
            columns = input("Enter numeric columns separated by comma: ")
            columns = [c.strip() for c in columns.split(",")]

            if all(c in numeric.columns for c in columns) and columns:
                plt.stackplot(
                    range(len(self.data)),
                    *[self.data[c].fillna(0).to_numpy() for c in columns],
                    labels=columns
                )
                plt.legend()
                plt.title("Stack Plot")

        elif choice == "7":
            if not numeric.empty:
                sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm")
                plt.title("Correlation Heatmap")

        elif choice == "8":
            column = input("Enter numeric column name: ")
            if column in numeric.columns:
                sns.boxplot(x=self.data[column])
                plt.title("Box Plot")

        else:
            print("Invalid choice!")
            return

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            plt.tight_layout()
            plt.show()
            print("Visualization displayed successfully!")

    def save_visualization(self):
        filename = input("Enter file name to save the plot (e.g., plot.png): ")

        try:
            plt.savefig(filename)
            print("Visualization saved as", filename, "successfully!")
        except Exception as e:
            print("Error saving visualization:", e)


def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 55)

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(path)

        elif choice == "2":
            analyzer.explore_data()

        elif choice == "3":
            analyzer.dataframe_operations()

        elif choice == "4":
            analyzer.clean_data()

        elif choice == "5":
            analyzer.statistical_analysis()

        elif choice == "6":
            analyzer.visualize_data()

        elif choice == "7":
            analyzer.save_visualization()

        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
