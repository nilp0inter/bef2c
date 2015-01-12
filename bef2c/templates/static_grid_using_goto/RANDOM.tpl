r = rand() / (RAND_MAX / 4 + 1);
switch (r) {
    case 0: 
        epd = DIR_DOWN;
        goto {{ cell.down.goto_label }};
        break;
    case 1:
        epd = DIR_LEFT;
        goto {{ cell.left.goto_label }};
        break;
    case 2:
        epd = DIR_RIGHT;
        goto {{ cell.right.goto_label }};
        break;
    case 3:
        epd = DIR_UP;
        goto {{ cell.up.goto_label }};
        break;
}
