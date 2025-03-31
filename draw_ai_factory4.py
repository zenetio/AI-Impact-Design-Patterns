from PIL import Image, ImageDraw

def draw_ai_enhanced_factory_diagram(output_path="images/ai_factory_diagram4.jpg"):
    """
    Generates a diagram illustrating the AI-Enhanced Factory Pattern 
    as described in ai_factory2.py using PIL.

    Args:
        output_path (str): The path to save the generated JPG image.
    """

    img_width = 800
    img_height = 400
    image = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(image)

    # Define positions and sizes for the boxes
    box_width = 150
    box_height = 80
    vertical_spacing = 120
    horizontal_spacing = 250

    # Traditional Factory Box
    x1, y1 = 50, 50
    draw.rectangle((x1, y1, x1 + box_width, y1 + box_height), fill="lightgray", outline="black")
    draw.text((x1 + 10, y1 + 20), "Traditional Factory\n(Fixed Pattern)", fill="black")

    # Factory Method Box
    x2, y2 = x1 + horizontal_spacing, y1
    draw.rectangle((x2, y2, x2 + box_width, y2 + box_height), fill="lightgray", outline="black")
    draw.text((x2 + 10, y2 + 20), "Factory Method\n(Static Logic)", fill="black")

    # Concrete Product Box
    x3, y3 = x2 + horizontal_spacing, y1
    draw.rectangle((x3, y3, x3 + box_width, y3 + box_height), fill="lightgray", outline="black")
    draw.text((x3 + 10, y3 + 20), "Concrete Product\n(A/B)", fill="black")

    # AI Engine Box
    x4, y4 = x1, y1 + vertical_spacing
    draw.rectangle((x4, y4, x4 + box_width, y4 + box_height), fill="lightgray", outline="black")
    draw.text((x4 + 10, y4 + 20), "AI Engine\n(Decision Making,\nParameter Tuning)", fill="black")

    # Arrows
    arrow_head_length = 30
    arrow_cap_width = 10

    # Arrow from Traditional Factory to Factory Method
    draw.polygon([(x1 + box_width // 2, y1 + box_height), (x2, y2)], fill="black", outline="black")

    # Arrow from Factory Method to Concrete Product
    draw.polygon([(x2 + box_width // 2, y2 + box_height), (x3, y3)], fill="black", outline="black")

    # Arrow from AI Engine to all boxes
    draw.polygon([(x4 + box_width//2, y4+box_height), (x1,y1)], fill="black", outline="black")


    image.save(output_path)
    print(f"Diagram saved to {output_path}")

if __name__ == '__main__':
    draw_ai_enhanced_factory_diagram()
