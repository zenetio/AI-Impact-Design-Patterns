import matplotlib.pyplot as plt

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the Singleton class (AIModelSingleton)
ax.add_patch(plt.Rectangle((3, 5), 2, 1, fill=True, edgecolor='black', facecolor='lightblue'))
ax.text(4, 5.5, 'AIModelSingleton', fontsize=10, ha='center', va='center', fontweight='bold')

# Draw the private instance variable
ax.add_patch(plt.Rectangle((3, 4), 2, 0.5, fill=True, edgecolor='black', facecolor='lightgray'))
ax.text(4, 4.25, '_instance = None', fontsize=9, ha='center', va='center')

# Draw the __new__ method
ax.add_patch(plt.Rectangle((3, 3), 2, 0.5, fill=True, edgecolor='black', facecolor='lightgreen'))
ax.text(4, 3.25, '__new__(cls, model_name)', fontsize=9, ha='center', va='center')

# Draw the client code
ax.add_patch(plt.Rectangle((1, 2), 2, 0.5, fill=True, edgecolor='black', facecolor='lightcoral'))
ax.text(2, 2.3, 'model1 = AIModelSingleton("GPT-4")', fontsize=9, ha='center', va='center')

ax.add_patch(plt.Rectangle((5, 2), 2, 0.5, fill=True, edgecolor='black', facecolor='lightcoral'))
ax.text(6, 2.3, 'model2 = AIModelSingleton("GPT-4")', fontsize=9, ha='center', va='center')

# Draw arrows showing the singleton behavior
ax.arrow(2, 2.5, 1, 0.5, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.arrow(6, 2.5, -1, 0.5, head_width=0.2, head_length=0.2, fc='black', ec='black')

# Add explanation text
ax.text(4, 1.5, 'Both model1 and model2 reference\nthe same instance', fontsize=9, ha='center', va='center')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 8)
ax.set_ylim(1, 6)
ax.axis('off')

# Save the illustration
image_path = "./images/ai_singleton_diagram.jpg"
plt.savefig(image_path, dpi=300, bbox_inches='tight')
plt.show()

# Provide the path for download
image_path