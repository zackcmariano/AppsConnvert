from calculator import calc_root, calc_display, calc_label, calc_buttons
from calc_class import Calculator


def main():
    root = calc_root()
    display = calc_display(root)
    label = calc_label(root)
    buttons = calc_buttons(root)
    calculator = Calculator(root, label, display, buttons)
    calculator.start()


if __name__ == '__main__':
    main()