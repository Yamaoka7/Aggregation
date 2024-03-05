# Perform aggregation on dataset
def aggregate_data(dataset, group_by_column, aggregation_function):
    return dataset.groupby(group_by_column).agg(aggregation_function)

# Example usage:
aggregated_data = aggregate_data(dataset, 'group_column', {'column': 'mean'})
print(aggregated_data.head())
