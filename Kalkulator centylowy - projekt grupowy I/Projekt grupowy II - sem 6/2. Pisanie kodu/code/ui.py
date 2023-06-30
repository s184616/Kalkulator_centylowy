import tkinter as tk

from chart import create_charts


def create_user_interface(main):
    """
    Create user interface

    :param main:
    :return:
    """

    def is_number(s):
        """
        Check if provided data is a double or integer
        :param s:
        :return:
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

    def append_data():
        """
        Append data to file
        """
        with open("data.csv", "a") as file:
            file.write(
                f"\n{selected_gender.get()}, {age_input.get()}, {height_input.get()}, {weight_input.get()},"
                f" {head_input.get()}")

    def is_empty_or_not_number():
        """
        Check if inputs are empty or not a number
        :return:
        """
        if age_input.get() == "" or height_input.get() == "" or weight_input.get() == "" or head_input.get() == "" \
                or not is_number(age_input.get()) or not is_number(height_input.get()) or not is_number(
                weight_input.get()) or not is_number(head_input.get()):
            return True
        else:
            return False

    def button_click():
        """
        Function called when button is clicked
        :return:
        """
        error_label = tk.Label(main, text="Wprowadź poprawne dane!", fg="red")
        # if any of the inputs is empty or not a number than show error message
        if is_empty_or_not_number():
            error_label.grid(row=12, column=0, columnspan=2)
            # hide window after 3 seconds
            main.after(3000, error_label.destroy)
        else:
            # if age is empty then increase previous age from data.csv file by 1
            if age_input.get() == "":
                with open("data.csv", "r") as file:
                    data = file.read()
                data = data.split("\n")
                data_list = []
                for i in data:
                    data_list.append(i.split(","))
                age_input.insert(0, str(int(data_list[-1][1]) + 1))
            # disable button after click
            input_button['state'] = 'disabled'
            # hide window after 3 seconds
            main.after(3000, error_label.destroy)
            success_label = tk.Label(main, text="Dane zostały zapisane!", fg="green")
            success_label.grid(row=12, column=0, columnspan=2)
            # hide window after 3 seconds
            main.after(3000, success_label.destroy)
            # append data to file
            append_data()
            create_charts(main)

    def change_button_state():
        """
        Change button state, to enabled
        :return:
        """
        input_button['state'] = 'normal'

    # button to change butt appending data state to enabled
    change_button_state_button = tk.Button(main, text="Wprowadź kolejne dane", command=change_button_state)

    tk.Label(main, text="Kalkulator centylowy", bg="#FFCC99", font=("Arial", 30)).grid(row=0, column=0, columnspan=2,
                                                                                       padx=10, pady=10)

    # create radio buttons, to select child's gender
    selected_gender = tk.StringVar()
    tk.Label(main, text="Płeć dziecka:", bg="#FFCC99").grid(row=1, column=0, padx=10, pady=10, columnspan=2)
    tk.Radiobutton(main,
                   text="Dziewczynka",
                   value="girl",
                   variable=selected_gender,
                   bg="#FFCC99",
                   highlightbackground="#FFCC99",
                   activebackground="#e6ac73").grid(row=2,
                                                    column=0,
                                                    padx=10,
                                                    pady=10)
    tk.Radiobutton(main,
                   text="Chłopczyk",
                   value="boy",
                   highlightbackground="#FFCC99",
                   activebackground="#e6ac73",
                   variable=selected_gender,
                   bg="#FFCC99").grid(row=2,
                                      column=1,
                                      padx=10,
                                      pady=10)

    # create input fields
    tk.Label(main, text="Wiek [miesiące]:", bg="#FFCC99").grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    age_input = tk.Entry(main)
    age_input.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

    tk.Label(main, text="Wzrost [cm]:", bg="#FFCC99").grid(row=5, column=0, padx=10, pady=10, columnspan=2)
    height_input = tk.Entry(main)
    height_input.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

    tk.Label(main, text="Waga [kg]:", bg="#FFCC99").grid(row=7, column=0, padx=10, pady=10, columnspan=2)
    weight_input = tk.Entry(main)
    weight_input.grid(row=8, column=0, padx=10, pady=10, columnspan=2)

    tk.Label(main, text="Obwód głowy [cm]:", bg="#FFCC99").grid(row=9, column=0, padx=10, pady=10, columnspan=2)
    head_input = tk.Entry(main)
    head_input.grid(row=10, column=0, padx=10, pady=10, columnspan=2)

    # create button to append data to file
    input_button = tk.Button(main, text="Zapisz dane", command=button_click)
    input_button.grid(row=11, column=0, padx=10, pady=10, columnspan=2)

    # button changing appending button state to enabled
    change_button_state_button.grid(row=12, column=0, columnspan=2, pady=10)

    # button to end program
    end_button = tk.Button(main, text="Zakończ", command=main.destroy)
    end_button.grid(row=13, column=0, padx=10, pady=10, columnspan=2)

