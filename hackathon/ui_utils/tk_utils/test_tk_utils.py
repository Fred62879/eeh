import time
from hackathon.ui_utils.tk_utils.tk_utils import BlockingTaskDialogFunction, hold_tkinter_root_context


def test_show_blocking_task_dialog():

    with hold_tkinter_root_context() as window:
        BlockingTaskDialogFunction(
            n_steps=100,
            message="Milking cows, please wait..."
        ).show_blocking_task_dialog(time.sleep(0.01) for _ in range(100))


if __name__ == "__main__":
    test_show_blocking_task_dialog()