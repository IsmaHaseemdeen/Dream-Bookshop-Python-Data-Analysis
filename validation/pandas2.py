import pandas as pd
import pandas.testing as pdt

# Read the dataset
df = pd.read_csv("Books.csv")

# Get actual result from data
actual_result = df['author'].value_counts().head(5).reset_index()
actual_result.columns = ['Author', 'BookCount']

# Sort actual result by Author for comparison consistency
actual_sorted = actual_result.sort_values(by='Author').reset_index(drop=True)

# Manually inserted values
manual_data = {
    'Author': ['Zuri Day', 'Valerie Jackson', 'Jeffrey Haynes', 'Jenni Fagan', 'Matt Jones'],
    'BookCount': [26, 22, 12, 12, 10]
}
expected_result = pd.DataFrame(manual_data)

expected_sorted = expected_result.sort_values(by='Author').reset_index(drop=True)

print("Original Result:")
print(actual_sorted)

print("Expected Result:")
print(expected_sorted)

pdt.assert_frame_equal(actual_sorted, expected_sorted)

print("Both datasets match – program is correct!.")
