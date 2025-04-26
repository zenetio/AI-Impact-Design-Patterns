import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Setup canvas
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')

# Draw component boxes
builder_box = Rectangle((0.1, 0.4), 0.2, 0.2, edgecolor='black', facecolor='lightblue')
model_box   = Rectangle((0.7, 0.4), 0.2, 0.2, edgecolor='black', facecolor='lightgreen')
for box in (builder_box, model_box):
    ax.add_patch(box)

# Add labels
ax.text(0.2, 0.5, 'AIModelBuilder', ha='center', va='center', fontsize=12)
ax.text(0.8, 0.5, 'Model\n(built)',      ha='center', va='center', fontsize=12)

# Draw arrows & annotate methods
# Input arrow: client → builder
ax.annotate('Config Params', xy=(0.1, 0.5), xytext=(0.0, 0.5),
            arrowprops=dict(arrowstyle='->'), ha='center', va='center')

# Builder method calls on itself
ax.annotate('', xy=(0.2, 0.6), xytext=(0.2, 0.7), arrowprops=dict(arrowstyle='->'))
ax.text(0.25, 0.65, 'set_layers()', ha='left', va='center', fontsize=9)
ax.annotate('', xy=(0.2, 0.4), xytext=(0.2, 0.3), arrowprops=dict(arrowstyle='->'))
ax.text(0.25, 0.35, 'set_optimizer()', ha='left', va='center', fontsize=9)

# Build arrow: builder → model
ax.annotate('', xy=(0.7, 0.5), xytext=(0.3, 0.5), arrowprops=dict(arrowstyle='->'))
ax.text(0.5, 0.52, 'build()', ha='center', va='bottom', fontsize=9)

# Output arrow: model → client
ax.annotate('', xy=(1.0, 0.5), xytext=(0.9, 0.5), arrowprops=dict(arrowstyle='->'))
ax.text(0.95, 0.52, 'Model', ha='center', va='bottom', fontsize=9)

# Save diagrams
plt.savefig('images/ai_builder_diagram.jpg', bbox_inches='tight')
plt.close()
