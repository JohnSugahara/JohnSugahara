from PIL import Image, ImageDraw, ImageFont
import math

# ======================================
# Condigurações
# ======================================

WIDTH  = 170
HEIGHT = 90

CHAR_W = 8
CHAR_H = 12

IMG_W = WIDTH * CHAR_W
IMG_H = HEIGHT * CHAR_H

FRAMES = 360
DURATION = 16

SCALE = 248
DIST  = 7

# caracteres por profundidade
ASCII = " .:-=+*#%@"


# TESSERACT (HIPERCUBO 4D)

vertices = []

# gera 16 vértices
for i in range(16):

    x = -1 if (i & 1) else 1
    y = -1 if (i & 2) else 1
    z = -1 if (i & 4) else 1
    w = -1 if (i & 8) else 1

    vertices.append([x,y,z,w])

# arestas:
# dois vértices conectam se diferirem em 1 bit
edges = []

for i in range(16):
    for j in range(i+1,16):

        diff = 0

        for b in range(4):
            if ((i >> b) & 1) != ((j >> b) & 1):
                diff += 1

        if diff == 1:
            edges.append((i,j))


# ROTAÇÕES 4D


def rotate_4d(v, a):

    x,y,z,w = v

    # XW
    x,w = (
        x*math.cos(a)-w*math.sin(a),
        x*math.sin(a)+w*math.cos(a)
    )

    # YZ
    y,z = (
        y*math.cos(a*0.7)-z*math.sin(a*0.7),
        y*math.sin(a*0.7)+z*math.cos(a*0.7)
    )

    # ZW
    z,w = (
        z*math.cos(a*1.2)-w*math.sin(a*1.2),
        z*math.sin(a*1.2)+w*math.cos(a*1.2)
    )

    return (x,y,z,w)


# PROJEÇÃO 4D -> 3D

def project4d(v):

    x,y,z,w = v

    w_factor = 2 / (w + 3)

    x *= w_factor
    y *= w_factor
    z *= w_factor

    return (x,y,z)


# PROJEÇÃO 3D -> 2D


def project3d(v):

    x,y,z = v

    factor = SCALE / (z + DIST)

    px = int(x * factor + WIDTH/2)
    py = int(y * factor + HEIGHT/2)

    return (px,py,z)


# LINHA ASCII


def draw_line(buffer,zbuf,x1,y1,z1,x2,y2,z2,char):

    dx = abs(x2-x1)
    dy = abs(y2-y1)

    steps = max(dx,dy)

    if steps == 0:
        return

    for i in range(steps+1):

        t = i / steps

        x = int(x1 + (x2-x1)*t)
        y = int(y1 + (y2-y1)*t)
        z = z1 + (z2-z1)*t

        if 0 <= x < WIDTH and 0 <= y < HEIGHT:

            if z < zbuf[y][x]:

                zbuf[y][x] = z
                buffer[y][x] = char

# FONT


try:
    font = ImageFont.truetype("consola.ttf", 12)
except:
    font = ImageFont.load_default()

# GIF


frames = []

for f in range(FRAMES):

    t = (f / FRAMES) * math.pi * 2

    transformed = []

    for v in vertices:

        r4 = rotate_4d(v, t)
        r3 = project4d(r4)

        transformed.append(r3)

    projected = [
        project3d(v)
        for v in transformed
    ]

    buffer = [
        [" " for _ in range(WIDTH)]
        for _ in range(HEIGHT)
    ]

    zbuf = [
        [999999 for _ in range(WIDTH)]
        for _ in range(HEIGHT)
    ]


    # Desenha arestas


    for a,b in edges:

        x1,y1,z1 = projected[a]
        x2,y2,z2 = projected[b]

        avgz = (z1 + z2) / 2

        # profundidade -> ascii
        brightness = int(
            ((avgz + 2) / 4) * (len(ASCII)-1)
        )

        brightness = max(
            0,
            min(len(ASCII)-1, brightness)
        )

        char = ASCII[brightness]

        draw_line(
            buffer,
            zbuf,
            x1,y1,z1,
            x2,y2,z2,
            char
        )


    # Renderiza o buffer ASCII para uma imagem
  

    img = Image.new(
        "RGB",
        (IMG_W, IMG_H),
        "black"
    )

    draw = ImageDraw.Draw(img)

    for y in range(HEIGHT):

        line = "".join(buffer[y])

        draw.text(
            (0, y * CHAR_H),
            line,
            fill="white",
            font=font
        )

    frames.append(img)



frames[0].save(
    "ascii_tesseract.gif",
    save_all=True,
    append_images=frames[1:],
    duration=DURATION,
    loop=0,
    disposal=2
)

print("GIF salvo: ascii_tesseract.gif")