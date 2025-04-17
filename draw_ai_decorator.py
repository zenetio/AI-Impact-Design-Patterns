import matplotlib.pyplot as plt

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the BaseClassifier
ax.add_patch(plt.Rectangle((1, 4), 2, 1, fill=True, edgecolor='black', facecolor='lightgray'))
ax.text(2, 4.5, 'BaseClassifier', fontsize=10, ha='center', va='center', fontweight='bold')
ax.text(2, 3.8, 'classify(data)', fontsize=9, ha='center', va='center')

# Draw the AIEnhancedClassifier (decorator)
ax.add_patch(plt.Rectangle((4, 4), 2, 1, fill=True, edgecolor='black', facecolor='lightblue'))
ax.text(5, 4.5, 'AIEnhancedClassifier', fontsize=10, ha='center', va='center', fontweight='bold')
ax.text(5, 3.8, 'classify(data)', fontsize=9, ha='center', va='center')

# Draw the AI Enhancement Layer
ax.add_patch(plt.Rectangle((4, 1.3), 2, 1.5, fill=True, edgecolor='black', facecolor='lightgreen'))
ax.text(5, 2.5, 'AI Enhancement Layer', fontsize=9, ha='center', va='center')
ax.text(5, 2.0, 'Features:\n- Predictive Analytics\n- Anomaly Detection\n- Pattern Recognition', fontsize=8, ha='center', va='center')

# Draw arrows showing data flow
# From client to AIEnhancedClassifier
ax.arrow(3.0, 3.0, 1.5, 1, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.text(2.5, 2.8, 'Client Request', fontsize=9, ha='center', va='center')

# From AIEnhancedClassifier to BaseClassifier
ax.arrow(4, 4.5, -1, 0, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.text(3, 4.7, 'Base Classification', fontsize=9, ha='center', va='center')

# From BaseClassifier to AIEnhancedClassifier
ax.arrow(2, 4, 2, 0, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.text(3, 3.7, 'Processed Data', fontsize=9, ha='center', va='center')

# From AIEnhancedClassifier to AI Enhancement Layer
ax.arrow(5, 4, 0, -1, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.text(5.2, 3.5, 'Enhancement', fontsize=9, ha='left', va='center')

# From AI Enhancement Layer to AIEnhancedClassifier
ax.arrow(5, 2.8, 0, 1, head_width=0.2, head_length=0.2, fc='black', ec='black')
ax.text(5.2, 2.7, 'Enhanced Output', fontsize=9, ha='left', va='center')

# Add explanation text
ax.text(5, 0.5, 'The AIEnhancedClassifier wraps the BaseClassifier\nwith additional AI capabilities while maintaining\nthe same interface. This allows for dynamic\nenhancement of existing functionality.', fontsize=9, ha='center', va='center')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Save the illustration
image_path = "./images/ai_decorator_diagram.jpg"
plt.savefig(image_path, dpi=300, bbox_inches='tight')
plt.show()