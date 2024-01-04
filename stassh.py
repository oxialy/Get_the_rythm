
def main():

    #init_userevent()

    run_main = True

    while run_main:

        draw_screen(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_SPACE:
                    pass
                if event.key == K_l:
                    logs.print_logs(logs.LOG_FILE)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(FPS)
