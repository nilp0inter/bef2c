// Push the string in the stack and jump to the end
switch (epd) {
    {% if cell.get_string('v') %}
    case DIR_DOWN:
        push_string("{{ cell.get_string('v').string }}");
        goto {{ cell.get_string('v').next_cell.goto_label }};
    {% endif %}
    {% if cell.get_string('<') %}
    case DIR_LEFT:
        push_string("{{ cell.get_string('<').string }}");
        goto {{ cell.get_string('<').next_cell.goto_label }};
    {% endif %}
    {% if cell.get_string('>') %}
    case DIR_RIGHT:
        push_string("{{ cell.get_string('>').string }}");
        goto {{ cell.get_string('>').next_cell.goto_label }};
    {% endif %}
    {% if cell.get_string('^') %}
    case DIR_UP:
        push_string("{{ cell.get_string('^').string }}");
        goto {{ cell.get_string('^').next_cell.goto_label }};
    {% endif %}
}
