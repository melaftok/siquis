# Example dictionary representing configuration or data mappings
data_mappings = {
    "pulse": "dataRef",
    # Add more key-value pairs if needed
}

# Accessing the value associated with the key 'pulse'
pulse_data_ref = data_mappings.get("pulse")

# Printing the value
print(pulse_data_ref)  # Output: dataRef
