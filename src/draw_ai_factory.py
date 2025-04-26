from PIL import Image, ImageDraw, ImageFont

def create_factory_method_diagram(output_path="factory_method_ai.jpg"):
    """Creates a JPEG image of the Factory Method pattern with AI impact."""

    # Image dimensions and colors
    width, height = 800, 400
    bg_color = (255, 255, 255)  # White
    box_color = (200, 200, 200)  # Light gray
    text_color = (0, 0, 0)  # Black
    arrow_color = (0, 0, 0)  # Black

    # Create a blank image
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Font settings
    try:
        font = ImageFont.truetype("arial.ttf", 16)  # Use Arial font if available
    except IOError:
        font = ImageFont.load_default()

    # Box dimensions and positions
    box_width = 200
    box_height = 80
    box1_x, box1_y = 50, 50
    box2_x, box2_y = box1_x + box_width + 50, box1_y
    box3_x, box3_y = box2_x + box_width + 50, box1_y
    box4_x, box4_y = 100, box1_y + box_height + 100

    # Draw boxes
    draw.rectangle([box1_x, box1_y, box1_x + box_width, box1_y + box_height], outline=box_color, width=2)
    draw.rectangle([box2_x, box2_y, box2_x + box_width, box2_y + box_height], outline=box_color, width=2)
    draw.rectangle([box3_x, box3_y, box3_x + box_width, box3_y + box_height], outline=box_color, width=2)
    draw.rectangle([box4_x, box4_y, box4_x + box_width, box4_y + box_height], outline=box_color, width=2)

    # Draw text in boxes
    draw.text((box1_x + 10, box1_y + 10), "Traditional Factory\n(Fixed Pattern)", fill=text_color, font=font)
    draw.text((box2_x + 10, box2_y + 10), "Factory Method\n(Static Logic)", fill=text_color, font=font)
    draw.text((box3_x + 10, box3_y + 10), "Concrete Product\n(A/B)", fill=text_color, font=font)
    draw.text((box4_x + 10, box4_y + 10), "AI Engine\n(Decision Making,\nParameter Tuning)", fill=text_color, font=font)

    # Draw arrows
    arrow_start1 = (box1_x + box_width, box1_y + box_height / 2)
    arrow_end1 = (box2_x, box2_y + box_height / 2)
    draw.line([arrow_start1, arrow_end1], fill=arrow_color, width=2)
    draw.polygon([arrow_end1[0], arrow_end1[1], arrow_end1[0] - 10, arrow_end1[1] - 5, arrow_end1[0] - 10, arrow_end1[1] + 5], fill=arrow_color)

    arrow_start2 = (box2_x + box_width, box2_y + box_height / 2)
    arrow_end2 = (box3_x, box3_y + box_height / 2)
    draw.line([arrow_start2, arrow_end2], fill=arrow_color, width=2)
    draw.polygon([arrow_end2[0], arrow_end2[1], arrow_end2[0] - 10, arrow_end2[1] - 5, arrow_end2[0] - 10, arrow_end2[1] + 5], fill=arrow_color)

    arrow_start3 = (box4_x + box_width / 2, box4_y)
    arrow_end3 = (box1_x + box_width / 2, box1_y + box_height)
    draw.line([arrow_start3, arrow_end3], fill=arrow_color, width=2)
    draw.polygon([arrow_end3[0], arrow_end3[1], arrow_end3[0] - 5, arrow_end3[1] + 10, arrow_end3[0] + 5, arrow_end3[1] + 10], fill=arrow_color)

    # Draw text for AI Analysis
    draw.text((box4_x + box_width / 2 - 80, box4_y - 40), "AI Analysis & Adaptation", fill=text_color, font=font)

    # Save the image
    img.save(output_path)
    print(f"Image saved as {output_path}")

create_factory_method_diagram("./images/factory_method_ai.jpg")