import pandas as pd
import pandas.testing as pdt

# Read the dataset
df = pd.read_csv("Books.csv")

# Group by language and count books
actual_result = df.groupby('language').size().reset_index(name='Language Distribution')

# Sort for consistent comparison
actual_sorted = actual_result.sort_values(by='language').reset_index(drop=True)

# Manually inserted values
manual_data = {
    'language': ['Chinese', 'English', 'French', 'German', 'Italian', 'Japanese'], 
    'Language Distribution': [93, 153, 129, 150, 56, 23]
}
expected_result = pd.DataFrame(manual_data)

expected_sorted = expected_result.sort_values(by='language').reset_index(drop=True)

print("Original Result:")
print(actual_sorted)

print("Expected Result:")
print(expected_sorted)

pdt.assert_frame_equal(actual_sorted, expected_sorted)

print("Both datasets match – program is correct!.")


