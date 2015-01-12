// Horizontal IF
if (!pop()) {
    epd = DIR_RIGHT;
    goto {{ cell.right.goto_label }};
} else {
    epd = DIR_LEFT;
    goto {{ cell.left.goto_label }};
}
