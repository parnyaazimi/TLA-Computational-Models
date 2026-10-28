# -*- coding: utf-8 -*-
"""
Watch the glider-collision logic gates (AND / NOT) live in pygame.

Unlike a plain run_pygame_life() call, this script also:
  - draws a highlighted rectangle around the output window, so you can see
    exactly where the collision/result is being checked
  - shows the current generation number and the final True/False result
  - runs slowly by default so the collision is easy to follow

Just edit GATE / INPUT_A / INPUT_B below and run:  python watch_logic_gates.py
"""
import pygame
import numpy as np

from logic_gates import GliderLogicGates

CELL_SCALE = 16
FPS = 10
EXTRA_FRAMES_AFTER = 40   # keep watching a bit after the "official" step count

# ---- Choose what to visualize ----
GATE = "NOT"        # "AND" or "NOT"
INPUT_A = False
INPUT_B = True        # only used when GATE == "AND"


def draw_grid(screen, grid, cell_scale, output_window):
    """Draw the board: dead=black, alive=white, output window=red outline."""
    rows, cols = grid.shape
    screen.fill((0, 0, 0))
    alive_ys, alive_xs = np.nonzero(grid)
    for y, x in zip(alive_ys, alive_xs):
        rect = pygame.Rect(x * cell_scale, y * cell_scale, cell_scale, cell_scale)
        pygame.draw.rect(screen, (255, 255, 255), rect)

    r0, r1, c0, c1 = output_window
    out_rect = pygame.Rect(
        c0 * cell_scale, r0 * cell_scale,
        (c1 - c0) * cell_scale, (r1 - r0) * cell_scale,
    )
    pygame.draw.rect(screen, (220, 40, 40), out_rect, width=2)


def watch(life, output_window, total_steps, title, result_label):
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("consolas", 18)

    rows, cols = life.grid.shape
    screen = pygame.display.set_mode((cols * CELL_SCALE, rows * CELL_SCALE + 30))
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    board_surface = pygame.Surface((cols * CELL_SCALE, rows * CELL_SCALE))

    step = 0
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        draw_grid(board_surface, life.grid, CELL_SCALE, output_window)
        screen.blit(board_surface, (0, 0))

        info = f"gen {step}/{total_steps}   final result = {result_label}"
        text_surface = font.render(info, True, (255, 255, 0))
        screen.fill((0, 0, 0), (0, rows * CELL_SCALE, cols * CELL_SCALE, 30))
        screen.blit(text_surface, (5, rows * CELL_SCALE + 5))

        pygame.display.flip()

        if step < total_steps + EXTRA_FRAMES_AFTER:
            life.evolve()
            step += 1

        clock.tick(FPS)

    pygame.quit()


def main():
    gates = GliderLogicGates()

    if GATE == "AND":
        life = gates.setup_and_gate(35, INPUT_A, INPUT_B)
        steps = gates.and_steps
        window = gates.and_out
        result = gates.run_and_gate(INPUT_A, INPUT_B)
        title = f"AND Gate - A={int(INPUT_A)} B={int(INPUT_B)}"
    else:
        life = gates.setup_not_gate(35, INPUT_A)
        steps = gates.not_steps
        window = gates.not_out
        result = gates.run_not_gate(INPUT_A)
        title = f"NOT Gate - A={int(INPUT_A)}"

    print(f"{title}  ->  result = {result}")
    watch(life, window, steps, title, result_label=str(result))


if __name__ == "__main__":
    main()
