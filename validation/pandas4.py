import pandas as pd
import pandas.testing as pdt

# Read the dataset
df = pd.read_csv("Books.csv")

# Compute actual values
null_count = df['ISBN'].isnull().sum()
row_count = len(df)
percentage_null = null_count / row_count * 100
non_null_count = df['ISBN'].notnull().sum()

# Create actual result as DataFrame
actual_result = pd.DataFrame({
    'Metric': ['Null Count', 'Row Count', 'Percentage Null', 'Non-Null Count'],
    'Value': [null_count, row_count, round(percentage_null, 10), non_null_count]
})

# Manually inserted expected values
manual_data = {
    'Metric': ['Row Count', 'Null Count', 'Percentage Null', 'Non-Null Count'],
    'Value': [9, 604, 1.4900662252, 595]
}
expected_result = pd.DataFrame(manual_data)

print("Original Result:")
print(actual_result)

print("Expected Result:")
print(expected_result)

pdt.assert_frame_equal(actual_result, expected_result, check_exact=False, rtol=1e-9)

print("All values match – program correct.")
