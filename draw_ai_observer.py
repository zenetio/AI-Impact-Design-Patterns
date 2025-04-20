import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Setup canvas
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')

# Draw component boxes
system_box   = Rectangle((0.1, 0.4), 0.2, 0.2, edgecolor='black', facecolor='lightblue')
analyzer_box = Rectangle((0.4, 0.4), 0.2, 0.2, edgecolor='black', facecolor='lightgreen')
alert_box    = Rectangle((0.7, 0.4), 0.2, 0.2, edgecolor='black', facecolor='lightcoral')
for box in (system_box, analyzer_box, alert_box):
    ax.add_patch(box)

# Add labels
ax.text(0.2, 0.5, 'SecuritySystem', ha='center', va='center', fontsize=12)
ax.text(0.5, 0.5, 'AIThreatAnalyzer\n(is_real_threat)', ha='center', va='center', fontsize=10)
ax.text(0.8, 0.5, 'SecurityAlert\n(update)', ha='center', va='center', fontsize=12)

# Draw arrows and annotate methods
# Arrow from SecuritySystem → AIThreatAnalyzer: checks if event is a real threat
ax.annotate('', xy=(0.4, 0.5), xytext=(0.3, 0.5), arrowprops=dict(arrowstyle='->'))
ax.text(0.35, 0.53, 'is_real_threat()', ha='center', va='bottom', fontsize=9)

# Arrow from SecuritySystem → SecurityAlert: notifies observers when threat is confirmed
ax.annotate('', xy=(0.7, 0.48), xytext=(0.3, 0.48), arrowprops=dict(arrowstyle='->'))
ax.text(0.5, 0.45, 'notify_observers()', ha='center', va='top', fontsize=9)

# Input/output flows
# Input arrow: external event data enters SecuritySystem
ax.annotate('Event Data', xy=(0.1, 0.5), xytext=(0.0, 0.5),
            arrowprops=dict(arrowstyle='->'), ha='center', va='center')
# Output arrow: SecurityAlert emits an Alert to the client
ax.annotate('', xy=(1.0, 0.5), xytext=(0.9, 0.5),
            arrowprops=dict(arrowstyle='->'))
ax.text(0.95, 0.52, 'Alert', ha='center', va='bottom', fontsize=9)

# Save diagrams
plt.savefig('images/ai_observer_diagram.jpg', bbox_inches='tight')
plt.close()
