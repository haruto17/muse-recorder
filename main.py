import flet as ft


def main(page):
    page.title = "Muse-Recorder"

    input_name = ft.TextField(label="Music Name", autofocus=True)
    input_achi = ft.TextField(label="Achievement")
    input_combo = ft.TextField(label="Max Combo")
    input_perfect = ft.TextField(label="Perfect")
    input_great = ft.TextField(label="Great")
    input_pass = ft.TextField(label="Pass")
    input_miss = ft.TextField(label="Miss")

    def btn_click(e):
        page.update()

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
        ft.ElevatedButton("Add", on_click=btn_click),
    )

ft.app(target=main)