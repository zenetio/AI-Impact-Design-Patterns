import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')

# Draw strategy boxes
cb_box = Rectangle((0.1, 0.4), 0.3, 0.2, edgecolor='black', facecolor='lightblue')
cf_box = Rectangle((0.6, 0.4), 0.3, 0.2, edgecolor='black', facecolor='lightgreen')
for box in (cb_box, cf_box):
    ax.add_patch(box)

# Labels
ax.text(0.25, 0.5, 'ContentBased\n(recommend)', ha='center', va='center', fontsize=11)
ax.text(0.75, 0.5, 'CollaborativeFiltering\n(recommend)', ha='center', va='center', fontsize=11)

# Input arrow: client → strategies
ax.annotate('user_data', xy=(0.1, 0.45), xytext=(0.0, 0.45),
            arrowprops=dict(arrowstyle='->'), ha='center', va='center')

# Output arrows: strategies → client
ax.annotate('', xy=(1.0, 0.45), xytext=(0.4, 0.45),
            arrowprops=dict(arrowstyle='->'))
ax.text(0.7, 0.42, 'recommend()', ha='center', va='top', fontsize=9)

# Save diagram
plt.savefig('images/ai_strategy_diagram.jpg', bbox_inches='tight')
plt.close()
