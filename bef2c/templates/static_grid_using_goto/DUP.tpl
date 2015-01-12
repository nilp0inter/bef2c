// Duplicate the top of the stack
if (st_head > 0) {
//    fprintf(stderr, "DUP[%d] %c\n", st_head, st_base[st_head - 1]);
    push(st_base[st_head - 1]);
}
