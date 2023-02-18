# This file is executed when selected in the Script drop-down
import gradio as gr

import modules.scripts as scripts
from modules.processing import Processed, process_images

from py.example import example_func

def text_button_click():
    print(f"scripts.basedir(): {scripts.basedir()}")

class Script(scripts.Script):
    def title(self):
        return "Extension Template"

    def ui(self, is_img2img):
        with gr.Accordion("testes",open = False):
            text_button = gr.Button("Push me")
            text_button.click(
                fn=text_button_click
            )
        return [text_button]

    def on_show(self):
        return [gr.Textbox.update(visible=True),
                gr.Button.update(visible=True),
                ]

    def run(self, p, text_button):
        # Generate button click
        print("aiueo")
        print(text_buton)
        return Processed(p, p.images, p.seed, "")
