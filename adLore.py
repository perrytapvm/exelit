continuous_axis = 'x_axis'
old_continuous_axis_channel_def = {'scale': 'linear', 'range': [0, 100]}

new_object = {continuous_axis: old_continuous_axis_channel_def}
# Or using the dict constructor
new_object = dict([(continuous_axis, old_continuous_axis_channel_def)])

print(new_object)
# Output: {'x_axis': {'scale': 'linear', 'range': [0, 100]}}
