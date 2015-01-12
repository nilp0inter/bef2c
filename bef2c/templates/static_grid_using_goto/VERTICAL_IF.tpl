// Vertical IF
if (!pop()) {
    epd = DIR_DOWN;
    goto {{ cell.down.goto_label }};
} else {
    epd = DIR_UP;
    goto {{ cell.up.goto_label }};
}
