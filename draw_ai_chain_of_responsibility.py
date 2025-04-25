import matplotlib.pyplot as plt

# draw_ai_chain_of_responsibility.py
# Generate a simple Chain of Responsibility pattern diagram
fig, ax = plt.subplots(figsize=(8, 3))

# Draw handler nodes
ax.text(0.1, 0.5, 'Handler A', ha='center', va='center', fontsize=10,
        bbox=dict(boxstyle='round', fc='lightblue'))
ax.text(0.5, 0.5, 'Handler B', ha='center', va='center', fontsize=10,
        bbox=dict(boxstyle='round', fc='lightgreen'))
ax.text(0.9, 0.5, 'Handler C', ha='center', va='center', fontsize=10,
        bbox=dict(boxstyle='round', fc='lightcoral'))

# Traditional chain arrows: A -> B -> C
ax.annotate('', xy=(0.45, 0.5), xytext=(0.15, 0.5), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(0.85, 0.5), xytext=(0.55, 0.5), arrowprops=dict(arrowstyle='->'))

# Draw AI selector above handlers
ax.text(0.5, 0.8, 'AI Selector', ha='center', va='center', fontsize=10,
        bbox=dict(boxstyle='round', fc='orange'))
# Dashed arrows from AI selector to each handler
for x in [0.1, 0.5, 0.9]:
    ax.annotate('', xy=(x, 0.6), xytext=(0.5, 0.75),
                arrowprops=dict(arrowstyle='->', linestyle='--', color='gray'))

ax.axis('off')
plt.tight_layout()
plt.savefig('images/ai_chain_of_responsibility.jpg')
print('AI Chain of Responsibility diagram saved to images/ai_chain_of_responsibility.jpg')
