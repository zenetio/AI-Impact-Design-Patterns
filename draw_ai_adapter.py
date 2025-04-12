import matplotlib.pyplot as plt

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the OldPredictionSystem (Legacy System)
ax.add_patch(plt.Rectangle((1, 4), 2, 1, fill=True, edgecolor='black', facecolor='lightgray'))
ax.text(2, 4.5, 'OldPredictionSystem', fontsize=10, ha='center', va='center', fontweight='bold')
ax.text(2, 3.8, 'classify(input_data)', fontsize=9, ha='center', va='center')

# Draw the AIAdapter (Bridge)
ax.add_patch(plt.Rectangle((4, 4), 2, 1, fill=True, edgecolor='black', facecolor='lightblue'))
ax.text(5, 4.5, 'AIAdapter', fontsize=10, ha='center', va='center', fontweight='bold')
ax.text(5.2, 3.8, 'predict(data)', fontsize=9, ha='center', va='center')

# Draw the AI Model (Modern System)
ax.add_patch(plt.Rectangle((7, 4), 2, 1, fill=True, edgecolor='black', facecolor='lightgreen'))
ax.text(8, 4.5, 'AI Model', fontsize=10, ha='center', va='center', fontweight='bold')
ax.text(8, 3.8, 'predict(data)', fontsize=9, ha='center', va='center')

# Draw arrows showing data flow
# From OldPredictionSystem to adapter
ax.arrow(3.0, 4.1, 0.8, 0, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.text(3.4, 4.3, 'Legacy Output', fontsize=9, ha='center', va='center')

# From AI Model to adapter
ax.arrow(7.0, 4.1, -0.8, 0, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.text(6.4, 4.3, 'AI Model Output', fontsize=9, ha='center', va='center')

# From client to adapter
ax.arrow(2.5, 3.5, 1.6, 0.45, head_width=0.2, head_length=0.2, fc='black', ec='black')  # Added arrow
ax.text(3.5, 3.5, 'Client Request', fontsize=9, ha='center', va='center')

# From adapter to old system
ax.arrow(4.5, 4, 0, -0.8, head_width=0.2, head_length=0.2, fc='black', ec='black')

# Draw the adapter's internal structure
ax.add_patch(plt.Rectangle((4, 2), 2, 1, fill=True, edgecolor='black', facecolor='lightyellow'))
ax.text(5, 2.5, 'Data Pre-processing\nFormat Conversion\nLegacy Compatibility', fontsize=9, ha='center', va='center')

# Add explanation text
ax.text(5, 1.5, 'The AIAdapter acts as a bridge between\nlegacy systems and modern AI models,\nhandling data conversion and maintaining\ncompatibility with existing systems.', fontsize=9, ha='center', va='center')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Save the illustration
image_path = "./images/ai_adapter_diagram.jpg"
plt.savefig(image_path, dpi=300, bbox_inches='tight')
plt.show()

# Provide the path for download
image_path