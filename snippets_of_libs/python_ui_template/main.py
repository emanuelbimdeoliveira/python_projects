from ui.app import App
from controller.controller import handle_execute

def main():
    app = App(on_execute=handle_execute)
    app.mainloop()

if __name__ == "__main__":
    main()