import matplotlib.pyplot as plt

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the Factory class (AIProductFactory)
ax.add_patch(plt.Rectangle((3, 5), 2, 1, fill=True, edgecolor='black', facecolor='lightblue'))
ax.text(4, 5.5, 'AIProductFactory', fontsize=10, ha='center', va='center', fontweight='bold')

# Draw the decision paths
ax.arrow(4, 5, -1.5, -1, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.arrow(4, 5, 0, -1, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.arrow(4, 5, 1.5, -1, head_width=0.2, head_length=0.2, fc='black', ec='black')

# Draw product outputs
ax.add_patch(plt.Rectangle((1, 3), 2, 1, fill=True, edgecolor='black', facecolor='lightgreen'))
ax.text(2, 3.5, 'Product A\n(Simple Item)', fontsize=9, ha='center', va='center')

ax.add_patch(plt.Rectangle((3, 3), 2, 1, fill=True, edgecolor='black', facecolor='lightcoral'))
ax.text(4, 3.5, 'Product B\n(Blue)', fontsize=9, ha='center', va='center')

ax.add_patch(plt.Rectangle((5, 3), 2, 1, fill=True, edgecolor='black', facecolor='lightyellow'))
ax.text(6, 3.5, 'Product A\n(Complex Item)', fontsize=9, ha='center', va='center')

# Add labels for decision conditions
ax.text(2.5, 4.2, 'complexity = "easy"', fontsize=9, ha='center', va='center')
ax.text(4, 4.4, 'complexity = "medium"', fontsize=9, ha='center', va='center')
ax.text(5.5, 4.2, 'complexity = "hard"', fontsize=9, ha='center', va='center')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 8)
ax.set_ylim(2, 7)
ax.axis('off')

# Save the illustration
image_path = "./images/ai_factory_diagram4.jpg"
plt.savefig(image_path, dpi=300, bbox_inches='tight')
plt.show()

# Provide the path for download
image_path
