/* `{{ transpiler.source }}`: Converted using bef2c

{{ transpiler.grid }}

*/
#include <ctype.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define STACK_INITIAL_SIZE 64
#define STACK_MAX_SIZE SIZE_MAX

#define DIR_DOWN  'D'
#define DIR_LEFT  'L'
#define DIR_RIGHT 'R'
#define DIR_UP    'U'

char *st_base = NULL;
size_t st_head = 0;
size_t st_size = 0;

/* START: Read only grid for get operand */
/*
const char grid[{{transpiler.grid.MAX_Y + 1}}][{{transpiler.grid.MAX_X + 1}}] = { {% for line in transpiler.grid.lines %}
    { "{{ line }}" },{% endfor %}
};
*/
/* END: Read only grid for get operand */

void stack_init() {
    st_size = STACK_INITIAL_SIZE;
    st_base = (char *) calloc(st_size, sizeof(char));
    if (!st_base) {
        perror("Can't initialize the stack");
        exit(1);
    }
    st_head = 0;
}

/*
void stackstatus() {
    size_t current = st_head;

    if (st_head > 0) fprintf(stderr, "STACK: ");

    while(current > 0) {
        if (isprint(st_base[current-1])) {
            fprintf(stderr, "\"%c\" ", st_base[current-1]);
        } else {
            fprintf(stderr, "%u ", st_base[current-1]);
        }
        current--;
    }

    if (st_head > 0) fprintf(stderr, "\n");
}
*/

inline char pop() {
    // stackstatus();
    if (st_head > 0) {
        return st_base[--st_head];
    } else {
        return 0;
    }
}

inline void reallocate_stack(size_t request) {
    if (st_head + request >= st_size) {
        if (st_size == STACK_MAX_SIZE) {
            fprintf(stderr, "Stack is full");
            exit(1);
        } else {
            while ((st_size - st_head) < request) {
                st_size *= 2;
    
                if (st_size > (size_t) 0xffffffff) {
                    // st_size overflow
                    st_size = STACK_MAX_SIZE;
                }
            }
                
            st_base = realloc(st_base, st_size);

            if(!st_base) {
                perror("Can't resize the stack");
                exit(1);
            }
        }
    }
}

inline void push(char value) {
    // stackstatus();
    reallocate_stack(1); 
    st_base[st_head++] = value;
}

void push_string(const char *string) {
    // stackstatus();
    size_t len = strlen(string);
    reallocate_stack(len);
    memcpy(&st_base[st_head], string, len);
    st_head += len;
}

int main() {
    char epd = DIR_RIGHT;  // Execution pointer direction
    stack_init();
    register char aux, a, b;
    int r;

    srand(time(NULL));  // Initialize the RNG

{% for cell in transpiler.grid %}
    {{ cell.goto_label }}: // Cell | X: {{ cell.x }}, Y: {{ cell.y }} | '{{ cell.raw_value }}' |
        {{ transpiler.render_cell(cell)|indent(8) }}
        {% if not cell.is_stringmode() %}
        switch(epd) {
{% if cell.down != cell %}
            case DIR_DOWN:  goto {{ cell.down.goto_label }};{% endif %}
{% if cell.left != cell %}
            case DIR_LEFT:  goto {{ cell.left.goto_label }};{% endif %}
{% if cell.right != cell %}
            case DIR_RIGHT: goto {{ cell.right.goto_label }};{% endif %}
{% if cell.up != cell %}
            case DIR_UP:    goto {{ cell.up.goto_label }};{% endif %}
        }
        {% endif %}
{% endfor %}
}
