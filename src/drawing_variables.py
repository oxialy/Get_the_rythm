from src import settings as sett

from .settings import WIDTH, HEIGHT

import pygame


def get_gradient(colA, colB, n=14):
    r1, g1, b1 = colA
    r2, g2, b2 = colB

    k_r = (r2 - r1) / n
    k_g = (g2 - g1) / n
    k_b = (b2 - b1) / n

    gradient = []

    for i in range(n):
        r = int(r1 + i * k_r)
        g = int(g1 + i * k_g)
        b = int(b1 + i * k_b)

        gradient.append((r, g, b))

    return gradient


colors = {
    'blue1': '#102080',
    'blue2': '#2040A3',
    'lightblue1': '#3858AA',
    'cyan1': '#207080',
    'seagreen1': '#106040',
    'green1': '#107720',
    'green2': '#22A038',
    'orange1': '#802060',
    'orange2': '#AA9227',
    'yellow1': '#A0bb10',
    'yellow2': '#AACC30',
    'lightgrey1': '#aaaaaa',
    'darkgrey1': '#404040',
    'grey1': '#707070',
    'grey2': '#999999',
    'red1': '#A01010',
    'purple1': '#600870',
    'purple2': '#901080',
    'black1': '#000000'
}

colB = {
    'lightblue1': "#5264AA",
    'blue2': "#4050A3",
    'green2': "#50A050",
    'green1': "#5151A3",
    'orange2': "#AA9266",
    'yellow1': "#AACC67",
    'red1': "#A03939",
    'purple1': "#904080",
    'black1': '#242424'
}

col1 = 35, 10, 40
col2 = 16, 22, 47

gradient = get_gradient(col1, col2, 25)

col3 = 120, 10, 10
col4 = 10, 120, 10
g2 = get_gradient(col4, col3, 12)

bg_color = '#105070'
bg_color_2 = '#A3B8CC'
#bg_color = bg_color_2

BACKGROUND_POS = (0, 0)
BACKGROUND = pygame.Surface((WIDTH - 2 * BACKGROUND_POS[0], HEIGHT - 2 * BACKGROUND_POS[1]))
BACKGROUND.fill(bg_color_2)









