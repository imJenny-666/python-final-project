from graphics import Canvas 

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PATCH_SIZE = 40
NUM_COL = CANVAS_WIDTH // PATCH_SIZE
NUM_ROW = CANVAS_HEIGHT // PATCH_SIZE

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    while True:
        background = input("What house does Harry Potter belong? (a)Gryffindor (b)Slytherin (c)Ravenclaw (d)Hufflepuff: ").lower()

        if background == 'a':
            print("Excellent! 10 points to Gryffindor!")
            # 酒紅色背景（Gryffindor）
            canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color='#800000')

            for row in range(NUM_ROW):
                for col in range(NUM_COL):
                    x = col * PATCH_SIZE
                    y = row * PATCH_SIZE
                    if (row + col) % 2 == 0:
                        draw_lightning_patch(canvas, x, y, PATCH_SIZE)
                    else:
                        draw_glasses_patch(canvas, x, y, PATCH_SIZE)
            break
        else:
            print("Wrong answer! Avada Kedavra...kidding! try again. I know you can do it. ")
            canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color='#D2B48C')
            canvas.create_text(10, 10, text = 'Exam Result:',font = 'Verdana Italic', font_size = 40, color ='#444444')
            canvas.create_text(10, CANVAS_HEIGHT*1/7, text = 'Outstanding',font = 'Verdana Italic ', font_size = 30, color ='#F5F5F5')            
            canvas.create_text(10, CANVAS_HEIGHT*2/7, text = 'Exceeds Expectations',font = 'Verdana Italic', font_size = 30, color ='#F5F5F5')
            canvas.create_text(10, CANVAS_HEIGHT*3/7, text = 'Acceptable',font = 'Verdana Italic', font_size = 30, color ='#F5F5F5')
            canvas.create_text(10, CANVAS_HEIGHT*4/7, text = 'Poor',font = 'Verdana Italic', font_size = 30, color ='#F5F5F5')
            canvas.create_text(10, CANVAS_HEIGHT*5/7, text = 'Dreadful',font = 'Verdana Italic', font_size = 30, color ='#F5F5F5')
            canvas.create_text(10, CANVAS_HEIGHT*6/7, text = 'Troll',font = 'Verdana Italic ', font_size = 30, color ='#444444')

        canvas.mainloop()

def draw_lightning_patch(canvas, x, y, size):
    relative_points = [
        (0.6, 0.1), (0.7, 0.6),
        (0.4, 0.5), (0.4, 0.99),
        (0.3, 0.4), (0.58, 0.48)
    ]

    coords = []
    for rx, ry in relative_points:
        px = x + rx * size
        py = y + ry * size
        coords.extend([px, py])

    canvas.create_polygon(*coords, color='gold', outline='black')

def draw_glasses_patch(canvas, x, y, size):
    radius = size * 0.15
    spacing = size * 0.1
    center_y = y + size / 2
    left_center_x = x + size * 0.3
    right_center_x = x + size * 0.7

    # 左眼
    canvas.create_oval(
        left_center_x - radius, center_y - radius,
        left_center_x + radius, center_y + radius,
        color='#F5F5F5', outline='black'
    )

    # 右眼
    canvas.create_oval(
        right_center_x - radius, center_y - radius,
        right_center_x + radius, center_y + radius,
        color='#F5F5F5', outline='black'
    )

    # 鼻樑          
    canvas.create_line(
        left_center_x + radius, center_y,
        right_center_x - radius, center_y,
        color='black'
    )

if __name__ == '__main__':
    main()