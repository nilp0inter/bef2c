// Skip the next cell
switch(epd) {                                                          
    case DIR_DOWN:  goto {{ cell.down.down.goto_label }};
    case DIR_LEFT:  goto {{ cell.left.left.goto_label }};
    case DIR_RIGHT: goto {{ cell.right.right.goto_label }};
    case DIR_UP:    goto {{ cell.up.up.goto_label }};
}  
