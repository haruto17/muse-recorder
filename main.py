import flet as ft
import writer
import gettime


def main(page):
    page.title = "Muse-Recorder"

    input_name = ft.TextField(label="Music Name", autofocus=True)
    input_achi = ft.TextField(label="Achievement")
    input_combo = ft.TextField(label="Max Combo")
    input_perfect = ft.TextField(label="Perfect")
    input_great = ft.TextField(label="Great")
    input_pass = ft.TextField(label="Pass")
    input_miss = ft.TextField(label="Miss")
    input_score = ft.TextField(label="Score")

    def btn_click(e):
        data_list = []
        data_list.append(input_name.value)
        data_list.append(input_achi.value)
        data_list.append(input_combo.value)
        data_list.append(input_perfect.value)
        data_list.append(input_great.value)
        data_list.append(input_pass.value)
        data_list.append(input_miss.value)
        data_list.append(input_score.value)
        data_list.append(gettime.get_now_time())
        writer.write_csv(data_list)
        input_name.value = ""
        input_achi.value = ""
        input_combo.value = ""
        input_perfect.value = ""
        input_great.value = ""
        input_pass.value = ""
        input_miss.value = ""
        input_score.value = ""
        page.update()
        input_name.focus()

    page.theme_mode = "dark"
    page.window_width = 300
    page.window_height = 700
    page.add(
        input_name,
        input_achi,
        input_combo,
        input_perfect,
        input_great,
        input_pass,
        input_miss,
        input_score,
        ft.ElevatedButton("Add", on_click=btn_click),
    )


ft.app(target=main)
