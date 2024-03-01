"""
class Window:
	function __init__(self, title, size):
		set_title(title)
		set_size(size)
        create_buttons()
		
	function create_buttons():
        beginning_algorithm = create_button()
        previous_step = create_button()
        generate_graph_Button = create_button(click_command=destroy_buttons())
        next_step = create_button()
        end_algorithm = create_button()

        beginning_algorithm.place()
        previous_step.place()
        generate_graph_Button.place()
        next_step.place()
        end_algorithm.place()

    function destroy_buttons():
        beginning_algorithm.destroy()
        previous_step.destroy()
        generate_graph_Button.destroy()
        next_step.destroy()
        end_algorithm.destroy()

        create_pop_up()

    function remove_pop_up():
        ask_label.remove_from_window()
        yes_button.remove_from_window()
        no_button.remove_from_window()

        create_buttons()

    function create_pop_up():
        yes_button = create_button(click_command=create_random_graph())
        no_button = create_button(click_command=remove_pop_up())
        ask_label = create_label()

        ask_label.place()
        yes_button.place()
        no_button.place()

    function create_random_graph():
        clear_graph()
        graph_obj = generate_graph()
        graph_position = get_graph_position()
        draw_graph(graph_obj, graph_position)
"""