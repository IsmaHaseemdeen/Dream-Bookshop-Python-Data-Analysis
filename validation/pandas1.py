import pandas as pd
import pandas.testing as pdt

# Read the dataset
df = pd.read_csv("Books.csv")

# Group by publication year and count books
actual_result = df.groupby('publication date').size().reset_index(name='Count of Books')

# Sort by year for comparison consistency
actual_sorted = actual_result.sort_values(by='publication date').reset_index(drop=True)

# Manually inserted values
manual_data = {
    'publication date': [
        2010, 2012, 2013, 2015, 2014, 2016, 2017,
        2018, 2019, 2020, 2021, 2022, 2024
    ],
    'Count of Books': [
        8, 61, 8, 51, 32, 17, 28,
        47, 24, 58, 128, 65, 77
    ]
}
expected_result = pd.DataFrame(manual_data)

expected_sorted = expected_result.sort_values(by='publication date').reset_index(drop=True)

print("Original Result:")
print(actual_sorted)

print("Expected Result:")
print(expected_sorted)

pdt.assert_frame_equal(actual_sorted, expected_sorted)

print("Both datasets match– program is correct!.")
